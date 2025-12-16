from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import api_router

def create_app() -> FastAPI:
    """
    Application Factory.
    """
    app = FastAPI(
        title=settings.APP_NAME,
        version="0.1.0",
        description="High-performance bulk email engine."
    )

    # Include API Routes
    app.include_router(api_router)

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    # This entry point is mostly for debugging in VS Code
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)