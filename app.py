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

# Endpoint to save individual test results
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

    # Determine which table to insert the result into based on test_type
    if test_type == 'Attention':
        query = '''INSERT INTO attention_test_results 
                    (test_type, user_answer, correct_answer, result, time_taken, correct_attempts, incorrect_attempts, timestamp) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    elif test_type == 'Memory':
        query = '''INSERT INTO memory_test_results 
                    (test_type, user_answer, correct_answer, result, time_taken, correct_attempts, incorrect_attempts, timestamp) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    elif test_type == 'Reading':
        query = '''INSERT INTO reading_test_results 
                    (test_type, user_answer, correct_answer, result, time_taken, correct_attempts, incorrect_attempts, timestamp) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    else:
        return jsonify({"message": "Invalid test type"}), 400

    # Insert the data into the appropriate table
    cursor.execute(query, 
                   (test_type, user_answer, correct_answer, result, time_taken, correct_attempts, incorrect_attempts, timestamp))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Result saved successfully!"})

# Endpoint to calculate scores and performance
@app.route('/calculate_performance', methods=['GET'])
def calculate_performance():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch the results from the memory test results table
    cursor.execute('SELECT correct_attempts, incorrect_attempts FROM memory_test_results')
    results = cursor.fetchall()

    total_correct = sum(result[0] for result in results)
    total_incorrect = sum(result[1] for result in results)
    total_tests = len(results)

    # Calculate scores
    if total_tests > 0:
        score = (total_correct / total_tests) * 100  # Score as a percentage
        memory_capacity = total_correct / total_tests * 100  # Assuming 100% capacity is all correct
    else:
        score = 0
        memory_capacity = 0

    cursor.close()
    conn.close()

    return jsonify({
        "score": score,
        "total_correct": total_correct,
        "total_incorrect": total_incorrect,
        "memory_capacity": memory_capacity
    })

if __name__ == '__main__':
    app.run(debug=True)
