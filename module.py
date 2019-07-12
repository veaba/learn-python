"""
@desc python module

"""

import sys


print(sys.argv)
for item in sys.argv:
    print("item:", item)
print("Python path：", sys.path)

print(sys)


print(__name__)  # __main__

