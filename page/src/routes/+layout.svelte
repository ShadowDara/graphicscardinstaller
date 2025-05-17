<script lang="ts">
	import '../lib/app.css';
	import Header from '$lib/Header.svelte';
	import { page } from '$app/stores';

	const { children } = $props<{ children: () => unknown; }>();	
</script>

<svelte:head>
    <meta name="title" content="{$page.data.title}">
    <meta name="description" content="a Software to easily install a new Graphic Card!">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="graphiccard, installer, graphiccard installer">
    <meta name="robots" content="index,follow">
    <meta name="author" content="Shadowdara">
    <meta property="og:title" content="{$page.data.title}">
    <meta property="og:description" content="a Software to easily install a new Graphic Card!">
    <meta property="og:image" content="">
    <meta property="og:url" content="/">
    <meta property="og:type" content="website">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{$page.data.title}</title>
</svelte:head>

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
