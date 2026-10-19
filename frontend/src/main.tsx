import React from "react";
import ReactDOM from "react-dom/client";
import { HashRouter } from "react-router-dom";
import App from "./App";
import { ProgressProvider } from "./progress/ProgressContext";
import { FlagProvider } from "./flags/FlagContext";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <HashRouter>
      <FlagProvider>
        <ProgressProvider>
          <App />
        </ProgressProvider>
      </FlagProvider>
    </HashRouter>
  </React.StrictMode>
);
