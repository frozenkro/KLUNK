import type Interaction from "../models/Interaction"

export const chat = async (proompt: string, conversationContext?: string) => {
    const reqInteraction: Interaction = {
        proompt: proompt,
        conversationContext: conversationContext
    } 

    const res = await fetch('http://localhost:8000/chat', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(reqInteraction)
    });
    const resInteraction: Interaction = await res.json();

    return resInteraction;
}