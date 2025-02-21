#ifndef BLOCKCHAIN_H
#define BLOCKCHAIN_H

#include "crypto.h"
#include <vector>
#include <string>

struct Block
{
    uint64_t index;
    std::vector<std::string> prev_hashes; // DAG ссылки
    std::vector<uint8_t> transactions;
    std::string timestamp;
    VRFResult vrf;
    std::string hash;

    Block(uint64_t idx, const std::vector<std::string> &prevs, const std::vector<uint8_t> &txs, const KeyPair &kp);
    bool verify_po19_vrf(const KeyPair &kp, uint64_t target) const;
};

class Blockchain
{
    std::vector<Block> dag_;
    KeyPair kp_;
    uint64_t target_;
    uint32_t shard_id_;

public:
    Blockchain(uint32_t shard = 0);
    void add_block(const std::vector<uint8_t> &txs);
    bool validate() const;
    uint64_t size() const { return dag_.size(); }
    const Block &last_block() const { return dag_.back(); }
};

#endif