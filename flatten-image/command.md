
# What is Flattening  Image

Flattening Docker images refers to the process of consolidating the layers of an image into a single layer. In Docker, an image is built up from a series of layers, where each layer represents a set of filesystem changes or instructions in the Dockerfile. These layers are stacked on top of each other, and the final image is the result of these layers combined.

This can be useful for several reasons:
1. <B>Reducing Image Size:</B> Flattening an image can reduce its size. Since each layer introduces some overhead, combining them into a single layer can result in a smaller image size.
2. <B>Optimizing for Caching:</B> Docker uses layer caching during the build process. If a layer changes, all subsequent layers need to be rebuilt. By flattening an image, you may reduce the number of layers, making it more likely that Docker can use cached layers during subsequent builds.


# Create an Image for testing flatten image



## Build Image

To create an image, we need to exeucte docker build command and need to provide a context.

1. Open terminal and change the directory to parent folder of dockerfile

    ```
    cd <project-root>/flatten-image
    ```
2. Execute docker build command and add current directory as context

    ```
    docker build -t flatten:latest .
    ```

3.  After image is created, we can run container using image.

    ```
    docker run --name flatten-test -p 8000:80 flatten
    ```


---

## How to create a Flattened Image

1. To flatten the image using the docker export and docker import commands:

    ```
    # Export the container's file system as a tarball
    docker export flatten-test > flatten-test.tar

    # Import the tarball as a new image
    docker import flatten-test.tar flattened:latest
    ```

2. Verify the layers of image flatten and flattened
    ```
    docker image history flatten
    docker image history flattened
    ```