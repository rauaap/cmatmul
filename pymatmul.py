import ctypes

libmatmul = ctypes.CDLL('./libmatmul.o')

class Matrix(ctypes.Structure):
    _fields_ = [
        ('rows', ctypes.c_size_t),
        ('cols', ctypes.c_size_t),
        ('arr', ctypes.POINTER(
            ctypes.POINTER(ctypes.c_int)
        ))
    ]

    def __new__(cls, arr):
        return libmatmul.make_matrix(len(arr), len(arr[0]))

    def __init__(self, arr):
        for i, row in enumerate(arr):
            self[i] = row

    def __repr__(self):
        joined_rows = ',\n\t'.join(str(self[i]) for i in range(self.rows))
        return '[\n\t' f'{joined_rows}' '\n]'

    def __getitem__(self, idx):
        match idx:
            case tuple():
                y, x = idx
                return self.arr[y][x]
            case int():
                row = self.arr[idx]
                return [row[i] for i in range(self.cols)]
            case _:
                raise TypeError

    def __setitem__(self, idx, val):
        match idx:
            case tuple():
                y, x = idx
                self.arr[y][x] = val
            case int():
                for i, v in enumerate(val):
                    self.arr[idx][i] = v
            case _:
                raise TypeError

    def __mul__(self, other):
        return libmatmul.matmul(self, other)

    def __del__(self):
        libmatmul.destroy_matrix(ctypes.byref(self))

libmatmul.make_matrix.restype = Matrix
libmatmul.make_matrix.argtypes = [ctypes.c_size_t, ctypes.c_size_t]

libmatmul.destroy_matrix.restype = None
libmatmul.destroy_matrix.argtypes = [ctypes.POINTER(Matrix)]

libmatmul.matmul.restype = Matrix
libmatmul.matmul.argtypes = [ctypes.POINTER(Matrix), ctypes.POINTER(Matrix)]

