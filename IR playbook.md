# Incident Response Playbook - Faulu Bank Phishing Scenario
Analyst: Dominic Cheruiyot | Home Lab SOC

**Scenario:** Staff clicks "Update payroll" phishing link.

**PREP:** Tools ready (Nmap, Zenmap, Wazuh), baselines from integrity.py, data encrypted from confidentiality.py
**IDENTIFY:** Wazuh alert impossible travel Eldoret->Russia, Nmap shows C2 Channel (Kill Chain Stage 6), check Privilege Escalation
**CONTAIN:** Disable account, block IP, isolate workstation, block domain at proxy (your switch proxy question!)
**ERADICATE:** Delete email from all mailboxes, force reset + MFA
**RECOVER:** Monitor auth.log 72h with integrity.py
**LESSONS LEARNED:** Update filters, 15-min staff training, update this playbook