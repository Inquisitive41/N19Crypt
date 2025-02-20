import hashlib
import secrets
import time
from Crypto.Cipher import AES
from Crypto.Util import Counter
from scipy.stats import entropy
import numpy as np


def generate_key(data, size):
    """Генерация динамических ключей на основе текста, соли и времени."""
    salt = secrets.token_bytes(16)
    timestamp = str(int(time.time())).encode()
    hash_input = data + salt + timestamp
    seed = int(hashlib.sha256(hash_input).hexdigest(), 16)
    return [(seed + i * 19) % len(data) for i in range(size)], salt, timestamp


def encrypt_n19(data):
    """Шифрование данных с помощью N19-Crypt."""
    key_positions, salt, timestamp = generate_key(data, len(data))

    # Уровень 1: Перестановка блоков по 19 байт
    blocks = [data[i : i + 19] for i in range(0, len(data), 19)]
    if len(blocks[-1]) < 19:
        blocks[-1] += b"\x00" * (19 - len(blocks[-1]))
    indices = np.argsort(key_positions[: len(blocks)])
    permuted = [blocks[i] for i in indices]
    permuted_data = b"".join(permuted)

    # Уровень 2: Нелинейная замена
    replaced = bytearray()
    for i, byte in enumerate(permuted_data):
        replaced.append((byte + key_positions[i % len(key_positions)]) % 256)

    # Уровень 3: AES-CTR
    aes_key = hashlib.sha256(data + salt).digest()[:16]
    ctr = Counter.new(128, initial_value=int.from_bytes(timestamp[:16], "big"))
    cipher = AES.new(aes_key, AES.MODE_CTR, counter=ctr)
    encrypted = cipher.encrypt(replaced)

    return encrypted, salt, timestamp


def decrypt_n19(encrypted, salt, timestamp):
    """Расшифровка данных."""
    data = encrypted
    key_positions, _, _ = generate_key(data, len(data))

    aes_key = hashlib.sha256(data + salt).digest()[:16]
    ctr = Counter.new(128, initial_value=int.from_bytes(timestamp[:16], "big"))
    cipher = AES.new(aes_key, AES.MODE_CTR, counter=ctr)
    replaced = cipher.decrypt(data)

    permuted = bytearray()
    for i, byte in enumerate(replaced):
        permuted.append((byte - key_positions[i % len(key_positions)]) % 256)

    blocks = [permuted[i : i + 19] for i in range(0, len(permuted), 19)]
    indices = np.argsort(key_positions[: len(blocks)])
    original = [None] * len(blocks)
    for i, idx in enumerate(indices):
        original[idx] = blocks[i]
    decrypted = b"".join(original).rstrip(b"\x00")

    return decrypted


def analyze_entropy(data):
    """Анализ энтропии данных."""
    bytes_data = np.frombuffer(data, dtype=np.uint8)
    return entropy(np.histogram(bytes_data, bins=256, density=True)[0])


if __name__ == "__main__":
    text = b"Bismi Allahi Arrahmani Arrahim"
    encrypted, salt, timestamp = encrypt_n19(text)
    decrypted = decrypt_n19(encrypted, salt, timestamp)
    print(f"Оригинал: {text}")
    print(f"Зашифровано: {encrypted.hex()[:32]}...")
    print(f"Расшифровано: {decrypted}")
    print(f"Энтропия: {analyze_entropy(encrypted):.4f}")
