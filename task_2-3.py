from ipaddress import ip_address
from task_1 import thread_ping
from tabulate import tabulate
from task_1 import list_with_ip


def host_range_ping(on_print=True):
    list_ip = []

    start_adress = input("Введите ip адрес: ")

    octets = start_adress.split('.')
    try:
        if octets[3] != '0':
            print("Последняя цифра октета должна быть 0")
            return

    except ValueError:
        print('Некорректный ip')

    list_octets = int(input('Введите количество адресов(не больше 255): '))

    if list_octets > 255:
        print('КОЛИЧЕСТВО БОЛЬШЕ 255')
        return

    for i in range(0, list_octets + 1):
        ip = int(ip_address(start_adress)) + i
        list_ip.append(ip_address(ip))

    thread_ping(list_ip, on_print)


def for_table():
    host_range_ping(False)


if __name__ == "__main__":
    for_table()
    print(tabulate(list_with_ip, headers='keys', tablefmt='grid', stralign='center'))
