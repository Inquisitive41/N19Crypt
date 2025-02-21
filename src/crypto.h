#ifndef CRYPTO_H
#define CRYPTO_H

#include <openssl/ec.h>
#include <openssl/sha.h>
#include <vector>
#include <string>

struct KeyPair
{
    EC_KEY *ec_key;                  // EC-VRF ключи
    std::vector<uint8_t> sphincs_sk; // SPHINCS+ секретный ключ
    std::vector<uint8_t> sphincs_pk; // SPHINCS+ публичный ключ
    KeyPair() : ec_key(nullptr) {}
    ~KeyPair()
    {
        if (ec_key)
            EC_KEY_free(ec_key);
    }
};

struct VRFResult
{
    std::vector<uint8_t> output;
    std::vector<uint8_t> proof;
};

KeyPair generate_keypair();
VRFResult vrf_generate(const std::string &input, const KeyPair &kp);
bool vrf_verify(const std::string &input, const VRFResult &vrf, const KeyPair &kp);

#endif