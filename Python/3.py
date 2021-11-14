print("Name : Riya Kumari")
print("Scholar No : 201112001", end="\n\n")

d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
hello = d['k1'][3]['tricky'][3]['target'][3]
print(hello)