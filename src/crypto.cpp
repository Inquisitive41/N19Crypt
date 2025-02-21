#include "crypto.h"
#include <openssl/bn.h>
#include <openssl/rand.h>

KeyPair generate_keypair()
{
    KeyPair kp;
    kp.ec_key = EC_KEY_new_by_curve_name(NID_secp256k1);
    if (!kp.ec_key || !EC_KEY_generate_key(kp.ec_key))
    {
        EC_KEY_free(kp.ec_key);
        throw std::runtime_error("Failed to generate EC key");
    }
    kp.sphincs_sk.resize(64); // Упрощённый SPHINCS+ (64 байта SK, 32 байта PK)
    kp.sphincs_pk.resize(32);
    if (RAND_bytes(kp.sphincs_sk.data(), 64) <= 0 || RAND_bytes(kp.sphincs_pk.data(), 32) <= 0)
    {
        throw std::runtime_error("Failed to generate random bytes");
    }
    return kp;
}

VRFResult vrf_generate(const std::string &input, const KeyPair &kp)
{
    VRFResult res;
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char *)input.c_str(), input.size(), hash);
    res.output.assign(hash, hash + SHA256_DIGEST_LENGTH);
    res.proof = res.output; // Упрощённый proof (в реальном VRF сложнее)
    return res;
}

bool vrf_verify(const std::string &input, const VRFResult &vrf, const KeyPair &kp)
{
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char *)input.c_str(), input.size(), hash);
    std::vector<uint8_t> expected(hash, hash + SHA256_DIGEST_LENGTH);
    return expected == vrf.output;
}