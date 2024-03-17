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