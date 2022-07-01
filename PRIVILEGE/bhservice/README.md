# Vulnerable BlackHat Service
## bhservice.py
**Config before using!**
**Change bhservice_task.vbs.txt to bhservice_task.vbs before using!**
First, install `pyinstaller`:
```bash
pip install pyinstaller
```
Use pyinstaller on the Python script:
```bash
pyinstaller -F --hiddenimport win32timezone bhservice.py
```
Then, on Windows, run as Administrator:
```bash
bhservice.exe install
```
On Linux:
```bash
sudo ./bhservice install
```
Then, on Windows, run as Administrator to start the service:
```bash
bhservice.exe start
```
On Linux:
```bash
sudo ./bhservice start
```
If you want to stop the service, on Windows as Administrator run:
```bash
bhservice.exe stop
```
On Linux:
```bash
sudo ./bhservice stop
```
