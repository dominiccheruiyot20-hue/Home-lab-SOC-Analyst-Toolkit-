# SOC Analyst Toolkit - Integrity - Dominic Cheruiyot
import hashlib

def calc_hash(filename):
    h = hashlib.sha256()
    with open(filename,"rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def create_baseline(log):
    hv = calc_hash(log)
    open("integrity_baseline.txt","w").write(f"{log}:{hv}")
    print(f"[+] Baseline: {hv}")

def verify(log):
    curr = calc_hash(log)
    stored = open("integrity_baseline.txt").read().split(":")[1].strip()
    if curr == stored:
        print(f"[OK] {log} not modified")
    else:
        print(f"[ALERT] INTEGRITY VIOLATION! {log} altered! Expected {stored} Found {curr}")

if __name__ == "__main__":
    open("auth.log","w").write("2026-09-12 10:00:01 - admin login success 192.168.1.5")
    create_baseline("auth.log")
    verify("auth.log")
    print("\n--- Simulating attacker (Defense Evasion) ---")
    open("auth.log","a").write("\n2026-09-12 10:05:00 - ATTACKER DELETED LOGS")
    verify("auth.log")