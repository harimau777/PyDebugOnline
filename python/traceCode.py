#!/bin/bash/ python

import sys
import cStringIO
import traceback
import re
import json

#********************
# setupTrace
#********************
def setupTrace():
  #Redirect stdout to a buffer so that we can capture it in traceCallback:
  stdout_ = sys.stdout
  stream = cStringIO.StringIO()
  sys.stdout = stream

  #Compile RegExs:
  lineNumber = re.compile('line (\d+)')
  func = re.compile('in ([^\n]+)\n')

  #Define the trace callback:
  def traceCallback(frame, event, arg):
    #Get any value displayed by this line of code:
    value = stream.getvalue().strip()
    stream.truncate(0)

    #Get the stack trace:
    callStack = map(lambda frame: [int(lineNumber.search(frame).group(1)), func.search(frame).group(1)], traceback.format_stack())
    callStack.pop() #Remove the frame corresponding to this callback

    #Print the stack trace and displayed value:
    sys.stdout = stdout_
    print json.dumps([callStack, value])
    sys.stdout = stream

    return traceCallback

  #Start the trace:
  sys.settrace(traceCallback)

#********************
# main
#********************
if __name__ == __main__
  code = sys.argv[1]
  setupTrace()
  exec(code)
