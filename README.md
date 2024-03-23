# Docker Volumes

The docker volumes are used to persist the aplication data. It is preferred way to share the data between containers.

Create and remove a volume 
```
docker volume create postgre-data
docker volume rm postgre-data
```
List down all volumes and inspect volume
```
docker volume ls
docker volume inspect <vol-name>
```

## Create a container with a volume using -v option
```
# Creating a PostgresSql database with volume

docker run -d --name db -p 5432:5432 -e POSTGRES_PASSWORD=password -v postgre-data:/var/lib/postgresql/data postgres
```

Get into the database conatiner and create tables and insert some data

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

## Create a container with a volume using bind option

```
# Create a data directory to bind with container

mkdir /home/ubuntu/data
cd /home/ubuntu/data
nano index.html
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
docker run -p 8080:80 -d --name web -v /home/ubuntu/data:/usr/share/nginx/html nginx
```

Browsre the nginx page
```
curl localhost:8080
```

Modify the index.html file content at /home/ubuntu/data using nano command and browse the nginx page, you will see the new changes

Similarly, we can get logs of nginx on host machine
```
docker run -p 8080:80 -d --name web -v /home/ubuntu/data:/usr/share/nginx/html -v /home/ubuntu/data:/var/log/nginx nginx
```

Descriptive way of adding a volume or mounting a directory

```
The option --mount help to add volume in descriptive. Here type can be bind or volume.

docker run -p 8080:80 -d --name web --mount type=bind,source=/home/ubuntu/data,destination=/var/log/nginx nginx

# Note: please ensure source, bind, and destination do not have space

docker run -p 5432:5432 -d --name db -e POSTGRES_PASSWORD=password --mount type=volume,source=postgre-data,destination=/var/lib/postgresql/data postgres

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