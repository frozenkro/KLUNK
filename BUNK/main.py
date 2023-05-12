from dotenv import load_dotenv
from fastapi import FastAPI
from BUNK.routers import proompt

def main():
    load_dotenv()

    app = FastAPI()
    app.include_router(proompt.router, prefix="/chat", tags=["chat"])


if __name__ == "__main__":
    main()
