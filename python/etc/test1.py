mygraph = {'A': ['B', 'C', 'D'],
           'B':[],
           'C': ['B', 'D'],
           'D': ['E', 'F'],
           'E': ['F'],
           'F': ['A']}

print(type(mygraph['B']))
print(len(mygraph['B']))
