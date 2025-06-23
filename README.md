# 🌦️ Weather Data Dashboard

A clean and elegant Flask web application to manually add, store, and display weather data for multiple cities.  
Weather records are saved with timestamps and unique location IDs in an Excel file — no external database required.

## 🔧 Features

🌍 Search and view saved weather data by city  
➕ Add new locations with temperature and timestamp  
📜 View complete weather history in a styled table  
💾 Auto-generated `Location ID` (e.g., LOC001, LOC002...)    
📁 Excel-based data storage (no external database)

## 📁 Project Structure

# Weather-Data-Dashboard
This is a simple Flask web app to store and view weather data for different cities. Users can add city name and temperature, and the app automatically saves the entry with a unique ID and timestamp in an Excel file. You can also view all saved weather history in order. The app uses a clean, dark-themed UI and works without any database.
weather-data-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│── Data.xlsx
├── templates/
│ ├── index.html
│ ├── add_location.html
│ ├── history.html
│ └── success_popup.html
