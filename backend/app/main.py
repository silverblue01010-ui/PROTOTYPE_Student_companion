from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time

from app.api.routes import user_routes, match_routes, session_routes
from app.utils.logger import logger
from app.utils.exceptions import global_exception_handler

# ✅ Create app
app = FastAPI(title="Smart Study Companion API")

# ✅ Global exception handler
app.add_exception_handler(Exception, global_exception_handler)

# ✅ CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Routers
app.include_router(session_routes.router, prefix="/api/sessions", tags=["Sessions"])
app.include_router(match_routes.router, prefix="/api/matches", tags=["Matches"])
app.include_router(user_routes.router, prefix="/api/users", tags=["Users"])

# ✅ Root route
@app.get("/")
async def root():
    return {"message": "Smart Study Companion API is running 🚀"}

# ✅ FIXED favicon route (NO FILE NEEDED)
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return {}  # prevents browser error

# ✅ Startup event
@app.on_event("startup")
async def startup_event():
    logger.info("Server started successfully")

# ✅ Logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time
    logger.info(f"{request.method} {request.url} - {duration:.4f}s")

    return response