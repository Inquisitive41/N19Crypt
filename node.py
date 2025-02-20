import asyncio
from blockchain import N19Chain


class Node:
    def __init__(self, blockchain, port):
        self.blockchain = blockchain
        self.port = int(port)
        self.peers = ["localhost:5001", "localhost:5002"]  # Пример пиров

    async def listen(self):
        server = await asyncio.start_server(self.handle_client, "localhost", self.port)
        async with server:
            await server.serve_forever()

    async def handle_client(self, reader, writer):
        data = await reader.read(100)
        block_hash = data.decode()
        print(f"Получен блок с хэшем на порту {self.port}: {block_hash}")
        writer.close()

    async def broadcast_block(self, block):
        for peer in self.peers:
            try:
                host, port = peer.split(":")
                reader, writer = await asyncio.open_connection(host, int(port))
                writer.write(block.hash.encode())
                await writer.drain()
                writer.close()
            except Exception as e:
                print(f"Ошибка при отправке к {peer} с порта {self.port}: {e}")

    async def mine_block(self, transactions):
        block = self.blockchain.add_block(transactions)
        await self.broadcast_block(block)
        return block

    async def run(self):
        await asyncio.gather(self.listen())
