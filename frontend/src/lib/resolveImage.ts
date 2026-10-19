// Resolve an image path found in exported Markdown to a URL the browser can
// load.  The exporter rewrites `../images/x.jpg` to `images/x.jpg`, and
// sync-data.mjs copies frontend-data/images -> public/data/images, so an
// image referenced as `images/x.jpg` must become `data/images/x.jpg`
// (relative to the app base, which handles hosting under a subpath such as
// /tutex/).

export function resolveImage(src: string | null | undefined): string {
  if (!src) return "";
  // Absolute / protocol-relative / data / blob URLs are used as-is.
  if (/^(https?:)?\/\//.test(src) || src.startsWith("data:") || src.startsWith("blob:")) {
    return src;
  }
  if (src.startsWith("/")) return src;
  if (src.startsWith("data/")) return src;
  if (src.startsWith("./data/")) return src.slice(2);
  if (src.startsWith("images/")) {
    return `data/images/${src.slice("images/".length)}`;
  }
  return src;
}
