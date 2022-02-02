import logging
import os

from fastapi import FastAPI
from .models.migrations import init_db
from .api import ping, summaries

log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(summaries.router, prefix='/summaries', tags=['summaries'])
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info('Starting up...')
    init_db(app)


@app.on_event('shutdown')
async def shutdown_event():
    log.info('Shutting down...')