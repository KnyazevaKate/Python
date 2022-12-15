import math
 
def cos(num):
    return math.cos(math.radians(num))
 
def sin(num):
    return math.sin(math.radians(num))
 
def tg(num):
    return math.tan(math.radians(num))
 
def ctg(num):
    return 1 / math.tan(math.radians(num))
 
def ln(num):
    return math.log(math.radians(num))
 
 
exp = "((1 + 2^3) / 3) * 12 - 4 + sin(30) + cos(60) + tg(45) + ctg(30) - ln(4)"
 
exp = exp.replace("^", "**")
 
print(eval(exp))