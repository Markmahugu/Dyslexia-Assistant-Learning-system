from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector
import datetime
import bcrypt  # for password hashing

app = Flask(__name__)

# MySQL database connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='',  # Replace with your MySQL password
            database='das_db'  # Replace with your actual database name
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to render the sign-up page
@app.route('/signup', methods=['GET'])
def render_signup():
    return render_template('signup.html')

# Route to handle sign-up form submission (POST request)
@app.route('/signup', methods=['POST'])
def signup():
    first_name = request.form['fname']
    last_name = request.form['lname']
    dob = request.form['dob']
    password = request.form['password']

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert the user into the database
    conn = get_db_connection()
    if not conn:
        return "Database connection error", 500
    
    cursor = conn.cursor()
    try:
        query = """
            INSERT INTO users (first_name, last_name, dob, password) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (first_name, last_name, dob, hashed_password))
        conn.commit()
        return redirect(url_for('render_signin'))  # Redirect to the signin page
    except mysql.connector.Error as err:
        return f"An error occurred: {str(err)}", 500  # Improved error handling
    finally:
        cursor.close()
        conn.close()

# Route to render the sign-in page
@app.route('/signin', methods=['GET'])
def render_signin():
    return render_template('signin.html')

# Sign-in route with user authentication
@app.route('/signin', methods=['POST'])
def signin():
    first_name = request.form.get('first_name')
    password = request.form.get('password')

    if not first_name or not password:
        return render_template('signin.html', error="Please provide both first name and password")

    conn = get_db_connection()
    if not conn:
        return render_template('signin.html', error="Database connection error")

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users WHERE first_name=%s", (first_name,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return redirect(url_for('selection'))  # Redirect to the selection page
        else:
            return render_template('signin.html', error="Invalid credentials")  # Invalid login
    except mysql.connector.Error as err:
        return render_template('signin.html', error=f"Database error: {str(err)}")
    finally:
        cursor.close()
        conn.close()

# New route for the selection page
@app.route('/selection', methods=['GET'])
def selection():
    return render_template('selection.html')  # Render the selection page

# Route to save user personality test results
@app.route('/save_personality', methods=['POST'])
def save_personality():
    user_id = request.form.get('user_id')
    personality = request.form.get('personality')

    if not user_id or not personality:
        return jsonify({'status': 'error', 'message': 'Invalid input data'}), 400

    conn = get_db_connection()
    if not conn:
        return jsonify({'status': 'error', 'message': 'Database connection error'}), 500

    cursor = conn.cursor()
    try:
        query = "INSERT INTO user_personality (user_id, personality) VALUES (%s, %s)"
        cursor.execute(query, (user_id, personality))
        conn.commit()
        return jsonify({'status': 'success', 'message': 'Personality saved successfully!'})
    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)}), 500  # Improved error handling
    finally:
        cursor.close()
        conn.close()

# Routes for different tests
@app.route('/attention_test')
def attention_test():
    return render_template('attention_test.html')

@app.route('/memory_test')
def memory_test():
    return render_template('memory_test.html')

@app.route('/reading_test')
def reading_test():
    return render_template('reading_test.html')

# Save individual test results
@app.route('/save_result', methods=['POST'])
def save_result():
    data = request.get_json()
    test_type = data.get('test_type')
    user_answer = data.get('user_answer')
    correct_answer = data.get('correct_answer')

    if not test_type or not user_answer or not correct_answer:
        return jsonify({'message': 'Missing required fields'}), 400

    result = "Correct" if user_answer == correct_answer else "Incorrect"
    timestamp = datetime.datetime.now()
    
    # Extract optional fields with default values
    time_taken = data.get('time_taken', 0)
    correct_attempts = data.get('correct_attempts', 0)
    incorrect_attempts = data.get('incorrect_attempts', 0)

    conn = get_db_connection()
    if not conn:
        return jsonify({'message': 'Database connection error'}), 500

    cursor = conn.cursor()
    try:
        query = f'''INSERT INTO {test_type.lower()}_test_results 
                    (test_type, user_answer, correct_answer, result, time_taken, correct_attempts, incorrect_attempts, timestamp) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

        # Execute the query
        cursor.execute(query, 
                       (test_type, user_answer, correct_answer, result, time_taken, correct_attempts, incorrect_attempts, timestamp))
        conn.commit()
        return jsonify({"message": "Result saved successfully!"})
    except mysql.connector.Error as err:
        return jsonify({'message': str(err)}), 500  # Improved error handling
    finally:
        cursor.close()
        conn.close()

# Calculate performance for memory tests
@app.route('/calculate_performance', methods=['GET'])
def calculate_performance():
    conn = get_db_connection()
    if not conn:
        return jsonify({'message': 'Database connection error'}), 500

    cursor = conn.cursor()
    try:
        cursor.execute('SELECT correct_attempts, incorrect_attempts FROM memory_test_results')
        results = cursor.fetchall()

        total_correct = sum(result[0] for result in results)
        total_incorrect = sum(result[1] for result in results)
        total_tests = len(results)

        if total_tests > 0:
            score = (total_correct / total_tests) * 100  # Score as a percentage
            memory_capacity = (total_correct / total_tests) * 100
        else:
            score = 0
            memory_capacity = 0

        return jsonify({
            "score": score,
            "total_correct": total_correct,
            "total_incorrect": total_incorrect,
            "memory_capacity": memory_capacity
        })
    except mysql.connector.Error as err:
        return jsonify({'message': str(err)}), 500  # Improved error handling
    finally:
        cursor.close()
        conn.close()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    