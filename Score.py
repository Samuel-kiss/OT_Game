import pygame
from Button import Button
from Settings import *

class Score:
    def __init__(self,score):
        self.score = score
        self.clicked = False
        self.image = pygame.transform.scale(pygame.image.load(join("dist/Assets", "background.png")), (WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.blit(self.image, (0, 0))
        self.screen_rect = self.screen.get_rect(center = (WINDOW_WIDTH / 2, 50))
        self.font = pygame.font.Font(join("dist/Assets", "Font_style.ttf"), 32)
        self.text = self.font.render("Score     Time",True,pygame.Color("black"))
        self.text_rect = self.text.get_rect(center=(WINDOW_WIDTH/2,self.text.get_height()))
        self.screen.blit(self.text, self.text_rect)

    def Animate(self,file):
        Back_button = Button(75, 25, 150, 50, "Back", 32)
        try:
            set_y = 100
            with open(file,"r") as file:
                next(file)
                for number,line in enumerate(file, start=1):
                    if number > 15:
                        break
                    line = line.replace("\t", " ").strip()
                    score,time = line.split(" ", 1)
                    score.replace(" ","").strip()
                    time.replace(" ","").strip()
                    text = self.font.render(f"{number:>3}.  {score:>4}   {time:>5}", True, pygame.Color("black"))
                    text_rect = text.get_rect(center = (WINDOW_WIDTH / 2 - 20, set_y))
                    self.screen.blit(text, text_rect)
                    set_y += text_rect.height


            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running =  False
                mouse_pos = pygame.mouse.get_pos()
                mouse_click = pygame.mouse.get_pressed()
                if Back_button.Detection(mouse_pos, mouse_click):
                    running = False
                    self.clicked = True

                self.screen.blit(Back_button.button, Back_button.button_rect)
                pygame.display.update()
            if self.clicked:
                from Main import End_Screen
                end_screen = End_Screen(score)
                end_screen.Run()

            pygame.quit()

        except FileNotFoundError:
            print("Chyba pri čítaní súboru")

