document.getElementById("bookBtn").addEventListener("click", function() {
    generateToken();
});

function generateToken() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var numberPlate = document.getElementById("numberPlate").value;

    // Generate token (dummy example)
    var token = name.substring(0, 3).toUpperCase() + '-' + Math.random().toString(36).substr(2, 9).toUpperCase();

    // Display token
    document.getElementById("token").innerHTML = "Your parking booking token is: " + token;
}
