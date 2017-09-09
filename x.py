node=0
def fun():
 global node
 node=1
del fun
fun()
print(node)
