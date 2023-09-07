from fastapi import FastAPI, HTTPException
from db import engine, Base
from routers import todos,users

app = FastAPI()
app.include_router(users.router)
app.include_router(todos.router)

@app.get("/")
def read_root():
    return "Welcome to the Todo API :)"
def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()



