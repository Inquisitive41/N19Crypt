#include "network.h"
#include <thread>
#include <iostream>

Node::Node(uint16_t port, uint32_t shard) 
    : acceptor_(io_context_, {boost::asio::ip::tcp::v4(), port}), bc_(shard) {
    peers_.push_back("127.0.0.1:5001"); // Пример пиров
}

void Node::start() {
    std::thread([this]() { 
        accept();
        io_context_.run();
    }).detach();
}

void Node::mine_block() {
    std::vector<uint8_t> txs(1000, 't'); // 1000 tx/блок
    bc_.add_block(txs);
    broadcast(bc_.last_block());
}

void Node::broadcast(const Block& block) {
    std::cout << "Блок #" << block.index << ": Хэш = " << block.hash.substr(0, 16) 
              << "..., Размер = " << block.transactions.size() << " байт\n";
    // Gossip-протокол (упрощённо, добавить позже)
}

void Node::accept() {
    acceptor_.async_accept([this](boost::system::error_code ec, boost::asio::ip::tcp::socket socket) {
        if (!ec) {
            std::cout << "Подключение на порту " << acceptor_.local_endpoint().port() << "\n";
        }
        accept();
    });
}