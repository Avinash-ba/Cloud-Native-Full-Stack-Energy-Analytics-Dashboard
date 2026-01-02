from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import energy

app = FastAPI(title="Energy Analytics API", version="1.0.0")

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(energy.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Energy Analytics API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
