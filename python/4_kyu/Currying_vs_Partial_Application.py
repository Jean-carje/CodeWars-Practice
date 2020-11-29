# Kata link:
# https://www.codewars.com/kata/53cf7e37e9876c35a60002c9/

# -------------------------------------
# Solution:

from inspect import signature


is_set = False
params = 0

def curry_partial(func, *partial_args):
    global is_set, params
    
    if not is_set:
        is_set = True
        try: 
            params = len(signature(func).parameters)
        except: 
            return func
        
    try:
        is_set = False
        return func(*partial_args[:params])
    
    except:
        is_set = True
    
        def wrapper(*extra_args):     
            args = (partial_args + extra_args)
            try:
                is_set = False
                return func(*args[:params])
            except:
                is_set = True
                return curry_partial(func, *args)
    
    return wrapper
