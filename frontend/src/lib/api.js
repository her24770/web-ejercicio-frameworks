/**
 * Módulo de comunicación con la API de Django.
 * Centraliza todas las llamadas HTTP para facilitar cambios de URL.
 */

// URL base del backend (variable de entorno o fallback para desarrollo local)
const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

/**
 * Obtiene todas las encuestas con sus opciones y votos.
 * @returns {Promise<Array>} Lista de encuestas
 */
export async function fetchPolls() {
  const res = await fetch(`${API_BASE}/api/polls/`);
  if (!res.ok) throw new Error("Error al cargar encuestas");
  return res.json();
}

/**
 * Obtiene una encuesta específica por ID.
 * @param {number} id - ID de la encuesta
 * @returns {Promise<Object>} Datos de la encuesta
 */
export async function fetchPoll(id) {
  const res = await fetch(`${API_BASE}/api/polls/${id}/`);
  if (!res.ok) throw new Error("Error al cargar encuesta");
  return res.json();
}

/**
 * Registra un voto para una opción específica.
 * @param {number} optionId - ID de la opción a votar
 * @returns {Promise<Object>} Encuesta actualizada con los nuevos conteos
 */
export async function vote(optionId) {
  const res = await fetch(`${API_BASE}/api/vote/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ option_id: optionId }),
  });
  if (!res.ok) throw new Error("Error al registrar voto");
  return res.json();
}
