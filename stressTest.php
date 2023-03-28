<?php
// define the MySQL connection settings
$servername = "localhost";
$username = "yourusername";
$password = "yourpassword";
$dbname = "yourdatabase";

// create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// define the query to be executed
$query = "SELECT * FROM yourtable";

// define the number of times to execute the query
$num_iterations = 100;

// execute the query for the given number of times
$start_time = microtime(true); // start timer
for ($i = 0; $i < $num_iterations; $i++) {
    $result = $conn->query($query);
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "id: " . $row["id"]. " - Name: " . $row["name"]. " - Email: " . $row["email"]. "<br>";
        }
    } else {
        echo "0 results";
    }
}
$end_time = microtime(true); // end timer

// calculate and print the time taken to execute the queries
echo "Time taken to execute the query " . $num_iterations . " times: " . ($end_time - $start_time) . " seconds";

// close connection
$conn->close();
?>
