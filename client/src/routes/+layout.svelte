<script>
	import Header from '../components/Header.svelte';
import './styles.css';
</script>

<div class="app">
	<div class="container">	<Header /></div>

	<main>
		<div class="container">
			<slot />
		</div>

		
	</main>

	<footer>
		<p>XeCore inc. 2020-2024 Join our <a href="https://discord.gg/hF8cHaZ7/682RSVnMG6">Discord</a>  </p>
	</footer>
</div>

<style>

	
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}
	
	.container {
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
	}

	main { 
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		margin-top: 12rem;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
