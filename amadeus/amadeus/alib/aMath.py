class Vec2:
    def __init__(self, x_value, y_value):
        self.x = x_value
        self.y = y_value

    def __repr__(self):
        return f'x: {str(self.x)}, y: {str(self.y)}'


class Vec3:
    def __init__(self, x_value, y_value, z_value):
        self.x = x_value
        self.y = y_value
        self.z = z_value

    def __repr__(self):
        print(f'x: {str(self.x)}, y: {str(self.y)}, z: {str(self.z)}')


class Vec4:
    def __init__(self, x_value, y_value, z_value, t_value):
        self.x = x_value
        self.y = y_value
        self.z = z_value
        self.t = t_value

    def __repr__(self):
        print(f'x: {str(self.x)}, y: {str(self.y)}, z: {str(self.z)}, t: {str(self.t)}')
