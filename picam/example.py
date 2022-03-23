# -*- coding:utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s : %(message)s")

import os
import time
import argparse
from picamera import PiCamera

# In[]

def take_capture(path):
  try:
    camera = PiCamera()
    camera.framerate = 30
    camera.start_preview()
    time.sleep(3)
    camera.capture(path)
    camera.stop_preview()

    logging.info("An image was generated at {}.".format(path))
  except Exception as err:
    logging.error(error)

def record_video(path, secs):
  try:
    camera = PiCamera()
    camera.framerate = 30
    camera.start_preview()
    camera.start_recording(path)
    time.sleep(secs)
    camera.stop_recording()
    camera.stop_preview()

    logging.info("An image was generated at {}.".format(path))
  except Exception as err:
    logging.error(err)  


# In[]

if __name__ == "__main__":
  
  parser = argparse.ArgumentParser()
  parser.add_argument("--type", required=True, type=str)
  parser.add_argument("--path", required=True, type=str)
  parser.add_argument("--second", type=int)
  args = parser.parse_args()

  if args.type == "image":
    take_capture(args.path)
  elif args.type == "video":
    try:
      secs = int(args.second)
    except Exception as err:
      logging.error("You should assign the second by using --second. Using the default 5 secs.")
    record_video(args.path, 5)
  else:
    logging.error("Type {} was not supported.".format(args.type))

