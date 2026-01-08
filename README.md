# GA4 Analytics Bridge & Dashboard

A professional data pipeline and visualization suite built to bridge Google Analytics 4 (GA4) data with a custom-engineered web dashboard.

## Overview
This project demonstrates an end-to-end technical solution for data extraction and visualization. It features a high-performance **FastAPI** backend that serves processed analytics data to a responsive **Tailwind CSS** dashboard.

### Key Technical Features:
- **Mock-Injection Architecture:** A secure demonstration mode that allows the system to run without exposing sensitive API keys, perfect for architectural reviews.
- **Asynchronous API:** Built with FastAPI to handle data requests efficiently.
- **Interactive Visualization:** Dynamic charting using Chart.js to track sessions and conversions.
- **Clean Codebase:** Fully decoupled frontend and backend for easy scalability.

## Tech Stack
- **Backend:** Python 3.13, FastAPI, Uvicorn
- **Data Handling:** Pandas (Ready for advanced ETL)
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API, Chart.js)

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/Maureenchepkirui/GA4-Analytics-Bridge.git](https://github.com/Maureenchepkirui/GA4-Analytics-Bridge.git)
   ```
   ## Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
   ## Start The Server
   ```bash
   python -m uvicorn main:app --reload
   ```
   Access the dashboard: Open http://127.0.0.1:8000/static/dashboard.html in your browser.
