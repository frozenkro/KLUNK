<script lang="ts">
    import Proompt from "./components/proompt.svelte";
	import { chat } from "./services/bunk";
	import type Interaction from "./models/Interaction";

	let promptResult: string;

	const firePrompt = async (prompt: string) => {
		const interaction: Interaction = await chat(prompt);
		promptResult = interaction.response;
	}
</script>

<main>
	<h1>its KLUNK!</h1>
	<p>{promptResult || ''}</p>

	<div class="prompt">
		<Proompt firePrompt={firePrompt} />
	</div>
	
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		font-size: 4em;
		font-weight: 100;
	}

	.prompt {
		position: fixed;
		bottom: 50px;
		left: 50%;
		transform: translateX(-50%);
		width: 100%
	}


	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>