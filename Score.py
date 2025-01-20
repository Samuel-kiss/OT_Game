import pygame.display

from Button import Button
from Settings import *

class Score:
    def __init__(self,score,file):
        self.score = score
        self.file = file
        self.clicked = False

        self.image = pygame.transform.scale(pygame.image.load(join("dist/Assets", "background.png")), (WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.blit(self.image, (0, 0))
        self.screen_rect = self.screen.get_rect(center = (WINDOW_WIDTH / 2, 50))

        self.font = pygame.font.Font(join("dist/Assets", "Font_style.ttf"), 32)
        self.text = self.font.render("Score     Time",True,pygame.Color("black"))
        self.text_rect = self.text.get_rect(center=(WINDOW_WIDTH/2,self.text.get_height()))
        self.screen.blit(self.text, self.text_rect)

        self.pressed = False
        self.start = 1
        self.lines_per_page = 15
        try:
            with open(file, "r") as file:
                self.lines = file.readlines()
                self.total_lines = len(self.lines)
        except FileNotFoundError:
            print("Chyba pri čítaní")

        self.Animate()

    def Animate(self):
        self.screen.blit(self.image, (0,0))
        self.screen.blit(self.text, self.text_rect)
        set_y = 100
        end = min(self.start + self.lines_per_page, self.total_lines)
        print(f"{self.total_lines}")
        for number,line in enumerate(self.lines[self.start:end], start=self.start):
            line = line.replace("\t", " ").strip()
            score,time = line.split(" ", 1)
            score.replace(" ","").strip()
            time.replace(" ","").strip()
            text = self.font.render(f"{number:>3}.  {score:>4}   {time:>5}", True, pygame.Color("black"))
            text_rect = text.get_rect(center = (WINDOW_WIDTH / 2 - 20, set_y))
            self.screen.blit(text, text_rect)
            set_y += text_rect.height

    def Run(self):
        Back_button = Button(75, 25, 150, 50, "Back", 32)
        Next_button = Button(WINDOW_WIDTH - 75, WINDOW_HEIGHT - 25, 150, 50, "Next", 32)
        Previous_button = Button(75, WINDOW_HEIGHT - 25, 150, 50, "Previous", 32)
        Clear_button = Button(WINDOW_WIDTH-75, 25, 150, 50, "Clear", 32)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running =  False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    mouse_click = pygame.mouse.get_pressed()

                    if Next_button.Detection(mouse_pos, mouse_click) :
                        if self.start+self.lines_per_page <= self.total_lines:
                            self.start += self.lines_per_page
                            self.Animate()

                    if Previous_button.Detection(mouse_pos, mouse_click):
                        if self.start > 1:
                            self.start -= self.lines_per_page
                            self.Animate()

                    if Clear_button.Detection(mouse_pos, mouse_click):
                        with open(self.file, "w") as file:
                            file.write("")
                        self.lines = []
                        self.total_lines = 0
                        self.start = 1
                        self.lines_per_page = 15
                        self.Animate()


                    if Back_button.Detection(mouse_pos, mouse_click):
                        from Main import Game
                        back = Game()
                        back.End_screen(self.score)

            self.screen.blit(Previous_button.button, Previous_button.button_rect)
            self.screen.blit(Next_button.button, Next_button.button_rect)
            self.screen.blit(Clear_button.button, Clear_button.button_rect)
            self.screen.blit(Back_button.button, Back_button.button_rect)

            pygame.display.update()

        pygame.quit()
        sys.exit()



