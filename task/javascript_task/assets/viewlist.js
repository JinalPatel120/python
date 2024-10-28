function loadUserData() {
  const tableBody = document.querySelector("#userTable tbody");
  tableBody.innerHTML = ""; // Clear existing rows

  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    const userData = JSON.parse(localStorage.getItem(key));

    if (userData) {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${userData.name}</td>
                <td>${userData.email}</td>
                <td>${userData.phone}</td>
                <td>${userData.zipcode}</td>
                <td>${userData.dob}</td>
                <td>${userData.gender}</td>
                <td>${userData.technology}</td>
                <td>${userData.hobby}</td>

                <td>
<button style="background-color: blue; border: none; padding: 5px 10px; cursor: pointer;" onclick="viewUser('${key}')">View</button>
<button style="background-color: green; border: none; padding: 5px 10px; cursor: pointer;" onclick="editUser('${key}')">Edit</button>
<button style="background-color: red; border: none; padding: 5px 10px; cursor: pointer;" onclick="deleteUser('${key}')">Delete</button>
                  
                </td>
            `;
      tableBody.appendChild(row);
    }
  }
}

function editUser(key) {
  const userData = JSON.parse(localStorage.getItem(key));
  if (userData) {
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

    window.currentEditKey = key;
  }
}

function deleteUser(key) {
  const userConfirmation = confirm(
    "Are you sure you want to delete this record?"
  );
  if (userConfirmation) {
    localStorage.removeItem(key);
    loadUserData();
    alert("Record deleted successfully.");
  } else {
    alert("Record not deleted.");
  }
}

function editUser(key) {
  window.location.href = `update.html?key=${key}`;
}

function viewUser(key) {
  window.location.href = `view_user.html?key=${key}`;
}

window.onload = loadUserData;
