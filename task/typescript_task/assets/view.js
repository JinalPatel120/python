"use strict";
function loadUserData(index) {
    const tableBody = document.querySelector('#userTable tbody');
    if (!tableBody)
        return;
    tableBody.innerHTML = '';
    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key) {
            const userData = JSON.parse(localStorage.getItem(key) || 'null');
            if (userData) {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${i + 1}</td>
                    <td>${userData.name}</td>
                    <td>${userData.email}</td>
                    <td>${userData.phone}</td>
                    <td>${userData.zipcode}</td>
                    <td>${userData.dob}</td>
                    <td>${userData.gender}</td>
                    <td>${userData.technology}</td>
                    <td>${userData.hobby}</td>
                    <td>
                        <button style="background-color: blue; border: none; width: 50%; padding: 10px 10px; cursor: pointer;" onclick="viewUser('${key}')">View</button>
                    </td>
                `;
                row.dataset.key = key;
                tableBody.appendChild(row);
            }
        }
    }
}
function showEditPopup() {
    const editPopup = document.getElementById('editPopup');
    if (editPopup)
        editPopup.style.display = 'block';
}
function closeEditPopup() {
    const editPopup = document.getElementById('editPopup');
    if (editPopup)
        editPopup.style.display = 'none';
}
function showDeletePopup() {
    const deletePopup = document.getElementById('deletePopup');
    if (deletePopup)
        deletePopup.style.display = 'block';
}
function closeDeletePopup() {
    const deletePopup = document.getElementById('deletePopup');
    if (deletePopup)
        deletePopup.style.display = 'none';
}
function editAll() {
    closeEditPopup();
    window.location.href = 'edit_all.html';
}
function editManually() {
    closeEditPopup();
    window.location.href = 'edit_all.html';
}
function deleteAllUsers() {
    if (confirm('Are you sure you want to delete all records?')) {
        localStorage.clear();
        loadUserData(0);
        closeDeletePopup();
        alert('All records deleted successfully.');
    }
}
function deleteSelectedUsers() {
    closeEditPopup();
    const selectedUsers = Array.from(document.querySelectorAll('#userTable tbody tr'));
    const userKeys = selectedUsers.map(row => row.dataset.key || '');
    if (userKeys.length > 0) {
        window.location.href = `user_details.html?key=${userKeys[0]}`;
    }
    else {
        alert('No user selected for editing.');
    }
}
function viewUser(key) {
    window.location.href = `view_user.html?key=${key}`;
}
window.onload = () => {
    loadUserData(0);
};
//# sourceMappingURL=view.js.map