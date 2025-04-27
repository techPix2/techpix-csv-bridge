echo "Montando container flask"
docker build -t flasks3 .
docker run --name flasks3-container -p 5000:5000 --restart unless-stopped -d flasks3