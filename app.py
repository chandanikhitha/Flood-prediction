from flask import Flask, request, render_template
import pickle
import os
import matplotlib.pyplot as plt
import requests

app = Flask(__name__)

# Load model
model = pickle.load(open(os.path.join(os.getcwd(), "model.pkl"), "rb"))

# 🌍 Weather API function
def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    temp = data['main']['temp']
    humidity = data['main']['humidity']

    return temp, humidity

# 📊 Graph function
import matplotlib.pyplot as plt
def create_graph(rainfall, temperature):
    values = [rainfall, temperature]
    labels = ['Rainfall', 'Temperature']

    plt.bar(labels, values)
    plt.title("Input Visualization")
    plt.savefig("static/graph.png")
    plt.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    rainfall = float(request.form['rainfall'])
    temperature = float(request.form['temperature'])
    city = request.form['city']

    # API use
    if city:
        temperature, humidity = get_weather(city)
    else:
        humidity = 50  # default

    create_graph(rainfall, temperature)

    prediction = model.predict([[rainfall, temperature]])

    if prediction[0] == 1:
        result = "⚠️ Flood Risk!"
    else:
        result = "✅ No Flood"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)