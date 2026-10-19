import { memo, useMemo } from "react";
import ReactMarkdown, { type Components } from "react-markdown";
import remarkGfm from "remark-gfm";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import rehypeRaw from "rehype-raw";
import type { PluggableList } from "unified";
import { KATEX_OPTIONS } from "../lib/katexOptions";
import { resolveImage } from "../lib/resolveImage";
import "katex/dist/katex.min.css";

function hasClass(node: unknown, wanted: string): boolean {
  if (!node || typeof node !== "object") return false;
  const el = node as { properties?: { className?: unknown } };
  const cls = el.properties?.className;
  if (Array.isArray(cls)) return cls.includes(wanted);
  return typeof cls === "string" && cls.split(/\s+/).includes(wanted);
}

/** After rehype-katex, warn (dev only) about any inline/display equation that
 * KaTeX could not render, identifying the surrounding block. */
function rehypeLogKatexErrors(blockId: string | undefined) {
  const walk = (node: unknown): boolean => {
    if (!node || typeof node !== "object") return false;
    const el = node as {
      children?: unknown[];
      tagName?: string;
    };
    if (el.tagName === "span" && hasClass(el, "katex-error")) {
      if (import.meta.env.DEV) {
        console.warn(
          `[katex] ${blockId ?? "(unknown block)"}: KaTeX failed to render an equation (shown in red)`
        );
      }
      return true;
    }
    for (const c of el.children ?? []) {
      if (walk(c)) return true;
    }
    return false;
  };
  return () => (tree: unknown) => {
    walk(tree);
  };
}

const components: Components = {
  img: ({ node: _node, ...props }) => {
    return (
      <img
        {...props}
        src={resolveImage(props.src)}
        alt={props.alt ?? ""}
        className="max-w-full h-auto my-3 rounded border border-black/10 dark:border-white/10"
        loading="lazy"
      />
    );
  },
  table: (props) => (
    <div className="overflow-x-auto my-3">
      <table className="border-collapse text-sm md:text-base">
        {props.children}
      </table>
    </div>
  ),
  th: (props) => (
    <th
      className="border border-black/15 dark:border-white/15 px-3 py-1.5 text-left font-semibold"
      {...props}
    />
  ),
  td: (props) => (
    <td
      className="border border-black/15 dark:border-white/15 px-3 py-1.5 align-top"
      {...props}
    />
  ),
  a: (props) => (
    <a
      className="text-accent underline decoration-accent/40 underline-offset-2 hover:decoration-accent"
      {...props}
    />
  ),
};

export interface MdProps {
  source: string;
  blockId?: string;
  className?: string;
}

/** One shared Markdown renderer for reader and exercise modes. */
export function Md({ source, blockId, className }: MdProps) {
  const rehypePlugins = useMemo<PluggableList>(
    () => [
      rehypeRaw,
      [rehypeKatex, KATEX_OPTIONS],
      rehypeLogKatexErrors(blockId),
    ],
    [blockId]
  );
  const remarkPlugins = useMemo<PluggableList>(
    () => [remarkMath, remarkGfm],
    []
  );
  return (
    <div className={className}>
      <ReactMarkdown
        remarkPlugins={remarkPlugins}
        rehypePlugins={rehypePlugins}
        components={components}
      >
        {source}
      </ReactMarkdown>
    </div>
  );
}

export default memo(Md);
