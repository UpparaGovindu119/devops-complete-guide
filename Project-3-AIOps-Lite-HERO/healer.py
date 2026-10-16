"""Self-healing script for Project-3 AIOps-Lite-HERO.
Monitors Kubernetes for non-running pods, asks Ollama for a fix command, and executes it.
Use with care: this script runs kubectl commands returned by an LLM — review before running in production.
"""
import subprocess, requests, time

def get_failed_pods():
    out = subprocess.check_output("kubectl get pods --field-selector=status.phase!=Running -o name", shell=True).decode()
    return out.splitlines()

def get_logs(pod):
    return subprocess.check_output(f"kubectl logs {pod} --tail=20", shell=True).decode()

while True:
    for pod in get_failed_pods():
        logs = get_logs(pod)
        # Ask Ollama for fix
        prompt = f"Logs:{logs}\nWhat kubectl command to fix? Reply only command."
        fix = requests.post("http://ollama:11434/api/generate", json={"model":"llama3.2:3b","prompt":prompt,"stream":False}).json()['response']
        print(f"HEALING {pod} with {fix}")
        subprocess.run(fix, shell=True)
    time.sleep(30)
