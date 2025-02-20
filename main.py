import asyncio
import secrets
import time
from block import Transaction
from blockchain import N19Chain
from node import Node
from n19crypt import analyze_entropy


async def run_node(port):
    """Запуск одной ноды."""
    blockchain = N19Chain()
    node = Node(blockchain, port)
    print(
        f"Нода на порту {port}: Генезис-блок: Хэш = {blockchain.chain[0].hash[:16]}..."
    )
    await node.run()


async def run_test():
    """Тест блокчейна с несколькими нодами."""
    ports = [5000, 5001, 5002]
    nodes = []

    # Запускаем три ноды
    for port in ports:
        node_task = asyncio.create_task(run_node(port))
        nodes.append(node_task)

    # Даём нодам время запуститься
    await asyncio.sleep(2)

    # Создаём основную цепочку и добавляем блоки
    blockchain = N19Chain()
    node = Node(blockchain, 5000)  # Основная нода
    large_data = secrets.token_bytes(330000)
    block_size = 1000
    blocks = [
        large_data[i : i + block_size] for i in range(0, len(large_data), block_size)
    ]

    start_time = time.time()
    for i, chunk in enumerate(blocks[:330]):  # 330 блоков
        tx = [Transaction("user1", "user2", 19)]
        block = await node.mine_block(tx)
        if i % 50 == 0:
            print(
                f"Блок #{block.index}: Хэш = {block.hash[:16]}..., "
                f"Размер = {len(block.encrypted_data)} байт"
            )

    end_time = time.time()
    print(
        f"Время создания цепочки: {end_time - start_time:.2f} сек"
    )  # Исправлено: start_time
    print(f"Количество блоков: {len(blockchain.chain)}")
    print(f"Цепочка валидна: {blockchain.is_chain_valid()}")
    print(
        f"Энтропия блока #1: {analyze_entropy(blockchain.chain[1].encrypted_data):.4f}"
    )

    # Корректное завершение нод
    for task in nodes:
        task.cancel()
    await asyncio.sleep(1)  # Даём время на завершение


if __name__ == "__main__":
    asyncio.run(run_test())
