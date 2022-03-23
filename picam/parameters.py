# -*- coding:utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s : %(message)s")

import os
import time
import argparse
from picamera import PiCamera

# In[]

def take_capture(exposure, awb, path):
  try:
    camera = PiCamera()
    camera.framerate = 30
    camera.start_preview()
    camera.exposure_mode = exposure
    camera.awb_mode = awb
    time.sleep(3)
    camera.capture(path)
    camera.stop_preview()

    logging.info("An image was generated at {}.".format(path))
  except Exception as err:
    logging.error(error)


# In[]

if __name__ == "__main__":
  
  parser = argparse.ArgumentParser()
  parser.add_argument("--exposure", required=True, type=str)
  parser.add_argument("--awb", required=True, type=str)
  parser.add_argument("--path", required=True, type=str)
  args = parser.parse_args()

  take_capture(args.exposure, args.awb, args.path)