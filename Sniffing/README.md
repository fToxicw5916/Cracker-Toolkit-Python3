# The Sniffing module
Network sniffers allow you to see packets entering and exiting a target machine. As a result, they have many practical uses before and after exploitation. In some cases, you'll be able to use existing sniffing tools like Wireshark or a Pythonic solution like Scapy. Nevertheless, there's an advantage to knowing how to throw together your own quick sniffer to view and decode network traffic. Writing a tool like this will also give you a deep appreciation for the mature tools, as these can painlessly take care of the finer points with little effort on your part. You'll also likely to pick up some Python techniques and perhaps a better understanding of how the low-level-networking bits work.
## sniffer.py
On one terminal, type:
```bash
python3 sniffer.py
```
On another terminal, type:
```bash
ping nostarch.com
```
In your first window, you should see some output. We have captured the ping request!
## sniffer_ip_header_decode.py
Open a terminal and run:
```bash
python3 sniffer_ip_header_decode.py
```
Then, on Windows, open a browser and open google.com, you should see some output from the terminal.

On Linux, open another terminal and run:
```bash
ping google.com
```
You should also be able to see some output on the first terminal.
