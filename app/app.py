from fastapi import FastAPI

#from app.routers import task_router

# Instancing the app
app = FastAPI()

# Instancing  the routers
# app.include_router(task_router.router)


# Testing service is on
@app.get("/")
async def endpoint_test():
    return {"message": "Service is Ok"}
