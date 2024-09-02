from api_router import router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tortoise.contrib.fastapi import register_tortoise

from database.tortoise_config import TORTOISE_CONFIG

import ssl
import os


PATH = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(title='TG Web App BOT.RF')

app.include_router(router=router)

register_tortoise(app=app, config=TORTOISE_CONFIG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="__main__:app", 
                host='localhost', 
                port=8080, 
                reload=True)
