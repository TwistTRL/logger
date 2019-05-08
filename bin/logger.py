#!/usr/bin/env python
"""logger.py

Usage:
  logger.py [--local|--utc] --format=<fnformat> --output=<outputDir>

Options:
  --utc      Use UTC date time for log file name (recommended)
  --local    Use local date time for log file name
  --format=<fnformat>     date time format for filename, e.g. "%Y-%m-%d"
  --output=<outputDir>    output directory
"""

from docopt import docopt
import os
from datetime import datetime

class Logger:
  fext = ".log"
  modes = set(["utc","local"])
  
  def __init__(self,mode,fnformat,outputDir):
    self.mode = mode
    assert(self.mode in Logger.modes)
    self.fnformat = fnformat
    self.fh = None
    self.fname = None
    
  def log(self,content):
    fh = self.getFileHandle()
    print(content,file = fh)
      
  def getFileHandle(self):
    curFName = None
    if self.mode=="utc":
      curFName = datetime.utcnow().strftime(self.fnformat)+self.fext
    elif self.mode=="local":
      curFName = datetime.now().strftime(self.fnformat)+self.fext
    else:
      raise TypeError()
    
    if curFName != self.fname:
      self.close()
      self.fname = curFName
      self.fh = open(os.path.join(outputDir,self.fname),'a')
    return self.fh
  
  def close(self):
    if self.fh:
      self.fh.close()
  
  def __del__(self):
    print("cleaning up")
    self.close()

if __name__ == "__main__":
  options = docopt(__doc__)
  fnformat = options["--format"]
  outputDir = options["--output"]
  mode = None
  if options["--local"]:
    mode = "local"
  if options["--utc"]:
    mode = "utc"
  
  logger = Logger(mode,fnformat,outputDir)
  print(mode,fnformat,outputDir)
  
  while True:
    content = input()
    logger.log(content)
