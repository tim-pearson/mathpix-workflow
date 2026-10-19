const prefix = window.location.pathname.startsWith("/tutex/")
  ? "/tutex"
  : "";

export const API_BASE = `${prefix}/api`;
