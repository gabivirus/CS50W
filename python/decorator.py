def  announce(ad):
    def wrapper():
        print('About to run the function')
        ad()
        print('Done with the function')
    return wrapper

@announce
def hello():
    print('Hello')
    #return print('Hello')

print("cade")