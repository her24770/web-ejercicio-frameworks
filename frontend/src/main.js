/**
 * Punto de entrada de la aplicación Svelte.
 * Monta el componente raíz App en el elemento #app del HTML.
 */

import App from "./App.svelte";

const app = new App({
  target: document.getElementById("app"),
});

export default app;
