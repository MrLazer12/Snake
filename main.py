import pygame
from pygame.locals import *
import os
import subprocess
# initializarea ferestrei/jocului
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

#== Meniul ==================================================
class MyMenu:
    # rezolutia la fereastra
    screen_width=600
    screen_height=600
    screen=pygame.display.set_mode((screen_width, screen_height))

    # Game Framerate
    clock = pygame.time.Clock()
    FPS=30
    #-----------------------------------------------------------------------------------------------------

    # culorile pentru text -----------------------------------------
    white=(255, 255, 255)
    black=(0, 0, 0)
    gray=(50, 50, 50)
    red=(255, 0, 0)
    green=(0, 255, 0)
    blue=(0, 0, 255)
    yellow=(255, 255, 0)

    # sriftul la text
    font = "fonts/MachineGunk-nyqg.ttf"
    font__RobotoMono_Regular = "fonts/RobotoMono-Regular.ttf"

    menu_status=False #setare meniu pornit/stans
    key_up_pressed=0
    key_down_pressed=0

    #-----------------------------------------------------------------------------------------------------
    def play_background_music(path_to_music):
        pygame.mixer.init()
        pygame.mixer.music.load(path_to_music)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)#merge infinit muzica
        
    #-----------------------------------------------------------------------------------------------------
    def change_game_icon_and_add_title(game_title, path_to_ico):
        #schimb imagine de titlu la fereastra si adaug text la titlu
        pygame.display.set_caption(game_title)
        pygame.display.set_icon(pygame.image.load(path_to_ico)) #formatul .ico nu merge

    #-----------------------------------------------------------------------------------------------------
    def text_format(message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)

        return newText

    #-----------------------------------------------------------------------------------------------------
    def play_sound(path_to_sound):
        pygame.mixer.find_channel().play(pygame.mixer.Sound(path_to_sound))

    #-----------------------------------------------------------------------------------------------------
    def main_menu(self):
        self.menu_status=True
        selected="start"

        while self.menu_status:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    #daca sa apasat tasta in sus-----------------------------------------------------------
                    if event.key==pygame.K_UP:
                        self.play_sound("sounds/menu_select.wav")
                        if self.key_up_pressed==0:
                            selected="quit"
                            self.key_up_pressed+=1
                        elif self.key_up_pressed==1:
                            selected="game_instructions"
                            self.key_up_pressed+=1
                        else:
                            selected="start"
                            self.key_up_pressed=0
                    #daca sa apasat tasta in jos------------------------------------------------------------
                    elif event.key==pygame.K_DOWN:
                        self.play_sound("sounds/menu_select.wav")
                        if self.key_down_pressed==0:
                            selected="game_instructions"
                            self.key_down_pressed+=1
                        elif self.key_down_pressed==1:
                            selected="quit"
                            self.key_down_pressed+=1
                        else:
                            selected="start"
                            self.key_down_pressed=0
                        
                    if event.key==pygame.K_RETURN:
                        if selected=="start":
                            menu.play_sound("sounds/phrases/game_start.wav")
                            pygame.time.delay(1350)
                            pygame.quit()
                            subprocess.call(" python snake.py", shell=True)

                        if selected=="game_instructions":
                            self.menu_status=False
                        if selected=="quit":
                            menu.play_sound("sounds/phrases/quit_game_sound.wav")
                            pygame.time.delay(1500)
                            pygame.quit()
                            quit()

            # Stilizarea Interfetei Principale a Meniului ----------------------------------------------------
            #punerea imaginii de fundal -----------------------------------
            bg = pygame.image.load("menu_images/bg_menu.jpg")
            self.screen.blit(bg, (-350, 0))

            title=self.text_format("Snake Game", self.font, 90, self.yellow)
            if selected=="start":
                text_start=self.text_format("START", self.font, 75, self.white)
            else:
                text_start = self.text_format("START", self.font, 75, self.black)

            if selected=="game_instructions":
                text_game_instructions=self.text_format("Instructions", self.font, 55, self.white)
            else:
                text_game_instructions = self.text_format("Instructions", self.font, 55, self.black)
                
            if selected=="quit":
                text_quit=self.text_format("QUIT", self.font, 75, self.white)
            else:
                text_quit = self.text_format("QUIT", self.font, 75, self.black)

            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            game_instructions_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()

            # amplasarea textului pe ecran--------------------------------------
            self.screen.blit(title, (self.screen_width/2 - (title_rect[2]/2), 80))
            self.screen.blit(text_start, (self.screen_width/2 - (start_rect[2]/2), 300))
            self.screen.blit(text_game_instructions, (self.screen_width/2.45 - (game_instructions_rect[2]/2), 372))
            self.screen.blit(text_quit, (self.screen_width/2 - (quit_rect[2]/2), 420))

            pygame.display.update()
            self.clock.tick(self.FPS)

    #-----------------------------------------------------------------------------------------------------
    def game_instructions_window(self):
        self.menu_status=True
        selected="go back"

        self.screen.blit(pygame.image.load("menu_images/bg_menu.jpg"), (-350, 0))
        self.screen.blit(pygame.image.load('menu_images/button_bg.png'), (240,500))
        self.screen.blit(pygame.image.load('menu_images/text_cover.png'), (-100,0))
        self.screen.blit(pygame.image.load("menu_images/spacebar.png"),(50,160))
        self.screen.blit(pygame.image.load("menu_images/down.png"), (15,210))
        self.screen.blit(pygame.image.load("menu_images/left.png"), (55,210))
        self.screen.blit(pygame.image.load("menu_images/up.png"), (95,210))
        self.screen.blit(pygame.image.load("menu_images/right.png"), (135,210))
        self.screen.blit(pygame.image.load("menu_images/Escape.png"), (118,260))
        self.screen.blit(pygame.image.load("menu_images/BackSpace.png"), (50,310))

        while self.menu_status:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        if selected=="go back":
                            self.menu_status=False
                            
            # Stilizarea Interfetei Principale a Meniului ----------------------------------------------------
            title=self.text_format("Game Instructions", self.font, 60, self.yellow)
            text_fullscreenmode=self.text_format("- fullscreenmode", self.font__RobotoMono_Regular, 24, self.white)
            text_go_back=self.text_format("- Go back to menu", self.font__RobotoMono_Regular, 24, self.white)
            test_arrows=self.text_format("- Snake movements", self.font__RobotoMono_Regular, 24, self.white)
            text_backspace=self.text_format("- Pause the game", self.font__RobotoMono_Regular, 24, self.white)
            title_rect=title.get_rect()

            # amplasarea textului pe ecran--------------------------------------
            self.screen.blit(title, (self.screen_width/2 - (title_rect[2]/1.7), 70))

            self.screen.blit(text_fullscreenmode, (180, 160))
            self.screen.blit(test_arrows, (180, 210))
            self.screen.blit(text_go_back, (180, 260))
            self.screen.blit(text_go_back, (180, 260))
            self.screen.blit(text_backspace, (180, 310))
            
            self.screen.blit(self.text_format("Go back", self.font, 60, self.black), (self.screen_width - 270, 520))

            pygame.display.update()
            self.clock.tick(menu.FPS)

#pornire menu
menu = MyMenu
menu.change_game_icon_and_add_title("Snake Game",'game-snake-logo.jpg')

while(True):
    menu.play_background_music("sounds/menu_background_sound.mp3")
    menu.main_menu(menu)

    menu.play_background_music("sounds/game_instructions_sound.mp3")
    menu.play_sound("sounds/phrases/game_instructions.wav")
    menu.game_instructions_window(menu)