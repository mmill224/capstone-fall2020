<?php
$dbServername = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "focalPoint";

$conn = new mysqli($dbServername, $dbUsername, $dbPassword, $dbName);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>