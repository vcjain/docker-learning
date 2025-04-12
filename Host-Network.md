
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
docker run -it --rm --network host ubuntu bash
```

Then inside the container:

```bash
apt update && apt install -y postgresql-client
```
```
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

- When you run a Docker container with --network host, you're using the host network namespace, which means:
  
  - The container shares the network stack with the host.
  - Any networking tools (like ip, hostname, whoami, etc.) inside the container may reflect host values, not isolated container values.
  - en you run bash inside the container, the prompt might show the host's IP or hostname, making it look like you’re on the host — even though you're actually still inside the container.

- When you run a container in default network then you will see the prompt as root@<conatiner ID>. This is so because by default conatiner ID is set as hostname of the container.
- You can check IP address of container using ```docker inspect <container-name>``` command. Or by command ```hostname -I``` inside the conatiner.
- You can check promot to use host name by running below command
  - ```export PS1="\u@\$(hostname -I | awk '{print $1}'):~# "```


