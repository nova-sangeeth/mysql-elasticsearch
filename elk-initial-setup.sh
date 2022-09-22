echo "Setting up max_map_count..."
sudo sysctl -w vm.max_map_count=262144
echo "Starting Containers"
docker compose down
docker compose build
docker compose up -d
