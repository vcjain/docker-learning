# Docker Link

A docker link is a old way of connecting 2 or more containers. As of now, we are using Network port to connect 2 containers, earlier using link we can connect 2 containers without exposing ports. 

Example
Create a database container 
docker run -d --name db  -e POSTGRES_PASSWORD=password postgres  
# we are skipping -p option to expose port 

Create a python container web and link it with DB conatiner above
```
docker run -d -p 8000:8000  --name web --link db vcjain/python-app
```

Above web app expose 2 APIs
```
1. /createdb - it will create a new table and insert record in it
2. /get - it will fetch record and display
```

Both API connect to database using environment variable added by Docker for source container port
DB_PORT_5432_TCP_PORT=5432
