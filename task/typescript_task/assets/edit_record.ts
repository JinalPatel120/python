interface User{
  id: number;
  key: string;
  name: string;
  email: string;
  phone: string;
  zipcode: string;
  dob: string;
  gender: string;
  hobby: string[];
  technology: string[];
}



let users: User[] = [];
let currentIndex: number = 0;

function loadAllUsers(): void {
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key) {
      const userData = localStorage.getItem(key);
      if (userData) {
        const parsedData: Omit<User, 'key'> = JSON.parse(userData);
        users.push({ key, ...parsedData });
      }
    }
  }
}

function loadUserDataforEdit(index: number): void {
  if (index >= 0 && index < users.length) {
    const userData = users[index];
    (document.getElementById("name") as HTMLInputElement).value = userData.name;
    (document.getElementById("email") as HTMLInputElement).value = userData.email;
    (document.getElementById("phone") as HTMLInputElement).value = userData.phone;
    (document.getElementById("zipcode") as HTMLInputElement).value = userData.zipcode;
    (document.getElementById("dob") as HTMLInputElement).value = userData.dob;
    (document.querySelector(`input[name="gender"][value="${userData.gender}"]`) as HTMLInputElement).checked = true;

    const hobbySelect = document.getElementById("hobby") as HTMLSelectElement;
    Array.from(hobbySelect.options).forEach((option) => {
      option.selected = userData.hobby.indexOf(option.value) !== -1;
    });

    const technologySelect = document.getElementById("technology") as HTMLSelectElement;
    Array.from(technologySelect.options).forEach((option) => {
      option.selected = userData.technology.indexOf(option.value) !== -1;
    });

    const updateForm = document.getElementById("updateForm") as HTMLFormElement;
    updateForm.dataset.key = userData.key;
  }
}

function prevUser(): void {
  if (currentIndex > 0) {
    currentIndex--;
    loadUserDataforEdit(currentIndex);
  }
}

function nextUser(): void {
  if (currentIndex < users.length - 1) {
    currentIndex++;
    loadUserDataforEdit(currentIndex);
  }
}

(document.getElementById("updateForm") as HTMLFormElement).addEventListener("submit", function (event) {
  event.preventDefault();

  const form = event.currentTarget as HTMLFormElement;
  const key = form.dataset.key;
  const updatedUserData:User = {
    id:users[currentIndex].id,
    key:key ?? '',
    name: (document.getElementById("name") as HTMLInputElement).value,
    email: (document.getElementById("email") as HTMLInputElement).value,
    phone: (document.getElementById("phone") as HTMLInputElement).value,
    zipcode: (document.getElementById("zipcode") as HTMLInputElement).value,
    dob: (document.getElementById("dob") as HTMLInputElement).value,
    gender: (document.querySelector('input[name="gender"]:checked') as HTMLInputElement).value,
    hobby: Array.from((document.getElementById("hobby") as HTMLSelectElement).selectedOptions).map(option => option.value),
    technology: Array.from((document.getElementById("technology") as HTMLSelectElement).selectedOptions).map(option => option.value),
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
window.onload = function (): void {
  loadAllUsers();
  loadUserDataforEdit(currentIndex);
  attachValidationListeners();
};

