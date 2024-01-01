
# Create an Image for Python application

## Build Image

To create an image, we need to exeucte docker build command and need to provide a context.

1. Open terminal and change the directory to parent folder of dockerfile

    ```
    cd <project-root>/python/flask-app
    ```
2. Execute docker build command and add current directory as context

    ```
    docker build -t python-app:latest .
    ```

3.After image is created, we can run container using image.

    docker run --name python-app -pc8000:8000 python-app:latest



Here 
- python-app:latest is the tag of the image.
- With '.' current directory is set as context for build command 

---

## Image Inspect command

1. To check complete details around an image run below command

    ```
    docker image inspect python-app
    ```
2. To print only metadata i.e. labels, run below command
    ```
    docker image inspect --format='{{json .Config.Labels}}' python-app
    ```