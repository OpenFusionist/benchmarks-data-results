
docker stop gas-execution-client
docker stop gas-execution-client-sync

docker rm gas-execution-client
docker rm gas-execution-client-sync

pkill runMemory.sh
pkill runSpeed.sh
pkill run.sh
