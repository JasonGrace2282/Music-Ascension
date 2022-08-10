import pygame, sys
from tiles import Tile
from setup import tilesize, width, height
from player import TeleportPlayer, NotePlayer

class TeleportLevel():
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.h_shift = 0
        self.v_shift = 0
        self.current_x = 0
        self.player_on_ground = False
        self.note_text = None
        self.gameover = pygame.image.load("../resources/gameover.png")
        self.restart = pygame.image.load("../resources/next.png")
        self.mainmenu = pygame.image.load("../resources/next.png")
        self.reset = False
        self.back = False
        self.complete = False
    
    def on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False
    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        pos = (0, 640) 

        for info in layout:
            if info[0] == 0.5:
                offset = 192
                pos = (offset+pos[0], pos[1]-32)
                tile = Tile(pos, (tilesize, tilesize), info[1])
                self.tiles.add(tile)

            if info[0] == 1:
                offset = 192
                pos = (offset+pos[0], pos[1]-64)
                tile = Tile(pos, (tilesize, tilesize), info[1])
                self.tiles.add(tile)
            
            if info[0] == 1.5:
                offset = 256
                pos = (offset+pos[0], pos[1]-64)
                tile = Tile(pos, (tilesize, tilesize), info[1])
                self.tiles.add(tile)
                
            if info[0] == 2:
                offset = 192
                pos = (offset+pos[0], pos[1]-128)
                tile = Tile(pos, (tilesize, tilesize), info[1])
                self.tiles.add(tile)
            
            if info[0] == 3:
                offset = 256
                pos = (offset+pos[0], pos[1]-128)
                tile = Tile(pos, (tilesize, tilesize), info[1])
                self.tiles.add(tile)
            
            if info[0] == 4:
                offset = 256
                pos = (offset+pos[0], pos[1]-256)
                tile = Tile(pos, (tilesize, tilesize), info[1])
                self.tiles.add(tile)
        
        player_sprite = TeleportPlayer((192, 512), self.display_surface)
        self.player.add(player_sprite)
    
    def scroll(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x

        if player_x < width/4 and direction_x < 0:
            self.h_shift = 8
            player.speed = 0
        elif player_x > width - width/4:
            self.h_shift = -8
            player.speed = 0
        elif player_y < height/4:
            self.v_shift = 4
        else:
            self.h_shift = 0
            self.v_shift = 0
            player.speed = 8
    
    def detect_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
            
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right < self.current_x or player.direction.x <= 0):
            player.on_right = False
        
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                note = pygame.font.SysFont(None, 30)
                self.note_text = note.render(sprite.note, True, (255, 255, 255))
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
            
            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling
        
    def run(self, delta):

        # level tiles
        self.tiles.update(self.h_shift, "x")
        self.tiles.update(self.v_shift, "y")
        self.tiles.draw(self.display_surface)
        self.scroll()
        if self.note_text != None:
            self.display_surface.blit(self.note_text, (0, 0))

        # player
        self.player.update(delta, self.h_shift)
        self.detect_collisions()
        self.on_ground()
        self.player.draw(self.display_surface)

        if self.player.sprite.rect.topleft[1] > height:
            self.display_surface.blit(self.gameover, (0, 0))
            self.display_surface.blit(self.restart, (0, 0))
            self.display_surface.blit(self.mainmenu, (0, 122))
            # self.mainmenu.get_rect().topleft = (0, 122)
            # print(self.mainmenu.get_rect().topleft)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    print(mouse)
                    """if self.restart.get_rect().collidepoint(event.pos):
                        print("why")
                        self.reset = True
                    elif self.mainmenu.get_rect().collidepoint(event.pos):
                        print("no u")
                        self.back = True"""
                    
class NoteLevel(TeleportLevel):
    def __init__(self, level_data, surface):
        super().__init__(level_data, surface)
    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        pos = (0, 100)
        for i in range(1, 6):
            tile = Tile(pos, (2000, 20))
            self.tiles.add(tile)
            pos = (pos[0], pos[1]+100)

        player_sprite = NotePlayer((192, 377.7777777), self.display_surface)
        self.player.add(player_sprite)
    
    def detect_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
    
    def scroll(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x

        if player_x < width/4 and direction_x < 0:
            self.h_shift = 8
            player.speed = 0
        elif player_x > width - width/4 and direction_x > 0:
            self.h_shift = -8
            player.speed = 0
        elif player_y < height/4:
            self.v_shift = 4
        else:
            self.h_shift = 0
            self.v_shift = 0
            player.speed = 8
    
    def run(self, delta):

        # level tiles
        self.tiles.update(self.h_shift, "x")
        self.tiles.update(self.v_shift, "y")
        self.tiles.draw(self.display_surface)
        self.scroll()

        # player
        self.player.update()
        self.detect_collisions()
        self.on_ground()
        self.player.draw(self.display_surface)