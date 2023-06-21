# gRPC in Google Cloud Run
** Key feature here is that the server.py listens on the PORT defined in the environment variable PORT.

## files included
- speaker.proto
- client.py
- server.py 
- requirements.txt
- Dockerfile

## generate grpc stub using python library grpc_tools
>python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. speaker.proto

## test
```
SET PORT=5150
python server.py
```

Now the server should be listening on port `5150`. 

>python client.py


## Containerizing the Server using Dockerfile and build our image on gcp

- We're going to use the official Dockerhub Python 3.8 image as our base image.
- We'll put all of our code in `/srv/grpc/`.
- We install our Python package dependencies into the container.
- Finally, we set our container up to run the server by default.

### initialize gcloud cli
```
gcloud init 
SET PROJECT_ID=<this is my gcp project id>
gcloud config set artifacts/location northamerica-northeast1-docker.pkg.dev/%PROJECT_ID%
gcloud config set artifacts/repository dave-docker-repo
```
### create a repo
```
gcloud artifacts repositories create dave-docker-repo --repository-format=python --location=northamerica-northeast1 --description="Dave Docker Repository"

gcloud artifacts repositories list
```
### tell gcloud to build the docker image on gcp and put it in the repo
>gcloud builds submit --region=northamerica-northeast1 --tag northamerica-northeast1-docker.pkg.dev/%PROJECT_ID%/dave-docker-repo/speaker:tag1


## Deploy a new service to Cloud Run
