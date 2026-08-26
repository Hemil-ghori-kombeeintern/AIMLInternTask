# Linux_Daily_Developer_Cheat_Sheet

# Navigation

## `pwd`

**What:** Shows the current working directory.

**Why use it:** Helps you know exactly where you are before running commands.

```bash
pwd
```

**Example:**

```
/home/hemil/projects
```

---

## `ls`

**What:** Lists files and directories.

**Why use it:** Quickly check what exists in the current directory.

```bash
ls
```

**Example:**

```
app.py  README.md  src  tests
```

---

## `ls -la`

**What:** Shows all files, including hidden files, with detailed information.

**Why use it:** Very useful for checking `.git`, `.env`, permissions, ownership, and file sizes.

```bash
ls -la
```

**Example:**

```
drwxr-xr-x  project
-rw-r--r--  .env
drwxr-xr-x  .git
```

---

## `cd`

**What:** Changes the current directory.

**Why use it:** Move between project folders.

```bash
cd project
```

**Example:**

```bash
cd backend
```

---

## `cd ..`

**What:** Goes one directory up.

**Why use it:** Quickly return to the parent folder.

```bash
cd ..
```

**Example:**

```
/home/hemil/project/backend
↓
/home/hemil/project
```

---

## `cd ~`

**What:** Goes to your home directory.

**Why use it:** Quickly return to your personal Linux directory.

```bash
cd ~
```

---

## `cd -`

**What:** Goes back to the previous directory.

**Why use it:** Useful when switching between two project folders.

```bash
cd -
```

---

## `clear`

**What:** Clears the terminal screen.

**Why use it:** Keeps the terminal clean and easier to read.

```bash
clear
```

---

## `history`

**What:** Shows previously executed commands.

**Why use it:** Find and reuse commands you ran earlier.

```bash
history
```

Example:

```bash
history | grep git
```

---

# Create Files & Folders

## `mkdir`

**What:** Creates a directory.

**Why use it:** Create folders for projects, source code, tests, etc.

```bash
mkdir project
```

**Example:**

```bash
mkdir backend
cd backend
```

---

## `mkdir -p`

**What:** Creates nested directories.

**Why use it:** Creates the complete directory path even if parent folders do not exist.

```bash
mkdir -p src/components
```

Creates:

```
src/
└── components/
```

---

## `touch`

**What:** Creates an empty file.

**Why use it:** Quickly create source files, configuration files, or documentation.

```bash
touch app.py
```

**Example:**

```bash
touch server.js README.md
```

---

# Copy, Move & Rename

## `cp`

**What:** Copies a file.

**Why use it:** Create backups or duplicate files.

```bash
cp file.txt backup.txt
```

**Example:**

```bash
cp .env .env.backup
```

---

## `cp -r`

**What:** Copies a directory and its contents.

**Why use it:** Duplicate a complete project/folder.

```bash
cp -r project backup/
```

---

## `mv`

**What:** Moves or renames files/directories.

**Why use it:** Rename files or move them between folders.

Rename:

```bash
mv old.txt new.txt
```

Move:

```bash
mv file.txt folder/
```

---

# Delete

## `rm`

**What:** Deletes a file.

**Why use it:** Remove files you no longer need.

```bash
rm file.txt
```

**Example:**

```bash
rm temporary.txt
```

---

## `rm -r`

**What:** Deletes a directory and its contents recursively.

**Why use it:** Remove a folder containing files/subfolders.

```bash
rm -r folder/
```

⚠️ Linux normally does not send deleted files to a recycle bin when using `rm`.

---

## `rm -rf`

**What:** Forcefully removes directories and their contents.

**Why use it:** Sometimes useful for removing a directory that contains protected files.

```bash
rm -rf folder/
```

⚠️ **Use with extreme care. Always verify the path first.**

---

# Read Files

## `cat`

**What:** Prints a file’s contents to the terminal.

**Why use it:** Quickly inspect small files such as JSON, configuration files, or README files.

```bash
cat file.txt
```

---

## `less`

**What:** Opens a file for scrolling.

**Why use it:** Better than `cat` for large files and logs.

```bash
less app.log
```

Useful keys:

```
Space → Next page
b     → Previous page
q     → Quit
```

---

## `head`

**What:** Shows the beginning of a file.

**Why use it:** Quickly inspect the first lines of a file or log.

```bash
head file.txt
```

First 20 lines:

```bash
head -n 20 file.txt
```

---

## `tail`

**What:** Shows the end of a file.

**Why use it:** Useful for checking the latest log entries.

```bash
tail app.log
```

---

## `tail -f`

**What:** Continuously follows new lines added to a file.

**Why use it:** Very useful for monitoring application/server logs.

```bash
tail -f app.log
```

Example:

```
Server started
Request received
Database connected
```

Press:

```
Ctrl + C
```

to stop following the log.

---

# Search

## `find`

**What:** Searches for files and directories.

**Why use it:** Find files when you don’t know exactly where they are.

```bash
find . -name "app.py"
```

Find all JavaScript files:

```bash
find . -name "*.js"
```

Example:

```bash
find src/ -name "*.py"
```

---

## `grep`

**What:** Searches for text inside files.

**Why use it:** Find code, error messages, configuration values, or function names.

```bash
grep "text" file.txt
```

Example:

```bash
grep "PORT" .env
```

---

## `grep -r`

**What:** Searches recursively inside directories.

**Why use it:** Search across an entire project.

```bash
grep -r "login" src/
```

---

# Users & Groups

## `whoami`

**What:** Shows the current username.

**Why use it:** Confirm which user you are currently using.

```bash
whoami
```

Example:

```
hemil
```

---

## `id`

**What:** Shows user ID, group ID, and group membership.

**Why use it:** Troubleshoot ownership and permission problems.

```bash
id
```

---

## `groups`

**What:** Shows groups the current user belongs to.

**Why use it:** Check whether you have access through a particular group.

```bash
groups
```

Specific user:

```bash
groups username
```

---

## `who`

**What:** Shows users currently logged into the system.

**Why use it:** More useful on shared Linux servers.

```bash
who
```

---

# Permissions

Linux permissions are divided into:

```
Owner | Group | Others
```

Permission types:

```
r = read
w = write
x = execute
```

Numeric values:

```
r = 4
w = 2
x = 1

7 = rwx
6 = rw-
5 = r-x
4 = r--
0 = ---
```

Check permissions:

```bash
ls -l
```

Example:

```
-rwxr-xr-- 1 hemil developers 1200 script.sh
```

Meaning:

```
Owner   → rwx → 7
Group   → r-x → 5
Others  → r-- → 4
```

So the permission is:

```
754
```

---

## `chmod`

**What:** Changes file or directory permissions.

**Why use it:** Give/remove read, write, or execute access.

### Common examples

```bash
chmod 755 script.sh
```

Use when:

```
Owner → read/write/execute
Group → read/execute
Others → read/execute
```

---

```bash
chmod 644 file.txt
```

Use for normal files:

```
Owner → read/write
Group → read
Others → read
```

---

```bash
chmod 700 private.sh
```

Use when only the owner should access the file.

---

```bash
chmod 600 secret.txt
```

Useful for private configuration/credential files.

---

### Symbolic permissions

Make script executable:

```bash
chmod +x script.sh
```

Give owner execute permission:

```bash
chmod u+x script.sh
```

Give group write permission:

```bash
chmod g+w file.txt
```

Remove others’ read permission:

```bash
chmod o-r file.txt
```

---

# `sudo`

**What:** Runs a command with elevated privileges.

**Why use it:** Some system-level operations require administrator/root permissions.

```bash
sudo apt update
```

Install software:

```bash
sudo apt install git
```

Change ownership:

```bash
sudo chown user:group file.txt
```

⚠️ Don’t use `sudo` unnecessarily. A command running with elevated privileges can modify system files.

---

# Ubuntu/Debian Packages

## `apt update`

**What:** Updates the local package information.

**Why use it:** Do this before installing/upgrading packages so the package information is current.

```bash
sudo apt update
```

---

## `apt upgrade`

**What:** Upgrades installed packages.

**Why use it:** Keep system software updated.

```bash
sudo apt upgrade
```

---

## `apt install`

**What:** Installs a package.

**Why use it:** Install development tools such as Git, curl, Python, etc.

```bash
sudo apt install git
```

Example:

```bash
sudo apt install git curl
```

---

## `apt remove`

**What:** Removes an installed package.

**Why use it:** Uninstall software you no longer need.

```bash
sudo apt remove git
```

---

# Networking

## `ip addr`

**What:** Shows network interfaces and IP addresses.

**Why use it:** Check your machine’s network configuration.

```bash
ip addr
```

---

## `ping`

**What:** Tests network connectivity to a host.

**Why use it:** Check whether a host is reachable.

```bash
ping google.com
```

Stop with:

```
Ctrl + C
```

---

# Pipes & Redirection

## Pipe `|`

**What:** Sends the output of one command to another command.

**Why use it:** Combine commands to filter or process information.

```bash
ps aux | grep node
```

Meaning:

```
ps aux → produces processes
        ↓
grep node → filters Node.js processes
```

---

## `>`

**What:** Writes command output to a file, replacing existing content.

**Why use it:** Save command output.

```bash
ls -la > files.txt
```

---

## `>>`

**What:** Appends output to a file.

**Why use it:** Add new output without deleting existing content.

```bash
ls -la >> files.txt
```

---

## `2>`

**What:** Redirects error output to a file.

**Why use it:** Save errors for debugging.

```bash
command 2> error.txt
```

---

# ⭐ Most Important Daily Commands

These are the commands you should remember first as a developer:

```bash
pwd
ls -la
cd
mkdir
touch
cp
mv
rm
cat
less
grep
find

chmod
chown
sudo
```

---

# 🧠 Quick Memory

```
Navigation
→ pwd, ls, cd

Files
→ mkdir, touch, cp, mv, rm

Read/Search
→ cat, less, grep, find

Permissions
→ ls -l, chmod, chown, sudo

Process
→ ps, top, kill

Network
→ ip, ping, curl, ss

Python
→ python3, venv, pip

Node
→ node, npm

Git
→ status, pull, add, commit, push
```

---

# Quick Reference Table

| Command | Why you use it | Example |
| --- | --- | --- |
| `pwd` | Know current location | `pwd` |
| `ls -la` | See all files/details | `ls -la` |
| `cd` | Move directories | `cd backend` |
| `mkdir` | Create folder | `mkdir src` |
| `touch` | Create file | `touch app.py` |
| `cp` | Copy | `cp a.txt b.txt` |
| `mv` | Move/rename | `mv old.js new.js` |
| `rm` | Delete | `rm temp.txt` |
| `cat` | Read small file | `cat README.md` |
| `less` | Read large file | `less app.log` |
| `grep` | Search text | `grep "error" app.log` |
| `find` | Find files | `find . -name "*.py"` |
| `chmod` | Change permissions | `chmod 755 script.sh` |
| `chown` | Change ownership | `sudo chown user file` |
| `sudo` | Admin operation | `sudo apt update` |
| `ps` | View processes | `ps aux` |