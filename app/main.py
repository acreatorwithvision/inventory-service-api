from fastapi import FastAPI

app = FastAPI(title="Inventory Service API")

@app.get("/")
def root():
    return {"message": "Inventory API is running"}