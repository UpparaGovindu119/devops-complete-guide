# Complete DevOps Learning Path - Structured Course

This is a complete DevOps learning course organized in the best learning order for freshers preparing for interviews and real-world projects.

## 🎯 Learning Timeline: 4-5 Months

---

## PHASE 1: Operating System & Version Control (Weeks 1-2)

### 1.1 Linux Fundamentals

**Why first?** Everything in DevOps runs on Linux. You must be comfortable with Linux before anything else.

#### ⭐ NAVIGATION COMMANDS

```bash
# Print current working directory
pwd
# Output: /home/ubuntu/project
# Use when: You need to know where you are in filesystem

# Change directory
cd /home
cd ..          # go to parent directory
cd ~           # go to home directory
cd -           # go to previous directory
cd /           # go to root directory
# Use when: Navigating between folders

# List files and directories
ls             # simple list
ls -l          # long format with details (IMPORTANT FOR DEVOPS)
ls -la         # show all files including hidden ones
ls -lah        # human-readable sizes
ls -lh /var/log # list specific directory
ls -R          # recursive listing
ls -t          # sort by modification time
ls -S          # sort by file size

# Use when: 
# - ls -l to check permissions before deployment
# - ls -lah to find hidden config files
# - ls -t to find recently modified files
```

#### ⭐ FILE CREATION & MANIPULATION

```bash
# Create empty file
touch myfile.txt
touch file1.txt file2.txt file3.txt
# Use when: Creating empty files for configuration

# Create directory
mkdir mydir
mkdir -p /path/to/nested/directory  # create parent directories too
# Use when: Creating project structure

# Copy files
cp source.txt destination.txt
cp -r /source/dir /destination/dir  # recursive copy for directories
cp -v file1.txt file2.txt            # verbose (show what's copying)
# Use when: Backing up config files before editing

# Move/Rename files
mv oldname.txt newname.txt
mv /path/to/file /new/path/file
# Use when: Organizing logs or config files

# Remove files
rm file.txt
rm -f file.txt               # force remove (don't ask)
rm -rf mydir/                # recursive remove directory
rm *.log                     # remove all .log files
# Use when: Cleaning up old logs or temp files
```

#### ⭐ FILE VIEWING COMMANDS - MOST IMPORTANT FOR DEVOPS

```bash
# ========== View entire file ==========
cat file.txt
cat /var/log/syslog
# Use when: You need to see full file quickly

# ========== View file with pagination ==========
less file.txt
# Inside less: 
#   q = quit
#   Space = scroll down
#   b = scroll up
#   / = search
#   n = next search result
#   N = previous search result
# Use when: File is large (100MB+ log file)

# ========== View first lines ==========
head file.txt
head -20 file.txt            # first 20 lines
head -n 5 /var/log/app.log
# Use when: Quick look at beginning of logs

# ========== View last lines - CRITICAL FOR DEBUGGING ==========
tail file.txt
tail -50 file.txt            # last 50 lines (MOST USEFUL)
tail -f /var/log/app.log     # FOLLOW in real-time (SUPER IMPORTANT)
tail -n 20 application.log
tail -f -n 100 /var/log/app.log  # follow AND show last 100 lines

# Use when: 
# - tail -f: monitoring live logs while debugging
# - tail -50: check recent errors
# - tail -f -n 100: see context while following

# Count lines in file
wc -l file.txt
wc -w file.txt               # word count
wc -c file.txt               # byte count
# Use when: Checking log file size
```

#### ⭐ TEXT EDITING - nano (EASY FOR BEGINNERS)

```bash
# Open file in nano
nano myfile.txt
nano /etc/nginx/nginx.conf

# NANO KEYBOARD SHORTCUTS:
# Ctrl+X     - exit (asks to save)
# Ctrl+O     - save
# Ctrl+W     - search
# Ctrl+G     - go to line
# Ctrl+K     - cut line
# Ctrl+U     - paste
# Alt+U      - undo
# Alt+E      - redo

# EXAMPLE WORKFLOW:
# 1. nano deployment.yaml
# 2. Make changes
# 3. Ctrl+X
# 4. Press 'y' to save
# 5. Press Enter to confirm filename

# Use when: Quick edits to config files
```

#### ⭐ TEXT EDITING - vi/vim (PROFESSIONAL STANDARD - MUST KNOW)

```bash
# Open file in vi
vi myfile.txt
vi /etc/nginx/nginx.conf
vi Dockerfile

# VI/VIM HAS TWO MODES:
# COMMAND MODE - when you open file (press ESC to enter)
# INSERT MODE - for typing (press 'i' to enter)

# ========== ENTER INSERT MODE ==========
i           # insert BEFORE cursor
I           # insert at BEGINNING of line
a           # append AFTER cursor
A           # append at END of line
o           # create NEW line BELOW
O           # create NEW line ABOVE

# Example: Open file, press 'i', type text, press ESC, then save

# ========== NAVIGATION IN COMMAND MODE (Press ESC first) ==========
h           # move left
j           # move down
k           # move up
l           # move right

# CURSOR MOVEMENT - FIRST/LAST OF FILE
gg          # go to FIRST line (most important!)
G           # go to LAST line (most important!)
:10         # go to line 10 (type colon, then number)
:$          # go to last line

# CURSOR AT FIRST/LAST CHARACTER OF LINE
^           # go to first character of line
$           # go to last character of line

# WORD MOVEMENT
w           # jump to next WORD
b           # jump to PREVIOUS word
e           # jump to END of word

# PRACTICAL EXAMPLE:
# gg = jump to top (good for checking file start)
# G = jump to end (good for checking errors at end)
# :100 = jump to line 100 (search error around line 100)

# ========== DELETION IN COMMAND MODE ==========
x           # delete character at cursor
dd          # delete ENTIRE line
d10d        # delete 10 lines
D           # delete from cursor to END of line
dw          # delete word

# ========== COPY/PASTE ==========
yy          # copy (yank) entire line
y10y        # copy 10 lines
p           # paste AFTER cursor
P           # paste BEFORE cursor
dd          # cut (delete) line

# EXAMPLE: Copy 5 lines and paste elsewhere
# 1. Position cursor on first line to copy
# 2. Type: 5yy
# 3. Move to destination
# 4. Type: p

# ========== UNDO/REDO ==========
u           # undo last change
Ctrl+r      # redo

# ========== FIND & REPLACE - MOST IMPORTANT ==========

# FIND TEXT
/word       # find "word" (press Enter)
n           # jump to next match
N           # jump to previous match
?word       # find backwards

# REPLACE (this is critical for DevOps configs!)
:s/old/new          # replace first in current line
:s/old/new/g        # replace ALL in current line
:%s/old/new/g       # replace ALL in entire file (MOST USED)
:10,20s/old/new/g   # replace in lines 10-20

# EXAMPLE: Change all "localhost" to "192.168.1.1"
# 1. Open file: vi config.conf
# 2. Type: :%s/localhost/192.168.1.1/g
# 3. Press Enter
# 4. Type: :wq

# PRACTICAL DEVOPS SCENARIOS:
# Change port in nginx config
# :%s/:80/:8080/g

# Change database host
# :%s/db.example.com/db.prod.com/g

# ========== SAVE & EXIT ==========
:w          # save (don't quit)
:q          # quit (only if no changes)
:wq         # save AND quit (MOST COMMON)
:q!         # quit WITHOUT saving (force)
:wq!        # force save and quit

# VIEW OPTIONS
:set number       # show line numbers (HELPFUL!)
:set nonumber     # hide line numbers
:set wrap         # enable line wrapping
:set nowrap       # disable line wrapping

# ========== COMPLETE EXAMPLE WORKFLOW ==========
# Scenario: Edit nginx config file

# 1. Open file
vi /etc/nginx/nginx.conf

# 2. Find error line
# Type: /error_log
# Type: n to find next

# 3. Edit that line
# Type: i (insert mode)
# Make changes
# Type: ESC (exit insert mode)

# 4. Find and replace multiple
# Type: :%s/localhost/0.0.0.0/g
# Press: Enter

# 5. Go to end to verify
# Type: G

# 6. Go to beginning to check
# Type: gg

# 7. Save and exit
# Type: :wq
# Press: Enter

# Use when: Professional editing, config files, Dockerfiles, YAMLs
```

#### ⭐ FILE SEARCHING & FILTERING - CRITICAL FOR TROUBLESHOOTING

```bash
# ========== SEARCH FOR TEXT IN FILES ==========
grep "error" /var/log/app.log
grep -i "ERROR" /var/log/app.log    # case-insensitive
grep -n "error" /var/log/app.log    # show line numbers (HELPFUL!)
grep -c "error" /var/log/app.log    # count matches
grep "error" /var/log/*.log         # search multiple files
grep -r "error" /var/log/           # recursive search in directories
grep -v "error" file.txt            # show lines NOT containing "error"
grep -A 5 "error" app.log           # show 5 lines AFTER match
grep -B 5 "error" app.log           # show 5 lines BEFORE match
grep -C 3 "error" app.log           # show 3 lines BEFORE and AFTER

# PRACTICAL DEVOPS SCENARIOS:
# Find all 404 errors in nginx log
grep "404" /var/log/nginx/access.log | wc -l

# Find errors with context
grep -B 2 -A 2 "Fatal" /var/log/app.log

# Find all failed login attempts
grep "Failed" /var/log/auth.log

# ========== FIND FILES BY NAME ==========
find / -name "myfile.txt"
find / -name "*.log"
find / -name "*.log" 2>/dev/null    # suppress error messages
find /var/log -mtime -7             # files modified in last 7 days
find /var/log -size +100M           # files larger than 100MB
find /var/log -type f -name "*.log" # only files
find /var/log -type d -name "apache*" # only directories

# Use when: 
# - Finding log files
# - Finding old files to clean up
# - Locating config files
```

#### ⭐ FILE PERMISSIONS - CRITICAL FOR SECURITY

```bash
# View permissions
ls -l file.txt
# Output: -rw-r--r-- 1 user group 1024 Nov 1 10:00 file.txt
# Meaning:
# - = file type
# rw- = owner (read, write, no execute)
# r-- = group (read only)
# r-- = others (read only)

# Permission Numbers:
# 7 = rwx (read, write, execute)
# 6 = rw- (read, write)
# 5 = r-x (read, execute)
# 4 = r-- (read only)
# 0 = --- (no permissions)

# ========== CHANGE PERMISSIONS (NUMERIC) ==========
chmod 755 script.sh      # rwxr-xr-x (common for executable scripts)
chmod 644 file.txt       # rw-r--r-- (common for regular files)
chmod 600 secret.txt     # rw------- (only owner can read/write)
chmod 777 file.txt       # rwxrwxrwx (DANGEROUS - everyone full access!)

# ========== CHANGE PERMISSIONS (SYMBOLIC) ==========
chmod +x script.sh       # add execute permission
chmod -x script.sh       # remove execute permission
chmod u+w file.txt       # add write for user
chmod g-r file.txt       # remove read for group
chmod o-rwx file.txt     # remove all permissions for others

# ========== CHANGE OWNERSHIP ==========
chown user file.txt           # change owner
chown user:group file.txt     # change owner and group
chown -R user:group mydir/    # recursive change (for directories)

# PRACTICAL DEVOPS SCENARIOS:
# Make script executable before running
chmod +x deploy.sh

# Give app full access to its directory
chown -R appuser:appgroup /opt/myapp
chmod -R 755 /opt/myapp

# Restrict access to sensitive files
chmod 600 ~/.ssh/id_rsa
chown ubuntu:ubuntu ~/.ssh/id_rsa

# Use when: Setting up deployment, securing files, fixing permission issues
```

#### ⭐ FILE SYSTEM INFORMATION

```bash
# ========== DISK SPACE ==========
df -h                    # show disk space in human-readable format
df -i                    # show inode usage
du -sh mydir/            # directory size
du -sh *                 # size of all items in current directory
du -sh /var/log/*        # size of each log directory

# Use when: Checking if disk is full (common error!)

# ========== MEMORY USAGE ==========
free -h                  # show memory in human-readable format
free -m                  # show memory in MB

# Use when: Checking if system is out of memory

# ========== SYSTEM INFORMATION ==========
uname -a                 # kernel and OS info
uname -r                 # kernel version only
cat /etc/os-release      # detailed OS information
lsb_release -a           # Linux version info

# Check CPU info
nproc                    # number of processors
cat /proc/cpuinfo        # detailed CPU information

# Use when: Understanding system capacity
```

#### ⭐ PROCESS MANAGEMENT - CRITICAL FOR DEVOPS

```bash
# ========== LIST PROCESSES ==========
ps                       # current shell processes
ps aux                   # all processes with details (MOST USED)
ps aux | grep java       # find specific process
ps aux | grep docker     # find docker processes
ps -ef                   # full format process list

# Use when: Finding which app is running

# ========== VIEW PROCESSES IN REAL-TIME ==========
top                      # basic process viewer
htop                     # better process viewer (install: apt install htop)
# Inside top/htop:
#   q = quit
#   M = sort by memory
#   P = sort by CPU
#   k = kill process
#   f = select columns

# Use when: Monitoring CPU and memory usage

# ========== PROCESS STATUS ==========
systemctl status nginx
systemctl status postgres
systemctl status jenkins

# Use when: Checking if service is running

# ========== START/STOP SERVICES ==========
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx

# Use when: Managing services

# ========== ENABLE ON BOOT ==========
sudo systemctl enable nginx    # start on boot
sudo systemctl disable nginx   # don't start on boot

# Use when: Ensuring service survives server restart

# ========== FIND PROCESS BY NAME ==========
pkill -f java             # kill all Java processes
pkill -9 nginx            # force kill
pgrep java                # find PID of Java process
pgrep -a nginx            # find PID with command line

# Use when: Stopping misbehaving apps

# ========== BACKGROUND/FOREGROUND ==========
job_command &             # run in background
Ctrl+Z                    # suspend process
bg                        # resume in background
fg                        # bring to foreground
jobs                      # list background jobs

# Use when: Running long tasks

# PRACTICAL DEVOPS SCENARIOS:
# Check if Java app is using too much memory
ps aux | grep java

# Kill stuck Docker process
pkill -9 docker

# Monitor CPU usage while deploying
top
```

#### ⭐ NETWORKING COMMANDS - CRITICAL FOR TROUBLESHOOTING

```bash
# ========== CHECK IP ADDRESS ==========
ip addr show
ip addr show eth0
ip route show

# Use when: Understanding network setup

# ========== CHECK CONNECTIVITY ==========
ping google.com
ping -c 5 google.com      # send 5 pings and exit

# Use when: Testing network connectivity

# ========== DNS RESOLUTION ==========
nslookup google.com
dig google.com
host google.com

# Use when: Testing DNS resolution

# ========== NETWORK CONNECTIONS - MOST IMPORTANT ==========
netstat -tulpn            # show all listening ports with PID (OLD)
netstat -a                # show all connections
netstat -an               # numeric format (faster)

ss -lntp                  # modern replacement (PREFERRED)
ss -lntp | grep 3000      # find process on port 3000
ss -lntp | grep LISTEN    # show listening ports

# Use when: 
# - Checking if port is in use
# - Finding which app is on which port
# - Diagnosing connection issues

# PRACTICAL SCENARIOS:
# Check if nginx is listening on port 80
ss -lntp | grep :80

# Check if Java app is on port 8080
ss -lntp | grep 8080

# ========== CHECK IF PORT IS OPEN ==========
curl http://localhost:3000
curl -I http://localhost:3000    # headers only
curl http://localhost:3000/health
curl -v http://localhost:3000    # verbose (see all details)

# Use when: Testing if web app responds

# ========== FIREWALL ==========
sudo ufw status
sudo ufw enable
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Use when: Configuring firewall rules
```

#### ⭐ TEXT PROCESSING COMMANDS

```bash
# ========== STREAM EDITOR (sed) ==========
sed 's/old/new/' file.txt        # replace first occurrence per line
sed 's/old/new/g' file.txt       # replace all occurrences
sed -i 's/old/new/g' file.txt    # replace in-file
sed '5d' file.txt                # delete line 5
sed '1,3d' file.txt              # delete lines 1-3

# ========== AWK (text processing) ==========
awk '{print $1}' file.txt        # print first column
awk '{print $1, $3}' file.txt    # print columns 1 and 3
awk 'NR==2' file.txt             # print line 2
awk -F: '{print $1}' /etc/passwd # use : as field separator

# ========== SORT ==========
sort file.txt                    # sort alphabetically
sort -n file.txt                 # sort numerically
sort -r file.txt                 # reverse sort
sort -u file.txt                 # unique sort (remove duplicates)

# ========== REMOVE DUPLICATES ==========
uniq file.txt
sort file.txt | uniq

# ========== COMPARE FILES ==========
diff file1.txt file2.txt
diff -y file1.txt file2.txt      # side-by-side comparison
```

#### ⭐ ENVIRONMENT & VARIABLES

```bash
# View environment variables
env
printenv
echo $HOME
echo $PATH
echo $USER
echo $PWD

# Set variable (temporary - only for this session)
export MY_VAR=value
export PATH=/new/path:$PATH

# Set variable (permanent - add to ~/.bashrc)
echo 'export MY_VAR=value' >> ~/.bashrc
source ~/.bashrc            # reload

# Check PATH
echo $PATH

# Use when: Managing system configuration
```

#### ⭐ PIPING & REDIRECTION - VERY USEFUL

```bash
# Pipe output to another command
ls -l | grep myfile
ps aux | grep java
cat log.txt | grep error
grep "error" /var/log/app.log | head -20

# Redirect output to file
command > output.txt       # overwrite file
command >> output.txt      # append to file
echo "hello" > file.txt

# Redirect error
command 2> error.txt       # redirect stderr
command 2>&1 output.txt    # redirect both stdout and stderr

# Redirect input
cat < input.txt

# Combine with pipe
ps aux | grep java | grep -v grep

# PRACTICAL DEVOPS SCENARIOS:
# Save all errors to file
terraform apply 2> errors.log

# Append deployment log
kubectl apply -f deployment.yaml >> deploy.log
```

#### ⭐ PACKAGE MANAGEMENT (Ubuntu/Debian)

```bash
# Update package list
sudo apt update

# Install package
sudo apt install package-name
sudo apt install -y package-name    # auto-yes

# Remove package
sudo apt remove package-name

# Update all packages
sudo apt upgrade

# Clean cache
sudo apt clean
```

---

### 1.2 TROUBLESHOOTING & LOG ANALYSIS - MOST CRITICAL SKILL

**Why?** 80% of DevOps time is spent debugging and reading logs.

#### ⭐ HOW TO READ LOGS EFFECTIVELY

```bash
# ========== FIND LOG FILES ==========
find /var/log -type f -name "*.log"

# Common log locations:
# /var/log/syslog          - system log
# /var/log/auth.log        - authentication
# /var/log/nginx/          - nginx web server
# /var/log/apache2/        - apache web server
# /var/log/docker/         - docker logs
# /var/log/jenkins/        - jenkins logs
# ~/.local/share/docker/   - app logs
# /opt/app/logs/           - application logs

# ========== TAIL FOR LIVE MONITORING (MOST IMPORTANT) ==========
# This is what you do 90% of the time when debugging

# Watch logs in real-time while something is running
tail -f /var/log/app.log

# Watch with line numbers (helpful!)
tail -f -n 50 /var/log/app.log    # follow with last 50 lines

# Watch multiple logs
tail -f /var/log/app.log /var/log/error.log

# Watch and filter for errors
tail -f /var/log/app.log | grep -i error

# Watch with timestamp
tail -f /var/log/app.log | grep "2024-01"

# Use when: 
# - Application just started, watching for startup errors
# - Deploying to production, monitoring for issues
# - Testing new code, checking for warnings

# ========== HEAD TO CHECK BEGINNING ==========
head -50 /var/log/app.log

# Use when: Understanding when logs started

# ========== FIND SPECIFIC ERRORS ==========
grep -i "error" /var/log/app.log
grep -i "failed" /var/log/app.log
grep "exception" /var/log/app.log
grep "fatal" /var/log/app.log
grep "500" /var/log/nginx/access.log  # HTTP 500 errors
grep "404" /var/log/nginx/access.log  # HTTP 404 errors

# Use when: Searching for specific issues

# ========== GET ERRORS WITH CONTEXT ==========
grep -B 5 -A 5 "error" /var/log/app.log
# -B 5 = show 5 lines BEFORE match
# -A 5 = show 5 lines AFTER match

# This is VERY HELPFUL to understand what caused the error!

# ========== COUNT ERROR OCCURRENCES ==========
grep "error" /var/log/app.log | wc -l
grep "404" /var/log/nginx/access.log | wc -l

# Use when: Assessing severity of issue

# ========== FIND ERRORS IN TIME WINDOW ==========
# Show errors from specific time
grep "2024-01-15 14:3" /var/log/app.log

# Use when: Issues happened at specific time

# ========== ANALYZE LOG PATTERNS ==========
# Find most common errors
grep "error" /var/log/app.log | sort | uniq -c | sort -rn

# Find top 10 IP addresses accessing your app
cut -d' ' -f1 /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -10

# Use when: Understanding system behavior
```

#### ⭐ COMMON TROUBLESHOOTING SCENARIOS

**SCENARIO 1: Application won't start**

```bash
# Step 1: Check if process is running
ps aux | grep java
ps aux | grep python
ps aux | grep node

# Step 2: Check recent logs
tail -100 /var/log/app.log

# Step 3: Look for ERROR or FATAL
grep -i "error\|fatal" /var/log/app.log | tail -20

# Step 4: Check specific error with context
grep -B 10 -A 5 "error" /var/log/app.log | tail -50

# Step 5: Check config file syntax
vim /etc/app/config.conf  # verify if config looks correct

# Step 6: Check permissions
ls -la /var/www/app/
ls -la /opt/app/

# Step 7: Try starting manually to see error
sudo systemctl restart app
journal ctl -xe  # see detailed error message

# Step 8: Check dependencies
# Is database running? Is cache running?
systemctl status postgres
systemctl status redis
```

**SCENARIO 2: High CPU usage**

```bash
# Step 1: See which process uses CPU
top
# Press 'P' to sort by CPU
# Note the PID of high-CPU process

# Step 2: Get more info about that process
ps aux | grep <PID>
ps -p <PID> -o lstart,cmd  # see when process started

# Step 3: Check if it's supposed to be running
# Is it a legitimate service or a runaway process?

# Step 4: If it's a runaway, kill it
kill -9 <PID>

# Step 5: Check logs for why it went crazy
tail -f /var/log/app.log

# Step 6: Check for infinite loops or memory leaks
grep -i "loop\|leak" /var/log/app.log
```

**SCENARIO 3: Disk is full**

```bash
# Step 1: Check disk usage
df -h
# If / or /var is 90%+ full, that's the problem

# Step 2: Find which directory uses space
du -sh /var/*
du -sh /home/*
du -sh /opt/*

# Step 3: Likely culprit: logs
du -sh /var/log/
ls -lhS /var/log/*.log | head -10

# Step 4: Check how big each log file is
ls -lh /var/log/app.log

# Step 5: Remove old logs (carefully!)
# Option 1: Delete old logs
rm /var/log/app.log.2023*

# Option 2: Rotate logs
logrotate -f /etc/logrotate.conf

# Step 6: Verify disk is freed
df -h

# Prevention: Add to crontab to rotate logs automatically
0 0 * * * /usr/sbin/logrotate -f /etc/logrotate.conf
```

**SCENARIO 4: Application responds with 404 errors**

```bash
# Step 1: Check if app is running
systemctl status app
ps aux | grep app

# Step 2: Check if it's listening on correct port
ss -lntp | grep app
ss -lntp | grep 3000

# Step 3: Check if port is correct in config
grep port /etc/app/config.conf
grep PORT ~/.env

# Step 4: Test if app responds
curl http://localhost:3000
curl http://localhost:3000/health
curl -v http://localhost:3000  # verbose to see all details

# Step 5: Check app logs for errors
tail -f /var/log/app.log

# Step 6: Check if firewall is blocking
sudo ufw status
sudo ufw allow 3000/tcp

# Step 7: Check nginx/apache config if using proxy
grep -i "upstream\|proxy_pass" /etc/nginx/nginx.conf

# Step 8: Check if routes are defined
grep "app.get\|app.post" app.js  # for Node.js
grep "@GetMapping" App.java      # for Java
```

**SCENARIO 5: Service keeps restarting**

```bash
# Step 1: Check service status
systemctl status app

# Step 2: Check recent logs
journalctl -u app -n 50

# Step 3: Look for crash reason
journalctl -u app -n 100 | grep -i "error\|crash\|exit"

# Step 4: Check app logs
tail -100 /var/log/app.log

# Step 5: Disable auto-restart temporarily to investigate
sudo systemctl disable app

# Step 6: Start manually and watch
/usr/bin/app --foreground
# This will show errors directly on terminal

# Step 7: Fix the issue (config, missing dependency, etc)

# Step 8: Re-enable auto-restart
sudo systemctl enable app
sudo systemctl start app

# Step 9: Verify it stays running
sleep 5 && systemctl status app
```

**SCENARIO 6: Memory keeps growing (memory leak)**

```bash
# Step 1: Check memory usage
free -h
df -h

# Step 2: Check which process uses memory
top
# Press 'M' to sort by memory

# Step 3: Get memory details
ps aux | sort -k4 -rn | head -5  # top 5 memory users

# Step 4: Check if it's increasing
# Run this twice with 10 second gap
ps -p <PID> -o pid,vsz,rss,cmd
# Wait 10 seconds
ps -p <PID> -o pid,vsz,rss,cmd
# If numbers increasing, it's a leak

# Step 5: Check logs for clues
tail -f /var/log/app.log

# Step 6: Temporary fix: restart the service
systemctl restart app

# Step 7: Find root cause (usually in app code)
# Check recent code changes
git log --oneline -20

# Step 8: Look for common causes
# - Unclosed connections
# - Accumulating data structures
# - Cache not clearing
grep -r "cache\|buffer" app.js
```

#### ⭐ QUICK REFERENCE: EMERGENCY DEBUGGING CHECKLIST

```bash
# ===== WHEN SOMETHING BREAKS =====

# 1. IS IT RUNNING?
ps aux | grep <app-name>
systemctl status <app-name>

# 2. CHECK LOGS
tail -50 /var/log/<app>.log
grep -i "error" /var/log/<app>.log | tail -20
grep -B 5 -A 5 "error" /var/log/<app>.log | tail -50

# 3. CHECK PORT
ss -lntp | grep <port-number>
curl http://localhost:<port>/health

# 4. CHECK DISK/MEMORY
df -h
free -h
du -sh /var/log/*

# 5. CHECK PROCESS HEALTH
top
ps aux | grep <process>

# 6. CHECK NETWORK
ping 8.8.8.8
ss -lntp
curl http://example.com

# 7. CHECK CONFIG
cat /etc/app/config.conf
echo $APP_ENV

# 8. CHECK PERMISSIONS
ls -la /opt/app/
ls -la /var/log/app.log

# 9. LIVE MONITOR
tail -f /var/log/app.log
top

# 10. RESTART
sudo systemctl restart <app>
sleep 2 && systemctl status <app>
```

---

### 1.3 Git and GitHub

**Why?** Version control is essential for team collaboration and CI/CD.

```bash
# Initialize repository
git init

# Configure git
git config user.name "Your Name"
git config user.email "your@email.com"

# Check status
git status

# Add files to staging
git add .

# Commit with message
git commit -m "Add feature: user login"

# Create a branch
git checkout -b feature/payment-gateway

# List branches
git branch -a

# Switch branch
git checkout main

# Merge branch
git merge feature/payment-gateway

# Add remote repository
git remote add origin https://github.com/user/repo.git

# Push to GitHub
git push -u origin main

# Pull latest changes
git pull origin main

# View commit history
git log --oneline

# View changes
git diff HEAD~1

# Revert commit
git revert <commit-hash>

# Reset to previous commit (CAREFUL!)
git reset --hard HEAD~1

# Stash changes temporarily
git stash

# Apply stashed changes
git stash pop
```

**Interview Questions:**

Q1: What is the difference between `git pull` and `git fetch`?
A: `git fetch` downloads changes without merging. `git pull` is `git fetch` + `git merge`.

Q2: How do you resolve a merge conflict?
A: Edit the conflicting files, remove conflict markers, stage the files, and commit.

Q3: What is a `.gitignore` file?
A: It specifies files/folders that should not be tracked by Git (e.g., `node_modules/`, `.env`, `*.log`).

Q4: Why should you never commit secrets to Git?
A: Secrets in Git history are permanent and visible to anyone with repo access. Use `.env` files and secret managers instead.

---

## PHASE 2: Build Tools & Code Quality (Weeks 3-4)

### 2.1 Maven

```bash
mvn -version
mvn clean
mvn compile
mvn test
mvn package
mvn install
mvn deploy
mvn package -DskipTests
mvn verify
mvn dependency:tree
```

### 2.2 SonarQube

```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts

mvn clean verify sonar:sonar \
  -Dsonar.projectKey=myproject \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=admin
```

---

## PHASE 3: Containerization (Weeks 5-6)

### 3.1 Docker

```bash
docker login
docker build -t myapp:1.0 .
docker images
docker run -d -p 8080:80 --name myapp myapp:1.0
docker ps
docker ps -a
docker logs <container-id>
docker logs -f <container-id>
docker exec -it <container-id> bash
docker stop <container-id>
docker rm <container-id>
docker rmi myapp:1.0
docker tag myapp:1.0 username/myapp:1.0
docker push username/myapp:1.0
docker pull ubuntu:22.04
docker inspect myapp:1.0
docker stats
```

---

## PHASE 4: Container Orchestration (Weeks 7-8)

### 4.1 Kubernetes (K8s)

```bash
kubectl cluster-info
kubectl get nodes
kubectl get pods
kubectl get pods -n kube-system
kubectl get pods -A
kubectl get deployments
kubectl get svc
kubectl get ingress
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl logs -f <pod-name>
kubectl logs <pod-name> --previous
kubectl exec -it <pod-name> bash
kubectl port-forward <pod-name> 8080:3000
kubectl apply -f deployment.yaml
kubectl delete -f deployment.yaml
kubectl delete pod <pod-name>
kubectl scale deployment myapp --replicas=5
kubectl set image deployment/myapp myapp=myapp:2.0
kubectl rollout undo deployment/myapp
kubectl rollout status deployment/myapp
kubectl create namespace production
kubectl top nodes
kubectl top pods
```

---

## PHASE 5: Infrastructure as Code (Weeks 9-10)

### 5.1 Terraform

```bash
terraform init
terraform fmt
terraform validate
terraform plan -out=tfplan
terraform apply tfplan
terraform apply -auto-approve
terraform show
terraform state list
terraform state show aws_instance.web
terraform state rm aws_instance.web
terraform destroy
terraform destroy -target=aws_instance.web
terraform output
terraform refresh
terraform import aws_instance.web i-1234567890abcdef0
```

---

## PHASE 6: CI/CD Pipeline Automation (Weeks 11-12)

### 6.1 Jenkins

```bash
sudo systemctl status jenkins
sudo systemctl start jenkins
sudo systemctl stop jenkins
sudo tail -f /var/log/jenkins/jenkins.log
```

---

## PHASE 7: Monitoring & Observability (Weeks 13-14)

### 7.1 Prometheus

```bash
docker run -d --name prometheus -p 9090:9090 prom/prometheus
```

### 7.2 Grafana

```bash
docker run -d --name grafana -p 3000:3000 grafana/grafana
```

---

## Interview Preparation Summary

### Core Concepts to Master:
1. Why DevOps exists (faster deployment, reliability)
2. CI/CD pipeline flow
3. Container advantages
4. Kubernetes orchestration
5. Infrastructure as Code benefits
6. Monitoring importance

### Hands-on Skills:
1. Write shell scripts
2. Create Dockerfile
3. Write K8s YAML manifests
4. Create Jenkins/GitHub Actions pipelines
5. Use Terraform
6. Query Prometheus metrics

### Soft Skills:
1. Debugging mindset
2. Reading logs effectively
3. Problem-solving approach
4. Communication of issues
5. Documentation

---

## Success Tips

✅ **Build a portfolio project** - E-commerce app deployed end-to-end
✅ **Practice troubleshooting** - Common errors and solutions
✅ **Understand the "why"** - Not just how to run commands
✅ **Keep a cheat sheet** - Commands you use frequently
✅ **Read documentation** - Official docs for tools you use
✅ **Join DevOps communities** - Learn from others' experiences
✅ **Stay updated** - New tools and best practices emerge

---

**Next Steps:**
1. Start with Phase 1 (Linux & Shell)
2. Complete one phase before moving to the next
3. Build the e-commerce project as you learn
4. Practice interview questions
5. Create GitHub portfolio
6. Contribute to open-source DevOps projects

Good luck! 🚀
