from flask import Flask, request, render_template, url_for
import os
import pandas as pd
import pickle
from werkzeug.utils import secure_filename
import json
import plotly.express as px
import plotly
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MODEL_PATH = 'ChurnAnalysisModel.sav'
model = pickle.load(open(MODEL_PATH, 'rb'))


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route("/analysis", methods=['GET', 'POST'])  # Corrected from "/analysis.html" to "/analysis"
def analysis():
    predictions_details = []
    warning = None
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                data = pd.read_csv(filepath)
                predictions = model.predict(data)
                probabilities = model.predict_proba(data)[:, 1]
                percentage_churn = (predictions == 1).mean() * 100
                predictions_details = [(i + 1, prediction, probability) for i, (prediction, probability) in
                                       enumerate(zip(predictions, probabilities))]
                if percentage_churn > 20:
                    warning = f"Warning: More than 20% ({percentage_churn:.2f}%) of the predictions indicate churn."
            except Exception as e:
                warning = "Failed to process the file for predictions."
            finally:
                os.remove(filepath)

    return render_template('analysis.html', predictions_details=predictions_details, warning=warning)



def ask_gemini(user_question):
    model = genai.GenerativeModel('gemini-pro')
    response_gemini = model.generate_content(
        f'Given the user input provide the most appropriate highly detailed response also provide short examples if possible in text format only, thankyou.{user_question}')
    response_gemini = response_gemini.text.replace('**', '').replace('*', '•')

    return response_gemini


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    gemini_response = None

    if request.method == 'POST':
        user_question = request.form['user_input']
        gemini_response = ask_gemini(user_question)

    return render_template('chat.html', gemini_response=gemini_response)


@app.route("/faq", methods=['GET', 'POST'])
def faq():
    return render_template('faq.html')


@app.route("/vis", methods=['GET', 'POST'])
def vis():
    return render_template('vis.html')


if __name__ == "__main__":
    app.run(debug=True)
