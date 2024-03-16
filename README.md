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

Create a container with a volume
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
            )

# List of all tables
\dt

# Insert a record in users table
INSERT INTO users (id , username, email ) 
            VALUES (1,    'vcjain', 'vcjain@self.com')

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


