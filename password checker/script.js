function checkPassword() {
    var password = document.getElementById("password").value;
    var strengthText = document.getElementById("result");
    var progressBar = document.getElementById("progress");
  var percentage = document.getElementById("strength-percentage");

  
    var score = 0;
    var length = password.length;
    var hasUpper = /[A-Z]/.test(password);
    var hasLower = /[a-z]/.test(password);
    var hasDigit = /\d/.test(password);
    var hasSpecial = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password);
  
    // Length
    if (length >= 8) {
      score += 1;
    }
    if (length >= 12) {
      score += 1;
    }
    if (length >= 16) {
      score += 1;
    }
  
    // Other criteria
    if (hasUpper) {
      score += 1;
    }
    if (hasLower) {
      score += 1;
    }
    if (hasDigit) {
      score += 1;
    }
    if (hasSpecial) {
      score += 1;
    }
    // Calculate percentage
  var strengthPercentage = (score / 8) * 100;
  progressBar.style.width = strengthPercentage + "%";
  percentage.innerHTML = Math.round(strengthPercentage) + "%";

  
    // Feedback
    var strength = "";
    if (score <= 2) {
      strength = "Weak";
    } else if (score <= 4) {
      strength = "Moderate";
    } else {
      strength = "Strong";
    }
  
    strengthText.innerHTML = "Your password strength is: " + strength;
  }
  