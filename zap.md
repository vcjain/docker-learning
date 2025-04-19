# OWASP ZAP Demo: Web App Vulnerability Scan on Ubuntu

This guide demonstrates how to:
1. Install OWASP ZAP on Ubuntu
2. Launch ZAP in headless mode
3. Run a scan against a sample application
4. Generate and view a report

---

## Step 1: Install OWASP ZAP on Ubuntu

### Option 1: Install via Snap (Recommended)
```bash
sudo snap install zaproxy
```

### Option 2: Download from Official Site
```bash
wget https://github.com/zaproxy/zaproxy/releases/download/v2.16.1/ZAP_2.16.1_Linux.tar.gz
tar -xvzf ZAP_2.16.1_Linux.tar.gz
cd ZAP_2.16.0
```

To launch the GUI:
```bash
./zap.sh
```

---

## Step 2: Run ZAP in Headless (CLI) Mode

You can run a scan against a test site (e.g. [http://testphp.vulnweb.com](http://testphp.vulnweb.com)) without launching the GUI.

Basic spider + active scan:
```bash
zap.sh -cmd -quickurl http://testphp.vulnweb.com -quickout zap-report.html
```

Explanation:
- `-cmd`: run in CLI mode
- `-quickurl`: target URL
- `-quickout`: output HTML report

---

## Step 3: Full Scan Example

For a deeper scan, you can run the full scan automation script:

```bash
zap.sh -cmd -autorun /path/to/full-scan.yaml
```

You can generate the `full-scan.yaml` file from the ZAP GUI (File > New Automation Plan) or write one manually (see [ZAP Automation Framework](https://www.zaproxy.org/docs/automate/)).

---

## 📄 Step 4: View the Report

The generated report (`zap-report.html`) can be opened in a browser:
```bash
xdg-open zap-report.html
```

You’ll see:
- Alerts categorized by risk level
- URLs scanned
- Request/response details

---

## Cleanup

If installed via Snap:
```bash
sudo snap remove zaproxy
```

If downloaded manually:
```bash
rm -rf ZAP_2.14.0*
```

---
