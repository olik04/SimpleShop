from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

# from fastapi.responses import ORJSONResponse

from core import settings
from core.models import db_helper
from api.api_V1 import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(
    # default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
app.include_router(
    router=api_router,
    prefix=settings.api.prefix,
)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
