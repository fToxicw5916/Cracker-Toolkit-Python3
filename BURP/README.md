# The Burp module
If you've ever tried hacking a web application, you've likely used Burp Suite to perform spidering, proxy browser traffic, and carry out other attacks. Burp Suite also allow you to create your own tooling, called *extensions*. Using Python, Ruby, or pure Java, you can add panels in the Burp GUI and build automation techniques into Burp Suite. That is what we will be doing in this section.

Install Jython before using the tools. You can download it [here](https://www.jython.org/download)

Let Burp load Jython - Click the Extender tab and click the Options tab. In Python Environment section, select the location of your Jython JAR file. You can leave the rest of the options alone. Now, we are ready to start!
## bhp_fuzzer.py
### Load the file
Click the Extender tab, then click the Add button. Add the Python file, then switch Standard Output to Show in UI, do the same for Standard Error.
### Attack!
We are going to use [this](http://testphp.vulnweb.com/) site for our first try. Use the search bar on their site to submit a search for the string "test". Capture the request, then right click and send it to Intruder. Click the Intruder tab, don't change anything and let Burp choose what it fuzz. Now click Payload, click the Payload Type drop-down and select Extension-Generated. In the Payload Options section, click the Select-Generator button and choose BHP Payload Generator from the drop-down. Now we're ready, click Intruder and then select Start Attack. Then, from the results, we can see that it has a SQL Injection exploit.
