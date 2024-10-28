interface User {
  name: string;
  email: string;
  phone: string;
  zipcode: string;
  dob: string;
  gender: string;
  hobby: string[];
  technology: string[];
}


function validateName(name: string){
  const errorElement = document.getElementById("nameError") as HTMLElement;
  if (name.trim() === "") {
    errorElement.textContent = "* Name is required";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validateEmail(email: string) {
  const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,3}){1,2}$/;
  const errorElement = document.getElementById("emailError") as HTMLElement;
  if (!emailPattern.test(email)) {
    errorElement.textContent = "* Invalid email address";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validatePhone(phone: string){
  const phonePattern = /^(?:\+91)?[0-9]{10}$/;
  const errorElement = document.getElementById("phoneError") as HTMLElement;
  if (!phonePattern.test(phone)) {
    errorElement.textContent = "* Invalid phone number";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validateZipcode(zipcode: string) {
  const zipPattern = /^[0-9]{6}$/;
  const errorElement = document.getElementById("zipcodeError") as HTMLElement;
  if (!zipPattern.test(zipcode)) {
    errorElement.textContent = "* Invalid Zipcode";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validateDob(dob: string) {
  const dobPattern = /^\d{2}-\d{2}-\d{4}$/;
  const errorElement = document.getElementById("dobError") as HTMLElement;

  if (!dobPattern.test(dob)) {
    errorElement.textContent = "* Date of Birth is required. Valid format is MM-DD-YYYY";
    return false;
  } else {
    const [month, day, year] = dob.split("-").map(Number);

    if (month < 1 || month > 12) {
      errorElement.textContent = "* Month must be between 01 and 12";
      return false;
    }

    if (day < 1 || day > 31) {
      errorElement.textContent = "* Day must be between 01 and 31";
      return false;
    }

    const today = new Date();
    const dobDate = new Date(year, month - 1, day);

    if (dobDate > today) {
      errorElement.textContent = "* Date of Birth cannot be in the future";
      return false;
    }
  }
  errorElement.textContent = "";
  return true;
}

function validateGender(gender: string){
  const errorElement = document.getElementById("genderError") as HTMLElement;
  if (!gender) {
    errorElement.textContent = "* Gender is required";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validateHobbies(hobby: string[]){
  const errorElement = document.getElementById("hobbyError") as HTMLElement;
  if (hobby.length === 0) {
    errorElement.textContent = "* At least one hobby must be selected";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validateTechnologies(technology: string[]){
  const errorElement = document.getElementById("technologyError") as HTMLElement;
  if (technology.length === 0) {
    errorElement.textContent = "* At least one technology must be selected";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function clearErrors(): void {
  document
    .querySelectorAll(".error")
    .forEach((error) => (error.textContent = ""));
}

function validateUserData(updatedUserData: User): boolean {
  let isValid = true;
  clearErrors();

  if (!validateName(updatedUserData.name)) isValid = false;
  if (!validateEmail(updatedUserData.email)) isValid = false;
  if (!validatePhone(updatedUserData.phone)) isValid = false;
  if (!validateZipcode(updatedUserData.zipcode)) isValid = false;
  if (!validateDob(updatedUserData.dob)) isValid = false;
  if (!validateGender(updatedUserData.gender)) isValid = false;
  if (!validateHobbies(updatedUserData.hobby)) isValid = false;
  if (!validateTechnologies(updatedUserData.technology)) isValid = false;
  return isValid;
}

function attachValidationListeners(): void {
  document
    .getElementById("name")
    ?.addEventListener("input", () =>
      validateName((document.getElementById("name") as HTMLInputElement).value)
    );
  document
    .getElementById("email")
    ?.addEventListener("input", () =>
      validateEmail((document.getElementById("email") as HTMLInputElement).value)
    );
  document
    .getElementById("phone")
    ?.addEventListener("input", () =>
      validatePhone((document.getElementById("phone") as HTMLInputElement).value)
    );
  document
    .getElementById("zipcode")
    ?.addEventListener("input", () =>
      validateZipcode((document.getElementById("zipcode") as HTMLInputElement).value)
    );
  document
    .getElementById("dob")
    ?.addEventListener("input", () =>
      validateDob((document.getElementById("dob") as HTMLInputElement).value)
    );
  document.querySelectorAll('input[name="gender"]').forEach((radio) => {
    radio.addEventListener("input", (event) =>
      validateGender(
        (document.querySelector('input[name="gender"]:checked') as HTMLInputElement).value
      )
    );
  });
  document
    .getElementById("hobby")
    ?.addEventListener("input", () =>
      validateHobbies(
        Array.from((document.getElementById("hobby") as HTMLSelectElement).selectedOptions).map(
          (option) => option.value
        )
      )
    );
  document
    .getElementById("technology")
    ?.addEventListener("input", () =>
      validateTechnologies(
        Array.from((document.getElementById("technology") as HTMLSelectElement).selectedOptions).map(
          (option) => option.value
        )
      )
    );
}

attachValidationListeners();
