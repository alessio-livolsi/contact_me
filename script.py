import os
import sys
import numpy
import string

if sys.version > '3':
    strl = str
else:
    strl = string


EMAIL = """
\u0061\u006C\u0065\u0073\u0073\u0069\u006F.\u006C\u0069\u0076\u006F\u006C\u0073\u0069@\u0070\u0072\u006F\u0074\u006F\u006E\u006D\u0061\u0069\u006C.\u0063\u006F\u006D
"""


y = string.ascii_letters
n = len(y)
M = numpy.identity(n, dtype=numpy.int32)
M[:n, n-1] = 1

a = numpy.array(list(map(ord, y)), dtype=numpy.int32)
x = ''.join(map(chr, numpy.dot(M, a)))
uncipher = strl.maketrans(x,y)

print( strl.translate(EMAIL, uncipher) )