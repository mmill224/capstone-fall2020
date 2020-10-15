<?php
//$dbPort = "3306"

$dbServername = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "airline";

$conn = new mysqli(/*$dbPort*/ $dbServername, $dbUsername, $dbPassword, $dbName);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

$conn = new mysqli($dbServername, $dbUsername, $dbPassword, $dbName);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?