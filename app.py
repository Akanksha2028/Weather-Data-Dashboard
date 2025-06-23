from flask import Flask, render_template, request, redirect
import pandas as pd
from datetime import datetime
import os, uuid

app = Flask(__name__)

def ensure_excel():
    if not os.path.exists('Data.xlsx'):
        df = pd.DataFrame(columns=['Location ID', 'City', 'Temperature', 'Timestamp'])
        df.to_excel('Data.xlsx', index=False)
ensure_excel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/saved_success")
def saved_success():
    return render_template("success_popup.html")

@app.route('/get_weather', methods=['POST'])
def get_weather():
    location = request.form['location'].strip().lower()
    df = pd.read_excel('Data.xlsx')
    df['City_clean'] = df['City'].astype(str).str.strip().str.lower()
    match = df[df['City_clean'] == location]
    if not match.empty:
        record = match.iloc[-1] 
        weather = {
            'City': record['City'],
            'Temperature': record['Temperature'],
            'Timestamp': record['Timestamp']
        }
        return render_template('index.html', weather=weather)
    else:
        return render_template('index.html', message="City not found")

@app.route('/add_location', methods=['GET', 'POST'])
def add_location():
    if request.method == 'POST':
        try:
            city = request.form['city'].strip().title()
            temperature = float(request.form['temperature'])
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if os.path.exists('Data.xlsx'):
                df = pd.read_excel('Data.xlsx')
            else:
                df = pd.DataFrame(columns=["Location ID", "City", "Temperature", "Timestamp"])

            if len(df) == 0:
                next_id = 1
            else:
                df['ID_Num'] = df['Location ID'].astype(str).str.extract(r'(\d+)', expand=False).astype(int)
                next_id = df['ID_Num'].max() + 1

            location_id = f"LOC{next_id:03}"
            new_entry = pd.DataFrame([{
                "Location ID": location_id,
                "City": city,
                "Temperature": temperature,
                "Timestamp": timestamp
            }])

            df = pd.concat([df, new_entry], ignore_index=True)
            df.drop(columns=['ID_Num'], errors='ignore', inplace=True)
            df.to_excel('Data.xlsx', index=False)

            return redirect('/saved_success')  

        except Exception as e:
            return f"❌ Error while saving: {e}"

    return render_template('add_location.html')

@app.route("/history")
def history():
    df = pd.read_excel("Data.xlsx")
    df['ID_Num'] = df['Location ID'].astype(str).str.extract(r'(\d+)', expand=False).astype(int)
    df = df.sort_values(by='ID_Num')
    df.drop(columns=['ID_Num'], inplace=True)
    history_data = df.to_dict(orient='records')
    return render_template("history.html", history=history_data)

if __name__ == '__main__':
    app.run(debug=True)
