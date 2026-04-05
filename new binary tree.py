class node:
    def __init__(self,val):
        self.__data=val
        self.__left=None
        self.__right=None
    def compare(self,val):
        if self.__data>val:
            self.__left=insert(self.__left,val)
        else:
            self.__right=insert(self.__right,val)
def insert(root,val):
    if root is None:
        root=node(val)
    else:
        root.compare(val)
    return root
root=None
a=[3,8,1,4,2,12,6,7]
for el in a:
    root=insert(root,el)

print(root)