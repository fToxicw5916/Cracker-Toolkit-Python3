# The Git module
**Install github3.py module before use!**
```bash
pip install github3.py
```
**Create a Github repo for this directory before use!**
```bash
cd GIT
git init
mkdir modules
mkdir config
mkdir data
touch .gitignore
git add .
git commit -m "Initialized."
git remote add origin https://github.com/<Your username>/<Your repo>.git
git push origin master
```
## github-trojan.py
```bash
python github_trojan.py
```
Then, run:
```bash
git pull origin master
```
You should receive the data files.
