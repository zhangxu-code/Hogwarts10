
def before(func):
    def new_now():
        print("setup")
        func()

    return new_now

@before
def now():
    print("2019")

def test_demo():
    now()