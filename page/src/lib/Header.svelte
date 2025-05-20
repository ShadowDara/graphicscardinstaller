<script>
	import { base } from "$app/paths";
</script>

<!-- Website Header -->

<header class="underline">
    <span><a href="{base}/">Home</a></span>
    <span><a href="{base}/troll_info">Info</a></span>
    <span><a href="{base}/docs">Docs</a></span>
    <span><a href="{base}/downloads">Download</a></span>
</header>

<style>
header {
    background-color: var(--header-bg-color);
    color: var(--header-text-color);
    padding: 0.8em 2rem;
    display: fixed;
    width: 100%;
    gap: 2rem;
    display: flex;
    justify-content: right;
}
</style>
