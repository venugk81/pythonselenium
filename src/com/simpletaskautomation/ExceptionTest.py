def exp_test():
    a = 10
    b = 20
    try:
        try:
            if a > 5:
                raise Exception("Sorry, no numbers below zero")
        except Exception as err1:
            print("error 1")
            raise
        finally:
            print(" im in finally 1")

    except Exception as err2:
        print(" error 2")
    finally:
        print("finally oouter 2")


exp_test()

x = -1

try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as exp:
    print("exp:", exp)
finally:
    print("im printing from finally")
print("testing")
