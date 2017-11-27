import random
print "Enter parent 1 gene:"
x=raw_input().strip()
print "Enter parent 2 gene:"
y=raw_input().strip()
p=random.randint(0,8)
print "Single point :",p
print "Crossover : ",x[:p]+y[p:]
