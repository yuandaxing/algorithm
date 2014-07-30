def logger(func_to_log) :
    def wrapped(*args, **kwargs) :
        print 'arguments were, %s, %s' %(args, kwargs)
        func_to_log(*args, **kwargs)
    return wrapped

#logger
def my_func(x, y) :
    return x * y

print my_func(10, 15)
