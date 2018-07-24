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
```python
>>>WARNING:root:Watch out!
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

If we then look at our **text file** called *example.log*, we will get

```python
>>>DEBUG:root:This message should go to the log file
>>>INFO:root:So should this
>>>WARNING:root:And this, too
```
###### Looks very ugly right now, but that can be fixed.

If you set the basicConfig() of the logging function, you will get to format how your log file will look. This will remove the 'root' part of any of the log messages.

For all the arguments for basicConfig, [click here.](https://docs.python.org/3/library/logging.html#logrecord-attributes)

```python
import logging

logging.basicConfig(
    format = "[%(levelname)s] (%(asctime)s) %(message)s",
    '''
    this will make the format of the log look like
    [INFO] (2018/08/08 23:59:59) Hi - which looks way better than what was shown above.
    '''
    datefmt = ("%Y/%m/%d %H:%M:%S"),
    '''
    This sets the format for what goes in the %(asctime) section.
    There are arguments for the time in the link below.
    '''
    level = logging.DEBUG, #shows everything above debug level
)
```

For all the arguments for datefmt, [see this link.](https://docs.python.org/2/library/time.html#time.strftime)

Now, if you run `logging.info('I told you so')` on a setup python file, then you will get

```
>>>[INFO] (2018/08/08 23:59:59) I told you so
```

You can also log variable data. This could mean that you can log data that the user inputs into the variable itself.

```python
import logging

x = 5
y = "Birds"

logging.basicConfig(
    format = "[%(levelname)s] %(message)s",
    level = logging.DEBUG,
)

logging.warning('%s types of %s', x, y)
```

Would output:

```python
>>>[WARNING] 5 types of Birds.
```

The logging priority levels are shown below.

| Level | Numeric Value |
| :---: | ---: |
| `CRITICAL` | 50 |
| `ERROR` | 40 |
| `WARNING` | 30 |
| `INFO` | 20 |
| `DEBUG` | 10 |
| `NOTSET` | 0 |
