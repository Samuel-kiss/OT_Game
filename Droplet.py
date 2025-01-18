
from Settings import *

class Droplet:
    def __init__(self):
        self.Droplets = []
        self.image = pygame.transform.scale(pygame.image.load(join("dist/Assets", "Kvapka.png")).convert_alpha(), (15, 20))
        self.create_time = 3000
        self.last_creation_time = pygame.time.get_ticks()
        self.speed = 3
        # Zvukový efekt trafenia
        self.effect = pygame.mixer.Sound(join("dist/Assets", "Music", "hurt.mp3"))
        self.effect.set_volume(0.2)

    def Create(self):
        time = pygame.time.get_ticks()
        if time-self.last_creation_time > self.create_time:
            poz_x = random.randint(0,WINDOW_WIDTH)
            rect = pygame.Rect(poz_x, 0, self.image.width, self.image.height)
            self.Droplets.append(rect)
            self.last_creation_time = time

    def Collision_and_Move(self,player):
        for droplet in self.Droplets:
            droplet.y += self.speed
            if droplet.y > WINDOW_HEIGHT:
                self.Droplets.remove(droplet)
            elif droplet.colliderect(player.rect):
                self.effect.play()
                player.bonus_life_quantity -= 1
                self.Droplets.remove(droplet)
    def Animation(self,screen):
        for droplet in self.Droplets:
            screen.blit(self.image, droplet)
    def Update(self,screen,player):
        self.Create()
        self.Collision_and_Move(player)
        self.Animation(screen)