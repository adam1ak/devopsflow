from fastapi import FastAPI

app = FastAPI(title="DevOpsFlow API", version="0.1.0")


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "devopsflow-backend"}
