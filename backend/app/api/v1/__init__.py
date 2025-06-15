from fastapi import APIRouter
from .endpoints import auth, tasks, achievements, goals

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(achievements.router, prefix="/achievements", tags=["achievements"])
api_router.include_router(goals.router, prefix="/goals", tags=["goals"]) 