from flask import Flask, render_template, request, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

# MySQL database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='',  # Replace with your MySQL password
        database='das_db'  # Use your existing database name
    )
    return conn

@app.route('/')
def index():
    return render_template('attention_test.html')

@app.route('/memory_test')
def memory_test():
    return render_template('memory_test.html')

@app.route('/reading_test')
def reading_test():
    return render_template('reading_test.html')

# Endpoint to save individual test results and overall performance
@app.route('/save_result', methods=['POST'])
def save_result():
    data = request.get_json()
    test_type = data['test_type']
    user_answer = data['user_answer']
    correct_answer = data['correct_answer']
    
    # Determine result
    result = "Correct" if user_answer == correct_answer else "Incorrect"
    timestamp = datetime.datetime.now()
    
    # Extract additional data
    time_taken = data.get('time_taken', 0)  # Default to 0 if not provided
    correct_attempts = data.get('correct_attempts', 0)  # Default to 0 if not provided
    incorrect_attempts = data.get('incorrect_attempts', 0)  # Default to 0 if not provided

    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert into appropriate table based on test type
    table_name = None
    if test_type == 'Attention':
        table_name = 'attention_test_results'
    elif test_type == 'Memory Test':
        table_name = 'memory_test_results'
    elif test_type == 'Reading Test':
        table_name = 'reading_test_results'

    if table_name:
        # Insert individual test result into the database
        cursor.execute(f'''INSERT INTO {table_name} 
                           (test_type, user_answer, correct_answer, result, time_taken, correct_attempts, incorrect_attempts, timestamp) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', 
                       (test_type, user_answer, correct_answer, result, time_taken, correct_attempts, incorrect_attempts, timestamp))
        conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Result saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
