from fastapi import FastAPI
from app.routers import course_routes
from app.routers import user_routes

app = FastAPI(title="Cadastro de Cursos")

app.include_router(course_routes.router)
app.include_router(user_routes.router)

@app.get("/")
def health():
    return {"message": "Hello World"}


