#!/bin/bash
for i in {1..3}; do
    ./n19vrf & # Запуск 3 узлов
done
sleep 10
pkill n19vrf