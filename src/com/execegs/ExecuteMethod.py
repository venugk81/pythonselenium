def click(obj, data):
    print("Obj: ", obj)
    print("data", data)


def execute_method(obj, action, data):
    if action == "click":
        exec('click(obj, action)')


execute_method("ele_object abc", "click", "abc daa")
