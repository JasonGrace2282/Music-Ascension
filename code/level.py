import pygame
from tiles import Tile
from setup import tilesize, width, height
from player import Player


class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.h_shift = 0
        self.v_shift = 0
        self.current_x = 0

        # dust
        self.player_on_ground = False

    def on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        pos = (0, 640)

        for num in layout:
            if num == 0.5:
                offset = 192
                pos = (offset + pos[0], pos[1] - 32)
                tile = Tile(pos, tilesize)
                self.tiles.add(tile)

            if num == 1:
                offset = 192
                pos = (offset + pos[0], pos[1] - 64)
                tile = Tile(pos, tilesize)
                self.tiles.add(tile)

            if num == 1.5:
                offset = 256
                pos = (offset + pos[0], pos[1] - 64)
                tile = Tile(pos, tilesize)
                self.tiles.add(tile)

            if num == 2:
                offset = 192
                pos = (offset + pos[0], pos[1] - 128)
                tile = Tile(pos, tilesize)
                self.tiles.add(tile)

            if num == 3:
                offset = 256
                pos = (offset + pos[0], pos[1] - 128)
                tile = Tile(pos, tilesize)
                self.tiles.add(tile)

            if num == 4:
                offset = 256
                pos = (offset + pos[0], pos[1] - 256)
                tile = Tile(pos, tilesize)
                self.tiles.add(tile)

        player_sprite = Player((192, 512), self.display_surface)
        self.player.add(player_sprite)

    def scroll(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x

        if player_x < width / 4 and direction_x < 0:
            self.h_shift = 8
            player.speed = 0
        elif player_x > width - width / 4:
            self.h_shift = -8
            player.speed = 0
        elif player_y < height / 4:
            self.v_shift = 1
        else:
            self.h_shift = 0
            self.v_shift = 0
            player.speed = 8

    def detect_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
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

        # player
        self.player.update(delta, self.h_shift)
        self.detect_collisions()
        self.on_ground()
        self.player.draw(self.display_surface)
