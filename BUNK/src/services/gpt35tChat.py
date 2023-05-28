import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
from models.Interaction import Interaction
from models.Message import Message, MessageType

def chat(interaction: Interaction):
    llm = OpenAI(temperature=1)
    waifu_template = PromptTemplate(
        input_variables = ['proompt'],
        template='''
        At the end of this prompt, there will be a message from a user, which will be wrapped in quotation marks. 
        Pretend that you are a kawaii anime waifu. Come up with a cute nickname for the user, and respond to their message in-character.
        \"{proompt}\"
        '''
    )

    waifu_memory = ConversationBufferMemory(input_key='proompt', memory_key='chat_history')

    waifu_chain = LLMChain(llm=llm, prompt=waifu_template, output_key='response', memory=waifu_memory)
    
    reply = waifu_chain.run({'proompt': interaction.proompt.content})
    interaction.response = Message(content=reply, type=MessageType.BOT, conversationContext=interaction.proompt.conversationContext)
    return interaction