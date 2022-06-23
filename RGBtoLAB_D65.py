import math

def rgb2lab ( inputColor ) :

   num = 0
   RGB = [0, 0, 0]
   
   #Normalization and Gamma companding
   
   for value in inputColor :
       value = float(value) / 255

       if value > 0.04045 :
           value = ( ( value + 0.055 ) / 1.055 ) ** 2.4
       else :
           value = value / 12.92

       RGB[num] = value * 100
       num = num + 1

   XYZ = [0, 0, 0,]
  
   #Mutiplying inverse matrix for XYZ coordinates
   
   X = RGB [0] * 0.4124 + RGB [1] * 0.3576 + RGB [2] * 0.1805
   Y = RGB [0] * 0.2126 + RGB [1] * 0.7152 + RGB [2] * 0.0722
   Z = RGB [0] * 0.0193 + RGB [1] * 0.1192 + RGB [2] * 0.9505
   XYZ[ 0 ] = round( X, 4 )
   XYZ[ 1 ] = round( Y, 4 )
   XYZ[ 2 ] = round( Z, 4 )

   XYZ[ 0 ] = float( XYZ[ 0 ] ) / 95.047         #D65 MODEL ref_X, ref_Y, ref_Z
   XYZ[ 1 ] = float( XYZ[ 1 ] ) / 100.0
   XYZ[ 2 ] = float( XYZ[ 2 ] ) / 108.883
   
   #Calculating f(x,y,z)
   num = 0
   for value in XYZ :

       if value > 0.008856 :
           value = math.pow(value,1.0/3)
       else :
           value = ( 7.787 * value ) + ( 16 / 116 ) # k/116 = 7.787 where k = 903.3

       XYZ[num] = value
       num = num + 1

   Lab = [0, 0, 0]

   #Calculating Lab from the above functions
   L = (116 * XYZ[ 1 ] ) - 16
   a = 500 * ( XYZ[ 0 ] - XYZ[ 1 ] )
   b = 200 * ( XYZ[ 1 ] - XYZ[ 2 ] )

   Lab [ 0 ] = round( L, 5 )
   Lab [ 1 ] = round( a, 5 )
   Lab [ 2 ] = round( b, 5 )

   return Lab

print(rgb2lab([100,100,100]))
