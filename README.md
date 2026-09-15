# Home-Lab SOC Analyst Toolkit
Built 100% on Android using Termux | Live: https://dominiccheruiyot20-hue.github.io/Home-lab-SOC-Analyst-Toolkit-/

### SOC Project: Python Log Analyzer for Brute Force Detection
**File:** `analyze.py`

This tool simulates a SIEM alert. It reads `logs.csv` and detects IPs with >5 failed logins.

**Code logic:**
- Works with pandas (PC) and fallback to csv module (Termux)
- Alerts: `[ALERT] Possible Brute Force`

**Run:**
`python analyze.py`

**Result:**
`ALERT! IP 192.168.1.15 - 7 fails`

### Other Labs
- Confidentiality.py, Integrity.py - CIA Triad
- IR playbook.md - Incident Response

Author: Dominic Cheruiyot - Huawei Competition Network Track
