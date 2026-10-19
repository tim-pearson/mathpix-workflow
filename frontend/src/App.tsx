import { lazy, Suspense, useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import type { Manifest } from "./types";
import { loadManifest } from "./data/load";
import { TopBar } from "./components/TopBar";

const Home = lazy(() => import("./routes/Home").then((m) => ({ default: m.Home })));
const Reader = lazy(() => import("./routes/Reader").then((m) => ({ default: m.Reader })));
const Practice = lazy(() =>
  import("./routes/Practice").then((m) => ({ default: m.Practice }))
);
const Stats = lazy(() => import("./routes/Stats").then((m) => ({ default: m.Stats })));

export default function App() {
  const [manifest, setManifest] = useState<Manifest | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadManifest()
      .then(setManifest)
      .catch((e) => setError(String(e)));
  }, []);

  if (error) {
    return (
      <div className="flex h-full items-center justify-center p-8">
        <div className="rounded-lg border border-line bg-paper p-6 text-center text-ink">
          <h1 className="text-lg font-semibold">Could not load data</h1>
          <p className="mt-1 text-sm text-muted">{error}</p>
          <p className="mt-3 text-xs text-muted">
            Run <code className="rounded bg-line/40 px-1">npm run sync-data</code> from
            <code className="rounded bg-line/40 px-1"> frontend/</code> and reload.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-full flex-col">
      <TopBar manifest={manifest} />
      <main className="min-h-0 flex-1 overflow-y-auto">
        <Suspense
          fallback={
            <div className="flex h-full items-center justify-center p-8 text-muted">
              Loading…
            </div>
          }
        >
          <Routes>
            <Route path="/" element={<Home manifest={manifest} />} />
            <Route path="/read/:chapter/:sectionId?" element={<Reader manifest={manifest} />} />
            <Route path="/practice/:chapter/:exerciseId?" element={<Practice manifest={manifest} />} />
            <Route path="/stats" element={<Stats manifest={manifest} />} />
            <Route path="*" element={<Home manifest={manifest} />} />
          </Routes>
        </Suspense>
      </main>
    </div>
  );
}
