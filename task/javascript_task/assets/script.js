document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const id = Date.now();
    const userData = {
        id: id,
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        zipcode: document.getElementById('zipcode').value,
        dob: document.getElementById('dob').value,
        gender: document.querySelector('input[name="gender"]:checked')?.value || '',
        hobby: Array.from(document.getElementById('hobby').selectedOptions).map(option => option.value),
        technology: Array.from(document.getElementById('technology').selectedOptions).map(option => option.value)
    };

    if (validateUserData(userData)) {
        localStorage.setItem(id, JSON.stringify(userData));
        alert('Registration successful!');
        document.getElementById('registerForm').reset();
    }
});


attachValidationListeners();

