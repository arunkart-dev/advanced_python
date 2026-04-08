# #reference_count
# import sys
# a = [1,2,3,4]
# print(sys.getrefcount(a))

import gc
import sys

a = [1,2,3]
b = [4,5.6]
del a
gc.collect()
print(sys.getrefcount(b))
