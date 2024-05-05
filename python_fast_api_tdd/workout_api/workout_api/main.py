from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(title='VivoApi')
app.include_router(api_router)


#docker-compose up -d
#docker ps
#alembic upgrade head
#make run