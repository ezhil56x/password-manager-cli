# Password Manager CLI

## Description

The Password Manager is a command-line tool that allows you to store, retrieve and generate passwords securely. It provides a simple way to manage your passwords without having to remember them. This tool uses a master password to secure your passwords. The master password is configured when you first run the tool and is used to encrypt and decrypt your passwords. It is written in Python and uses the cryptography module and mariadb or mysql server to store the passwords. This tool uses `pyperclip` module to copy the password to the clipboard.

## Requirements

- Python 3.6 or higher
- mariadb or mysql server

## Installation

1. Clone the repository

```
git clone https://github.com/ezhil56x/password-manager-cli.git
```

2. Go to password-manager-cli directory

```
cd password-manager-cli
```

3. Install mariadb or mysql server

```
sudo apt install mariadb-server
```

4. Login to mariadb or mysql server and create a user

```
sudo mysql -u root
```

```
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';
```

5. Install the required packages using the following command

```
pip install -r requirements.txt
```

## Usage

1. Run --config for the first time to configure the master password and databases

```
python password_manager.py --config
```

2. To store a new credential, run the following command

```
python password_manager.py --operation store --master-password <master-password> --service <servicename> --password <password>
```

3. To retrieve a credential, run the following command

```
python password_manager.py --operation retrieve --master-password <master-password> --search <search>
```

4. To generate a password, run the following command

```
python password_manager.py --operation generate --length <length>
```

5. For help, run the following command

```
python password_manager.py --help
```
