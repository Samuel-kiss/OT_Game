from Settings import *

class  Bonuses():
    def __init__(self):
        #Načítanie Bonusov
        self.Bonuses = []
        self.create_time = 3000
        self.speed = 3
        self.last_creation_time = pygame.time.get_ticks()

        #Načítanie obrázkov
        self.double_jump_img = pygame.transform.scale(pygame.image.load(join("dist/Assets", "Bonus", "double_jump.png")), (20, 20))
        self.extra_life_img =  pygame.transform.scale(pygame.image.load(join("dist/Assets", "Bonus", "extra_health.png")), (20, 20))
        self.rect = self.double_jump_img.get_rect()

        #Zvukový efekt zobratia
        self.effect = pygame.mixer.Sound(join("dist/Assets", "Music", "pickup.mp3"))
        self.effect.set_volume(0.2)


    def Create(self,player):
        time = pygame.time.get_ticks()
        if time - self.last_creation_time > self.create_time:
            new_x = random.randint(max(50, player.rect.x - 150), min(WINDOW_WIDTH- 70, player.rect.x + 150))
            type = random.choice(["double_jump", "extra_life"])
            self.rect = pygame.Rect(new_x, 0, self.rect.width, self.rect.height)
            bonus = {"rect": self.rect, "type": type}
            self.Bonuses.append(bonus)
            self.last_creation_time = time

    def Move(self, player):
        for bonus in self.Bonuses:
            bonus["rect"].y += self.speed
            if bonus["rect"].y > WINDOW_HEIGHT:
                self.Bonuses.remove(bonus)
            elif bonus["rect"].colliderect(player.rect):
                self.effect.play()
                if bonus["type"] == "double_jump":
                    player.double_jump_quantity += 1  # Pridanie dvojskoku
                elif bonus["type"] == "extra_life":
                    player.bonus_life_quantity += 1  # Pridanie extra života
                self.Bonuses.remove(bonus)

    def Animation(self, screen):
        for bonus in self.Bonuses:
            if bonus["type"] == "double_jump":
                bonus_image = self.double_jump_img
            else:
                bonus_image = self.extra_life_img
            screen.blit(bonus_image, (bonus["rect"].x, bonus["rect"].y))

    def Update(self, screen,player):
        self.Create(player)
        self.Move(player)
        self.Animation(screen)