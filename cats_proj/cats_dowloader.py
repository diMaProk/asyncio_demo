from time import time

import requests


def get_file(url):
    response = requests.get(url, allow_redirects=True)
    return response


def write_file(response):
    filename = f'cats/file-sync-{int(time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    url = 'https://loremflickr.com/320/240'
    for _ in range(20):
        write_file(get_file(url))


if __name__ == '__main__':
    print('Downloading started ...')
    n = 3
    exec_time = 0
    for _ in range(3):
        start = time()
        main()
        delta = time() - start
        print(delta)
        exec_time += delta
    print(f'Average: {round(exec_time/n, 2)}')
