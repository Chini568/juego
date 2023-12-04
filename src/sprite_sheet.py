import pygame

class Sprites:
    def __init__(self, sheet:pygame.Surface, w_player, h_player, rows, cols, keys = None) -> None:
        self.sheet = sheet
        self.height = self.sheet.get_height()
        self.rows = rows 
        self.col = cols
        self.w_player = w_player
        self.h_player = h_player
        self.keys = keys
        
    def get_animation(self, scale = 1):
        self.width = scale * self.sheet.get_width()
        self.height = scale * self.sheet.get_height()
        self.w_player = scale * self.w_player
        self.h_player = scale * self.h_player

        self.sheet = pygame.transform.scale(self.sheet, (self.width,  self.height))
        contador_cols = 0

    
        animation_list = []

        for row in range(self.rows):
            for _ in range(self.col):
                animation_list.append(self.sheet.subsurface((contador_cols * self.w_player, row * self.h_player , self.w_player, self.h_player  )))
                # animation_row.append((contador_cols * WIDTH_PLAYER, row * HEIGHT_PLAYER, WIDTH_PLAYER, HEIGHT_PLAYER ))
                contador_cols += 1
            contador_cols = 0
        return animation_list
    
    def get_animation_dict(self, scale = 1):
        self.width = scale * self.sheet.get_width()
        self.height = scale * self.sheet.get_height()
        self.w_player = scale * self.w_player
        self.h_player = scale * self.h_player

        self.sheet = pygame.transform.scale(self.sheet, (self.width,  self.height))
        contador_cols = 0

        animation_dict = {}

        for row in range(self.rows):
            animation_row = []
            for _ in range(self.col):
                animation_row.append(self.sheet.subsurface((contador_cols * self.w_player, row * self.h_player , self.w_player, self.h_player  )))
                # animation_row.append((contador_cols * WIDTH_PLAYER, row * HEIGHT_PLAYER, WIDTH_PLAYER, HEIGHT_PLAYER ))
                contador_cols += 1
            animation_dict[self.keys[row]] = animation_row
            contador_cols = 0
        return animation_dict
