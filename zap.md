# OWASP ZAP Demo: Web App Vulnerability Scan on Ubuntu

This guide demonstrates how to:
1. Launch ZAP in headless mode
2. Run a scan against a sample application
3. Generate and view a report

---

Run the following command to start the ZAP container
```
docker run -dt --name cont1 ghcr.io/zaproxy/zaproxy:stable /bin/bash

```
Run the following command to create ZAP workspace for scanning the vulnerabilities:
```
docker exec cont1 mkdir /zap/wrk

```
Run the following command to connect to the container:
```
docker exec -it cont1 sh

```
Run the following command to initiate scanning of the workspace:
```
zap-baseline.py -t https://medium.com/ -r report.html -I
```

It will take couple of minutes to run the scan and then exit from container. Execute the following command to copy the report to the Docker host:
```
docker cp cont1:/zap/wrk/report.html /home/labuser/report.html
```
Open the report.html in browser.

<img width="1232" alt="image" src="https://github.com/user-attachments/assets/27a72de8-3564-4e27-9638-785f4e2ec137" />


