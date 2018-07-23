# Try / Except


###### Try / Except is pretty useful for python, where you don't want to have any sort of problems with errors breaking the code.

In python, a typical Try/Except code block is iterated (for example, inside a code block).

```python
import logging as log

'''
This imports the log function which allows
us to mark down any types of errors that
happen during the try/except loops.
'''

log.basicConfig(
  format = "[%(levelname)s] (%(asctime)s) %(message)s",
  '''
  formats the log message, not actually needed for the program to work
  REMEMBER TO PUT COMMA AT THE END OF A LINE
  '''
  datefmt = ("%Y/%m/%d %H:%M:%S")
  #sets the format for asctime
  level = log.DEBUG,
  """
  allows messages from debug to critical appear in the console.
  (this can also be moved into a log file which will be explained a bit below)
  """
)

while True:
  try:
    x = float(input("number 1"))
    log.info("first number placed which was "+str(x))
    y = float(input("number 2"))
    log.info("second number placed which was "+str(y))
    print(x/y)
  except(ZeroDivisionError):
    log.error("Attempted to divide by 0")
  except(ValueError);
    log.error("Given a non-float compatible character")

'''
Basically, if you give something that isn't part of the "float" thing, then
the code won't break and will instead log an error message, then go for
the try again. This code will keep on iterating. If the computer gets something
it cannot process, the data will just be requested again (without breaking)
which is essential to make sure the program doesn't crash. This works better
if you use it in a subprogram, where you can do try/except/else, and if you
don't set an exception that happens to apply to your case, then it will
return the else statement (as long as you 'define' it)
'''
```

Try/Except is super cool stuff
