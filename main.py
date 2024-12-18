import uvicorn
from fastapi import FastAPI, HTTPException, status

from service import operations_router

app = FastAPI()
app.include_router(operations_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
        host="0.0.0.0",
        port=8000
    )

