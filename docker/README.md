docker pull --platform=linux/arm64 ghcr.io/sagernet/sing-box:v1.9.4
docker images 
# 查找镜像ID
docker images | grep sing-box

docker save xxxxxxx > sing-box-yjs.tar

