# Docker Compose

Docker compose is a tool that can help us to define multiple containers in a configuration file and run them in a single click. Most of time when we are working on a application, we have multiple containers to run, web and app server, database, redis, database gui tool etc. In order to make application up and running, we need to run all the containers and that to in an predefine order. Like we will need to run a database container before app server, so that it can make connection after successfully launch.

Docker compose help us to define all the containers required for an application and execute them with single command. We can also shutdown all the containers with a single command. 

We can also manage the dependencies between container, and execute them in a predefine order and can apply delay between 2 container run.

# Install Docker Compose on Ubuntu 18.04

Reference  - https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04

Follow below steps 
Check the current release and if necessary, update it in the command below:
```
sudo curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```
Next set the permissions:
```
sudo chmod +x /usr/local/bin/docker-compose
```

Verify that the installation was successful by checking the version:
```
docker-compose --version
```

## Running applicaiton using Docker compose

```
sudo docker-compose up -d

sudo docker ps
```
Let get into the database container and create tables and insert some data, if you are using fresh volume which doesn't have any tables.

```
docker exec -it db /bin/bash
```
Connect with postgressql database
```
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

