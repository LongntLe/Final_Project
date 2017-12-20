from segmenttree import SegmentTree

class screen:
    def __init__(self):
        self.l = 10
        self.x = 0
        self.y = 0

    def translate(self, v_x, v_y):
        return self.x + v_x, self.y + v_y # rectangle center translation

    def zoom(self, k):
        return self.l*k # homothety with ratio k

if __name__ == '__main__':
    segtree = SegmentTree(1, 8)
    data = [
        [1, 10],
        [3, 8],
        [2, 6],
        [4, 12],
        [8, 11]
    ]

    for segment in data:
        segtree.add(segment[0], segment[1], 1)
    
