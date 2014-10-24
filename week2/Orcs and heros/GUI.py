import pygame
import sys
from pygame.locals import *
from HeroClass import Hero
from OrcClass import Orc
from Fight import Fight
from Weapon import Weapon


class Player:
    def __init__(self, name, entity):
        self.name = name
        self.entity = entity
        self.position = None
        self.image = self.set_image()

    def set_image(self):
        if isinstance(self.entity, Hero):
            image = pygame.image.load('hero.jpg')
            return pygame.transform.scale(image, (50, 50))
        elif isinstance(self.entity, Orc):
            image = pygame.image.load('orc.jpg')
            return pygame.transform.scale(image, (50, 50))

    def set_position(self, position):
        self.position = position

    def move(self, direction):
        if direction == 'up':
            self.position[1] -= 10
        elif direction == 'down':
            self.position[1] += 10
        elif direction == 'left':
            self.position[0] -= 10
        elif direction == 'right':
            self.position[0] += 10


def colide(place1, place2):
    top_col = place1[0] <= place2[0] + 50
    bot_col = place1[0] + 50 >= place2[0]
    right_col = place1[1] + 50 >= place2[1]
    left_col = place1[1] <= place2[1] + 50
    if top_col and left_col and right_col and bot_col:
        return True


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('Orcs and Heros')
        self.player_1 = None
        self.player_2 = None

    def set_player(self, name, entity):
        if self.player_1:
            same_classes = isinstance(self.player_1.entity, type(entity))
            same_names = self.player_1.name == name
            if same_classes or same_names:
                return False

            self.player_2 = Player(name, entity)
            return True

        self.player_1 = Player(name, entity)
        return True

    def set_player_position(self, player, position):
        player.set_position(position)

    def draw_players(self):
        self.screen.blit(self.player_1.image, self.player_1.position)
        self.screen.blit(self.player_2.image, self.player_2.position)

    def get_player_input(self):
        pass

    def move_players(self, key):
            if key == K_RIGHT:
                self.player_1.move('right')
            if key == K_LEFT:
                self.player_1.move('left')
            if key == K_UP:
                self.player_1.move('up')
            if key == K_DOWN:
                self.player_1.move('down')

            if key == K_d:
                self.player_2.move('right')
            if key == K_a:
                self.player_2.move('left')
            if key == K_w:
                self.player_2.move('up')
            if key == K_s:
                self.player_2.move('down')

    def main(self):
        frostmourne = Weapon('Sword', 400, 0.8)
        gorehowl = Weapon('Axe', 400, 0.3)
        hero = Hero('Arthas', 10000, 'Lich King')
        orc = Orc('Hellscream', 12000, 1.5)
        hero.equip_weapon(frostmourne)
        orc.equip_weapon(gorehowl)
        self.set_player('player_1', hero)
        self.set_player('player_2', orc)
        self.set_player_position(self.player_1, [50, 50])
        self.set_player_position(self.player_2, [350, 350])
        winner = 'no one'
        myfont = pygame.font.SysFont("monospace", 20)
        clock = pygame.time.Clock()
        while True:
            self.screen.fill((100, 0, 0))
            self.draw_players()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    self.move_players(event.key)
            if colide(self.player_1.position, self.player_2.position):
                fight = Fight(self.player_1.entity, self.player_2.entity)
                winner = fight.simulate_fight()
                break

            self.draw_players()
            pygame.display.update()
            clock.tick(30)

        while True:
            self.screen.fill((100, 0, 0))
            pygame.display.update()
            print_text = myfont.render(winner, 1, (0, 100, 0))
            self.screen.blit(print_text, (50, 50))
            pygame.display.update()
            clock.tick(30)


if __name__ == '__main__':
    Game().main()
