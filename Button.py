
from Settings import *

class Button:
    def __init__(self,x,y,width,height,content,size):
        #Tlačito Start
        self.image = pygame.transform.scale(pygame.image.load(join("dist/Assets", "button.png")), (width, height)).convert_alpha()
        self.button = pygame.Surface((width,height),pygame.SRCALPHA)
        self.button.blit(self.image, (0, 0))
        self.button_rect = self.button.get_rect(center=(x,y))

        self.font = pygame.font.Font(join("dist/Assets", "Font_style.ttf"), size)
        self.text = self.font.render(content,True,pygame.Color('black'))
        self.text_rect = self.text.get_rect(center=(width/2,height/2))
        self.button.blit(self.text,self.text_rect)

    def Detection(self,position,pressed):
        if self.button_rect.collidepoint(position):
            if pressed[0]:
                return True
            return False
        return False
