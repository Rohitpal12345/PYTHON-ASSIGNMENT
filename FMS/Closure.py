#
def outer():
    def inner():
        print("i am inner")
        return inner
f=outer()
f()