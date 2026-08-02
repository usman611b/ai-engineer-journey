class Matrix:
    def __init__(self , data):
        self.data = [list(row) for row in data]
        self.rows = len(self.data)
        self.cols = len(self.data[0]) if self.data else 0
        self.shape = (self.rows , self.cols)

    def __repr__(self):
        rows_str = "\n  ".join(str(row) for row in self.data)
        return f"Matrix({self.shape}):\n  {rows_str}"

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape.")
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])
    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape.")
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])
    def scalar_multiply(self, scalar):
        return Matrix([
            [self.data[i][j] * scalar for j in range(self.cols)]
            for i in range(self.rows)
        ])
    def elementwise_multiply(self, other):
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape.")
        return Matrix([
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ])
    def matmul(self , other):
        if self.cols != other.rows:
            raise ValueError("Incompatible matrix dimensions")
        return Matrix([
            
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            
            for i in range(self.rows)
        ])
    def transpose(self):
        return Matrix([
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ])

A = Matrix([[1, 2, 3], [4, 5, 6]])
B = Matrix([[7, 8, 9], [10, 11, 12]])
C = Matrix([[1, 2],[3, 4],[5 , 6]])
added_matrix = A + B
print(added_matrix)  # Output: Matrix((2, 3)):  
print(A)
print(B)
print(C)
matrix_mul = A.matmul(C)
print(matrix_mul)
print(A.transpose())