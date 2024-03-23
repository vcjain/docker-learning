# Docker Compose

Docker compose is a tool that can help us to define multiple containers in a configuration file and run them in a single click. Most of time when we are working on a application, we have multiple containers to run, web and app server, database, redis, database gui tool etc. In order to make application up and running, we need to run all the containers and that to in an predefine order. Like we will need to run a database container before app server, so that it can make connection after successfully launch.

Docker compose help us to define all the containers required for an application and execute them with single command. We can also shutdown all the containers with a single command. 

We can also manage the dependencies between container, and execute them in a predefine order and can apply delay between 2 container run.

