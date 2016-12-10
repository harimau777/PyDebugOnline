#! /bin/bash/ python

import sys
import cStringIO
import traceback
import re

#********************
# Trace Functions
#********************
def parseCallStack(callStack):
  for line in callStack:
    'line \d+'
    'in [^\n]+\n'

def setupTrace():
  #Redirect stdout to a buffer so that we can capture it in the trace callback:
  stdout_ = sys.stdout
  stream = cStringIO.StringIO()
  sys.stdout = stream

  #Define the trace callback:
  def traceCallback(frame, event, arg):
    value = stream.getvalue()
    stream.truncate(0)
    callStack = []
    for line in traceback.format_stack():
      i = re.search('line (\d+)', line)
      j = re.search('in ([^\n]+)\n', line)
      callStack.append([i.group(1), j.group(1)])

    sys.stdout = stdout_
    print [callStack, value]
    sys.stdout = stream
    

    return traceCallback

  #Start the trace:
  sys.settrace(traceCallback)



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
