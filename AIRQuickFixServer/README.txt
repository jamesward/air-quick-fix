This project is a simple example using PyAMF and Google App Engine
with an Adobe AIR application that lets you load an image, push it to
Google App Engine, run the I'm feeling lucky image enhancement on it,
and then the image is passed back to the AIR application where it can
be saved. PyAMF is included in the source tree as a convenience to
easily downloading and using the example. PyAMF is covered by the MIT
open source license - more details can be found in the pyamf/license.txt
file and we would like to say thanks to the PyAMF team for making this
so drop dead easy.

To see the application demo, just point your browser at:

http://airquickfix.appspot.com

and follow the instructions there. To use the code yourself you will need to
make a couple of changes to the source:

First, in the AIRQuickFixServer/app.yaml file, change the name of the 
application to an appspot name that you own, otherwise you won't be able
to deploy the application.

Secondly, in the AIRQuickFixClient/src/QuickFix.mxml file, find the
mx:RemoteObject tag and update the endpoint to point to one of either:

"<yourappname>.appspot.com/image" (if you have deployed it to an appspot 
name that you own) or

"localhost:8080/image" if you are debugging with the server running on
your local machine (from the SDK). You will then need to rebuild the
QuickFix.air application (in flexbuilder), and copy the resulting
QuickFix.air file into AIRQuickFixServer/static to be able to enjoy the
whole user experience (including the single click install of the AIR
application).
