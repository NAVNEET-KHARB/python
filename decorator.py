def greet(fx):
    def mfx():
        print("Hi, Good Morning.")
        fx()
        print("Thank you for using this function.")
    return mfx


@greet
def hello():
    print("Hello World.")


# my_func = greet(hello)
# my_func()
# hello()
hello()
# import logging


# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(
#             f"Calling{func.__name__} with args = {args} and kwargs = {kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated


# @log_function_call
# def my_func(a, b):
#     return a+b


# _a = my_func(9, 2)
# print(_a)
