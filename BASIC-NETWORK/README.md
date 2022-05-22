# The Basic-Network module
The network is and always will be the sexiest arena for a hacker. An attacker can do almost anything with simple network access, such as scan for hosts, inject packets, sniff data, and remotely exploit hosts. But if you've worked your way into the deepest depths of an enterprise target, you may find yourself in a bit of conundrum: you have no tools to execute network attacks. No netcat. No wireshark. No compiler, and no means to install one. However, you might be surprised to find that in many cases, you'll have a Python install. So that's where we'll begin.
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

## ssh_cmd.py
### Connect to Linux server
```bash
python3 ssh_cmd.py
```

## ssh_rcmd.py and ssh_server.py
### Server side
```bash
python3 ssh_server.py
```
### Client
```bash
python3 ssh_rcmd.py
```
