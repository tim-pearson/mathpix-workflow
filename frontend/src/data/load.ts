import type { ChapterData, Manifest, SearchEntry, Stats } from "../types";

const BASE = `${import.meta.env.BASE_URL}data/`;

let manifestPromise: Promise<Manifest> | null = null;
let searchPromise: Promise<SearchEntry[]> | null = null;
let statsPromise: Promise<Stats> | null = null;
const chapterCache = new Map<string, Promise<ChapterData>>();

async function fetchJson<T>(url: string): Promise<T> {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Failed to load ${url}: ${res.status}`);
  return res.json() as Promise<T>;
}

export function dataUrl(path: string): string {
  return `${BASE}${path}`;
}

export function loadManifest(): Promise<Manifest> {
  if (!manifestPromise) {
    manifestPromise = fetchJson<Manifest>(dataUrl("manifest.json"));
  }
  return manifestPromise;
}

export function loadChapter(slug: string): Promise<ChapterData> {
  let p = chapterCache.get(slug);
  if (!p) {
    p = fetchJson<ChapterData>(dataUrl(`chapters/${slug}.json`));
    chapterCache.set(slug, p);
  }
  return p;
}

export function loadSearchIndex(): Promise<SearchEntry[]> {
  if (!searchPromise) {
    searchPromise = fetchJson<SearchEntry[]>(dataUrl("search-index.json"));
  }
  return searchPromise;
}

export function loadStats(): Promise<Stats> {
  if (!statsPromise) {
    statsPromise = fetchJson<Stats>(dataUrl("stats.json"));
  }
  return statsPromise;
}

export function clearDataCache(): void {
  manifestPromise = null;
  searchPromise = null;
  statsPromise = null;
  chapterCache.clear();
}
