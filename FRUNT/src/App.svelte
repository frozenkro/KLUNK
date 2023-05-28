<script lang="ts">
    import Proompt from "./components/proompt.svelte";
	import { ChatService } from "./BUNK/services/ChatService";
	import type { Interaction } from "./BUNK/models/Interaction";
	import type { Message } from "./BUNK/models/Message";
	import { MessageType } from "./BUNK/models/MessageType";
    import Conversation from "./components/conversation.svelte";
    import { onMount } from "svelte";

	let messages: Message[]; 

	onMount(() => {
		messages = [];
	})

	const firePrompt = async (prompt: string) => {
		const message: Message = {
			type: MessageType.USER,
			content: prompt,
			timestamp: new Date().toISOString()
		}
		messages = [...messages, message];

		let interaction: Interaction = {
			proompt: message
		}
		interaction = await ChatService.proomptChatPost(interaction);
		const response = interaction.response;
		response.type = MessageType.BOT;
		response.timestamp = new Date().toISOString();
		messages = [...messages, interaction.response];
	}
</script>

<main>
	<h1>its KLUNK!</h1>

	<Conversation messages={messages} />

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