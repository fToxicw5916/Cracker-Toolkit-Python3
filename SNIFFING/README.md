# The Sniffing module
## sniffer.py
On one terminal, type:
```bash
python3 sniffer.py
```
On another terminal, type:
```bash
ping nostarch.com
```
In your first window, you should see some output.

## sniffer-ip-header-decode.py
Open a terminal and run:
```bash
python3 sniffer_ip_header_decode.py
```
Then, on Windows, open a browser and open `google.com`, you should see some output from the terminal.
On Linux, open another terminal and run:
```bash
ping google.com
```
You should also be able to see some output on the first terminal.

## sniffer-with-icmp.py
Open a terminal and run:
```bash
python3 sniffer_with_icmp.py
```
Then, on Windows, open a browser and open `google.com`, you should see some output from the terminal.
On Linux, open another terminal and run:
```bash
ping google.com
```

## scanner.py
**Change parameters before use! Use `ifconfig` on Linux or `ipconfig` on Windows to check your IP address. I'm on 192.168.0.187, so we set the scanner to hit 192.168.0.0/24.**
```bash
python scanner.py
```
You should see an output that tells you what hosts are responding.
