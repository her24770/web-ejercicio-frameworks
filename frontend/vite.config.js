/**
 * Configuración de Vite para el proyecto Svelte.
 * Vite es el bundler/dev-server que usa Svelte por defecto.
 */

import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

export default defineConfig({
  plugins: [svelte()],
  server: {
    // Necesario para que Vite acepte conexiones desde fuera del contenedor
    host: "0.0.0.0",
    port: 5173,
  },
});
