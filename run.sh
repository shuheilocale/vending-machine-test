NAME=vending-machine-test
VERSION=0.0.1

docker run -it --rm \
        -v $PWD/src:/usr/src \
        --name $NAME \
        $NAME:$VERSION python3.9 run.py