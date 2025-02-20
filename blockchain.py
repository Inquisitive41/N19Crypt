import time  # Исправление: добавлен импорт
from block import Block, Transaction


class N19Chain:
    """Класс блокчейна N19-Chain."""

    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Создание генезис-блока."""
        genesis_tx = [Transaction("genesis", "network", 19000000)]  # 19 млн токенов
        return Block(0, "0" * 64, genesis_tx, int(time.time()))

    def get_latest_block(self):
        """Получение последнего блока."""
        return self.chain[-1]

    def add_block(self, transactions):
        """Добавление нового блока."""
        previous_block = self.get_latest_block()
        new_block = Block(
            previous_block.index + 1,
            previous_block.hash,
            transactions,
            int(time.time()),
        )
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        """Проверка целостности цепочки."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
            if int(current.hash, 16) % 19 != 0:
                return False
        return True
