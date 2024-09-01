from api_router import router

from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise

from database.tortoise_config import TORTOISE_CONFIG

from fastapi.middleware.cors import CORSMiddleware


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
    uvicorn.run(app="__main__:app", host='0.0.0.0', port=8080, reload=True)
