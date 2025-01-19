import os.path
from Settings import *
from Player import Player
from Platform import Platform
from Bonuses import Bonuses
from Droplet  import Droplet
from Button import  Button
from Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.file = "score.txt"
        if not os.path.exists(self.file) or os.path.getsize(self.file) == 0:
            with open(self.file, "w") as file:
                file.write("Score \tTime \n")

        self.running = True
        self.minutes = None
        self.seconds = None
        self.time = None

        self.font = pygame.font.Font(join("dist/Assets", "Font_style.ttf"), 24)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("OT Game")

        self.clock = pygame.time.Clock()
        self.tick = pygame.time.get_ticks()

        self.background = pygame.image.load(join("dist/Assets", "background.png")).convert_alpha()
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.blit(self.background, (0, 0))


        #Načítanie tried do hry
        self.Player = Player()
        self.Platform = Platform()
        self.Bonus = Bonuses()
        self.Droplet = Droplet()

        #Pesnička na pozadí hry
        self.background_music = pygame.mixer.Sound(join("dist/Assets", "Music", "Background_music.mp3"))
        self.background_music.set_volume(0.1)


        # Zvuk po minutí životov
        self.end_effect = pygame.mixer.Sound(join("dist/Assets", "Music", "game_over.mp3"))
        self.end_effect.set_volume(0.3)

        # Pesnička na pozadí
        self.music = pygame.mixer.Sound(join("dist/Assets", "Music", "start_end_music.mp3"))
        self.music.set_volume(0.2)


    def Start_screen(self):
        Start = True
        Start_button = Button(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 100, 50, "Start", 32)
        self.music.play(loops=-1)
        while Start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Start = False
                    self.running = False

            mouse_position = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            if Start_button.Detection(mouse_position, mouse_click):
                Start = False
                self.music.stop()
                hra = Game()
                hra.Run()

            self.screen.blit(Start_button.button, Start_button.button_rect)

            self.clock.tick(60)
            pygame.display.update()

    def End_screen(self,score):
        end = True
        Again_button = Button(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 80, 200, 50, "Play Again", 32)
        Score_button = Button(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 200, 50, "Score", 32)
        self.screen.blit(self.background, (0, 0))
        self.music.play(loops=-1)
        font = pygame.font.Font(join("dist/Assets", "Font_style.ttf"), 50)
        text_score = font.render(f"Your Score: {score}", True, pygame.Color('black'))
        text_rect = text_score.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 150))
        self.screen.blit(text_score, text_rect)

        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False
                    self.running = False

            self.screen.blit(Score_button.button, Score_button.button_rect)
            self.screen.blit(Again_button.button, Again_button.button_rect)

            mouse_position = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            if Score_button.Detection(mouse_position, mouse_click):
                end = False
                self.music.stop()
                tabulka = Score(score)
                tabulka.Animate(self.file)

            if Again_button.Detection(mouse_position, mouse_click):
                end = False
                self.music.stop()
                self.end_effect.stop()
                self.Player.hurt_sound.stop()
                hra = Game()
                hra.Run()

            self.clock.tick(60)
            pygame.display.update()


    def Bonus_Icons(self):
        self.screen.blit(pygame.transform.scale(self.Bonus.extra_jump_img, (30, 30)), (10, 50))
        extra_jump_text = self.font.render(f"x {self.Player.extra_jump_quantity}", True, pygame.Color('black'))
        self.screen.blit(extra_jump_text, (50, 50))

        self.screen.blit(pygame.transform.scale(self.Bonus.extra_life_img, (30, 30)), (10, 90))
        extra_life_text = self.font.render(f"x {self.Player.bonus_life_quantity}", True, pygame.Color('black'))
        self.screen.blit(extra_life_text, (50, 90))

    def Time_and_Score(self):
        score_text = self.font.render(f"Score: {self.Platform.score}", True, pygame.Color('black'))
        self.screen.blit(score_text, (10, 10))

        time = (pygame.time.get_ticks() - self.tick) // 1000
        self.seconds = time % 60
        self.minutes = time // 60
        self.time = self.font.render(f"Time: {self.minutes:02}:{self.seconds:02}", True, pygame.Color('black'))
        self.screen.blit(self.time, (WINDOW_WIDTH - self.time.width - 10, 10))

    def Run(self):
        self.background_music.play(loops=-1)
        while self.running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.Player.bonus_life_quantity < 0:
                self.running = False

            self.Bonus_Icons()
            self.Time_and_Score()
            self.Platform.Update(self.screen, self.Player)
            self.Player.Update(self.Platform, self.screen)
            self.Bonus.Update(self.screen, self.Player)
            self.Droplet.Update(self.screen, self.Player)

            pygame.display.update()
            self.clock.tick(60)

        self.background_music.stop()

        with open(self.file,"a") as file:
            file.write(f"{self.Platform.score:>4}   {self.minutes:02}:{self.seconds:02}\n")

        if self.Player.bonus_life_quantity < 0:
            self.end_effect.play()
            self.running = False
            self.End_screen(self.Platform.score)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.Start_screen()
