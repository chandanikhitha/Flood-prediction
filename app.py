from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# ✅ Safe model load
model = None
if os.path.exists("model.pkl"):
    model = pickle.load(open("model.pkl", "rb"))

# ✅ Home route
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return "Model not loaded!"

    try:
        # ✅ Get input values
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])

        # ✅ Model prediction
        prediction = model.predict([[rainfall, temperature]])[0]

        # 🔥 Flood warning logic
        if prediction == 1:
            result = "⚠️ Flood Warning!"
        else:
            result = "✅ No Flood"

        # ✅ Send result to HTML
        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return f"Error: {str(e)}"

# ✅ Run locally
if __name__ == "__main__":
    app.run(debug=True)