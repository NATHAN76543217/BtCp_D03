import numpy as np


class NumPyCreator():
    """
        a Numpy Wrapper
    """
    def from_list(self, lst, dtype=int):
        return np.array(lst, dtype=dtype)

    def from_tuple(self, tpl, dtype=int):
        return np.array(tpl, dtype)

    def from_iterable(self, iter, dtype=int):
        return np.array(iter, dtype=dtype)

    def from_shape(self, shape, value=0, dtype=int):
        res = 1
        for val in shape:
            res *= val
        return np.array([value] * res, dtype=dtype).reshape(shape)

    def random(self, shape):
        return np.random.rand(*shape)

    def identity(self, n, dtype=float):
        return np.identity(n, dtype=dtype)


if __name__ == "__main__":
    npc = NumPyCreator()

    from_lst = npc.from_list([[1, 2, 3], [6, 3, 4]])
    print("from list =\n", from_lst)

    from_tpl = npc.from_tuple(("a", "b", "c"), dtype=str)
    print("\nfrom tuple =", from_tpl)

    from_iter = npc.from_iterable(range(5))
    print("\nfrom iterable =", from_iter)

    shape = (3, 5)
    print("\nshape =", shape)
    from_shape = npc.from_shape(shape, dtype=float)
    print("from_shape =\n", from_shape)
    from_random = npc.random(shape)
    print("\nfrom random=\n", from_random)
    from_identity = npc.identity(4)
    print("\nfrom identity =\n", from_identity)
