from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import random
from datetime import datetime, timedelta

app = FastAPI(title="GA4 Analytics Bridge")

# Serve the frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/ga4-report")
async def get_report():
    """Returns mock data for portfolio demonstration."""
    data = []
    for i in range(7):
        date = (datetime.now() - timedelta(days=7-i)).strftime('%Y-%m-%d')
        data.append({
            "date": date,
            "sessions": random.randint(150, 450),
            "conversions": random.randint(5, 25),
            "engagedSessions": random.randint(100, 300)
        })
    return JSONResponse(content=data)

@app.get("/")
async def root():
    return {"message": "API is running. Visit /static/dashboard.html"}