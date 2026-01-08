from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import random
from datetime import datetime, timedelta

app = FastAPI(title="GA4 Analytics Bridge")

# Tells Python where to find your HTML file
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/ga4-report")
async def get_report():
    """Generates dynamic mock data for the dashboard demo."""
    data = []
    # Create 7 days of data
    for i in range(7):
        date = (datetime.now() - timedelta(days=7-i)).strftime('%b %d')
        data.append({
            "date": date,
            "sessions": random.randint(150, 600),
            "conversions": random.randint(5, 45)
        })
    return JSONResponse(content=data)

@app.get("/")
async def root():
    return {"status": "online", "message": "Visit /static/dashboard.html"}