<script>
  /**
   * Componente PollCard: muestra una encuesta completa con botones de voto
   * y barras de progreso tras votar.
   *
   * Demuestra características clave de Svelte:
   * 1. Reactive declarations ($:) para calcular porcentajes
   * 2. onMount para cargar datos iniciales
   * 3. Svelte store para estado compartido
   * 4. Transitions (fade, fly) para animaciones
   * 5. localStorage para persistir el voto
   */

  import { onMount } from "svelte";
  import { fade } from "svelte/transition";
  import { writable } from "svelte/store";
  import VoteBar from "./VoteBar.svelte";
  import { fetchPolls, vote } from "./api.js";

  // ── Svelte Store ─────────────────────────────────────────────────────────
  // writable() crea un store reactivo: cualquier componente que lo suscriba
  // se actualiza automáticamente cuando cambia el valor.
  const pollStore = writable(null);

  // Estado local del componente
  let loading = true;
  let error = null;
  let votedOptionId = null; // ID de la opción que votó el usuario
  let voting = false; // Evita doble-click
  let intervalId; // Referencia al intervalo de polling

  // ── Reactive declarations ($:) ────────────────────────────────────────────
  // El bloque $: se re-ejecuta automáticamente cuando cambian sus dependencias.
  // Aquí calculamos los porcentajes cada vez que $pollStore cambia.
  $: poll = $pollStore;

  $: percentages = poll
    ? poll.options.reduce((acc, opt) => {
        const total = poll.total_votes || 1; // Evitar división por cero
        acc[opt.id] = (opt.votes / total) * 100;
        return acc;
      }, {})
    : {};

  $: hasVoted = votedOptionId !== null;

  // ── onMount ──────────────────────────────────────────────────────────────
  // Se ejecuta una sola vez cuando el componente se monta en el DOM.
  // Equivale a useEffect(() => {...}, []) en React.
  onMount(async () => {
    // Recuperar voto previo del localStorage
    const stored = localStorage.getItem("voted_option_id");
    if (stored) votedOptionId = parseInt(stored);

    // Carga inicial
    await cargarEncuesta();

    // Polling cada 3 segundos para simular tiempo real
    intervalId = setInterval(cargarEncuesta, 3000);

    // Función de cleanup: se llama cuando el componente se desmonta
    return () => clearInterval(intervalId);
  });

  // ── Funciones ─────────────────────────────────────────────────────────────

  async function cargarEncuesta() {
    try {
      const polls = await fetchPolls();
      if (polls.length > 0) {
        // Actualizar el store con set()
        pollStore.set(polls[0]);
      }
      error = null;
    } catch (e) {
      error = "No se pudo conectar con el servidor. ¿Está corriendo el backend?";
    } finally {
      loading = false;
    }
  }

  async function handleVote(optionId) {
    if (hasVoted || voting) return;
    voting = true;

    try {
      // La API devuelve la encuesta actualizada
      const updatedPoll = await vote(optionId);
      pollStore.set(updatedPoll);

      // Persistir la elección en localStorage
      votedOptionId = optionId;
      localStorage.setItem("voted_option_id", optionId.toString());
    } catch (e) {
      error = "Error al registrar tu voto. Intenta de nuevo.";
    } finally {
      voting = false;
    }
  }
</script>

<div class="poll-card">
  {#if loading}
    <!-- fade transition: aparece/desaparece suavemente -->
    <div class="status" in:fade>
      <div class="spinner"></div>
      <p>Conectando con el servidor...</p>
    </div>

  {:else if error}
    <div class="status error" in:fade>
      <p>{error}</p>
      <button on:click={cargarEncuesta} class="retry-btn">Reintentar</button>
    </div>

  {:else if poll}
    <div in:fade={{ duration: 300 }}>
      <!-- Cabecera de la encuesta -->
      <div class="poll-header">
        <h2 class="poll-question">{poll.question}</h2>
        <span class="total-badge">{poll.total_votes} votos totales</span>
      </div>

      {#if !hasVoted}
        <!-- Modo votación: mostrar botones -->
        <div class="options-grid">
          {#each poll.options as option (option.id)}
            <button
              class="option-btn"
              on:click={() => handleVote(option.id)}
              disabled={voting}
            >
              {option.text}
            </button>
          {/each}
        </div>
        <p class="hint">Haz clic en una opción para votar</p>

      {:else}
        <!-- Modo resultados: mostrar barras de progreso -->
        <div class="results">
          {#each poll.options as option (option.id)}
            <VoteBar
              {option}
              percentage={percentages[option.id] || 0}
              isVoted={option.id === votedOptionId}
            />
          {/each}
        </div>
        <p class="hint pulse">Actualizando en tiempo real cada 3 segundos...</p>
      {/if}
    </div>
  {/if}
</div>

<style>
  .poll-card {
    background: var(--color-card);
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
    max-width: 560px;
    width: 100%;
  }

  .poll-header {
    margin-bottom: 1.8rem;
  }

  .poll-question {
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--color-text);
    margin: 0 0 0.6rem 0;
    line-height: 1.3;
  }

  .total-badge {
    display: inline-block;
    background: var(--color-badge-bg);
    color: var(--color-primary);
    font-size: 0.8rem;
    font-weight: 600;
    padding: 0.2rem 0.7rem;
    border-radius: 999px;
  }

  .options-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.8rem;
    margin-bottom: 1rem;
  }

  .option-btn {
    background: var(--color-btn-bg);
    color: var(--color-text);
    border: 2px solid var(--color-border);
    border-radius: 10px;
    padding: 0.9rem 1rem;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .option-btn:hover:not(:disabled) {
    background: var(--color-primary);
    color: white;
    border-color: var(--color-primary);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
  }

  .option-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  .results {
    margin-top: 0.5rem;
  }

  .hint {
    text-align: center;
    font-size: 0.8rem;
    color: var(--color-muted);
    margin-top: 1rem;
  }

  .hint.pulse {
    animation: pulse 2s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 0.6; }
    50% { opacity: 1; }
  }

  .status {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    padding: 2rem 0;
    color: var(--color-muted);
  }

  .status.error {
    color: #ef4444;
  }

  .spinner {
    width: 36px;
    height: 36px;
    border: 3px solid var(--color-track);
    border-top-color: var(--color-primary);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }

  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  .retry-btn {
    background: var(--color-primary);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1.2rem;
    cursor: pointer;
    font-size: 0.9rem;
  }
</style>
