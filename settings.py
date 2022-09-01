class Settings:
    TURTLE_SIZE = 20
    r = 40

    def __init__(self, windows_x, window_y):
        self.x = windows_x
        self.y = window_y
        self.start_x = - self.x / 2 + self.r + 10
        self.start_y = - self.y / 2 + self.r + 10
        self.x_end = self.x / 2 - self.r
        self.y_end = self.y / 2