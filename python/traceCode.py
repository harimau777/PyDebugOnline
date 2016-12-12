#!/bin/bash/python

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
  exceptionType = re.compile('exceptions\.([^\']+)\'')

  #Define the trace callback:
  def traceCallback(frame, event, arg):
    #Get any value displayed by this line of code:
    if (event == 'exception') or (event == 'c_exception'):
      value = exceptionType.search(str(arg[0])).group(1) + ': ' + arg[1]
    else:
      value = stream.getvalue().strip()
    stream.truncate(0)

    #Get the stack trace:
    callStack = map(lambda frame: [int(lineNumber.search(frame).group(1)), func.search(frame).group(1)], traceback.format_stack())
    callStack = callStack[1 : -1] #Remove the frame corresponding to this callback

    #Determine if the program has halted:
    if event == 'line':
      halted = False
    elif (event == 'exception') or (event == 'c_exception'):
      halted = True
    elif ((event == 'return') or (event == 'c_return')) and (len(callStack) == 1):  #If we are returning from the last frame in the callstack
      halted = True
    else: #Do not print a trace for events other than line, exceptions, and returning from the last frame in the callstack
      return traceCallback  

    #Print the stack trace and displayed value:
    sys.stdout = stdout_
    print json.dumps([callStack, halted, value])
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
  group = parser.add_mutually_exclusive_group(required = True)
  group.add_argument('-s', '--string', dest = 'code', help = 'String containing the code to be parsed')
  group.add_argument('-f', '--file', dest = 'file', type=argparse.FileType('r'), help='File containing the code to be parsed')
  args = parser.parse_args()

  #If the code was supplied as a file, then read the file
  if args.file != None:
    if os.fstat(args.file.fileno()).st_size <= 1048576:
      return args.file.read()
    else:
      return 'Error: File too large'
  else:
    return args.code.replace("\\n", "\n")

#********************
# main
#********************
if __name__ == '__main__':
  code = parseArguments()
  setupTrace()
  exec(code)
