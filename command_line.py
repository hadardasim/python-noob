import sys
import getopt
import cv2
import numpy

# example for using open-cv + command line arguments
# cacluate the difference between two images.
# if output file is specified save the result to file, else display the result

def main(argv):
   input1 = ''
   input2 = ''
   outputfile = ''
   gain = 1.0
   try:
      opts, args = getopt.getopt(argv, "hf:s:g:o:", ["first=", "second=", "gain=", "out="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-f", "--first"):
         input1 = arg
      elif opt in ("-s", "--second"):
         input2 = arg
      elif opt in ("-o", "--out"):
         outputfile = arg
      elif opt in ("-g", "--gain"):
         gain = float(arg)

   img1 = cv2.imread(input1, cv2.IMREAD_GRAYSCALE)
   img2 = cv2.imread(input2, cv2.IMREAD_GRAYSCALE)
   gray1 = numpy.float32(img1) * 1.0/255.0
   gray2 = numpy.float32(img2) * 1.0/255.0
   im3 = 0.5 + (gray1-gray2) * gain

   if len(outputfile) == 0:
      cv2.imshow('image', im3)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
   else:
      cv2.imwrite(outputfile, im3*255.0)

if __name__ == "__main__":
   main(sys.argv[1:])