<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Parking Booking</title>
    <link rel="stylesheet" type="text/css" href="home.css">
</head>
<body>
    <div class="container">
        <h1>Car Parking Booking</h1>
        <form id="bookingForm">
            <label for="name">Name:</label>
            <input type="text" id="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" required pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" placeholder="Format: 123-456-7890">

            <label for="slot">Slot:</label>
            <input type="slot" id="slot" required>

            <label for="numberPlate">Number Plate:</label>
            <input type="text" id="numberPlate" required>
            
            <button type="button" id="bookBtn">Book Parking</button>
        </form>

        <div id="token"></div>
    </div>

    <script src="home.js"></script>
</body>
</html>
