import platform
from ipaddress import ip_address
import threading
from subprocess import Popen, PIPE

google = ip_address('64.233.191.200')
yandex = ip_address('8.8.8.8')
my_ip = ip_address('185.165.163.94')

ip_list = [google, yandex, my_ip]
list_with_ip = []


def host_ping(ip_adr, on_print):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    with Popen(['ping', param, '1', ip_adr], stdout=PIPE, stderr=PIPE) as response:
        if response.wait() == 0:
            list_with_ip.append({'Reachable': ip_address(ip_adr)})
            if on_print:
                print(f'Узел доступен {ip_adr}')
            return True
        else:
            list_with_ip.append({'Unreachable': ip_address(ip_adr)})
            if on_print:
                print(f'Узел недоступен {ip_adr}')
            return False


def thread_ping(ip_list, on_print=True):
    th_list = []
    for ip_adr in ip_list:
        th_list.append(threading.Thread(target=host_ping, args=(str(ip_adr), on_print,)))

    for th in th_list:
        th.start()

    for t in th_list:
        t.join()

    list_with_ip.sort(key=lambda x: x.get('Reachable') or x.get('Unreachable'))


if __name__ == '__main__':
    thread_ping(ip_list)
