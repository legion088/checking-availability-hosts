import asyncio
import aioping
import os


async def check_available_hosts(hostname: str):
    try:
        await aioping.ping(hostname) * 1000
        print("UP", hostname)
    except TimeoutError:
        print("DOWN:", hostname)
    except Exception as err:
        print(f"Возникло исключение для {hostname}", err)


def check_validation_lines(lines: list) -> list:
    if not lines:
        raise ValueError("Файл пустой!")
    forbidden_characters = [
        ',', '~', ':', '!', ' ', '@', '#',
        '$', '%', '^', '&', '`', '.', '()',
        '{}', '_'
    ]

    if any(char in line for char in forbidden_characters for line in lines):
        raise ValueError("Строка содержит запрещающий символ!")
    return [line.strip() for line in lines]


def open_readlines_file(file: str) -> list:
    with open(file, "r") as f:
        return f.readlines()


def run(hosts: list):
    coroutines = [check_available_hosts(host) for host in hosts]
    tasks = [asyncio.ensure_future(coroutine) for coroutine in coroutines]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))


if __name__ == '__main__':
    lines = open_readlines_file("hosts.txt")
    hosts = check_validation_lines(lines)
    run(hosts)
    os.system("pause")	
