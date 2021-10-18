
class Controller:
    def __init__(self):
        pass

    def value_x(self, x_error, old_max, old_min):
        old_range = (old_max - old_min)
        new_range = (1000 - -1000)
        new_value = (((x_error - old_min) * new_range) / old_range) + -1000
        return new_value

    def value_y(self, y_error, old_max, old_min):
        old_range = (old_max - old_min)
        new_range = (1000 - -1000)
        new_value = (((y_error - old_min) * new_range) / old_range) + -1000
        return new_value


a = Controller()
print(a.value_y(25, 100, 0))
