#include "blockchain.h"
#include <chrono>

Block::Block(uint64_t idx, const std::vector<std::string> &prevs, const std::vector<uint8_t> &txs, const KeyPair &kp)
    : index(idx), prev_hashes(prevs), transactions(txs)
{
    timestamp = std::to_string(std::chrono::system_clock::now().time_since_epoch().count());
    std::string vrf_input = timestamp + (prevs.empty() ? "0" : prevs[0]);
    vrf = vrf_generate(vrf_input, kp);

    std::string input = std::to_string(index) + timestamp +
                        std::string(vrf.output.begin(), vrf.output.end());
    for (const auto &ph : prev_hashes)
        input += ph;
    input.insert(input.end(), transactions.begin(), transactions.end());
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char *)input.c_str(), input.size(), hash);
    this->hash = std::string((char *)hash, SHA256_DIGEST_LENGTH);
}

bool Block::verify_po19_vrf(const KeyPair &kp, uint64_t target) const
{
    uint64_t output_int = *(uint64_t *)vrf.output.data();
    return (output_int % 19 == 0) && (output_int < target) &&
           vrf_verify(timestamp + (prev_hashes.empty() ? "0" : prev_hashes[0]), vrf, kp);
}

Blockchain::Blockchain(uint32_t shard) : shard_id_(shard)
{
    kp_ = generate_keypair();
    target_ = UINT64_MAX / (19 * 100 * 10); // 100 узлов, 0.1 сек
    dag_.emplace_back(0, std::vector<std::string>{"0"}, std::vector<uint8_t>(1000, 'g'), kp_);
}

void Blockchain::add_block(const std::vector<uint8_t> &txs)
{
    std::vector<std::string> prevs;
    size_t start = dag_.size() > 5 ? dag_.size() - 5 : 0;
    for (size_t i = start; i < dag_.size(); i++)
        prevs.push_back(dag_[i].hash);
    Block new_block(dag_.size(), prevs, txs, kp_);
    if (new_block.verify_po19_vrf(kp_, target_))
    {
        dag_.push_back(new_block);
    }
}

bool Blockchain::validate() const
{
    for (size_t i = 1; i < dag_.size(); i++)
    {
        if (!dag_[i].verify_po19_vrf(kp_, target_))
            return false;
    }
    return true;
}