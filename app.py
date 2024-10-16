from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import mysql.connector
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()  # Set your secret key here

# Load environment variables from .env file
load_dotenv()

# Database connection configuration
db_config = {
    'user': 'root',
    'password': os.getenv('DB_PASSWORD'),  # Use environment variable
    'host': 'localhost',
    'database': 'comprehension_assessment'
}

# Helper function to check answers
def check_answers(answer1, answer2):
    score = 0
    # Interest-Based Reading and Explanation scoring
    if "cheetah" in answer1.lower() and "fastest" in answer1.lower():
        score += 10  # Add 10% for correct answer

    # Image-Based Comprehension Testing scoring
    keywords = ['ball', 'doctor', 'car']
    if any(keyword in answer2.lower() for keyword in keywords):
        score += 10  # Add 10% for correct answer

    return score

@app.route('/')
def index():
    return render_template('comprehensiv.html')  # Render the HTML file

@app.route('/submit', methods=['POST'])
def submit():
    answer1 = request.form['answer1']
    answer2 = request.form['answer2']
    
    score = check_answers(answer1, answer2)
    print(f"Score calculated: {score}")  # Debugging statement

    try:
        # Store results in the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO results (answer1, answer2, score) VALUES (%s, %s, %s)", (answer1, answer2, score))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Your answers have been submitted successfully!')  # Flash a success message
         
    except mysql.connector.Error as err:
        flash(f"Error: {err}")  # Flash the error message

    return redirect(url_for('home'))  # Redirect to the home route

# New route to handle AI prompts
@app.route('/api/assist/prompt', methods=['POST'])
def handle_prompt():
    data = request.json
    prompt = data.get('prompt')
    print(prompt)

    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'gpt-3.5-turbo',  # or 'gpt-4'
                'messages': [{'role': 'user', 'content': prompt}]
            }
        )

        response.raise_for_status()  # Raise an error for bad responses
        ai_message = response.json()['choices'][0]['message']['content']
        return jsonify({'message': ai_message})

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
        return jsonify({'error': 'An error occurred while fetching the response.'}), 500
    except Exception as e:
        print(f"Other error occurred: {e}")  # Log any other error
        return jsonify({'error': 'An error occurred while fetching the response.'}), 500
# Home endpoint
@app.route('/home')
def home():
    return render_template('home.html')  # Render the home template

if __name__ == '__main__':
    app.run(debug=True)
