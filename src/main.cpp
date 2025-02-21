#include "network.h"
#include <chrono>
#include <thread>

int main()
{
    Node node1(5000, 0);
    Node node2(5001, 1);
    node1.start();
    node2.start();

    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < 1000; i++)
    {
        node1.mine_block();
        std::this_thread::sleep_for(std::chrono::milliseconds(100)); // 0.1 сек/блок
        if (i % 100 == 0)
        {
            std::cout << "Создан блок #" << i << "\n";
        }
    }
    auto end = std::chrono::high_resolution_clock::now();
    double duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() / 1e6;
    std::cout << "Время: " << duration << " сек\n";
    std::cout << "Скорость: " << 1000 / duration << " блоков/сек\n";
    std::cout << "TPS: " << (1000 * 1000) / duration << " tx/s\n";
    return 0;
}