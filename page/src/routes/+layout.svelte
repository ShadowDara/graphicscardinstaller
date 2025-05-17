<script lang="ts">
	import '../lib/app.css';
	import Header from '$lib/Header.svelte';

	let { children } = $props();
</script>

<div class="flex min-h-screen flex-col">
	<Header></Header>

	<nav>
		<!-- Navigation für alle Seiten -->
	</nav>

	{@render children()}

	<footer>
		<!-- Gemeinsamer Footer -->
	</footer>
</div>

<style>
	* {
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}
</style>
