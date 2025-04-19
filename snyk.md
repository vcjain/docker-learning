

# Snyk Demo: Scanning Docker Images for Vulnerabilities on Ubuntu

This guide demonstrates how to:
1. Install Snyk CLI on Ubuntu
2. Authenticate with Snyk
3. Create a sample vulnerable Docker image
4. Scan the image using Snyk

---

## Step 1: Install Snyk CLI on Ubuntu

Install using `npm`:
```bash
sudo apt update
```
```
sudo apt install -y nodejs npm
```
```
sudo npm install -g snyk
```

Verify installation:
```bash
snyk --version
```

---

## Step 2: Authenticate with Snyk

Sign up at https://snyk.io if you don’t have one. 

Then authenticate via CLI:
```bash
snyk auth
```

This will open a browser for you to log in.

---

## Step 3: Create a Sample Vulnerable Docker Image

Use an intentionally vulnerable image or build one yourself.

### Use Intentionally Vulnerable Image
```bash
docker pull vulnerables/web-dvwa
docker tag vulnerables/web-dvwa my-vulnerable-app
```


## 🔎 Step 4: Scan Docker Image Using Snyk

Run the scan:
```bash
snyk container test my-vulnerable-app
```

You will see a detailed vulnerability report, e.g.:

```
✗ High severity vulnerability found in openssl
  - desc: Potential leak
  - from: openssl@1.0.2
```

You can upload the results with:
```
snyk container monitor my-vulnerable-app

```
Go to https://app.snyk.io

Navigate to Projects


---

## Cleanup (Optional)

```bash
docker rmi my-vulnerable-app
```

---
# 🛠️ Trivy vs Snyk: Vulnerability Scanning Tool Comparison

| Feature                         | **Trivy**                                           | **Snyk**                                             |
|----------------------------------|------------------------------------------------------|-------------------------------------------------------|
| **Developer**                   | Aqua Security                                       | Snyk Ltd.                                             |
| **Open Source**                | ✅ Yes (Apache 2.0)                                  | ❌ CLI is open-source, but full service is proprietary |
| **Installation**               | Simple APT install or single binary                | Requires Node.js + NPM (for CLI)                      |
| **Authentication Required?**   | ❌ No (unless using Trivy Cloud features)           | ✅ Yes (requires account and login for full use)       |
| **Scan Targets**               | - Container Images<br>- Filesystem<br>- Git Repos<br>- SBOM<br>- Kubernetes | - Container Images<br>- Code Repos<br>- Dependencies |
| **Supported Languages**        | Many (Python, Go, Java, JS, Ruby, PHP, etc.)        | Many (JS, Java, Python, Go, .NET, Ruby, PHP, etc.)    |
| **Container Image Scanning**   | ✅ Yes                                              | ✅ Yes                                                 |
| **Infrastructure as Code (IaC)**| ✅ Yes (Terraform, CloudFormation, etc.)           | ✅ Yes (via Snyk IaC)                                  |
| **License Scanning**           | ✅ Yes (via `--license` flag)                      | ✅ Yes (built-in with dashboard reporting)             |
| **Custom Policies**            | Partial (via configuration or Enterprise options)  | ✅ Available in paid tiers                            |
| **Output Formats**             | JSON, Table, Template                              | CLI Output, JSON, Snyk Dashboard                      |
| **CI/CD Integration**          | ✅ Yes (supports GitHub Actions, GitLab, Jenkins, etc.) | ✅ Yes (GitHub, GitLab, Jenkins, Azure, etc.)    |
| **Dashboard/UI**              | Optional (via Trivy Cloud or Aqua Enterprise)      | ✅ Yes (Feature-rich dashboard)                        |
| **Free Tier Limitations**     | Mostly fully featured                               | Limited number of private repos and scans per month   |
| **Performance**               | ⚡ Fast (local scanning)                            | ⏳ Slower (due to network calls to Snyk servers)       |

---

## 📝 Summary

- **Trivy** is best for fast, offline scans with full CLI control and minimal setup. Ideal for self-hosted and open-source-friendly environments.
- **Snyk** offers a rich SaaS platform with deep integrations, better UI, and advanced tracking, but requires login and has usage limits on the free plan.

---

