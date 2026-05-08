from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, products 


app = FastAPI(title="small-fullstack-app")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"], 
)


app.include_router(users.router)
app.include_router(products.router)


@app.get("/")
def home():
    return {"status": "Running!"}
