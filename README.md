# Docker Volumes

The docker volumes are used to persist the aplication data. It is preferred way to share the data between containers.

Create and remove a volume 
```
docker volume create volume1
```
```
docker volume rm volume1
```
List down all volumes and inspect volume
```
docker volume ls
```
```
docker volume inspect <vol-name>
```

## Create a container with a volume using -v option
```
docker volume create postgre-data
```
### Creating a PostgresSql database with volume
```
docker run -d --name db -p 5432:5432 -e POSTGRES_PASSWORD=password -v postgre-data:/var/lib/postgresql/data postgres:16-alpine
```

### Expose a volume directory in image

To expose the the volume directory in the image, we need to specify Volume instruction in the dockerfile. Below is an example of exposing the Volume in dockerfile. When a user creates a container from below image then he can specify the volume path of container in -v option 
```
    FROM some_base_image

    # Create a directory for the volume
    RUN mkdir /path/to/volume

    # Specify the volume, 
    # you can use below path in -v option in run command
    VOLUME /path/to/volume

    # Other instructions for setting up your container
```


Let get into the database container and create tables and insert some data.

```
docker exec -it db /bin/bash

# connect with postgressql database
psql -U postgres -d postgres
```
```
# Create a new table Users
CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            );

# List of all tables
\dt

# Insert a record in users table
INSERT INTO users (id , username, email ) 
            VALUES (1,    'vcjain', 'vcjain@self.com');

```

Select the records in the database
```
select * from users;
```

Delete the container and run the conatiner again
```
docker rm -f db

docker run -d --name db -p 5432:5432 -e POSTGRES_PASSWORD=password -v postgre-data:/var/lib/postgresql/data postgres
```
Select the records in the database
```
# We should get old record which is created with the conatiner we have deleted.

SELECT * FROM users;
```

Clean resources
```
docker rm -f db
docker volume rm postgre-data
```
<br><br>
# Bind Mount

Below is the format to specify a bind option
```
Option# 1 -
docker run -v <Absolute path to host directory>:<path to volume directory> image-name

Option# 2 - 
docker run --mount type=bind,source=<Absolute path to host directory>,destination=<path to volume directory> image-name

```
Lets do a practice to bind directory from a host to conatiner. We will create a nginx container and will bind the host directory with a contaioner directory where nginx index.html page is located. When we change the index.html content in host, it will be reflected in the container and vise versa. 
```
# Create a data directory to bind with container

mkdir /home/ubuntu/data
cd /home/ubuntu/data
sudo nano index.html
```
Copy below content to the nano editor
```
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to My Website</title>
</head>
<body>
    <h1>Hello, world!</h1>
    <p>This is my custom index page.</p>
</body>
</html>
```

Run a nginx container and bind the html directory
```
sudo docker run -p 8080:80 -d --rm --name web -v /home/ubuntu/data:/usr/share/nginx/html nginx

# Here /usr/share/nginx/html is the directory in which default page index.html of nginx server is located.
```

Browsre the nginx page
```
curl localhost:8080
```

Modify the index.html file content at /home/ubuntu/data using nano command and browse the nginx page, you will see the new changes

Similarly, we can get logs of nginx on host machine
```
sudo docker run -p 8080:80 -d --name web -v /home/ubuntu/data:/usr/share/nginx/html -v /home/ubuntu/data:/var/log/nginx nginx

# Here the logs from nginx server are generated at /var/log/nginx directory in the container.
```

## Verbose way of adding a volume or mounting a directory

```
The option --mount help to add volume in descriptive. Here type can be bind or volume.

docker run -p 8080:80 -d --name web --mount type=bind,source=/home/ubuntu/data,destination=/var/log/nginx nginx

# Note: please ensure source, bind, and destination do not have space

docker run -p 5432:5432 -d --name db -e POSTGRES_PASSWORD=password --mount type=volume,source=postgre-data,destination=/var/lib/postgresql/data postgres

# Option with readonly bind, it can apply for both named volume and bind type.
docker run -p 8080:80 -d --name web --mount type=bind,source=/home/ubuntu/data,destination=/var/log/nginx,readonly nginx

```
## tmpfs Mount
The tmpfs mount option in Docker allows you to create a temporary, in-memory storage within a container. When you mount a tmpfs filesystem at a specific directory (e.g., /app) in a Docker container, any files or directories created within that directory will exist only in memory and will not be persisted to disk for permanent storage.

```
sudo docker run -d --name web --mount type=tmpfs,destination=/app nginx

# Note: There is no source in tmpfs mount type

docker inspect web --format '{{ json .Mounts }}'
```

## Applying Labels and Filters
```
sudo docker volume create --label use=dbdata db
sudo docker volume create --label use=appdata app
```
List volumes based on applied filter
```
sudo docker volume ls --filter "label=use=dbdata"
```

## Prune volumes
To delete unused volumes we can use prune command, as we have used for Image and Network
```
sudo docker volume prune
```

## Device Mapper

```
sudo nano /etc/docker/daemon.json
```

Add following content into it 
```
{
    "storage-driver": "devicemapper"
}
```

Restart service
```
sudo systemctl restart docker
```

Check Docker info
```
sudo docker info
```

## Backup and Restore

There is no straight forward way to backup a volume and restore it. We will need to backup a volume directory manually and will need to restore it as well it manually. 

There can be manu usecases for backing up and volume like taking  replicating data across multiple environments.

Lets run a postgres container with a volume, create a table and records. 

We will then run a backup container, which will create a backup tar file and will run a restore conatiner to restore the volume from the tar file. 

As we will restore the volume on the same machine, we will delete the db container and volume after taking backup. To test restoration, we will create db container again after restoration and will see if we have earlier table data available.

Run a postgres and pgadmin container
```
docker run -d --name db -p 5432:5432 -e POSTGRES_PASSWORD=password -v postgre-data:/var/lib/postgresql/data postgres

docker run -p 5080:80  -e 'PGADMIN_DEFAULT_EMAIL=vcjain@self.com'  -e 'PGADMIN_DEFAULT_PASSWORD=admin' -d --name pg dpage/pgadmin4:latest

# Access pgadmin at http://localhost:5080 and login with email and password provided in above command.
```

Run a docker inspect command to fetch IP address of postgres and connect a server using postgres server private IP address
```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db

# Connect to database in pgadmin and Create a new table Users
CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            );

# List of all tables
\dt

# Insert a record in users table
INSERT INTO users (id , username, email ) 
            VALUES (1,    'vcjain', 'vcjain@self.com');
```

Run a container to backup a volume
```
docker run --rm -v postgre-data:/volume -v /Users/vikashjain/temp/data:/backup alpine tar -czf /backup/postgres_data_backup.tar -C /volume .
```

Delete existing volume
```
docker volume ls
docker volume rm  postgre-data
````

Restore volume
```
docker run --rm -v postgre-data:/volume -v  /Users/vikashjain/temp/data:/backup alpine tar -xzf /backup/postgres_data_backup.tar -C /volume
```

Create postgre container again and check if we have existing table and record.
