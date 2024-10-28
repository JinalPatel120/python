var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var users = [];
var currentIndex = 0;
function loadAllUsers() {
    for (var i = 0; i < localStorage.length; i++) {
        var key = localStorage.key(i);
        if (key) {
            var userData = localStorage.getItem(key);
            if (userData) {
                var parsedData = JSON.parse(userData);
                users.push(__assign({ key: key }, parsedData));
            }
        }
    }
}
function loadUserDataforEdit(index) {
    if (index >= 0 && index < users.length) {
        var userData_1 = users[index];
        document.getElementById("name").value = userData_1.name;
        document.getElementById("email").value = userData_1.email;
        document.getElementById("phone").value = userData_1.phone;
        document.getElementById("zipcode").value = userData_1.zipcode;
        document.getElementById("dob").value = userData_1.dob;
        document.querySelector("input[name=\"gender\"][value=\"".concat(userData_1.gender, "\"]")).checked = true;
        var hobbySelect = document.getElementById("hobby");
        Array.from(hobbySelect.options).forEach(function (option) {
            option.selected = userData_1.hobby.indexOf(option.value) !== -1;
        });
        var technologySelect = document.getElementById("technology");
        Array.from(technologySelect.options).forEach(function (option) {
            option.selected = userData_1.technology.indexOf(option.value) !== -1;
        });
        var updateForm = document.getElementById("updateForm");
        updateForm.dataset.key = userData_1.key;
    }
}
function prevUser() {
    if (currentIndex > 0) {
        currentIndex--;
        loadUserDataforEdit(currentIndex);
    }
}
function nextUser() {
    if (currentIndex < users.length - 1) {
        currentIndex++;
        loadUserDataforEdit(currentIndex);
    }
}
document.getElementById("updateForm").addEventListener("submit", function (event) {
    event.preventDefault();
    var form = event.currentTarget;
    var key = form.dataset.key;
    var updatedUserData = {
        id: users[currentIndex].id,
        key: key !== null && key !== void 0 ? key : '',
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        zipcode: document.getElementById("zipcode").value,
        dob: document.getElementById("dob").value,
        gender: document.querySelector('input[name="gender"]:checked').value,
        hobby: Array.from(document.getElementById("hobby").selectedOptions).map(function (option) { return option.value; }),
        technology: Array.from(document.getElementById("technology").selectedOptions).map(function (option) { return option.value; }),
    };
    if (validateUserData(updatedUserData)) {
        if (key) {
            localStorage.setItem(key, JSON.stringify(updatedUserData));
            alert("User updated successfully.");
            window.location.href = "view.html";
            loadUserDataforEdit(currentIndex);
        }
    }
});
window.onload = function () {
    loadAllUsers();
    loadUserDataforEdit(currentIndex);
    attachValidationListeners();
};
