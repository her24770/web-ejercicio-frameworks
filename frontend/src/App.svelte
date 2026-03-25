<script>
  import PollCard from "./lib/PollCard.svelte";
</script>

<main>
  <header>
    <div class="logo">
      <span class="logo-icon">🗳️</span>
      <span class="logo-text">VotaWeb</span>
    </div>
  </header>

  <section class="card-container">
    <PollCard />
  </section>
</main>

<style>
  :global(:root) {
    --color-bg: #f0f2ff;
    --color-card: #ffffff;
    --color-text: #1e1b4b;
    --color-muted: #6b7280;
    --color-primary: #6366f1;
    --color-border: #e0e7ff;
    --color-btn-bg: #f5f3ff;
    --color-track: #e0e7ff;
    --color-bar: #a5b4fc;
    --color-badge-bg: #eef2ff;
  }

  :global(*) {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  :global(body) {
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: var(--color-bg);
    min-height: 100vh;
    color: var(--color-text);
  }

  main {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem 1rem;
    gap: 2rem;
  }

  header {
    text-align: center;
  }

  .logo {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }

  .logo-icon {
    font-size: 2rem;
  }

  .logo-text {
    font-size: 2rem;
    font-weight: 800;
    color: var(--color-primary);
    letter-spacing: -0.05em;
  }

  .card-container {
    display: flex;
    justify-content: center;
    width: 100%;
  }
</style>
