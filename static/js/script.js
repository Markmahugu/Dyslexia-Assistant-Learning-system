document.getElementById('sign-up-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Get Date of Birth inputs
    const day = document.getElementById('dob-day').value;
    const month = document.getElementById('dob-month').value;
    const year = document.getElementById('dob-year').value;
    
    if (!day || !month || !year) {
        alert("Please select your full date of birth.");
        return;
    }
    
    const dob = new Date(`${year}-${month}-${day}`);
    const age = calculateAge(dob);

    // Make sure the age is valid
    if (age < 5 || age > 120) {
        alert("Please enter a valid age.");
        return;
    }

    alert(`Your age is: ${age} years old.`);
    // Proceed with the form submission (could be to a backend API)
});

// Age calculation function
function calculateAge(dob) {
    const diffMs = Date.now() - dob.getTime();
    const ageDt = new Date(diffMs);

    return Math.abs(ageDt.getUTCFullYear() - 1970);
}
