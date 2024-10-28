interface User {
    id: number;
    name: string;
    email: string;
    phone: string;
    zipcode: string;
    dob: string;
    gender: string;
    hobby: string[];
    technology: string[];
  }
  
  document.getElementById('registerForm')?.addEventListener('submit', function (event: Event) {
    event.preventDefault();
  
    const id: number = Date.now();
    const userData: User = {
      id: id,
      key: id.toString(),
      name: (document.getElementById('name') as HTMLInputElement).value,
      email: (document.getElementById('email') as HTMLInputElement).value,
      phone: (document.getElementById('phone') as HTMLInputElement).value,
      zipcode: (document.getElementById('zipcode') as HTMLInputElement).value,
      dob: (document.getElementById('dob') as HTMLInputElement).value,
      gender: (document.querySelector('input[name="gender"]:checked') as HTMLInputElement)?.value || '',
      hobby: Array.from((document.getElementById('hobby') as HTMLSelectElement).selectedOptions).map(option => option.value),
      technology: Array.from((document.getElementById('technology') as HTMLSelectElement).selectedOptions).map(option => option.value)
    };
  
    if (validateUserData(userData)) {
      localStorage.setItem(id.toString(), JSON.stringify(userData));
      alert('Registration successful!');
      (document.getElementById('registerForm') as HTMLFormElement).reset();
    }
  });
  
  attachValidationListeners();
  