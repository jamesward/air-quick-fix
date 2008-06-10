import logging
import wsgiref.handlers

from pyamf.remoting.gateway.wsgi import WSGIGateway
from pyamf.amf3 import ByteArray

from google.appengine.api.images import Image
    
def fiximage(data):
  """Take an uploaded image, call I'm feeling lucky
  and put it back out to the user.
  """
  logging.info("Transforming image...")
  logging.info("In data size: %d" % (len(data),))
  
  image_in = Image(str(data))
  image_in.im_feeling_lucky()
  
  image_out = ByteArray()
  image_out.write(image_in.execute_transforms())
  
  logging.info("Out data size: %d" % (len(image_out),))
  return image_out
    
services = {
    'image.fiximage': fiximage
}

def main():
  logging.info("Starting app")
  application = WSGIGateway(services)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
