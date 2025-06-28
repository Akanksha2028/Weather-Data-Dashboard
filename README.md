# 🌦️ Weather Data Dashboard

A simple and clean Flask-based web application to fetch, store, and view weather information using Excel as a database. Built with a Dark Grey Theme using Bootstrap and Weather Icons.

---

## 📖 About This Project

This project helps you:
- 🔍 Search weather for any city (from saved data)
- ➕ Add new city weather info with temperature
- 📋 View weather history (with auto-generated IDs)
- 🕒 Live clock in header
- 🌤️ Weather emoji based on temperature (hot/cold)

Data is stored in an `Excel` file. No SQL database is used — making it beginner-friendly and easy to deploy.

---

## 🔧 Features

- 💻 Built using Python + Flask
- 🌤️ Animated weather emojis
- 📁 Excel file (`Data.xlsx`) as the database
- 📊 History table sorted by location ID
- 🔄 Responsive layout and search

---

## 📸 Screenshots

### 🏠 Home Page
![Home_page](https://github.com/user-attachments/assets/1fede736-cc30-4bb5-b7aa-37d03ccf7589)

### 🌤️ Get Weather Page
![Get_Weather_Page](https://github.com/user-attachments/assets/e985283c-7e45-4e8b-a315-35da26574afe)

### ➕ Add Location Page
![Add_Location_page](https://github.com/user-attachments/assets/cea5527c-08ce-416a-8487-54d3e8122269)

### 📋 Weather History page
![Weather_History_page](https://github.com/user-attachments/assets/178ee06f-e921-43e8-8814-2fcdf03d0448)

### ✅ Success Popup
![Saved_Successful_page](https://github.com/user-attachments/assets/f41425fd-cd5b-4f49-9b7f-9de4118ac367)

weather_application/
├── app.py
├── Data.xlsx
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── add_location.html
│   ├── history.html
│   └── success_popup.html
│
├── static/
│   └── style.css
│
└── images/
    ├── Home_page.png
    ├── emoji_weather.png
    ├── add_location.png
    ├── weather_history.png
    └── success_popup.png

