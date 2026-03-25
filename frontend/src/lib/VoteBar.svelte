<script>
  /**
   * Componente VoteBar: barra de progreso animada para una opción de voto.
   *
   * Props recibidas del componente padre (PollCard):
   * - option: objeto { id, text, votes }
   * - percentage: porcentaje calculado reactivamente en el padre
   * - isVoted: si el usuario votó por esta opción
   */

  // Svelte: las props se declaran con export let
  export let option;
  export let percentage = 0;
  export let isVoted = false;

  // Svelte transitions: importamos fade y fly para animar la barra
  import { fly } from "svelte/transition";
</script>

<!-- fly transition: la barra entra deslizándose desde la izquierda -->
<div class="vote-bar-wrapper" in:fly={{ x: -20, duration: 400 }}>
  <div class="vote-bar-header">
    <span class="option-text" class:voted={isVoted}>
      {option.text}
      {#if isVoted}
        <span class="voted-badge">Tu voto ✓</span>
      {/if}
    </span>
    <span class="vote-stats">{option.votes} votos · {percentage.toFixed(1)}%</span>
  </div>

  <div class="progress-track">
    <!-- El ancho de la barra se actualiza reactivamente gracias a la prop percentage -->
    <div
      class="progress-fill"
      class:voted-fill={isVoted}
      style="width: {percentage}%"
    ></div>
  </div>
</div>

<style>
  .vote-bar-wrapper {
    margin-bottom: 1rem;
  }

  .vote-bar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.4rem;
    font-size: 0.95rem;
  }

  .option-text {
    font-weight: 500;
    color: var(--color-text);
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .option-text.voted {
    color: var(--color-primary);
    font-weight: 700;
  }

  .voted-badge {
    background: var(--color-primary);
    color: white;
    font-size: 0.7rem;
    padding: 0.1rem 0.4rem;
    border-radius: 999px;
    font-weight: 600;
  }

  .vote-stats {
    font-size: 0.85rem;
    color: var(--color-muted);
  }

  .progress-track {
    height: 10px;
    background: var(--color-track);
    border-radius: 999px;
    overflow: hidden;
  }

  .progress-fill {
    height: 100%;
    background: var(--color-bar);
    border-radius: 999px;
    /* Animación CSS para que la barra crezca suavemente */
    transition: width 0.6s ease;
  }

  .progress-fill.voted-fill {
    background: var(--color-primary);
  }
</style>
