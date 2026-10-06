# Top 100 DevOps Commands Cheat Sheet

This cheatsheet contains the most commonly used DevOps commands in Linux, Docker, Kubernetes, Git, AWS, Jenkins, Terraform, and troubleshooting.

---

## 1. Linux Basics

```bash
pwd                     # Print working directory
ls -la                  # List files with hidden files and details
cd /path/to/dir         # Change directory
mkdir -p dir/subdir     # Create nested directories
touch file.txt          # Create empty file
cp source.txt dest.txt  # Copy file
cp -r dir1 dir2         # Copy directory recursively
mv old.txt new.txt      # Move or rename file
rm file.txt             # Remove file
rm -rf dir              # Remove directory recursively
find / -name file.txt  # Find file by name
find /var/log -name "*.log"  # Find log files
grep "error" file.log  # Search for text in file
grep -i "error" file.log # Case-insensitive search
grep -n "error" file.log # Show line numbers
head file.log           # First 10 lines
head -50 file.log      # First 50 lines
tail file.log           # Last 10 lines
tail -f file.log        # Follow log in real time
cat file.txt            # View file contents
less file.txt           # View file page by page
chmod 755 script.sh     # Change permissions
chmod +x script.sh      # Make executable
chown user:user file.txt # Change ownership
ps aux                  # List all running processes
ps -ef | grep java     # Find Java process
top                     # Monitor system resources
uptime                  # Show uptime
free -h                 # Show memory usage
df -h                   # Show disk usage
du -sh /path            # Show disk usage of directory
uname -a                # System info
whoami                  # Current user
id                      # User details
sudo apt update          # Update package list
sudo apt install pkg    # Install package
sudo systemctl status nginx # Check service
sudo systemctl restart nginx # Restart service
```

---

## 2. Git & GitHub

```bash
git init
git clone https://github.com/user/repo.git
git status
git add .
git add file.txt
git commit -m "Add feature"
git push origin main
git pull origin main
git branch
git checkout -b feature/test
git checkout main
git merge feature/test
git log --oneline
git diff
git diff HEAD~1
git stash
git stash pop
git revert <commit>
git reset --hard HEAD~1
git remote -v
git fetch origin
git tag
git show <commit>
```

---

## 3. Docker Commands

```bash
docker ps
docker ps -a
docker images
docker pull nginx
docker run -d -p 80:80 nginx
docker run -d -p 3000:3000 --name app app:latest
docker stop app
docker rm app
docker logs app
docker logs -f app
docker exec -it app bash
docker build -t app:1.0 .
docker tag app:1.0 user/app:1.0
docker push user/app:1.0
docker rmi app:1.0
docker inspect app
docker stats
docker system df
docker network ls
docker volume ls
docker-compose up -d
docker-compose down
docker-compose logs -f
docker-compose build
```

---

## 4. Dockerfile Common Commands

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["node", "server.js"]
```

---

## 5. Kubernetes Commands

```bash
kubectl get pods
kubectl get svc
kubectl get deploy
kubectl get ns
kubectl get nodes
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl logs -f <pod-name>
kubectl exec -it <pod-name> -- sh
kubectl apply -f deployment.yaml
kubectl delete -f deployment.yaml
kubectl scale deployment myapp --replicas=3
kubectl rollout status deployment/myapp
kubectl rollout undo deployment/myapp
kubectl get ingress
kubectl get pvc
kubectl get configmap
kubectl get secret
kubectl top pod
kubectl top node
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl port-forward svc/myapp 8080:80
kubectl set image deployment/myapp myapp=myapp:v2
kubectl get all
kubectl cluster-info
kubectl config current-context
```

---

## 6. Jenkins Commands

```bash
sudo systemctl status jenkins
sudo systemctl start jenkins
sudo systemctl stop jenkins
sudo systemctl restart jenkins
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
sudo tail -f /var/log/jenkins/jenkins.log
```

---

## 7. Terraform Commands

```bash
terraform init
terraform validate
terraform fmt
terraform plan
terraform apply
terraform apply -auto-approve
terraform destroy
terraform destroy -auto-approve
terraform output
terraform show
terraform state list
terraform workspace list
terraform import aws_instance.web i-1234567890abcdef0
```

---

## 8. AWS CLI Commands

```bash
aws --version
aws configure
aws s3 ls
aws s3 cp file.txt s3://bucket/
aws ec2 describe-instances
aws ec2 run-instances --image-id ami-123 --count 1 --instance-type t2.micro
aws eks list-clusters
aws iam list-users
aws cloudwatch list-metrics
aws logs tail /aws/lambda/my-function --follow
```

---

## 9. Maven Commands

```bash
mvn -version
mvn clean
mvn compile
mvn test
mvn package
mvn install
mvn deploy
mvn dependency:tree
mvn sonar:sonar
mvn verify
```

---

## 10. Debugging & Troubleshooting Commands

```bash
journalctl -xe
journalctl -u nginx -n 50
journalctl -f
systemctl status app
systemctl restart app
systemctl logs app
ss -lntp | grep 8080
netstat -tulpn | grep 8080
curl -I http://localhost:3000
curl http://localhost:3000/health
ping google.com
nslookup google.com
dig google.com
lsof -i :8080
df -h
free -h
du -sh /var/log
tail -f /var/log/syslog
tail -f /var/log/nginx/error.log
grep -i "error" /var/log/app.log
grep -n "404" /var/log/nginx/access.log
```

---

## 11. Ansible Commands

```bash
ansible --version
ansible-playbook playbook.yml
ansible-playbook playbook.yml -i inventory.ini
ansible all -m ping
ansible-doc -l
ansible-galaxy install username.role
```

---

## 12. Bash Scripting Essentials

```bash
#!/bin/bash
set -e
echo "Hello world"
DATE=$(date +%F)
if [ -f file.txt ]; then
  echo "File exists"
fi
for i in {1..5}; do echo $i; done
while true; do echo "Loop"; sleep 2; done
```

---

## 13. Useful Shortcuts

```bash
Ctrl+C       # Stop current command
Ctrl+Z       # Suspend process
bg           # Resume process in background
fg           # Bring process to foreground
!!           # Repeat last command
!grep        # Run previous command containing grep
history      # Show command history
clear        # Clear terminal
```

---

## 14. Interview-Focused Quick Commands for DevOps

```bash
# Check if service is running
systemctl status nginx

# Check port usage
ss -lntp | grep 80

# Check logs
tail -f /var/log/syslog

# Check disk usage
df -h

# Check CPU and memory
top
free -h

# Restart application service
systemctl restart myapp

# Check Kubernetes pod logs
kubectl logs -f pod-name

# Check deployment status
kubectl rollout status deployment/myapp

# Check Docker containers
docker ps -a

# Check if port forwarded correctly
kubectl port-forward svc/myapp 8080:80
```

---

## Final Tips

- Learn the command + meaning + real scenario + troubleshooting.
- In DevOps, you are not judged only by running commands; you are judged by how quickly you identify root cause.
- The most important habit: check logs first, then resource usage, then config, then dependencies.

"Logs first, root cause second, fix third."

