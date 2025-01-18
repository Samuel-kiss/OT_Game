
from Settings import *


class Player:
    def __init__(self):
        self.moving = False
        self.jumping = False
        self.on_platform = False
        self.double_jump = False

        self.walk_images = {"right": [], "left": []}
        self.jump_images = {"right": [], "left": [],"double":[]}
        self.Load_walk_images()
        self.Load_jump_images()

        self.direction = "right"
        self.image = pygame.image.load("dist/Assets/Owlet.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

        self.image_index = 0
        self.double_jump_index = 0
        self.speed = 5
        self.fall = 0
        self.double_jump_quantity = 0
        self.bonus_life_quantity = 0
        self.g_force = 0.5
        self.jump = -10

        #Načítanie zvukov
        self.jump_sound = pygame.mixer.Sound(join("dist/Assets", "Music", "jump.mp3"))
        self.jump_sound.set_volume(0.9)

        self.double_jump_sound = pygame.mixer.Sound(join("dist/Assets", "Music", "double_jump.mp3"))
        self.double_jump_sound.set_volume(0.9)

        self.walk_sound = pygame.mixer.Sound(join("dist/Assets", "Music", "walk.mp3"))
        self.walk_sound.set_volume(0.9)

        self.hurt_sound = pygame.mixer.Sound(join("dist/Assets", "Music", "hurt.mp3"))
        self.hurt_sound.set_volume(0.3)




    def Load_walk_images(self):
        for name in self.walk_images.keys():
            for folder_path,sub_folders,file_names in walk(join("dist/Assets", "Walk", name)):
                for file_name in sorted(file_names, key=lambda name: int(name.split(".")[0])):
                    full_path = join(folder_path,file_name)
                    surface = pygame.image.load(full_path).convert_alpha()
                    self.walk_images[name].append(surface)


    def Load_jump_images(self):
        for name in self.jump_images.keys():
            for folder_path,sub_folders,file_names in walk(join("dist/Assets", "Jump", name)):
                for file_name in sorted(file_names, key=lambda name: int(name.split(".")[0])):
                    full_path = join(folder_path,file_name)
                    surface = pygame.image.load(full_path).convert_alpha()
                    self.jump_images[name].append(surface)



    def Gravitation(self,platforms):
        self.fall += self.g_force
        self.rect.y += self.fall

        if self.rect.y > WINDOW_HEIGHT:
            self.hurt_sound.play()
            if self.bonus_life_quantity > 0:
                platform = platforms.Platforms[0]
                self.rect.y = platform.y-20
                self.rect.x = platform.x+(platform.width/2)
                self.fall = 0

            self.bonus_life_quantity -= 1



    def Move(self):
        keys = pygame.key.get_pressed()

        self.moving = False
        self.jumping = False
        self.double_jump = False

        if keys[pygame.K_LEFT]:
            if not self.rect.x< 0:
                self.rect.x -= self.speed
                self.direction = "left"
                self.moving = True

        if keys[pygame.K_RIGHT]:
            if not self.rect.x+self.rect.width-6 > WINDOW_WIDTH:
                self.rect.x += self.speed
                self.direction = "right"
                self.moving = True

        if keys[pygame.K_SPACE]:
            if self.on_platform:
                self.jumping = True
                self.fall = self.jump
                self.jump_sound.play()
                self.on_platform = False
            if not self.rect.y <= 0:
                if not self.on_platform and self.fall>0 and self.double_jump_quantity > 0:
                    self.double_jump = True
                    self.double_jump_sound.play()
                    self.fall = self.jump
                    self.double_jump_quantity -= 1
            else:
                self.rect.y = 0

        if self.moving and self.on_platform:
            self.walk_sound.play()
        else:
            self.walk_sound.stop()

    def Collision(self,platforms):
        self.on_platform = False
        mid_bottom = pygame.Rect(self.rect.midbottom[0]-1,self.rect.midbottom[1],2,2)
        for platform in platforms.Platforms:
            if mid_bottom.colliderect(platform) and self.fall > 0:
                self.rect.y = platform.y-20
                self.fall = 0
                self.on_platform = True



    def Animation(self,screen):
        if not self.on_platform:
            if self.jumping:
                if self.image_index < len(self.jump_images[self.direction]):
                    self.image = self.jump_images[self.direction][self.image_index]
                    self.image_index += 1
                else:
                    self.image = self.jump_images[self.direction][-1]
            else:
                self.image = self.jump_images[self.direction][-1]
                self.image_index = 0

            if self.double_jump:
                if self.double_jump_index < len(self.jump_images["double"]):
                    double_jump_img = self.jump_images["double"][self.double_jump_index]
                    double_jump_rect = double_jump_img.get_rect(center=(self.rect.centerx,self.rect.bottom+15))
                    screen.blit(double_jump_img,double_jump_rect)
            else:
                self.double_jump_index = 0
        else:
            if self.moving:
                self.image_index = (self.image_index+1) % len(self.walk_images[self.direction])
                self.image = self.walk_images[self.direction][self.image_index]
            else:
                self.image = self.walk_images[self.direction][0]
                self.image_index = 0
        screen.blit(self.image, self.rect.topleft)



    def Update(self,platforms,screen):
        self.Move()
        self.Collision(platforms)
        self.Gravitation(platforms)
        self.Animation(screen)



