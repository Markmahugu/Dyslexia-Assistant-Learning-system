// Initialize variables for tracking test data
let currentSequenceIndex = 0;
let selectedAnswer = [];
let startTime, endTime;
let correctAttempts = 0;
let incorrectAttempts = 0;

// Define the sequences to be tested
const sequences = [
    { type: 'shapes', value: generateRandomShapes(5) }, // Shapes sequence
];

// Event listeners for starting the test and submitting answers
document.getElementById('start-test-btn').addEventListener('click', startTest);
document.getElementById('submit-answer-btn').addEventListener('click', checkAnswer);

// Function to start the test
function startTest() {
    if (currentSequenceIndex < sequences.length) {
        startTime = Date.now(); // Start timer
        showSequence(sequences[currentSequenceIndex].value);
    } else {
        showFinalResult(); // Show final result if all sequences are done
    }
}

// Function to display the sequence to the user
function showSequence(sequence) {
    document.getElementById('letter-sequence').innerText = sequence;
    document.getElementById('start-test-btn').style.display = 'none';

    // Hide the sequence after 3 seconds and show the answer section
    setTimeout(() => {
        document.getElementById('letter-sequence').innerText = '';
        document.getElementById('answer-section').style.display = 'block';
        displayShapeOptions(); // Show shape options
    }, 3000); // Display sequence for 3 seconds
}

// Function to display clickable shape options for the user to select
function displayShapeOptions() {
    const shapes = ['🔴', '🟢', '🔵', '🟡', '🟠', '🟣'];
    const shapeOptionsContainer = document.getElementById('shape-options');
    shapeOptionsContainer.innerHTML = ''; // Clear previous options

    // Create a button for each shape
    shapes.forEach(shape => {
        const shapeButton = document.createElement('button');
        shapeButton.textContent = shape;
        shapeButton.style.fontSize = '30px';
        shapeButton.style.margin = '5px';
        shapeButton.onclick = () => selectShape(shape); // Add onclick event
        shapeOptionsContainer.appendChild(shapeButton);
    });
}

// Function to track and display user's selected shapes
function selectShape(shape) {
    selectedAnswer.push(shape); // Add selected shape to the answer array

    // Display the selected shapes to the user
    const selectedShapesContainer = document.getElementById('selected-shapes');
    selectedShapesContainer.innerText = selectedAnswer.join(' '); // Show in order
}

// Function to check if the user's answer is correct
function checkAnswer() {
    const correctAnswer = sequences[currentSequenceIndex].value;
    const resultElement = document.getElementById('result');

    if (selectedAnswer.join('') === correctAnswer) {
        correctAttempts++;
        resultElement.innerText = 'Correct!';
    } else {
        incorrectAttempts++;
        resultElement.innerText = `Incorrect! The correct sequence was: ${correctAnswer}`;
    }

    resultElement.style.display = 'block';
    document.getElementById('answer-section').style.display = 'none';
    document.getElementById('next-test-btn').style.display = 'block'; // Show next test button

    // Save result to the database
    saveResult(selectedAnswer.join(''), correctAnswer);

    selectedAnswer = []; // Reset for the next test
    currentSequenceIndex++; // Move to the next sequence
}

// Function to save the result to the database
function saveResult(userAnswer, correctAnswer) {
    const endTime = Date.now();
    const timeTaken = (endTime - startTime) / 1000; // Time in seconds

    const data = {
        test_type: 'Memory Test',
        user_answer: userAnswer,
        correct_answer: correctAnswer,
        time_taken: timeTaken,
        correct_attempts: correctAttempts,
        incorrect_attempts: incorrectAttempts,
    };

    fetch('/save_result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => console.log(data.message))
    .catch((error) => console.error('Error:', error));
}

// Function to generate random unique shapes
function generateRandomShapes(length) {
    const shapes = ['🔴', '🟢', '🔵', '🟡', '🟠', '🟣'];
    
    // Shuffle the shapes array and slice to the required length
    const shuffledShapes = shapes.sort(() => 0.5 - Math.random());
    return shuffledShapes.slice(0, length).join('');
}

// Function to show final result after completing all tests
function showFinalResult() {
    alert('You have completed all tests! Thank you for participating.');
}
