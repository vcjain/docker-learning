
This is to demonstrate:

- Docker containers using **host network mode**
- Skipping Docker’s internal network bridge
- Fast network performance (but less isolation)

>  **Host networking only works as expected on Linux**. On Mac/Windows, Docker uses a virtualized network so `--network host` does not function the same way.

---

Run a PostgreSQL database **on the host** and access it from a **Docker container using `--network host`** with `psql`.


### 1. Start PostgreSQL on Host (Linux)

```bash
sudo apt update
```
```
sudo apt install postgresql -y
```

Set up your DB (optional):
```bash
sudo -u postgres psql
# Inside psql:
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydb OWNER myuser;
\q
```

Verify it’s listening on `localhost:5432`:
```bash
ss -tuln | grep 5432
```

### 2. Run Ubuntu Container with `--network host`

```bash
docker run -it --rm \
  --network host \
  ubuntu bash
```

Then inside the container:

```bash
apt update && apt install -y postgresql-client
psql -h 127.0.0.1 -U myuser -d mydb
```

> Use password: `mypassword`


### Expected Output

You should see:
```
psql (14.x)
Type "help" for help.

mydb=>
```

You can run queries like:
```sql
SELECT NOW();
```

---

NOTE: Inside the container, `localhost` or `127.0.0.1` refers to the **host machine**, unlike bridge mode where you'd use service names or IPs.

---

## Cleanup

```bash
# From inside container
exit

# (Optional) Stop PostgreSQL on host
sudo systemctl stop postgresql
```

---

## Notes

- **This is only recommended for trusted containers** due to reduced network isolation.
- Useful for performance testing or when the container needs to bind to privileged ports (like 80/443).

