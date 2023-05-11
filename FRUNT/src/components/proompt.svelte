<script lang="ts">
    export let firePrompt;

	let input;
    let hover: boolean = false;
    const mailboxes: string[][] = [['📪','📭'],['📫','📬']]
    let justSent: boolean = false;

    $: mailIcon = justSent ? mailboxes[1][1] : mailboxes[!!input ? 1 : 0][hover ? 1 : 0];
    

    const setHover = (on: boolean = true) => {
        hover = on;
    }

    const send = () => {
        justSent = true
        setTimeout(() => {
            justSent = false;
        }, 1500);

        
        firePrompt(input);
        input = "";
    }

</script>

<input bind:value={input} on:keypress={e => e.key === "Enter" && send() }>
<button on:mouseover={e => setHover(true)} 
    on:focus={e => setHover(true)} 
    on:mouseout={e => setHover(false)} 
    on:blur={e => setHover(false)}
    on:click={e =>send()}>
    {mailIcon}
</button>

<style>
    input {
        width: 60%;
        height: 50px;
    }
    button {
        font-size: 2em;
        position: relative;
        right: 62px;
        top: 3px;
        background: none;
        border: none;
    }
</style>