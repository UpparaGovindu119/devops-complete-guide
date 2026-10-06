# Python for DevOps Course

This course explains Python in a practical DevOps way. Every topic includes:
- Telugu understanding
- English code examples
- Real DevOps use cases
- Interview-focused explanation

---

## 1. Why Python in DevOps?

### Telugu explanation
Python అనేది చాలా సులభమైన మరియు శక్తివంతమైన programming language. DevOps లో ఇది చాలా ముఖ్యమైన పాత్ర పోషిస్తుంది.

DevOps లో Python ఉపయోగం:
- 반복되는 పనులు ఆటోమేట్ చేయడం
- Docker, Kubernetes, Jenkins వాడే scripts తయారు చేయడం
- Cloud APIs (AWS, Azure, GCP) తో work చేయడం
- Log files చదవడం మరియు analyze చేయడం
- Application health checks చేయడం
- Deployment మరియు rollback scripts తయారు చేయడం
- Config files manage చేయడం

### English explanation
Python is a simple and powerful programming language widely used in DevOps.

It is used for:
- automation of repetitive tasks
- interacting with Docker, Kubernetes, and Jenkins
- working with cloud APIs
- reading, parsing, and analyzing log files
- checking application health and environment checks
- writing deployment and rollback scripts
- managing configuration files and infrastructure tasks

### Example
```python
print("Hello DevOps")
```

### Why this matters
This is the simplest Python script. In DevOps, scripts like this are used to automate routine work such as server checks and deployment steps.

---

## 2. Python Basics

### 2.1 Variables

```python
name = "devops"
count = 10
is_ready = True

print(name)
print(count)
print(is_ready)
```

### Telugu explanation
Variables data 저장 చేసేందుకు ఉపయోగపడతాయి. DevOps లో server names, ports, status, versions మొదలగునవి variables గా store చేయవచ్చు.

### Real DevOps use case
```python
server_name = "web-server-01"
port = 8080
status = "running"

print(f"Server: {server_name}, Port: {port}, Status: {status}")
```

---

### 2.2 Input and Output

```python
name = input("Enter server name: ")
print(f"Server name is {name}")
```

### Telugu explanation
Input from user or terminal capture చేయవచ్చు. DevOps scripts లో configuration values input గా తీసుకోవచ్చు.

### Real DevOps use case
```python
env = input("Enter environment (dev/prod): ")
print(f"Deploying to {env} environment")
```

---

### 2.3 Lists

```python
servers = ["web-01", "web-02", "db-01"]
print(servers)
print(servers[0])
```

### Telugu explanation
List అనేది multiple values store చేయగల collection. DevOps లో servers, ports, file names, service names listasుగా use చేయవచ్చు.

---

### 2.4 Loops

```python
for server in ["web-01", "web-02", "db-01"]:
    print(server)
```

### Telugu explanation
Loop use చేయడం ద్వారా multiple servers or files మీద iterate చేయవచ్చు.

### Real DevOps use case
```python
for service in ["nginx", "docker", "jenkins"]:
    print(f"Checking service: {service}")
```

---

### 2.5 Conditionals

```python
status = "running"

if status == "running":
    print("Service is healthy")
else:
    print("Service is unhealthy")
```

### Telugu explanation
Conditionals help check if a service is healthy or if an environment is production or development.

---

### 2.6 Functions

```python
def check_status(service_name):
    if service_name == "nginx":
        return "healthy"
    return "unknown"

print(check_status("nginx"))
```

### Telugu explanation
Functions reusable logic create చేయడానికి ఉపయోగపడతాయి. DevOps లో scripts modularize చేయడానికి చాలా ఉపయోగం ఉంది.

---

## 3. Python for Linux Automation

### Telugu explanation
DevOps లో Linux commands చాలా ముఖ్యమైనవి. Python ఈ commands run చేయడానికి సహాయపడుతుంది.

### Example: run shell commands
```python
import subprocess

result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)
```

### Explanation
This runs `ls -la` command from Python and prints output.

### Real DevOps use case
```python
import subprocess

result = subprocess.run(["df", "-h"], capture_output=True, text=True)
print(result.stdout)
```

This checks disk usage from a Python script.

---

### Example: check if a process is running
```python
import subprocess

result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
if "nginx" in result.stdout:
    print("nginx is running")
else:
    print("nginx is not running")
```

### Telugu explanation
DevOps లో process running or not check చేయడానికి ఈ pattern ఉపయోగపడుతుంది.

---

## 4. Python for Log Analysis

### Telugu explanation
Production లో logs అతి ముఖ్యమైనవి. Python ఉపయోగించి logs చదివి error files filter చేయవచ్చు.

### Example: read a log file
```python
with open('/var/log/syslog', 'r') as file:
    for line in file:
        if 'error' in line.lower():
            print(line.strip())
```

### Real DevOps use case
```python
log_file = '/var/log/app.log'

with open(log_file, 'r') as file:
    for line in file:
        if 'ERROR' in line.upper():
            print(line.strip())
```

### Telugu explanation
This script only prints error lines. This helps in troubleshooting production issues quickly.

---

### Example: count errors in log file
```python
log_file = '/var/log/app.log'
count = 0

with open(log_file, 'r') as file:
    for line in file:
        if 'ERROR' in line.upper():
            count += 1

print(f"Total errors: {count}")
```

### Real DevOps use case
This is used in incident analysis to count error frequency.

---

## 5. Python for Docker Automation

### Telugu explanation
Python can run Docker commands automatically. This reduces manual work in DevOps.

### Example: check Docker containers
```python
import subprocess

result = subprocess.run(['docker', 'ps', '-a'], capture_output=True, text=True)
print(result.stdout)
```

### Real DevOps use case
A script can detect whether all containers are running properly before deployment.

### Example: stop a container automatically
```python
import subprocess

subprocess.run(['docker', 'stop', 'myapp'], check=True)
print('Container stopped successfully')
```

---

## 6. Python for Kubernetes Automation

### Telugu explanation
Kubernetes commands are often used manually, but Python can automate them.

### Example: get Kubernetes pods
```python
import subprocess

result = subprocess.run(['kubectl', 'get', 'pods'], capture_output=True, text=True)
print(result.stdout)
```

### Real DevOps use case
Before deployment, a script can verify whether all pods are healthy.

### Example: delete a pod
```python
import subprocess

subprocess.run(['kubectl', 'delete', 'pod', 'myapp-pod'], check=True)
print('Pod deleted')
```

---

## 7. Python for Jenkins and CI/CD

### Telugu explanation
Python can be used to trigger scripts, validate builds, parse results, and automate deployment tasks.

### Example: run Maven build using Python
```python
import subprocess

result = subprocess.run(['mvn', 'clean', 'package'], capture_output=True, text=True)
print(result.stdout)
if result.returncode != 0:
    print(result.stderr)
    raise SystemExit(1)
```

### DevOps use case
This script checks if Maven build succeeded. If not, pipeline fails early.

---

## 8. Python for AWS Automation

### Telugu explanation
AWS has APIs. Python can call AWS APIs using boto3 library.

### Example: list EC2 instances
```python
import boto3

client = boto3.client('ec2')
response = client.describe_instances()
print(response)
```

### Real DevOps use case
- list running instances
- start or stop EC2 instances
- check resource health
- automate cloud provisioning

### Example: stop EC2 instance
```python
import boto3

client = boto3.client('ec2')
client.stop_instances(InstanceIds=['i-1234567890abcdef0'])
print('Instance stop request sent')
```

---

## 9. Python for JSON and YAML Files

### Telugu explanation
DevOps configuration files are often JSON or YAML. Python can read and parse them automatically.

### JSON example
```python
import json

config = {"app": "myapp", "port": 8080}
print(json.dumps(config, indent=2))
```

### YAML example
```python
import yaml

config = {"app": "myapp", "port": 8080}
print(yaml.dump(config))
```

### Real DevOps use case
This is used for configuration management, deployment metadata, and environment files.

---

## 10. Python for File and Directory Automation

### Telugu explanation
Python can create folders, read files, rename files, backup directories, and clean logs.

### Example: create directory
```python
import os

os.makedirs('/tmp/devops_backup', exist_ok=True)
print('Directory created')
```

### Example: backup files
```python
import shutil

shutil.copy('/etc/hosts', '/tmp/hosts_backup.txt')
print('File backed up')
```

### Real DevOps use case
Used in backup scripts and deployment tasks.

---

## 11. Python for Monitoring and Alerts

### Telugu explanation
Monitoring scripts can check service health and alert on failures.

### Example: health check script
```python
import urllib.request

try:
    response = urllib.request.urlopen('http://localhost:3000/health', timeout=5)
    print('Health check passed')
except Exception as e:
    print('Health check failed:', e)
```

### Real DevOps use case
This verifies that an application is healthy before deployment or during system monitoring.

---

## 12. Python and Error Handling

### Telugu explanation
In DevOps, scripts must fail gracefully and show clear messages when commands fail.

### Example
```python
import subprocess

try:
    subprocess.run(['kubectl', 'get', 'pods'], check=True)
    print('Kubernetes command succeeded')
except Exception as e:
    print('Kubernetes command failed:', e)
```

### Real DevOps use case
This helps detect deployment or cluster failures early.

---

## 13. Python Libraries Common in DevOps

### Important libraries
- `subprocess` → run shell commands
- `os` → file and system operations
- `json` → JSON parsing
- `yaml` → YAML processing
- `requests` → HTTP API calls
- `boto3` → AWS automation
- `logging` → structured logs
- `pathlib` → file handling

---

## 14. Python DevOps Interview Questions

### Q1: Why is Python used in DevOps?
**Answer:**
Python is used because it is simple, readable, and very effective for automation, cloud APIs, scripting, and log processing.

### Q2: What Python modules are useful in DevOps?
**Answer:**
`subprocess`, `json`, `yaml`, `os`, `requests`, `boto3`, `logging`, `pathlib`.

### Q3: How is Python used in Docker automation?
**Answer:**
It can run Docker commands, check container status, stop containers, and automate deployment tasks.

### Q4: How is Python used in Kubernetes automation?
**Answer:**
It can run `kubectl` commands, check pod health, and automate rollout or rollback steps.

### Q5: How is Python used in AWS DevOps?
**Answer:**
It can automate EC2 operations, S3 management, IAM checks, and infrastructure validation using boto3.

---

## 15. Best Practices for Python in DevOps

- keep scripts simple and readable
- use clear error messages
- avoid hardcoding secrets
- use logging instead of just printing messages
- handle exceptions properly
- use YAML/JSON config files where possible
- use version control for automation scripts

---

## 16. Real-World Python DevOps Example

```python
import subprocess
import sys

services = ['docker', 'kubectl', 'git']

for service in services:
    result = subprocess.run(['which', service], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{service} is installed")
    else:
        print(f"{service} is missing")
        sys.exit(1)
```

### Telugu explanation
This script checks whether required tools are installed before deployment starts. This is a very common DevOps automation pattern.

---

## 17. Final Summary

Python is one of the most important languages for DevOps because it can automate:
- Linux commands
- Docker tasks
- Kubernetes checks
- AWS operations
- Jenkins pipeline tasks
- log monitoring
- health checks
- deployment scripts
- infrastructure automation

If you learn Python well, your DevOps skill becomes much stronger.

---

## 18. Next Step

Practice these scripts:
- run `ls` and `df` from Python
- read log files and print errors
- automate Docker status checks
- automate `kubectl get pods`
- list AWS EC2 instances using boto3
- write health check script for an app

This is the best way to build real DevOps confidence.

