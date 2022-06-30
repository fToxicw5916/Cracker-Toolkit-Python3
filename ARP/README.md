# The ARP module
**All of the scripts in this module used Scapy! Install before use!**
```bash
pip install scapy
```
## mail-sniffer.py
```bash
sudo python mail_sniffer.py
```
When you are trying to login with a mail client, you should see some outputs.

## arper.py
On Linux, run `sudo su`, and then use:
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```
to enable forward packets. On Mac, use:
```bash
sudo sysctl -w net.inet.ip.forwarding=1
```
to enable it.
Then, run the Python script as root:
```bash
sudo python arper.py 192.168.1.193 192.168.1.154 en0
```

## recapper.py
Remember to change some of the variable in the program before running!
```bash
sudo apt-get install libopencv-dev python3-opencv python3-numpy python3-scipy
```
Then, run:
```bash
python3 recapper.py
```

## detector.py
Remember to change some of the variables in the program before running!
Run:
```bash
python3 detector.py
```
