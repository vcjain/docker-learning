## Docker Image Practice Problems

---

### Problem 1: Hello World Container
Create a Dockerfile that prints "Hello, Docker!" when the container runs.

**Steps:**
1. Use a small base image (e.g. `alpine`).
2. Use `CMD` to echo a string when the container runs.
3. Build and run the image.

---

### Problem 2: Keep the Container Running
Create a container based on Ubuntu that keeps running continuously (e.g., idle service).

**Steps:**
1. Use `ubuntu` as base image.
2. Use `CMD` to run an infinite process like `tail -f /dev/null`.
3. Run it in detached mode and verify it stays up.

---

### Problem 3: Add Labels to Your Image
Create a Docker image that includes labels:
- `maintainer`: your email
- `version`: 1.0
- `lang`: python3

**Steps:**
1. Add `LABEL` instructions to your Dockerfile.
2. Build the image.
3. Use `docker inspect` to confirm the labels exist.

---

### Problem 4: Python Script Runner
Write a simple Python script and create a Docker image that runs the script on container start.

**Steps:**
1. Create a simple Python script `script.py`.
2. Use the `python:3.11-slim` image.
3. Copy the script and set `CMD` to run it.

---

### Problem 5: Serve Static HTML Page via NGINX
Serve a custom `index.html` page using the `nginx` base image.

**Steps:**
1. Create a basic `index.html`.
2. Use `nginx:alpine` image.
3. Copy the HTML file to `/usr/share/nginx/html/`.

---

### Problem 6: Rebuild and Version Your Image
1. Build an image tagged `v1`
2. Modify it (change command or label), and build again as `v2`
3. Run both and compare outputs

**Steps:**
1. Create two different Dockerfiles with small differences.
2. Build them with different tags.
3. Run both images and compare the output.

---

### Problem 7: Dangling Images
Build images and remove their tags to create dangling images. Use:
- `docker images -f dangling=true` to find them
- `docker image prune` to clean them

**Steps:**
1. Build an image and tag it.
2. Re-tag it and remove the original tag.
3. Check for dangling images.

---

### Problem 8: Inspect Image Details
Inspect an image and answer:
- What is the base image used?
- What commands were used to build it?
- What labels does it have?

**Steps:**
1. Build an image.
2. Use `docker inspect <image>` to find base image, labels, entrypoint, CMD.

---

### Problem 9: Docker History
Use `docker history` to view the image build layers. Answer:
- How many layers are in your image?
- Which command added the most size?

**Steps:**
1. Build an image with at least two `RUN` instructions.
2. Run `docker history` to view layer info.

---

### Problem 10: Interactive Ubuntu Container
Run an interactive Ubuntu container using bash, explore the file system, and try commands like `ls`, `pwd`, `echo`, and `apt update`.

**Steps:**
1. Run an Ubuntu container in interactive mode.
2. Use standard Linux commands inside it.
3. Exit the container when done.

