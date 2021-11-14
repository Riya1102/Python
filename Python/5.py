print("Name : Riya Kumari")
print("Scholar No : 201112001", end="\n\n")

def Dog(s):
    return 'dog' in s.lower().split()

s=input("Enter string: ")
print("Presence of dog in string: ",Dog(s))