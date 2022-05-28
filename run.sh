open -a xQuartz
docker build -t lost-princess .
docker run -it --rm --name testing -e DISPLAY=192.168.1.4:0 -v /tmp/.X11-unix:/tmp/.X11-unix \
  --privileged lost-princess