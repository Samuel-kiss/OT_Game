from Settings import *

class Platform:
    def __init__(self):
        self.platform_width = 100
        self.platform_image = pygame.transform.scale(pygame.image.load(join("dist/Assets", "Platforms", "cloud.png")), (self.platform_width , 20)).convert_alpha()
        self.new_platform_img = pygame.transform.scale(pygame.image.load(join("dist/Assets", "Platforms", "cloud_vytvorenie.png")), (self.platform_width , 20)).convert_alpha()
        self.rect = self.platform_image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.Platforms = [self.rect]
        self.new_platform_rect = None
        self.change_time = 2000
        self.show_time = 500
        self.last_change = pygame.time.get_ticks()
        self.score = 0

    def Add_platform(self,player):
        time = pygame.time.get_ticks()
        if self.new_platform_rect is None and time - self.last_change>self.change_time-self.show_time:
            last_platform = self.Platforms[-1]
            new_x = random.randint(max(50,last_platform.x-100),min(WINDOW_WIDTH - 100, last_platform.x + 100))
            new_y = random.randint(max(200,last_platform.y-100),min(WINDOW_HEIGHT - 50, last_platform.y + 100))
            self.new_platform_rect = pygame.Rect(new_x, new_y, self.platform_width, self.new_platform_img.get_height())

        if time-self.last_change > self.change_time:
            self.Platforms.append(self.new_platform_rect)
            self.new_platform_rect = None

            if len(self.Platforms) > 1:
                self.Platforms.pop(0)
                if player.rect.y < WINDOW_HEIGHT and player.bonus_life_quantity >= 0:
                    self.score += 10


            self.last_change = time
            self.change_time = max(500, self.change_time - 50)
            self.platform_width = max(50, self.platform_width - 5)
            self.platform_image = pygame.transform.scale(self.platform_image, (self.platform_width, 20)).convert_alpha()
            self.new_platform_img = pygame.transform.scale(self.new_platform_img, (self.platform_width, 20)).convert_alpha()

    def Animation(self,screen):
            for platform in self.Platforms:
                screen.blit(self.platform_image, platform)
                if self.new_platform_rect is not None:
                    screen.blit(self.new_platform_img, (self.new_platform_rect.x, self.new_platform_rect.y))

    def Update(self,screen,player):
        self.Add_platform(player)
        self.Animation(screen)

