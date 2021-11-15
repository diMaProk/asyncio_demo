import asyncio
from time import time

import aiohttp


async def get_file(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_file(data)


def write_file(data):
    filename = f'cats/file-async-{int(time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)


async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(20):
            task = asyncio.create_task(get_file(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    print('Downloading started ...')
    n = 3
    exec_time = 0
    for _ in range(3):
        start = time()
        asyncio.run(main())
        delta = time() - start
        print(delta)
        exec_time += delta
    print(f'Average: {round(exec_time / n, 2)}')