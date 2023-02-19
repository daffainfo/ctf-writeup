# Bruh
`-`

## About the Challenge
We are given a website and a file (You can get the file [here](index.php))
```php
<?php

$servername = "127.0.0.1";
$username = "ctf";
$dbname = "login";
$password = "ctf123";

// Create connection
$conn = new mysqli($servername, $username, $password,$dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if(!empty($_GET['username']) && !empty($_GET['password']))
{
    $username=mysqli_real_escape_string($conn,$_GET['username']);
    $password=mysqli_real_escape_string($conn,$_GET['password']);
    if (preg_match("/admin/i",$username) && $_SERVER['REMOTE_ADDR']!=="127.0.0.1")
    {
        die("Admins login are allowed locally only");
    }
    else
    {
        $res=$conn->query("select * from users where username='$username' and password='$password'"); # admin admin
        if($res->num_rows > 0)
        {
            $user=$res->fetch_assoc();
            echo ($user['username']==="admin")?"0xL4ugh{test_flag}":"sorry u r not admin";
        }
        else
        {
            echo "Error : Wrong Creds";
        }

    }
}
else
{
    echo "Please Fill All Fields";
}
?>
```

To print the flag, we need to request to the website with 2 parameter, `username` and `password` and the value of these 2 parameters is `admin`. But there is some check, we can input an `admin` in the username.

## How to Solve?
We need to bypass `preg_match("/admin/i",$username)` this code by using unicode character. So from `admin` to `ádmin` will bypass the check and the website will print the flag

```
0xL4ugh{My_Broo_Ag@in_fREE_pALESTINE}
```