<script lang="ts">
    import type { Message } from "../BUNK/models/Message";
    import { MessageType } from "../BUNK/models/MessageType";

    export let messages: Message[] = [];

</script>

<div class="conversation">
    {#each messages as message}
        {#if message.type === MessageType.USER}
            <p class="right-speech-bubble">{message.content}</p>
        {:else if message.type === MessageType.BOT}
            <p class="left-speech-bubble">{message.content}</p>
        {/if}
    {/each}

</div>

<style>
    .conversation {
        height: 100%;
        max-height: 40vh;
        overflow-y: scroll;
        padding: 1em;
    }

    /* Speech bubble on the left side */
.left-speech-bubble {
  position: relative;
  background-color: #eef2ff;
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  margin-right: auto;
  margin-left: 20px;
  max-width: 60%;
}

.left-speech-bubble::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: -10px;
  border-width: 10px;
  border-style: solid;
  border-color: transparent transparent transparent #eef2ff;
}

/* Speech bubble on the right side */
.right-speech-bubble {
  position: relative;
  background-color: #fff5e6;
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  margin-left: auto;
  margin-right: 20px;
  max-width: 60%;
}

.right-speech-bubble::after {
  content: '';
  position: absolute;
  bottom: 0;
  right: -10px;
  border-width: 10px;
  border-style: solid;
  border-color: transparent #fff5e6 transparent transparent;
}

</style>