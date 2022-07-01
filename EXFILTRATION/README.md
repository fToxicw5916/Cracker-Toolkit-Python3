# The Exfiltration module
## cryptor.py
Run:
```bash
python cryptor.py
```
First. Then, delete the '#' sign at the bottom of the file and add it to the 'generate' line, so it look like this:
```python
# generate()
plaintext = b'hey there you.'
print(decrypt(encrypt(plaintext)))
```
Then, run the program again.

## email-exfil.py
**Run after configuration!**
```bash
python email_exfil.py
```

## transmit-exfil.py
**Run after configuration!**
```bash
python transmit_exfil.py
```

## paste-exfil.py
**Run after configuration!**
You will need a pastebin account and a API key to run.
```bash
python paste_exfil.py
```

## exfil.py
Run:
```bash
python exfil.py
```
