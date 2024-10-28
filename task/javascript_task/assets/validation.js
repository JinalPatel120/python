function validateName(name) {
  const errorElement = document.getElementById("nameError");
  if (name.trim() === "") {
    errorElement.textContent = "* Name is required";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validateEmail(email) {
  const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,3}){1,2}$/;
  const errorElement = document.getElementById("emailError");
  if (!emailPattern.test(email)) {
    errorElement.textContent = "* Invalid email address";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validatePhone(phone) {
  const phonePattern = /^(?:\+91)?[0-9]{10}$/;
  const errorElement = document.getElementById("phoneError");
  if (!phonePattern.test(phone)) {
    errorElement.textContent = "* Invalid phone number";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validateZipcode(zipcode) {
  const zipPattern = /^[0-9]{6}$/;
  const errorElement = document.getElementById("zipcodeError");
  if (!zipPattern.test(zipcode)) {
    errorElement.textContent = "* Invalid Zipcode";
    return false;
  }
  errorElement.textContent = "";
  return true;
}


function validateDob(dob) {
    const dobPattern = /^\d{2}-\d{2}-\d{4}$/;
    const errorElement = document.getElementById("dobError");
  
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
  

function validateGender(gender) {
  const errorElement = document.getElementById("genderError");
  if (!gender) {
    errorElement.textContent = "* Gender is required";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validateHobbies(hobby) {
  const errorElement = document.getElementById("hobbyError");
  if (hobby.length === 0) {
    errorElement.textContent = "* At least one hobby must be selected";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function validateTechnologies(technology) {
  const errorElement = document.getElementById("technologyError");
  if (technology.length === 0) {
    errorElement.textContent = "* At least one technology must be selected";
    return false;
  }
  errorElement.textContent = "";
  return true;
}

function clearErrors() {
  document
    .querySelectorAll(".error")
    .forEach((error) => (error.textContent = ""));
}




function validateUserData(updatedUserData) {
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

function attachValidationListeners() {
  document
    .getElementById("name")
    .addEventListener("change", () =>
      validateName(document.getElementById("name").value)
    );
  document
    .getElementById("email")
    .addEventListener("input", () =>
      validateEmail(document.getElementById("email").value)
    );
  document
    .getElementById("phone")
    .addEventListener("change", () =>
      validatePhone(document.getElementById("phone").value)
    );
  document
    .getElementById("zipcode")
    .addEventListener("change", () =>
      validateZipcode(document.getElementById("zipcode").value)
    );
  document
    .getElementById("dob")
    .addEventListener("change", () =>
      validateDob(document.getElementById("dob").value)
    );
  document.querySelectorAll('input[name="gender"]').forEach((radio) => {
    radio.addEventListener("change", (event) =>
      validateGender(
        document.querySelector('input[name="gender"]:checked').value
      )
    );
  });
  document
    .getElementById("hobby")
    .addEventListener("change", () =>
      validateHobbies(
        Array.from(document.getElementById("hobby").selectedOptions).map(
          (option) => option.value
        )
      )
    );
  document
    .getElementById("technology")
    .addEventListener("change", () =>
      validateTechnologies(
        Array.from(document.getElementById("technology").selectedOptions).map(
          (option) => option.value
        )
      )
    );
}

attachValidationListeners();
