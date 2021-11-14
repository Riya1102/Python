print("Name : Riya Kumari")
print("Scholar No : 201112001", end="\n\n")

def domain_finder(s):
    ans = ""
    a = len(s)
    for i in range(a):
        if(s[i]=="@"):
            ans = ans + s[i+1:]
            return ans

s = "riyak@domain.com"
print(domain_finder(s))