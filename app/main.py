from fastapi import FastAPI
from app.routers import task_router
from fastapi_sqlalchemy import DBSessionMiddleware, db
from app.utilities.utility_data_task import DATABASE_URL


# Instancing the app
app = FastAPI()

# middlewares
# middlewares = [Middleware(CORSMiddleware)]

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)

# middlewares
# middlewares = [Middleware(CORSMiddleware)]


# app initialization
app_title = "Task API Project"
app_version = "0.1.0"
app_description = "Demo API where can see a Repository pattern implementation with Docker, RabbitMQ, GO microservices, frontend using FLet and login, authentication using supabase"

# Instancing  the routers
app.include_router(task_router.router)


# Testing service is on
@app.get("/")
async def index():
    # for health check of server when logs are disabled in production
    return {"title": app.title, "version": app.version, "description": app.description}
