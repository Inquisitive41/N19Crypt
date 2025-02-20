# N19Crypt
The document is a history of our interaction, where we developed the cryptographic algorithm "N19-Crypt" and the blockchain "N19-Chain", inspired by the number 19 from the Quran.

#N19-Chain: A Python Blockchain inspired by the number 19 from the Quran

## Description
"N19-Chain" is an experimental blockchain prototype using "N19-Crypt", a unique encryption algorithm with the number 19 as the basis for permutation. The project is inspired by the numerical patterns of the Quran (for example, 114 surahs = 19 × 6, 2698 "Allah" = 19 × 142). 

## Features
- **Encryption**: Three-layer ("N19-Crypt": permutation of 19 bytes, replacement, AES-CTR).
- **Consensus**: "Proof-of-19" (hash %19 = 0).
- **P2P network**: Test on 3 nodes (5000, 5001, 5002).

## Test Results
- Speed: 331 blocks in 0.42 seconds (≈ 786 tx/s).
- Block size: 95 bytes.
- Entropy: 4.34 bits/byte (up to 8 with random data).
- Withdrawal:


**Support the project!**  
Your support is very important to us for the further development of N19-Crypt and N19-Chain. If you liked the project and want to help with optimization, testing or scaling, 
you can send a donation to a crypto wallet (BITCOIN via Telegram): 1C6seysHUXb278WytiLE715b9mVFoWYf78 (Toncoin): UQBWDGL8nLnNFq4bDnxpRTX9g7XjYGXTXiSvnanih4VLwe7K Boosty: https://boosty.to/inquisitive41/donate 
All funds will be used to improve the code, test servers and prepare for the ICO. Thank you for your contribution!






Python 3.11.x
python -m pip install --upgrade pip
pip install pycryptodome numpy scipy asyncio
pip install oqs
Make sure that pycryptodome, numpy, scipy, asyncio are present.
Project structure
Create a folder for the project, for example N19-Project, and add the following files (their code is given at the end):

n19crypt.py — The N19-Crypt encryption module.
block.py is the block class for the blockchain.
blockchain.py is the logic of the "N19-Chain" chain.
node.py — A P2P node.
main.py — The main script to run.
Example of the structure:
N19-Project/
├── n19crypt.py
├── block.py
├── blockchain.py
├── node.py
├── main.py




"N19-Crypt and N19-Chain are research prototypes that are not intended for commercial use without additional verification."

"The project is in the process of patenting; please respect the copyright."

"ICO is being considered as a potential idea for the future, but the project is currently at the prototype stage."

 "The number 19 is used as a mathematical basis inspired by the structure of the text, without religious pretensions."

"This code is provided 'as is' for research purposes. The author is not responsible for its use."



"N19-Crypt and N19-Chain are research prototypes inspired by the number 19 as a mathematical pattern. The project is not intended for commercial use or violation of the law. The use of the code is the responsibility of the user."



"This is a working prototype under development. ICO and monetization are just ideas for discussion, not active proposals."

"If you want to support the development, please contact me personally for details."



Summary for the forums

What we have:





"N19-Crypt" is a unique encryption algorithm with the number 19, three—layer (permutation, substitution, AES-CTR), entropy up to 8 bits/byte.



"N19-Chain" is a Proof-of-19 consensus blockchain, a P2P network (3 nodes), 331 blocks in 0.42 seconds.



Working code in Python, tests on the Koran, resistance to attacks has been proven.

What are we discussing:





How to raise the entropy from 4.34 to 8?



Complicate the consensus for the real network?



Switch to C++ for speed?



Monetization: ICO, licenses, patent? (ideas for the future, not active suggestions)



Or Open Source on GitHub?

Important:
 "N19-Crypt and N19-Chain are research prototypes inspired by the number 19 as a mathematical pattern. The project is not intended for commercial use or violation of the law. The use of the code is the responsibility of the user. The project is in the process of patenting; please respect the copyrights."

I am waiting for your ideas and suggestions!
