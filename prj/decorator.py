#coding=utf-8
import datetime

def cost_time(func):
    def deco(*args, **kwargs):
        start = datetime.datetime.now()
        f = func(*args, **kwargs)
        end = datetime.datetime.now()
        time = end - start
        print(time)
        return f
    return deco