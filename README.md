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
CREATE TABLE USERS 
```





