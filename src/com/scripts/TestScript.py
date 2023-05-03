import os.path
import sys
from selenium.webdriver.common.by import By

from src.com.scripts.BaseClass import BaseClass


# bc = BaseClass()
#
# x = bc.get_element("name", "q")
# if x != None:
#     x.send_keys("testing")
#     x.submit()
# bc.quit()


def time_entry():
    bc = BaseClass()
    try:
        ele = bc.get_element("name", "q")
        if ele != None:
            ele.send_keys("testing")
            ele.submit()
    except:
        print("Error occurred")
    finally:
        bc.quit()
        print("driver is closed.")


time_entry()

abs_path = os.path.dirname(__file__)
print("Print abs path: ", abs_path)
rel_path = "data\\notes.txt"
str_full = full_path = os.path.join(abs_path, rel_path)
file_exists = os.path.exists(str_full)
print("File Exists: ", file_exists)
print("File path: ", str_full)

ROOT_DIR = os.path.abspath(os.curdir)
print("root: ", ROOT_DIR)
sys_path = sys.path[1]
file_exists = os.path.exists(os.path.join(sys_path, rel_path))
print("check file path again: ", file_exists)
print("sys.path[1]: ", sys.path[1])

print("----------------print file content---------------")
file_full_path = os.path.join(sys_path, rel_path)
print(file_full_path)
f = open(file_full_path, "r")
print(f.read())


