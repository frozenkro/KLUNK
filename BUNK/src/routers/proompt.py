from fastapi import APIRouter
from models.Interaction import Interaction
from services.gpt35tChat import chat

router = APIRouter()


@router.post("/")
async def proompt(req: Interaction):
    return chat(req)
