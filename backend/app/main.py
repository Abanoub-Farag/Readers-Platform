from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.session import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Readers Platform",
        lifespan=lifespan
    )

    @app.get("/health", tags=["health"])
    async def health() -> dict[str, str]:
        return {"status" : "ok"}

    return app


app = create_app()