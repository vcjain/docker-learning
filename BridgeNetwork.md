

This guide demonstrates how to use Docker networking to run a PostgreSQL database container and access it via a pgAdmin container UI.


### 1. Create a Docker Network

```bash
docker network create my-network
```

This custom network allows containers to talk to each other using their names as hostnames.


### 2. Run PostgreSQL Container

```bash
docker run -d \
  --name my-postgres \
  --network my-network \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  postgres:15
```

> This runs a PostgreSQL database with user `myuser`, password `mypassword`, and database `mydb`.


### 3. Run pgAdmin Container

```bash
docker run -d \
  --name my-pgadmin \
  --network my-network \
  -e PGADMIN_DEFAULT_EMAIL=admin@demo.com \
  -e PGADMIN_DEFAULT_PASSWORD=admin123 \
  -p 5050:80 \
  dpage/pgadmin4
```

> pgAdmin will be available on your browser at `http://localhost:5050`

---

## Access pgAdmin UI

1. Visit [http://localhost:5050](http://localhost:5050)
2. Login using:
   - **Email**: `admin@demo.com`
   - **Password**: `admin123`


## Connect pgAdmin to PostgreSQL

1. Click **"Add New Server"**
2. **General Tab**:
   - **Name**: `Local Postgres`
3. **Connection Tab**:
   - **Host name/address**: `my-postgres`
   - **Port**: `5432`
   - **Username**: `myuser`
   - **Password**: `mypassword`
   - Save Password

4. Click **Save**

You should now see your PostgreSQL server and database in the pgAdmin dashboard.

---

### Try to access DB from another Container

```
docker run -it --rm \
  --name pg-client \
  --network my-network \
  ubuntu bash
```
Then inside the Ubuntu shell:
```
apt update && apt install -y postgresql-client
psql -h my-postgres -U myuser -d mydb
```
When prompted for a password, enter:
```
mypassword
```

Run query
```
SELECT NOW();
```

---
## Cleanup

To stop and remove everything:

```bash
docker stop my-postgres my-pgadmin
docker rm my-postgres my-pgadmin
docker network rm my-network
```
