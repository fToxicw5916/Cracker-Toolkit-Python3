# The Offensive Forensics module
**Install Volatility and pycryptodome before use!**
```bash
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3/
python setup.py install
pip install pycryptodome
```
To see the plug-ins Volatility offers, as well as a list of options, use:
```bash
vol --help
```
On Linux or Mac, use:
```bash
python vol.py --help
```
The windows.info plug-in shows the operating system and kernel information of the memory sample:
```bash
vol -f WinDev2007Eval-Snapshot4.vmem windows.info
```
The registry.printkey plug-in can output values of a key in the registry. Key `ControlSet001/Services` lists the installed services:
```bash
vol -f WinDev2007Eval-7d959ee5.vmem windows.registry.printkey --key 'ControlSet001/Services'
```
