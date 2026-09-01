class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        tr_count = tl_count = br_count = bl_count = 0
        for ex_point in self.points.keys():
            if ex_point[0] == point[0] and ex_point[1] != point[1]:
                l = abs(ex_point[1] - point[1])
                if ex_point[1] > point[1]:
                    ## T.R
                    tr_count += self.points.get((point[0], point[1] + l), 0) * self.points.get((point[0] + l, point[1]), 0) * self.points.get((point[0] + l, point[1] + l), 0)
                    ## T.L
                    tl_count += self.points.get((point[0], point[1] + l), 0) * self.points.get((point[0] - l, point[1]), 0) * self.points.get((point[0] - l, point[1] + l), 0)
                else:
                    ## B.R
                    br_count += self.points.get((point[0], point[1] - l), 0) * self.points.get((point[0] + l, point[1]), 0) * self.points.get((point[0] + l, point[1] - l), 0)
                    ## B.L
                    bl_count += self.points.get((point[0], point[1] - l), 0) * self.points.get((point[0] - l, point[1]), 0) * self.points.get((point[0] - l, point[1] - l), 0)
        
        return tr_count + tl_count + br_count + bl_count
