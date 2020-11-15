from socket import AddressFamily
from networkscan import Networkscan
from psutil import net_if_addrs
from os import getlogin
from datetime import datetime, date
from time import sleep
from utils.c_print import c_print
from utils.c_text_line import c_text
from threading import Thread


class Network(Thread):
    date_now = datetime.now()
    date_str = date.today().strftime('%d/%m/%Y')

    def __init__(self, ip_address="192.168.0.0/24"):
        Thread.__init__(self)
        self.ip_address = ip_address
        self.scan_time = f"{c_text('Scanning realizado as', 'blue')} {c_text(f'{self.date_now.hour}:{self.date_now.minute}:{self.date_now.second}', 'cyan')} " \
                         f"{c_text('de ', 'blue')}"
        self.scan_time += f"{c_text(f'{self.date_str}', 'yellow')}{c_text(' 🔎 :', 'blue')}\n"
        self.machine_ip = self.get_machine_ip()
        c_print(f"Máquina que pediu scanning {c_text(f'{self.machine_ip}/{getlogin()}. {self.scan_time}', 'green')}",
                "blue")

    @staticmethod
    def get_machine_ip():
        my_machine_ip = ""
        for ip in net_if_addrs():
            family = net_if_addrs()[ip][0][0]
            mask = net_if_addrs()[ip][0][2]
            if family == AddressFamily.AF_INET and mask == "255.255.255.0":
                my_machine_ip = net_if_addrs()[ip][0][1]

        return my_machine_ip

    def run_scan(self):
        scan = Networkscan(self.ip_address)
        count_number = 0
        scan.run()
        c_print("=" * 22, "green")
        for ip in scan.list_of_hosts_found:
            count_number += 1
            c_print(f"{count_number}# {ip}", 'green')
        c_print("=" * 22, "green")
        c_print("\nFinalizando aguarde...", "yellow")
        sleep(2)
        c_print(f"IP(s) encontrado(s): {count_number}", "yellow")
        c_print("Scanning finalizado com sucesso :)", "cyan")

    def run(self):
        self.run_scan()
