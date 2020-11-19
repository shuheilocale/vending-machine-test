NAME=vending-machine-test
VERSION=0.0.1

docker run -it --rm \
        -v $PWD/src:/usr/src \
        -e RUN_MODE=DEBUG \
        --name $NAME \
        $NAME:$VERSION /bin/bash