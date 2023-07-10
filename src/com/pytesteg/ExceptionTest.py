from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

#good
# https://hackmd.io/@jenc/SJYmGcKsK

def ex():

    mytuple = (("apple", "banana"), ("a", "b"))
    for xtup in mytuple:
        for x in xtup:
            try:

                if x == "a":
                    raise Exception("Error occurred: ", x)
                print(x)
            except Exception as err:
                print("in exception block", err)
            finally:
                print("in the finally block")



ex()
