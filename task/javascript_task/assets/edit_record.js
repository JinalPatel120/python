let users = [];
let currentIndex = 0;

function loadAllUsers() {
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    const userData = JSON.parse(localStorage.getItem(key));
    if (userData) {
      users.push({ key, ...userData });
    }
  }
}

function loadUserData(index) {
  if (index >= 0 && index < users.length) {
    const userData = users[index];
    document.getElementById("name").value = userData.name;
    document.getElementById("email").value = userData.email;
    document.getElementById("phone").value = userData.phone;
    document.getElementById("zipcode").value = userData.zipcode;
    document.getElementById("dob").value = userData.dob;
    document.querySelector(
      `input[name="gender"][value="${userData.gender}"]`
    ).checked = true;
    const hobbySelect = document.getElementById("hobby");
    Array.from(hobbySelect.options).forEach((option) => {
      option.selected = userData.hobby.includes(option.value);
    });

    const technologySelect = document.getElementById("technology");
    Array.from(technologySelect.options).forEach((option) => {
      option.selected = userData.technology.includes(option.value);
    });

    document.getElementById("updateForm").dataset.key = userData.key;
  }
}

function prevUser() {
  if (currentIndex > 0) {
    currentIndex--;
    loadUserData(currentIndex);
  }
}

function nextUser() {
  if (currentIndex < users.length - 1) {
    currentIndex++;
    loadUserData(currentIndex);
  }
}

document
  .getElementById("updateForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const key = this.dataset.key;
    const updatedUserData = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      phone: document.getElementById("phone").value,
      zipcode: document.getElementById("zipcode").value,
      dob: document.getElementById("dob").value,
      gender: document.querySelector('input[name="gender"]:checked').value,
      hobby: Array.from(document.getElementById("hobby").selectedOptions).map(
        (option) => option.value
      ),
      technology: Array.from(
        document.getElementById("technology").selectedOptions
      ).map((option) => option.value),
    };

    if (validateUserData(updatedUserData)) {
      localStorage.setItem(key, JSON.stringify(updatedUserData));
      alert("User updated successfully.");
      window.location.href = "view.html";
      loadUserData(currentIndex);
    }
  });

window.onload = function () {
  loadAllUsers();
  loadUserData(currentIndex);
  attachValidationListeners();
};
