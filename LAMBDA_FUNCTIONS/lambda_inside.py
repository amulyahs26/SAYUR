def multiplier(factor):
    return lambda x:x*factor

double=multiplier(5)

print(double(2))