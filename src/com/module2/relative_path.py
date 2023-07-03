import os
import sys
absolute_path = os.path.dirname(__file__)
relative_path = "src/lib"
# full_path = os.path.join(absolute_path, relative_path)
print(absolute_path)
# https://towardsthecloud.com/get-relative-path-python

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)

ROOT_DIR = os.path.abspath(os.curdir)
print(ROOT_DIR)
print(sys.path[1])
print(os.path.dirname(sys.modules['__main__'].__file__))