from fastapi import FastAPI
from .routes import router
from .database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

# FastAPI app instance (THIS IS IMPORTANT)
app = FastAPI(title="User Management API")

# Register routes
app.include_router(router)
