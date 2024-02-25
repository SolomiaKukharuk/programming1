class Vector:
    def __init__(self, *args):
        self.coords = args

    def dim(self) -> float:
        return len(self.coords)

    def norm(self) -> float:
        m = 0
        for i in self.coords:
            m += i * i
        return m ** 0.5

    def max_(self):
        return max(self.coords)

    def min_(self):
        return min(self.coords)

    def middle_arithmetic(self):
        return sum(self.coords) / self.dim()

    def __str__(self):
        return f"{self.coords}"

    def __repr__(self):
        return f"Vector{self.coords}"


with open('input01.txt', 'r') as f1, open('input02.txt', 'r') as f2, open('input03.txt', 'r') as f3, open('input04.txt',
                                                                                                          'r') as f4:
    lines = f1.readlines()
    lines2 = f2.readlines()
    lines3 = f3.readlines()
    lines4 = f4.readlines()
    lines.extend(lines2)
    lines.extend(lines3)
    lines.extend(lines4)
    max_norm = 0
    max_component = float('-inf')
    min_component = float('inf')
    _min_component = float('inf')
    _max_component = float('-inf')
    max_dim = 0
    lst_ma = []
    max_norm_vectors = []
    min_dim_vector = None
    min_dim = float('inf')
    min_norm = float('inf')
    max_component_vectors = []
    min_component_vectors = []
    max_largest_component_vector = None
    min_smallest_component_vector = None
    for line in lines:
        data = line.split()
        coordinates = [float(x) for x in data]
        args = coordinates
        vec = Vector(*args)
        if vec.dim() >= max_dim:
            max_dim_vectors = []
            max_dim = vec.dim()
            max_dim_vectors.append(vec)

        for vec in max_dim_vectors:
            if vec.norm() < min_norm:
                min_norm = vec.norm()
                min_norm_vector = vec
    if len(max_dim_vectors) == 1:
        print('Розмірність цього вектора найбільша:', max_dim_vectors[0])
    else:
        print('Розмірність цього вектора найбільша:', min_norm_vector)

        if vec.norm() > max_norm:
            max_norm_vectors.append(vec)
            max_norm = vec.norm()
        elif vec.norm() == max_norm:
            max_norm_vectors.append(vec)

        for vec in max_norm_vectors:
            if vec.dim() < min_dim:
                min_dim = vec.dim()
                min_dim_vector = vec
    if len(max_norm_vectors) == 1:
        print('Довжина цього вектора найбільша:', max_norm_vectors[0])
    else:
        print('Довжина цього вектора найбільша:', min_dim_vector)
        lst_ma.append(vec.middle_arithmetic())
        malst = (sum(lst_ma) / len(lst_ma))
        print('Середнє арифметичне списку:', malst)
        counter = 0
        if vec.middle_arithmetic() > malst:
            counter += 1
        print('Кількість векторів в яких середнє арифметичне більше за середнє арифметичне списку', counter)

        if vec.max_() > max_component:
            max_component_vectors.append(vec)
            max_component = vec.max_()
        elif vec.max_() == max_component:
            max_component_vectors.append(vec)
            for vec in max_component_vectors:
                if vec.min_() < _min_component:
                    max_largest_component_vector = vec

    if len(max_component_vectors) == 1:
        print('Вектор з максимальною найбільшою компонентою:', max_component_vectors[0])
    else:
        print('Вектор з максимальною найбільшою компонентою:', max_largest_component_vector)

        if vec.min_() > min_component:
            min_component_vectors.append(vec)
            min_component = vec.min_()
        elif vec.min_() == min_component:
            min_component_vectors.append(vec)
            for vec in min_component_vectors:
                if vec.max_() > _max_component:
                    min_smallest_component_vector = vec

    if len(min_component_vectors) == 1:
        print('Вектор з мінімальною найменшою компонентою:', min_component_vectors)
    else:
        print('Вектор з мінімальною найменшою компонентою:', min_smallest_component_vector)
