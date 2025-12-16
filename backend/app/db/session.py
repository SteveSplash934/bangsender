from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings

# Create the Async Engine
# echo=True will log SQL queries to console (turn off in prod)
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=(settings.MODE == "dev"),
    future=True
)

# Create the Session Factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

# Dependency for FastAPI Routes
async def get_db():
    """
    Yields a database session for the request scope.
    Closes it automatically when request finishes.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()