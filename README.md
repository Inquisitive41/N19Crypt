# N19Crypt
Документ представляет собой историю нашего взаимодействия, где мы разработали криптографический алгоритм "N19-Crypt" и блокчейн "N19-Chain", вдохновлённые числом 19 из Корана.
**Поддержите проект!**  
Нам очень важна ваша поддержка для дальнейшего развития "N19-Crypt" и "N19-Chain". Если вам понравился проект и вы хотите помочь с оптимизацией, тестами или масштабированием, 
вы можете отправить донат на криптокошелёк (BITCOIN через Телеграм): 1C6seysHUXb278WytiLE715b9mVFoWYf78    (Toncoin): UQBWDGL8nLnNFq4bDnxpRTX9g7XjYGXTXiSvnanih4VLwe7K   
Все средства пойдут на улучшение кода, серверы для тестов и подготовку к ICO. Спасибо за ваш вклад!






Python 3.11.x
python -m pip install --upgrade pip
pip install pycryptodome numpy scipy asyncio
pip install oqs
Убедитесь, что pycryptodome, numpy, scipy, asyncio присутствуют.
Структура проекта
Создайте папку для проекта, например N19-Project, и добавьте следующие файлы (их код приведён в конце):

n19crypt.py — Модуль шифрования "N19-Crypt".
block.py — Класс блока для блокчейна.
blockchain.py — Логика цепочки "N19-Chain".
node.py — P2P-нода.
main.py — Основной скрипт для запуска.
Пример структуры:
N19-Project/
├── n19crypt.py
├── block.py
├── blockchain.py
├── node.py
├── main.py
