A **Docker overlay network** lets containers **communicate across multiple Docker hosts** (e.g., multiple EC2 instances) using an internal, virtual network.


## Overlay Network: Demonstrable Example (Multi-Host Setup)

We’ll create:

- A **Docker Swarm**
- Two nodes (can be 2 EC2 instances or 2 VMs)
- A **service running Nginx**
- An **overlay network** to allow communication between containers across hosts

---

## What You Need

- **2 Linux EC2 instances** (Ubuntu recommended)
- Docker installed on both
- **Security group** allowing:
  - TCP: 2377 (Swarm management)
  - TCP/UDP: 7946 (node communication)
  - UDP: 4789 (overlay network)
  - TCP: 80 (HTTP demo)

---

## Step-by-Step Guide


### Step 1: Initialize Swarm on **Manager Node**

On Node 1:

```bash
docker swarm init --advertise-addr <NODE_1_PUBLIC_IP>
```

It will output something like:

```bash
docker swarm join --token SWMTKN-1-xyz ... <NODE_1_IP>:2377
```


### Step 2: Join Worker Node to the Swarm

Run the `docker swarm join` command on Node 2 (the worker).


### Step 3: Create an Overlay Network on Manager

```bash
docker network create --driver overlay --attachable demo-overlay
```

> `--attachable` allows standalone containers (not just services) to attach


### Step 4: Run Nginx Service on the Overlay Network

```bash
docker service create --name web --network demo-overlay --publish 80:80 nginx
```

Swarm will schedule it on one of the nodes.



### Step 5: Run Ubuntu Container on Another Node and Test

On **Node 2** (or any node), run:

```bash
docker run -it --rm --network demo-overlay --name os ubuntu bash
```

Inside the container:

```
apt update && apt install -y curl
curl web
```

You’ll see the default Nginx welcome page — the request went **through the overlay network**.


## Cleanup

```bash
docker service rm nginx-demo
docker network rm demo-overlay
```

On worker:

```bash
docker swarm leave
```

On manager:

```bash
docker swarm leave --force
```

---

Please create a compose file to run the above services on a single host. The compose file should include the following services:
- **Nginx** running on port 80
- **Ubuntu** running on port 8080
- **Overlay Network** with the name `demo-overlay`

---

Compose file 
```
version: "3.8"

services:
  nginx-demo:
    image: nginx
    networks:
      - demo-overlay
    ports:
      - "80:80"
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.role == worker  # Optional: restrict to worker node

  ubuntu-client:
    image: ubuntu
    command: ["sleep", "3600"]  # Keeps the container running
    networks:
      - demo-overlay
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.role == worker  # Optional

networks:
  demo-overlay:
    driver: overlay
    attachable: true
```
