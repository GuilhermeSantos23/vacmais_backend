from fastapi import FastAPI

app = FastAPI(title="Vac+ API")


@app.get("/")
def root():
    return {"message": "API está online"}
