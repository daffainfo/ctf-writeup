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
    if ($username=="admin" && $_SERVER['REMOTE_ADDR']!=="127.0.0.1")
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

To print the flag, we need to send a request to the website with 2 parameters, `username` and `password` and the value of these 2 parameters is `admin`. But there is some check, we can input an `admin` in the username.

## How to Solve?
We need to bypass `$username=="admin"` this code by capitalizing one of the character. So from `admin` to `aDmin` will bypass the check and the website will print the flag

```
0xL4ugh{oH_mY_BruuoohH_pLAEStine_iN_our_Hearts}
```