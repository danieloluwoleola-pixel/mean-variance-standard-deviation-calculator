# main2.py
from mean_var_std import calculate

# Test with the example
result = calculate([0,1,2,3,4,5,6,7,8])
for key, value in result.items():
    print(f"{key}: {value}")