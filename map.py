class Map:

    def __init__(self, x, y, image):
        self.image = image
        self.pos_x = x
        self.pos_y = y
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

    def update(self, get_screen):
        if self.image is not None:
            get_screen.blit(self.image, self.rect)
