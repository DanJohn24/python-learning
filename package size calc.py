weight_error = True
single_dim_error = True
dim_error = True

verdict = True

weight = int(input("please enter weight: "))
width = int(input("please enter height: "))
length = int(input("please enter length: "))
depth = int(input("please enter depth: "))

dim_sum = width + length + depth
if weight > 2000:
    weight_error = False
if width > 60 or length > 60 or depth > 60:
    single_dim_error = False
if dim_sum > 90:
    dim_error = False

if weight_error == False or single_dim_error == False or dim_error == False:
    verdict = False
else:
    verdict = True

print ("\n")
print("The sum of the dimensions of your package (",dim_sum,"cm) are under ,or equal to, 90cm - ", dim_error)
print ("At",weight,"g your package is under ,or equal to, the 2,000G max for small package - ",weight_error)
print ("No package dimension is over ,or equal to, 60cm - ",single_dim_error)
print ("\n")

if verdict == False:
    print ("Your package is big")
else:
    print ("Your package is small")
