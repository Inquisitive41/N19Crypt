#include "blockchain.h"
#include <cassert>
#include <iostream>

void test_vrf()
{
    KeyPair kp = generate_keypair();
    VRFResult vrf = vrf_generate("test", kp);
    assert(vrf_verify("test", vrf, kp));
    std::cout << "VRF тест пройден\n";
}

void test_dag()
{
    Blockchain bc;
    bc.add_block(std::vector<uint8_t>(1000, 't'));
    assert(bc.size() == 2);
    assert(bc.validate());
    std::cout << "DAG тест пройден\n";
}

int main()
{
    test_vrf();
    test_dag();
    return 0;
}