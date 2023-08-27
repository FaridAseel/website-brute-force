# website-brute-force

Brute Force1: Brute Force with Username and Password Lists
This code is designed for Brute Force attacks on a login page using various combinations of usernames and passwords from provided lists.
It begins by reading lists of usernames and passwords from separate files. 
It then systematically sends POST requests to the specified URL (page_url) with different combinations of credentials.
If a successful login attempt is detected, the script prints the matched credentials and exits.
If no valid credentials are found, it displays a message indicating that no matching username-password combination was located in the provided lists.

CBrute Force2: Brute Force with Username Input
This code accepts a username as input and attempts Brute Force attacks on a login page using a list of passwords.
It reads the list of passwords from a file, and for each password in the list,
it sends a POST request to the specified URL (page_url) with the provided username and the current password.
If a successful login attempt is detected, the script prints the matched credentials and exits.
If no valid credentials are found after trying all passwords, it displays a message indicating that the password was not found in the list.

Please keep in mind that the ethical and responsible use of these scripts is crucial.
Unauthorized penetration testing or attempting to gain unauthorized access to systems is illegal and unethical. 
Always ensure you have proper authorization before testing or using these scripts on any system.
