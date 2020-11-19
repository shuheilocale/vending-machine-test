NAME=vending-machine-test
VERSION=0.0.1

docker build -t $NAME:$VERSION .
docker run -it --rm \
        -v $PWD/src:/usr/src \
        --name $NAME \
        $NAME:$VERSION /bin/bash