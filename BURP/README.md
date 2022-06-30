# The Burp module
**Install Jython before using! You can download it [here](https://www.jython.org/download)**
## bhp-fuzzer.py
### Load the file
Click the Extender tab, then click the Add button. Add the Python file, then switch Standard Output to Show in UI, do the same for Standard Error.
### Attack!
We are going to use [this](http://testphp.vulnweb.com/) site for our first try. Use the search bar on their site to submit a search for the string "test". Capture the request, then right click and send it to Intruder. Click the Intruder tab, don't change anything and let Burp choose what it fuzz. Now click Payload, click the Payload Type drop-down and select Extension-Generated. In the Payload Options section, click the Select-Generator button and choose BHP Payload Generator from the drop-down. Now we're ready, click Intruder and then select Start Attack. Then, from the results, we can see that it has a SQL Injection exploit.

## bhp-bing.py
Load the file by the samw way. Right click the GET request you got, and you should see a "Send to Bing" option. Click it, you should start to see results from Bing. If you click the Target tab and select Scope, you should see new items automatically added to the target scope.
## bhp-wordlist.py
Load the file by the same way we have loaded the previous scripts. In the Dashboard tab, select New live Task, when the dialog appears, choose Add all links observed in traffic and click OK. After you configured the scan, browse to a website and run it. Once Burp has visited all the links on the target site, select all the requests in the top-right pane in the Target tab, right-click them to bring up to the context menu, and select Create Wordlist. Now check the Output Tab of the extension. You should see a wordlist ready there.
