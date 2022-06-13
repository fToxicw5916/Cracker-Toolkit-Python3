# The Git module
Suppose you've compromised a machine. Now you want it to automatically perform tasks and report its findings back to you. In this module, we'll create a trojan framework that will appear innocuous on the remote machine, but we'll be able to assign it all sorts of nefarious tasks.

You don't need to run dirlister.py and environment.py.
## github-trojan.py
Run:
```bash
python github_trojan.py
```
Then, run:
```bash
git pull origin master
```
You should receive the data files.
