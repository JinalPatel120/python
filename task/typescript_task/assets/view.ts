interface UserData {
    name: string;
    email: string;
    phone: string;
    zipcode: string;
    dob: string;
    gender: string;
    technology: string;
    hobby: string;
}

function loadUserData(index:number): void {
    const tableBody = document.querySelector<HTMLTableSectionElement>('#userTable tbody');
    if (!tableBody) return;
    tableBody.innerHTML = '';

    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key) {
            const userData: UserData | null = JSON.parse(localStorage.getItem(key) || 'null');

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

function showEditPopup(): void {
    const editPopup = document.getElementById('editPopup');
    if (editPopup) editPopup.style.display = 'block';
}

function closeEditPopup(): void {
    const editPopup = document.getElementById('editPopup');
    if (editPopup) editPopup.style.display = 'none';
}

function showDeletePopup(): void {
    const deletePopup = document.getElementById('deletePopup');
    if (deletePopup) deletePopup.style.display = 'block';
}

function closeDeletePopup(): void {
    const deletePopup = document.getElementById('deletePopup');
    if (deletePopup) deletePopup.style.display = 'none';
}

function editAll(): void {
    closeEditPopup();
    window.location.href = 'edit_all.html';
}

function editManually(): void {
    closeEditPopup();
    window.location.href = 'edit_all.html';
}

function deleteAllUsers(): void {
    if (confirm('Are you sure you want to delete all records?')) {
        localStorage.clear();
        loadUserData(0);
        closeDeletePopup();
        alert('All records deleted successfully.');
    }
}

function deleteSelectedUsers(): void {
    closeEditPopup();
    const selectedUsers = Array.from(document.querySelectorAll<HTMLTableRowElement>('#userTable tbody tr'));
    const userKeys = selectedUsers.map(row => row.dataset.key || '');

    if (userKeys.length > 0) {
        window.location.href = `user_details.html?key=${userKeys[0]}`;
    } else {
        alert('No user selected for editing.');
    }
}

function viewUser(key: string): void {
    window.location.href = `view_user.html?key=${key}`;
}

window.onload = () => {
    loadUserData(0); 
  };