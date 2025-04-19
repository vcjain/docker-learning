# Trivy Demo: Scanning Docker Images for Vulnerabilities on Ubuntu

This guide demonstrates how to:
1. Install Trivy on Ubuntu
2. Create a sample vulnerable Docker image
3. Scan the image using Trivy

---

## Step 1: Install Trivy on Ubuntu

```bash
sudo apt update
```
```
sudo apt install -y wget apt-transport-https gnupg lsb-release
```
```
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo gpg --dearmor -o /usr/share/keyrings/trivy.gpg
```
```
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/trivy.list > /dev/null
```
```
sudo apt update
```
```
sudo apt install -y trivy
```
```
trivy --version
```

---


## Step 2: Create a Sample Vulnerable Docker Image



### Use Intentionally Vulnerable Image
```bash
docker pull vulnerables/web-dvwa
docker tag vulnerables/web-dvwa my-vulnerable-app:latest
```

---

## Step 3: Scan Docker Image Using Trivy

Run Trivy scan:
```bash
trivy image my-vulnerable-app
```

Optional: Save results to file
```bash
trivy image --format table --output trivy-report.json my-vulnerable-app
```

---

## Output Sample

Trivy will return a list of vulnerabilities grouped by OS packages and application libraries. Example output:

```
Total: 10 (UNKNOWN: 0, LOW: 2, MEDIUM: 5, HIGH: 2, CRITICAL: 1)
```

---

##  Cleanup (Optional)

To clear cache
```
trivy clean --scan-cache
```

```bash
docker rmi my-vulnerable-app
```

