# Docker Content Trust

Content trust in Docker refers to a security feature that enables the verification of the authenticity and integrity of Docker images. In this we signed the docker image before pushing it to repo and while pulling signature is validated. 

We can enable the docker trust we need to set environment variable DOCKER_CONTENT_TRUST=1

Login into Docker Hub registry
```
docker login -u <username>
```

Generate Keys used in docker content trust for signing images 
```
docker trust key generate <signername>
```
Example
```
docker trust key generate vcjain
```

Add signer user to repo
```
docker trust signer add --key <signername>.pub <signer name> <repo>
```

> Example 
```
docker trust signer add --key vcjain.pub vcjain vcjain/dct-test
```

Create a image, which we can test for signing using docker content trust
```
mkdir dct
cd dct
vi dockerfile
``` 

Enter below content and save the file - ESC --> :wq
```
    FROM busybox:latest

    CMD echo It Worked!
```
Create a Image of above docker file and run it.

```
docker build -t vcjain/dct-test:unsigned .
docker run vcjain/dct-test:unsigned
```

Enable the Docker Content Trust

```
export DOCKER_CONTENT_TRUST=1
docker run vcjain/dct-test:unsigned

Output : You will get error. With Docker Trust Content enable, docker will only pull and run a signed image
    docker: No valid trust data for unsigned.
```

Create a new tag of the image as signed and push it.
```
docker image tag vcjain/dct-test:unsigned vcjain/dct-test:signed
docker push vcjain/dct-test:signed
docker run vcjain/dct-test:signed
```

Disable the Docker Content Trust
```
export DOCKER_CONTENT_TRUST=0
```








