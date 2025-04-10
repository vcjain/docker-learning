# Docker Networks

A computer network is a group of computers connected with each other to communicate. Similarly a docker network, a containers are connected with each other to communicate and collaborate. These containers can run on same Docker Host or they may run on different docker host running on remote machine. 

In Docker Networking is implemented using Drivers. Following drivers are supported by Docker for connectivity.


1. Bridge
2. Host
3. Overlay
4. Macvlan
5. Ipvlan
6. None


## Basic commands
List all networks 
```
docker network ls
```

### How to check IP Address of a container
```
docker inspect <container-name>

# Example
docker run --name web --rm -d nginx
docker inspect web

# Using format option
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web
```

## Bridge Networks

This is a default network in Docker. Docker creates a default netwrok with name bridge and every container created without any explicit network secified will be created in brdige network.

### Create a user define bridge network

```
docker network create --driver=bridge my-net

docker network ls

# Here you can omit --driver option, it will take bridge by default
```

### Run a container on user define network
```
docker run --name web --rm --network my-net -d nginx

docker inspect web

Output
"Networks": {
    "my-net": {
        "IPAMConfig": null,
        "Links": null,
        "Aliases": [
            "187cdc762aa6"
        ],
        "NetworkID": "efc86b0c4013db45a3067ba9b296fd1334765b4f2583c882c363e6191b21539b",
        "EndpointID": "0287cc4aa9f88f52430c14d29fe38ca9e5a0298926cd32b2afbd417a0f7c9840",
        "Gateway": "172.20.0.1",
        "IPAddress": "172.20.0.2",
```



### Connect a running container to a user define network
```
docker network connect my-net web
docker network connect my-net1 web

docker inspect
```

### Disconnect a container from user define network
```
docker network diconnect my-net1 web

docker inspect web
```

### Demonstrate on how 2 container can communicate with container name

```
docker run --it --rm --name web --network my-net -p 8000:80 nginx
```
```
docker run --it --rm --name os --network my-net  ubuntu /bin/bash
```

### Fix: Install `ping` in Ubuntu Container

To ping `web` from inside your `os` container:

**Update and install ping (via iputils-ping):**

```bash
apt update
apt install iputils-ping -y
```
**Ping the nginx container by its name (if using Docker Compose or if you know the name):**

```bash
ping web
```


## Host Network
In Host network, the docker will not create a isolated network, instead will use Host machine network itself. The container's created in the network will have ip address of host only.

We can not create a Host network, but we can connect with a Host network
```
docker run --name web1 --rm --network host -it alpine
    
docker inspect

# the ip address that will be assign is from host netwoek space only.
```

## Overlay Network

An overlay network in Docker is a type of network that allows containers running on different Docker hosts to communicate with each other as if they were on the same host or network. This is particularly useful in distributed systems or container orchestration platforms like Docker Swarm or Kubernetes.

To create a overlay network 
```
docker network create -d overlay  my-overlay-net 

# Options
--attachable - optional and enables a standalone containers to connect with the network

--opt encrypted - optional and enable encryption for data transmitted over overlay network
```

Before you start, you must ensure that participating nodes can communicate over the network. The following table lists ports that need to be open to each host participating in an overlay network:

Ports	Description
- 2377/tcp	The default Swarm control plane port, is configurable with docker swarm join --listen-addr
- 4789/udp	The default overlay traffic port, configurable with docker swarm init --data-path-addr
- 7946/tcp, 7946/udp	Used for communication among nodes, not configurable



## Macvlan Network

This is a type of network driver in Docker that allows containers to have their own MAC addresses, making them appear as individual devices on the network.

Each container connected to a macvlan network is assigned a unique MAC address. This makes the containers appear as separate devices on the network, similar to physical machines.

When you create a Macvlan network and attach containers to it, Docker configures the containers to use a virtual network interface that is associated with the physical network interface of the host. This allows the containers to communicate directly with the physical network, as if they were physical machines connected to the same network.

Create a macvlan network
```
sudo docker network create -d macvlan --subnet=172.16.86.0/24 --gateway=172.16.86.1 -o parent=docker0 macvlan


# List Networks
sudo docker network ls
```

Create a container in macvlan network
```
sudo docker run --name web -it --network macvlan nginx
sudo docker inspect web

# Check the Mac Address in Network section.
```

## None
The None network in Docker is a special network mode that isolates containers from any networking. When you create a container with the --network=none option, Docker places the container into its own network namespace with no network interfaces. This means the container has no network connectivity, neither to the host nor to any other containers.

The None network is useful in scenarios where you want to run a container in complete isolation from the network, like  -     1. If you have a container that doesn't require network access for its functionality and you want to minimize its attack surface, you can use the None network to isolate it completely.

```
docker run --name isolated-nginx --network=none -d nginx

docker inspect isolated-nginx
```

To verify that the NGINX server is running, we can still access it from within the container. We can use docker exec to execute commands inside the container and curl to make a request to the NGINX server

```
docker exec isolated-nginx curl http://localhost
```

## Configuring DNS configuration
Containers use the same DNS servers as the host by default, but you can override this with --dns. 

```
sudo nano /etc/docker/daemon.json

# Add following lines

{
    "dns": ["8.8.8.8"]
}

# Note: Press Ctrl+X to exit the editor. Then type Y and press Enter to save the file.
```

Restart the docker
```
sudo systemctl restart docker
```

Use the following command to test the DNS by looking up an external domain:
```
sudo docker run nicolaka/netshoot nslookup google.com

# Output
    Server:         8.8.8.8
    Address:        8.8.8.8#53

    Non-authoritative answer:
    Name:   google.com
    Address: 142.251.215.238
    Name:   google.com
    Address: 2607:f8b0:400a:800::200e
```

Use the following command to run a container with a custom DNS and test it by doing an nslookup:
```
sudo docker run --dns 8.8.4.4 nicolaka/netshoot nslookup facebook.com

# Output
    Server:         8.8.4.4
    Address:        8.8.4.4#53

    Non-authoritative answer:
    Name:   facebook.com
    Address: 157.240.3.35
    Name:   facebook.com
    Address: 2a03:2880:f101:83:face:b00c:0:25de
```

## Applying Labels & Filters

```
sudo docker network create -d bridge --label platform.type=backend  mybridge
```

List network based on filter
```
sudo docker network ls --filter "label=platform.type=backend"
```

## Network Prune

We can use the following command to clean up networks which aren’t used by any containers:
```
docker network prune
```

<br><br>
# Docker Link

A docker link is a old way of connecting 2 or more containers. As of now, we are using Network port to connect 2 containers, earlier using link we can connect 2 containers without exposing ports. 








