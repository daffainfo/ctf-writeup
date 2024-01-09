# babystrechy
> More byte mean more secure

> Although this is a web challenge, the script is ran directly with PHP because it doesn't need to have an HTML website attached. Run the command below to connect!

## About the Challenge
We are given a PHP file like the code below
```php
<?php
$password = exec("openssl rand -hex 64");

$stretched_password = "";
for($a = 0; $a < strlen($password); $a++) {
    for($b = 0; $b < 64; $b++)
        $stretched_password .= $password[$a];
}

echo "Fear my 4096 byte password!\n> ";

$h = password_hash($stretched_password, PASSWORD_DEFAULT);

while (FALSE !== ($line = fgets(STDIN))) {
    if(password_verify(trim($line), $h)) die(file_get_contents("flag"));
    echo "> ";
}
die("No!");

?>
```
So the code will generate a password of 64 hex characters
```php
$password = exec("openssl rand -hex 64");
```
And then each character will be repeated up to 64 times
```php
$stretched_password = "";
for($a = 0; $a < strlen($password); $a++) {
    for($b = 0; $b < 64; $b++)
        $stretched_password .= $password[$a];
}
```
After stretch the password, the stretched password will be hashed using `password_hash` function
```php
$h = password_hash($stretched_password, PASSWORD_DEFAULT);
```
The code will check your input, if your input passes `password_verify` function, and then the code will print the flag
```php
while (FALSE !== ($line = fgets(STDIN))) {
    if(password_verify(trim($line), $h)) die(file_get_contents("flag"));
    echo "> ";
}
die("No!");
```

## How to Solve?
Simply by creating a python script to bruteforce the hash. You can check the code [**here**](https://github.com/kos0ng/ctf-writeups/blob/master/solver/2023/irisctf/web/babystretch/solver.py). After running the code we will retrieve the flag
```
irisctf{truncation_silent_and_deadly}
```