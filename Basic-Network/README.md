# The Basic-Network module
## netcat.py
### Get help:
```bash
python3 netcat.py --help
```

### Start a Command Shell:
Server side:
```bash
python3 netcat.py -t 127.0.0.1 -p 5555 -l -c
```
Client side:
```bash
python3 netcat.py -t 127.0.0.1 -p 5555
```
Use CTRL-D to send the End of file (EOF) marker and start the command shell.

### Execute a single command:
Server side:
```bash
python3 netcat.py -t 127.0.0.1 -p 5555 -l -e="cat /etc/passwd"
```
Client side (1):
```bash
python3 netcat.py -t 127.0.0.1 -p 5555
```
Client side (2):
You can also use the original NC:
```bash
nc 127.0.0.1 5555
```

### Send out requests:
```bash
echo -ne "GET / HTTP/1.1\r\nHost: www.bing.com\r\n\r\n" | python3 netcat.py -t www.bing.com -p 80
```

## proxy.py
### Get help:
```bash
python3 proxy.py
```

### Against FTP server:
```bash
sudo python3 proxy.py 127.0.0.1 21 ftp.sun.ac.za 21 True
```
Use sudo because port 21 is a privileged port.
On another terminal:
```bash
ftp 127.0.0.1
```
