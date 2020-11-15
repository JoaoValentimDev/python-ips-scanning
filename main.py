#!/venv/bin/python
from Network import Network
from utils.c_print import c_print
from os import getlogin


def main():
    try:
        c_print("Scanning v1.0", "purple", "underline")
        net = Network()
        net.start()
    except KeyboardInterrupt:
        c_print(f"Scanning cancelado pelo usuário {getlogin()} :(", "red")
    else:
        exit(0)


if __name__ == '__main__':
    main()
