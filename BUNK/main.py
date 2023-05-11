from fastapi import FastAPI
from pydantic import BaseModel

class Prompt(BaseModel):
    prompt: str


app = FastAPI()

@app.get("/testReverse")
async def root(prompt: Prompt):
    return ({ "prompt": prompt.prompt, "reverse": prompt.prompt[::-1] })