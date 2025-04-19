# docker-learning


Docker is an open platform for developing, shipping, and running applications.

Docker allows you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications.

You can download and install Docker on multiple platforms. Below are the steps to install it on Ubuntu

If you have docker already installed, then you can uinstall it first

## Uninstall Docker
```
sudo apt-get remove docker-ce
sudo apt-get remove docker-ce-cli
```

## Install Docker using the below URL
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04 

```
sudo apt update
```
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```
sudo apt update
```
```
apt-cache policy docker-ce
```
```
sudo apt install docker-ce -y
```

Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it’s running:
```
sudo systemctl status docker
```

### Executing Docker command without sudo


By default, the docker command can only be run the root user or by a user in the docker group, which is automatically created during Docker’s installation process. If you attempt to run the docker command without prefixing it with sudo or without being in the docker group, you’ll get an output like this:

If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group:

```
sudo usermod -aG docker ${USER}
```
-- This will add the current user to docker group

To apply the new group membership, log out of the server and log back in.

To verify if installation is successful, we can run below command

```
docker run hello-world

Output
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete
Digest: sha256:bfea6278a0a267fad2634554f4f0c6f31981eea41c553fdf5a83e95a41d40c38
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```


## Connecting to a remote Docker Engine/host

By default, the docker daemon is allowed to accept request from local machine itself, but we can enable it to accept request from a remote 
Machine as well. The cli can run on a local machine and when you execute commands like docker run or ps then those commands will get executed 
On the remote docker daemon running on another machine.


You can follow the instructions here - https://docs.docker.com/config/daemon/remote-access/

Use the below command to open an override file for docker.service in a text editor.

```
sudo systemctl edit docker.service 
```

Add or modify the following lines, substituting your own values.
```
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375
```
Save the file.

Reload the systemctl configuration.
```
 sudo systemctl daemon-reload
```
Restart Docker.
```
 sudo systemctl restart docker.service
```

To execute command from a remote

```
export DOCKER_HOST=tcp://<IPAddress>:2375
```

Now when you run a docker command then it will get executed on remote Docker **(without sudo)**
```
docker ps
docker images

# Run above command without sudo. When you run Docker commands with sudo, it typically runs them in the context of the root user. This means that environment variables like DOCKER_HOST might not set globally. 
```

To check available version on a machine please run command
```
apt-cache madison docker-ce | awk '{ print $3 }'
```
