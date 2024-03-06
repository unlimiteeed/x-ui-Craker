# x-ui Cracker
x-ui Cracker is a tool for cracking x-ui panels using a list of URLs, usernames, and passwords. It can be used to automate the process of testing multiple combinations of credentials against multiple URLs.

## Features
- Crack x-ui panels using a list of URLs, usernames, and passwords.
- Supports reading credentials from files.
- Saves successful login attempts to a file.
- Color-coded output for better readability.
## Requirements
- Python 3.x
- colorama library (install using pip install colorama)
## Usage
To run the script with default settings:

```
python x-ui.py -lf urls.txt
```
This will use default credentials (admin as username and admin as password) and test them against the URLs listed in urls.txt.

## Advanced Usage
To specify custom usernames and passwords files:

```
python x-ui.py -lf urls.txt -uf usernames.txt -pf passwords.txt
```
This will use the usernames and passwords listed in usernames.txt and passwords.txt respectively.

