const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const targetLetter = document.getElementById('target-letter');
const grid = document.getElementById('letter-grid');
const scoreDisplay = document.getElementById('score-display');
const totalRounds = 5; // Set total rounds for the test
let currentRound = 0;
let correctAnswers = 0;
let startTime;

// Generate random letters for the current round
function generateRandomLetters() {
    const randomLetters = Array.from({ length: 36 }, () =>
        letters[Math.floor(Math.random() * letters.length)]
    );
    const correctPosition = Math.floor(Math.random() * 36);
    randomLetters[correctPosition] = targetLetter.textContent; // Ensure the target letter is included
    return randomLetters;
}

// Render the current round
function renderRound() {
    if (currentRound < totalRounds) {
        // Generate a new target letter
        targetLetter.textContent = letters[Math.floor(Math.random() * letters.length)];
        const randomLetters = generateRandomLetters();
        grid.innerHTML = ''; // Clear previous grid

        randomLetters.forEach(letter => {
            const div = document.createElement('div');
            div.classList.add('grid-item');
            div.textContent = letter;
            div.addEventListener('click', () => handleAnswer(div)); // Attach the click event
            grid.appendChild(div);
        });
    } else {
        finishTest(); // Finish the test if all rounds are completed
    }
}

// Handle the user's answer
function handleAnswer(selectedDiv) {
    const userAnswer = selectedDiv.textContent;
    const correctAnswer = targetLetter.textContent;
    const result = userAnswer === correctAnswer ? 'Correct' : 'Incorrect';
    
    if (result === 'Correct') {
        correctAnswers++;
    }
    
    alert(result);
    
    // Send the result to the Flask backend
    fetch('/save_result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            test_type: 'Attention',
            user_answer: userAnswer,
            correct_answer: correctAnswer,
            result: result
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        currentRound++; // Increment current round here
        scoreDisplay.textContent = `Score: ${correctAnswers} / ${currentRound}`; // Update score display
        renderRound(); // Render the next round
    })
    .catch(error => console.error('Error:', error));
}

// Finish the test and display results
function finishTest() {
    const endTime = new Date().getTime();
    const timeTaken = (endTime - startTime) / 1000; // Time in seconds
    const percentageScore = (correctAnswers / totalRounds) * 100; // Calculate percentage score

    alert(`Test Complete! Your score is ${percentageScore.toFixed(2)}%. Time taken: ${timeTaken.toFixed(2)} seconds.`);

    // Calculate attentiveness
    const attentiveness = (percentageScore / timeTaken * 100).toFixed(2); // Simple formula for attentiveness

    alert(`Your attentiveness score is: ${attentiveness}%`);

    // Store results in the database
    fetch('/save_result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            test_type: 'Attention',
            user_answer: null,  // No user answer for final results
            correct_answer: null,  // No correct answer for final results
            is_final_result: true,  // Indicate this is the final result
            score_percentage: percentageScore,
            time_taken: timeTaken,
            attentiveness_score: attentiveness
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        // Optionally, redirect to the next test (e.g., memory test)
        window.location.href = '/templates/memory_test.html'; // Redirect to memory test or wherever you want
    })
    .catch(error => console.error('Error:', error));
}


// Start the timer and the first round
startTime = new Date().getTime();
renderRound(); // Start the first round
