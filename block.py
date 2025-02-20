import hashlib
import json
from n19crypt import encrypt_n19


class Transaction:
    """Класс транзакции."""

    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def to_dict(self):
        return {"sender": self.sender, "receiver": self.receiver, "amount": self.amount}


class Block:
    """Класс блока в N19-Chain."""

    def __init__(self, index, previous_hash, transactions, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        tx_data = json.dumps([tx.to_dict() for tx in transactions]).encode()
        self.encrypted_data, self.salt, self.enc_timestamp = encrypt_n19(
            tx_data + bytes.fromhex(previous_hash)
        )
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Вычисление хэша блока с консенсусом Proof-of-19."""
        while True:
            value = (
                str(self.index)
                + self.previous_hash
                + self.encrypted_data.hex()
                + str(self.timestamp)
                + str(self.nonce)
            ).encode()
            hash_result = hashlib.sha256(value).hexdigest()
            hash_int = int(hash_result, 16)
            if hash_int % 19 == 0:  # Po19
                return hash_result
            self.nonce += 1

    def to_dict(self):
        """Сериализация блока в словарь."""
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "timestamp": self.timestamp,
            "encrypted_data": self.encrypted_data.hex(),
            "salt": self.salt.hex(),
            "enc_timestamp": self.enc_timestamp.hex(),
            "nonce": self.nonce,
            "hash": self.hash,
        }
