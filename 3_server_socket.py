import asyncio


async def handle_connection(reader, writer):
    peername = writer.get_extra_info('peername')
    print(f'Connection from {peername}')
    while True:
        try:
            request = await asyncio.wait_for(reader.readline(), timeout=10.0)
            if request:
                print(f'Received: {request.decode()}')
                writer.write(b'Hello from server\n')
            else:
                print(f'Connection from {peername} closed by peer')
                break
        except asyncio.TimeoutError:
            print(f'Connection from {peername} closed by timeout')
            break
    writer.close()


async def main():
    server = await asyncio.start_server(client_connected_cb=handle_connection, host='localhost', port=5000)
    addr = server.sockets[0].getsockname()
    print(f'Server started on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Server stopped')
