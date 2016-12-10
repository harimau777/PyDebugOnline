#! /bin/bash/ python

import sys
import cStringIO
import traceback
import re

#********************
# Trace Functions
#********************
def setupTrace():
  #Redirect stdout to a buffer so that we can capture it in the trace callback:
  stdout_ = sys.stdout
  stream = cStringIO.StringIO()
  sys.stdout = stream

  #Compile RegExs:
  lineNumber = re.compile('line (\d+)')
  function = re.compile('in ([^\n]+)\n')

  #Define the trace callback:
  def traceCallback(frame, event, arg):
    #Get any value displayed by this line of code:
    value = stream.getvalue()
    stream.truncate(0)

    #Get the stack trace:
    callStack = map(lambda frame: [int(lineNumber.search(frame).group(1)), function.search(frame).group(1)], traceback.format_stack())
    callStack.pop() #Remove the frame corresponding to this callback

    #Print the stack trace and displayed value:
    sys.stdout = stdout_
    print [callStack, value]
    sys.stdout = stream

    return traceCallback

  #Start the trace:
  sys.settrace(traceCallback)

#Test Code:
import random
def main():
    print "In main"
    for i in range(5):
        print i, random.randrange(0, 10)
    print "Done."

setupTrace()
main()

#********************
# AJAX Functions
#********************

# def sendMessage(message):
#   return
#  req = requests.post('___http___', data = {'message', message})
