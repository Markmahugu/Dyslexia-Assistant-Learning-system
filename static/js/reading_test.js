const scrambledText = "The qciuk brown fox jmups over the alyz dog.";
const correctText = "The quick brown fox jumps over the lazy dog.";

const userAnswerTextarea = document.getElementById('user-answer');
const submitAnswerButton = document.getElementById('submit-answer');

// Track attempts
let correctAttempts = 0;
let incorrectAttempts = 0;
let startTime;
let endTime;

// Start the timer when the test is displayed
window.onload = function() {
    startTime = new Date();
    document.getElementById('scrambled-text').innerText = scrambledText;
};

// Handle user's sentence submission
submitAnswerButton.addEventListener('click', () => {
    endTime = new Date();
    const userAnswer = userAnswerTextarea.value.trim();
    let result = (userAnswer === correctText) ? 'Correct' : 'Incorrect';
    
    if (result === 'Correct') {
        correctAttempts++;
    } else {
        incorrectAttempts++;
    }
    
    alert(result);

    // Calculate time taken in seconds
    const timeTaken = Math.round((endTime - startTime) / 1000);
    
    // Send result to Flask
    fetch('/save_result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            test_type: 'Reading',
            user_answer: userAnswer,
            correct_answer: correctText,
            time_taken: timeTaken,
            correct_attempts: correctAttempts,
            incorrect_attempts: incorrectAttempts
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        if (result === 'Correct') {
            // Redirect to the next page (e.g., back to home)
            window.location.href = '/';
        }
    })
    .catch(error => console.error('Error:', error));
});
