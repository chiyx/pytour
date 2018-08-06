# -*- coding: UTF-8 -*-

import sys
import asyncio

from charfinder import UnicodeNameIndex


CRLF = b'\r\n'
PROMPT = b'?> '

index = UnicodeNameIndex()  # <2>


@asyncio.coroutine
def handle_queries(reader, writer):
    while True:
        writer.write(PROMPT)
        yield from writer.drain()
        data = yield from reader.readline()
        try:
            query = data.decode().strip()
        except UnicodeDecodeError:
            query = '\x00'
        client = writer.get_extra_info('peername')  # <9>
        print('Received from {}: {!r}'.format(client, query))  # <10>
        if query:
            if ord(query[:1]) < 32:  # <11>
                break
            lines = list(index.find_description_strs(query))  # <12>
            if lines:
                writer.writelines(
                    line.encode() + CRLF for line in lines)  # <13>
            writer.write(index.status(
                query, len(lines)).encode() + CRLF)  # <14>
            yield from writer.drain()  # <15>
            print('Sent {} results'.format(len(lines)))  # <16>


# BEGIN TCP_CHARFINDER_MAIN
def main(address='127.0.0.1', port=2323):  # <1>
    port = int(port)
    loop = asyncio.get_event_loop()
    server_coro = asyncio.start_server(handle_queries, address, port,
                                       loop=loop)  # <2>
    server = loop.run_until_complete(server_coro)  # <3>

    host = server.sockets[0].getsockname()  # <4>
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))  # <5>
    try:
        loop.run_forever()  # <6>
    except KeyboardInterrupt:  # CTRL+C pressed
        pass

    print('Server shutting down.')
    server.close()  # <7>
    loop.run_until_complete(server.wait_closed())  # <8>
    loop.close()  # <9>


if __name__ == '__main__':
    main(*sys.argv[1:])  # <10>
# END TCP_CHARFINDER_MAIN
