#!/bin/bash/ python

import sys
import cStringIO
import traceback
import re
import json
import argparse
import os

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
# parseArguments
#********************
def parseArguments():
  #Parse command line arguments:
  parser = argparse.ArgumentParser(description = 'Steps through Python code and prints debug information to STDOUT')
  parser.add_argument('-h', '--help', action = 'help', help = 'Display help')
  group = parser.add_mutually_exclusive_group(required = True)
  group.add_argument('-s', '--string', dest = 'code', help = 'String containing the code to be parsed')
  group.add_argument('-f', '--file', dest = 'file', type=argparse.FileType('r'), help='File containing the code to be parsed')
  parser.parse_args()

  #If the code was supplied as a file, then read the file
  if file in locals():
    if os.fstat(file.fileno()).st_size <= 1048576:
      code = file.read()
    else:
      return 'Error: File too large'

  return code

#********************
# main
#********************
if __name__ == __main__
  code = parseArguments()
  setupTrace()
  exec(code)
