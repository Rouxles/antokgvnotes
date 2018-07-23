# Logging in Python 3

Logging is a very basic feature of Python that doesn't do anything in terms of coding, but is very useful for helping with debugging and provides a good log (duh) of what's going on as long as the programmer sets it initially.

[Very helpful website with basically everything you need](https://docs.python.org/3/howto/logging.html)

**First of all, you need to import the logging function**

To do so, do `import logging` at the top of your python file.

This will put the prebuilt function of logging that python has, and imports it into your python file.

---

## A very simple example of logging is in the code shown below.

```Python
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
```
This will output
```
WARNING:root:Watch out!
```
**Why is this?**  
This is because Python is set to only log values of WARN and above, so the INFO tag will not show because it is not high enough priority for it to show on the console log.

To fix this, one of the solutions is to log everything into a standalone text file.

```python
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

What the above will do is make a file called example.log (if it isn't already created), then add everything above the logging level DEBUG into the text file.

If we then look at our text file, we will get

```
DEBUG:root:This message should go to the log file
INFO:root:So should this
WARNING:root:And this, too
```
Looks very ugly right now, but that can be fixed.
