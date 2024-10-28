"use strict";
var _a;
(_a = document.getElementById('registerForm')) === null || _a === void 0 ? void 0 : _a.addEventListener('submit', function (event) {
    var _a;
    event.preventDefault();
    const id = Date.now();
    const userData = {
        id: id,
        key: id.toString(),
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        zipcode: document.getElementById('zipcode').value,
        dob: document.getElementById('dob').value,
        gender: ((_a = document.querySelector('input[name="gender"]:checked')) === null || _a === void 0 ? void 0 : _a.value) || '',
        hobby: Array.from(document.getElementById('hobby').selectedOptions).map(option => option.value),
        technology: Array.from(document.getElementById('technology').selectedOptions).map(option => option.value)
    };
    if (validateUserData(userData)) {
        localStorage.setItem(id.toString(), JSON.stringify(userData));
        alert('Registration successful!');
        document.getElementById('registerForm').reset();
    }
});
attachValidationListeners();
//# sourceMappingURL=script.js.map