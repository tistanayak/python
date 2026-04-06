import copy

class Mat:
    def __init__(self, A):
        self.nr = len(A)   
        self.nc = len(A[0]) 
        self.data = copy.deepcopy(A)

    def mul(self, b):
        if self.nc == b.nr:
            A = []
            for i in range(self.nr):
                Ci = []
                for j in range(b.nc):
                    s = 0
                    for k in range(self.nc):
                        s += self.data[i][k] * b.data[k][j]
                    Ci.append(s)
                A.append(Ci)
            return Mat(A)
        else:
            print("Multiplication not possible")

    def display(self):
        for row in self.data:
            print(row)


A = [[4,5,6],[2,5,4]]

B = [[1,8,5,2],[-1, 5,6,2],[8,-2,3,7]]

a = Mat(A)
b = Mat(B)

c = a.mul(b)

print("Result of Multiplication:")
c.display()
