#---Number Systems---
#--Built-in Functions

num=10

binary_Result=bin(num)
Octal_Result=oct(num)
Hexa_Result=hex(num)

print("Integer value", num)
print("Binary value", bin(num))
print("Octal value", oct(num))
print("Hexa value", hex(num))

print("------------------------")

print("Binary back to integer", int(binary_Result,2)) #--base of 2

print("------------------------")

print("Octal back to integer", int(Octal_Result,8)) #--base of 8

print("------------------------")

print("HexaDecimal back to integer", int(Hexa_Result,16)) #--base of 16
