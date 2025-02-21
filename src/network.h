#ifndef NETWORK_H
#define NETWORK_H

#include "blockchain.h"
#include <boost/asio.hpp>
#include <memory>

class Node
{
    boost::asio::io_context io_context_;
    boost::asio::ip::tcp::acceptor acceptor_;
    Blockchain bc_;
    std::vector<std::string> peers_;

public:
    Node(uint16_t port, uint32_t shard = 0);
    void start();
    void mine_block();
    void broadcast(const Block &block);

private:
    void accept();
};

#endif