"""Self-healing script for Project-3 AIOps-Lite-HERO (SAFE MODE).
This version adds explicit safety controls to avoid running arbitrary kubectl commands returned by an LLM.

Controls:
- HEALER_DRY_RUN=true  -> the script will NOT execute any commands; it will only log and print suggested fixes.
- HEALER_AUTO_APPROVE=yes -> the script will execute suggested commands automatically (DANGEROUS). Use only in a safe test environment.
- The script always appends suggestions to healer-suggestions.log for audit.

Usage examples:
- Dry run (safe): HEALER_DRY_RUN=true python healer.py
- Manual review: python healer.py  (script will print suggestions but not run them)
- Auto-approve (dangerous): HEALER_AUTO_APPROVE=yes python healer.py
"""

import subprocess, requests, time, os

SUGGESTIONS_LOG = "healer-suggestions.log"

def get_failed_pods():
    try:
        out = subprocess.check_output("kubectl get pods --field-selector=status.phase!=Running -o name", shell=True).decode()
        return [p.strip() for p in out.splitlines() if p.strip()]
    except subprocess.CalledProcessError:
        return []


def get_logs(pod):
    try:
        return subprocess.check_output(f"kubectl logs {pod} --tail=50", shell=True).decode()
    except subprocess.CalledProcessError:
        return ""


def ask_ollama_for_fix(logs):
    prompt = f"Logs:{logs}\nWhat kubectl command to fix? Reply only command."
    try:
        res = requests.post("http://ollama:11434/api/generate", json={"model":"llama3.2:3b","prompt":prompt,"stream":False}, timeout=20)
        if res.status_code == 200:
            return res.json().get('response','').strip()
    except Exception as e:
        print("Ollama request failed:", e)
    return ""


def log_suggestion(pod, fix):
    with open(SUGGESTIONS_LOG, 'a') as f:
        f.write(f"{time.asctime()} - {pod} - {fix}\n")


if __name__ == '__main__':
    DRY_RUN = os.getenv('HEALER_DRY_RUN', '').lower() == 'true'
    AUTO = os.getenv('HEALER_AUTO_APPROVE', '').lower() == 'yes'

    print("Healer started - DRY_RUN=", DRY_RUN, " AUTO_APPROVE=", AUTO)

    while True:
        pods = get_failed_pods()
        if not pods:
            # sleep a little if nothing to do
            time.sleep(30)
            continue

        for pod in pods:
            logs = get_logs(pod)
            fix = ask_ollama_for_fix(logs)
            if not fix:
                print(f"No fix suggested for {pod}")
                continue

            print(f"SUGGESTED for {pod}: {fix}")
            log_suggestion(pod, fix)

            if DRY_RUN:
                print(f"DRY RUN -- not executing: {fix}")
                continue

            if AUTO:
                print(f"AUTO-APPROVE -- executing: {fix}")
                try:
                    subprocess.run(fix, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Command failed: {e}")
                continue

            # default behaviour: prompt user for confirmation on console
            try:
                answer = input(f"Execute the suggested command for {pod}? [y/N]: ").strip().lower()
            except Exception:
                answer = 'n'

            if answer == 'y':
                try:
                    subprocess.run(fix, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Command failed: {e}")
            else:
                print("Skipped execution; suggestion logged.")
        time.sleep(30)
