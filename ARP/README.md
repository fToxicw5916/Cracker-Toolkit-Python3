# The ARP module
Occasionally, you run into such a well-though-out, amazing Python library that even dedicating a whole chapter to it can't do it justice. Scapy is what we are talking about. The work you have done in the privious chapters could have done with just one or two lines of Scapy. If you don't have Scapy, goto https://scapy.net/ to install it.
## mail_sniffer.py
Run:
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
