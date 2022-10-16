import pygame
import random
import math

version = 'v1.1'

class Game:
    def __init__(self, title, widght, height, framerate):
        pygame.init()
        print(f'snasyy/space-invaders {version}')

        self.running = True
        self.spaceship = Spaceship(self, 370, 515)
        self.score = 0
        self.is_break = False
        self.enemy_check = True
        self.enemy_collision = True

        self.enemies = []
        for i in range(12):
            self.enemies.append(Enemy(self, random.randint(0, 736), random.randint(30, 130)))

        self.background_img = pygame.image.load("images/stars.png")
        self.title = pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((widght, height))
        self.clock = pygame.time.Clock()

        while self.running:
            self.clock.tick(framerate)
            self.screen.fill((225, 0, 0))
            self.screen.blit(self.background_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(-10)

                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(10)

                    if event.key == pygame.K_SPACE:
                        self.spaceship.fire_bullet()

                    if event.key == pygame.K_UP:
                        if not self.is_break:
                            self.is_break = True
                        else:
                            self.is_break = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(10)

                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(-10)

            self.spaceship.update()
            if len(self.spaceship.bullets) > 0:
                for bullet in self.spaceship.bullets:
                    if bullet.is_fired == True:
                        bullet.update()
                    else:
                        self.spaceship.bullets.remove(bullet)

            if self.enemy_check == True:
                self.x1 = self.enemies[0].x
                self.x2 = self.enemies[1].x
                self.x3 = self.enemies[2].x
                self.x4 = self.enemies[3].x
                self.x5 = self.enemies[4].x
                self.x6 = self.enemies[5].x
                self.x7 = self.enemies[6].x
                self.x8 = self.enemies[7].x
                self.x9 = self.enemies[8].x
                self.x10 = self.enemies[9].x
                self.x11 = self.enemies[10].x
                self.x12 = self.enemies[11].x

                self.y1 = self.enemies[0].y
                self.y2 = self.enemies[1].y
                self.y3 = self.enemies[2].y
                self.y4 = self.enemies[3].y
                self.y5 = self.enemies[4].y
                self.y6 = self.enemies[5].y
                self.y7 = self.enemies[6].y
                self.y8 = self.enemies[7].y
                self.y9 = self.enemies[8].y
                self.y10 = self.enemies[9].y
                self.y11 = self.enemies[10].y
                self.y12 = self.enemies[11].y

            for enemy in self.enemies:
                enemy.update()

                if self.enemy_collision == True:
                    enemy.check_collision()

                if enemy.y > self.spaceship.y:
                    self.enemy_check = False
                    for i in self.enemies:
                        i.y = 1000
                    self.print_go()
                    self.is_break = None
                    break

                if self.is_break == True:
                    self.enemy_check = False
                    self.enemy_collision = False
                    self.game_break()

                elif self.is_break == False:
                    self.is_break = None
                    self.enemy_check = True
                    self.enemy_collision = True

                    self.enemies[0].x = self.x1
                    self.enemies[1].x = self.x2
                    self.enemies[2].x = self.x3
                    self.enemies[3].x = self.x4
                    self.enemies[4].x = self.x5
                    self.enemies[5].x = self.x6
                    self.enemies[6].x = self.x7
                    self.enemies[7].x = self.x8
                    self.enemies[8].x = self.x9
                    self.enemies[9].x = self.x10
                    self.enemies[10].x = self.x11
                    self.enemies[11].x = self.x12

                    self.enemies[0].y = self.y1
                    self.enemies[1].y = self.y2
                    self.enemies[2].y = self.y3
                    self.enemies[3].y = self.y4
                    self.enemies[4].y = self.y5
                    self.enemies[5].y = self.y6
                    self.enemies[6].y = self.y7
                    self.enemies[7].y = self.y8
                    self.enemies[8].y = self.y9
                    self.enemies[9].y = self.y10
                    self.enemies[10].y = self.y11
                    self.enemies[11].y = self.y12

            self.print_score()
            self.print_highscore( )
            pygame.display.update()

    def print_go(self):
        go_font = pygame.font.Font("freesansbold.ttf", 64)
        go_text = go_font.render("GAME OVER", True, (250, 0, 0))
        self.screen.blit(go_text, (200, 250))

    def print_score(self):
        score_font = pygame.font.Font("freesansbold.ttf", 24)
        score_text = score_font.render("Score: " + str(self.score), True, (250, 250, 250))
        self.screen.blit(score_text, (8, 8))

    def print_highscore(self):
        highscore_file = open("highscore.txt", "r")
        highscore = int(highscore_file.read())

        if highscore < self.score:
            highscore_set = open("highscore.txt", "w")
            highscore_set.write(str(self.score))
            highscore_set.close()

        highscore_file.close()

        highscore_font = pygame.font.Font("freesansbold.ttf", 24)
        highscore_text = highscore_font.render("Highscore: " + str(highscore), True, (250, 250, 250))
        self.screen.blit(highscore_text, (8, 40))


    def print_break(self):
        break_font = pygame.font.Font("freesansbold.ttf", 24)
        break_text = break_font.render("Pause", True, (250, 250, 250))
        self.screen.blit(break_text, (8, 75))

    def game_break(self):
        self.print_break()
        while True:
            for i in self.enemies:
                i.y = -1000
            break



class Spaceship:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.chance_x = 0
        self.spaceship_img = pygame.image.load("images/spaceship.png")
        self.bullets = []

    def fire_bullet(self):
        self.bullets.append(Bullet(self.game, self.x, self.y))
        self.bullets[len(self.bullets) - 1].fire()


    def move(self, speed):
        self.chance_x += speed

    def update(self):
        self.x += self.chance_x
        if self.x < 0:
            self.x = 0
        elif self.x > 736:
            self.x = 736
        self.game.screen.blit(self.spaceship_img, (self.x, self.y))


class Bullet:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.is_fired = False
        self.bullet_speed = 10
        self.bullet_img = pygame.image.load("images/bullet.png")

    def fire(self):
        self.is_fired = True

    def update(self):
        self.y -= self.bullet_speed
        if self.y <= 0:
            self.is_fired = False
        self.game.screen.blit(self.bullet_img, (self.x, self.y))


class Enemy:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.chance_x = 5
        self.chance_y = 60
        self.enemy_img = pygame.image.load("images/enemy.png")

    def check_collision(self):
        for bullet in self.game.spaceship.bullets:
            distance = math.sqrt(math.pow(self.x - bullet.x, 2)) + math.pow(self.y - bullet.y, 2)
            if distance < 35:
                bullet.is_fired = False
                self.game.score += 1
                self.x = random.randint(0, 736)
                self.y = random.randint(30, 130)

    def update(self):
        self.x += self.chance_x
        if self.x >= 736:
            self.y += self.chance_y
            self.chance_x = -5
        elif self.x <= 0:
            self.y += self.chance_y
            self.chance_x = 5
        self.game.screen.blit(self.enemy_img, (self.x, self.y))


if __name__ == "__main__":
    game = Game("Space Invaders", 800, 600, 50)
