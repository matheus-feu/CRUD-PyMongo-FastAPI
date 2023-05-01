import logging

from fastapi import FastAPI
from pymongo import MongoClient

from app.api.v1.api import api_router
from app.core.settings import settings

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

app = FastAPI(title=settings.project_name, version=settings.app_version, description=settings.project_description)


@app.on_event("startup")
def startup_db_client():
    logging.info("Starting db client...")
    app.mongodb_client = MongoClient(settings.mongodb_uri)
    app.mongodb = app.mongodb_client[settings.mongodb_name]


@app.on_event("shutdown")
def shutdown_db_client():
    logging.info("Closing db client...")
    app.mongodb_client.close()


app.include_router(api_router, prefix=settings.app_v1_prefix)

if __name__ == "__main__":
    import uvicorn

    logging.info("Starting server...")
    logging.info("Swagger UI available at http://localhost:8000/docs")

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
