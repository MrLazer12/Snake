import turtle
import time
import random
from screeninfo import get_monitors#aflare rezolutie la monitor pentru fullscreen
import subprocess#pentru a crea o iluzie de pornire intr-o fereastra
import pygame

pygame.mixer.init()

class game_settings:
    score = 0 #scorul initial
    high_score = 0 #scorul cel mai inalt acumulat, in timpul jocului
    delay = 0.1 #timp de intarziere
    level=1 #nivel curent jucat
    
    paused = False

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)

    #CREARE FEREASTRA TURTLE ------------------------------------------------------------------------------------------------
    def create_game_window(window_width,window_height):
        wind = turtle.Screen()
        #schimb imagine de titlu la fereastra si adaug text la titlu
        root = turtle.Screen()._root # acest root este de fapt un tkinter's Tk obiect care are metoda iconbitmap
        root.iconbitmap("game-snake-logo.ico") #imaginea trebuie sa fie strict .ico
        wind.title("Snake Game")

        # inaltimea si largimea a ferestrei
        wind.setup(width=window_width, height=window_height)
        wind.tracer(0)#funcție  utilizată pentru a activa sau opri animația la sarpe și pentru a seta o întârziere(delay)
        # wind._root.resizable(False, False) # disable full-screen mode/resize screen
        return wind
    
    #------ PORNIRE SUNET ---------------------------------------------------------------------------------------------------
    def play_background_sound(path_to_music):
        pygame.mixer.music.load("sounds/forest_wind_and_birds.mp3")
        pygame.mixer.music.play(-1)#merge infinit muzica

    def play_sound(path_to_music):
        pygame.mixer.find_channel().play(pygame.mixer.Sound(path_to_music))
    #------------------------------------------------------------------------------------------------------------------------
    def gobackToMenu():
        pygame.mixer.music.stop()#oprire muzica, ca ea sa nu cante cand niam dus la meniu
        turtle.bye()
        subprocess.call(" python main.py", shell=True)

    #------------------------------------------------------------------------------------------------------------------------
    def check_what_level_is(self):
        #nivel 1 ------------------------
        if self.score<100:
            wind.bgpic('levels/level_1.png') #imagine stric doar in png sau gif
            wind.update() # aratare imagine
            self.level=1
            self.delay=0.065
            self.write_current_score(self)
        #nivel 2 ------------------------
        elif self.score==100:
            wind.bgpic('levels/level_2.png')
            wind.update()
            self.level=2
            self.delay=0.055
            self.write_current_score(self)
        #nivel 3 ------------------------
        elif self.score==200:
            wind.bgpic('levels/level_3.png')
            wind.update()
            self.level=3
            self.delay=0.035
            self.write_current_score(self)
    #------------------------------------------------------------------------------------------------------------------------
    #scrirea scorului curent obtinut in joc/pierdere de joc=========================
    def write_current_score(self):
        #verificare daca sa pus/nu pus jocul la pauza
        if game.paused==True:
            self.pen.clear()
            self.pen.penup()
            self.pen.hideturtle()
            self.pen.goto(0,0)
            self.pen.write("PAUSED...", align="center", font=("Arial", 50, "bold"))
        else:
            self.pen.clear()
            font_size=18
            #veficare daca ecranul este pus in mod fullscreen
            if x_limit>290:
                self.pen.goto(0,470)
                font_size=25
            else:
                self.pen.goto(0,260)
            self.pen.write("Level: {} Score: {} High Score: {} ".format(self.level, self.score, self.high_score), align="center", font=("Arial", font_size, "bold"))


    # FUNCTII PENTRU CAZUL CAND JUCATORUL A PIERDUT =====================================
    def if_lost_restart_the_game(self):
        
        head.goto(0, 0)
        head.direction = "Stop"

        #ducem segmentele de la coada in inafara ecranului
        for segment in snake.segments:
            segment.goto(1000, 1000)

        snake.segments.clear()
        snake.nr_segments=0

        food.goto(45, 60)
        self.pen.goto(0,0)
        self.pen.clear()
        self.pen.write("You lost!!!\nYour Score: {} \nYour High Score: {} ".format(self.score, self.high_score), align="center", font=("Arial", 20, "bold"))
        self.pen.goto(0,260)
        self.play_sound("sounds/game_lost.wav")
        self.play_sound("sounds/phrases/try_again.wav")
        time.sleep(3)
        
        self.score = 0
        snake.initial_tail=0
        head.hideturtle()
    #-----------------------------------------------------------------------------------------------------------------------


class MySnake:
    segments = []
    nr_segments=0
    initial_tail=0

    #creare imagini prin register_shape pentru sarpe, mancare etc
    head_up = 'snake_body/head_up.gif'
    head_down = 'snake_body/head_down.gif'
    head_left = 'snake_body/head_left.gif'
    head_right = 'snake_body/head_right.gif'

    food1_img = 'food/apple.gif'
    food2_img = 'food/food2.gif'
    food3_img = 'food/food3.gif'

    body_upDOWN = 'snake_body/body_upDOWN.gif'
    body_left_right = 'snake_body/body_left.gif'

    colt_josStanga = 'snake_body/colt_josStanga.gif'
    colt_josDreapta = 'snake_body/colt_josDreapta.gif'
    colt_susStanga = 'snake_body/colt_susStanga.gif'
    colt_susDreapta = 'snake_body/colt_susDreapta.gif'

    tail_up = 'snake_body/tail_up.gif'
    tail_down = 'snake_body/tail_down.gif'
    tail_left = 'snake_body/tail_left.gif'
    tail_right = 'snake_body/tail_right.gif'

    def __init__(self, wind):
        wind.register_shape(self.head_up)
        wind.register_shape(self.head_down)
        wind.register_shape(self.head_left)
        wind.register_shape(self.head_right)

        wind.register_shape(self.food1_img)
        wind.register_shape(self.food2_img)
        wind.register_shape(self.food3_img)

        wind.register_shape(self.body_upDOWN)
        wind.register_shape(self.body_left_right)

        wind.register_shape(self.tail_up)
        wind.register_shape(self.tail_down)
        wind.register_shape(self.tail_left)
        wind.register_shape(self.tail_right)

        wind.register_shape(self.colt_josStanga)
        wind.register_shape(self.colt_josDreapta)
        wind.register_shape(self.colt_susStanga)
        wind.register_shape(self.colt_susDreapta)

    # capul sarpelui --------------------------------------------------
    def create_snake_head(self):
        head = turtle.Turtle()
        head.shape(self.head_up)
        head.penup()
        head.goto(0, 0)
        head.direction = "Stop"

        return head
    #------------------------------------------------------------------------------------------------------------------------
    
    # creare mancare pentru sarpe -----------------------------------------
    def create_snake_food(self):
        food = turtle.Turtle()

        shapes = random.choice([self.food1_img, self.food2_img, self.food3_img])
        food.speed(0)
        food.shape(shapes)
        food.penup()

        return food
    #------------------------------------------------------------------------------------------------------------------------
    def add_segment(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape(snake.body_upDOWN)

        new_segment.penup()
        self.segments.append(new_segment)

    # setare butoane de navigare --------------------------------------
    @staticmethod#daca nu pun da eroare -> TypeError: 0 positional arguments but 1 was given
    def goup():
        if head.direction != "down":
            head.direction = "up"
    @staticmethod
    def godown():
        if head.direction != "up":
            head.direction = "down"
    @staticmethod
    def goleft():
        if head.direction != "right":
            head.direction = "left"
    @staticmethod
    def goright():
        if head.direction != "left":
            head.direction = "right"

    def move(self):
        if head.direction == "up":
            y = head.ycor() #aflam coordonatele lui y
            head.sety(y+24)
            head.shape(self.head_up)

        if head.direction == "down":
            y = head.ycor() #aflam coordonatele lui y
            head.sety(y-24)
            head.shape(self.head_down)

        if head.direction == "left":
            x = head.xcor() #aflam coordonatele lui x
            head.setx(x-24)
            head.shape(self.head_left)

        if head.direction == "right":
            x = head.xcor() #aflam coordonatele lui x
            head.setx(x+24)
            head.shape(self.head_right)

    # Schimbare imagine la coada la diferit event keypress(sus/jos, stanga/dreapta) ------------
    def display_snake_segments_images_correctly(self):
        if len(self.segments)!=0:
            for index in range(len(self.segments)):
                if index+1 != len(self.segments):
                    #segment precedent
                    x_segment_previos = self.segments[index-1].xcor()
                    y_segment_previos = self.segments[index-1].ycor() 

                    #segment curent
                    x_segment = self.segments[index].xcor()
                    y_segment = self.segments[index].ycor() 

                    #segment urmator
                    x_segment_next = self.segments[index+1].xcor() 
                    y_segment_next = self.segments[index+1].ycor()

                    #pozitionare corecta a cozii in directie sus/jos, stanga/dreapta---------------------
                    if x_segment>x_segment_next or x_segment<x_segment_next:
                        self.segments[index+1].shape(self.body_left_right)
                    else:
                        self.segments[index+1].shape(self.body_upDOWN)

                    #colturile--------------------------------------------------------------------------
                    #gasim coltul                  
                    if ( (y_segment==y_segment_next and x_segment==x_segment_previos) or
                        (x_segment==x_segment_next and y_segment==y_segment_previos) ):
                        
                        #y = constant, x - se schimba, x_curent>x_urmatorul
                        if y_segment==y_segment_next and x_segment>x_segment_next:
                            if y_segment>y_segment_previos:
                                self.segments[index+1].shape(self.colt_susDreapta)
                            else:
                                self.segments[index+1].shape(self.colt_josDreapta)
                        
                        #x = constant, y - se schimba, y_curent>y_urmatorul
                        elif x_segment==x_segment_next and y_segment>y_segment_next:
                            if x_segment<x_segment_previos:
                                self.segments[index+1].shape(self.colt_susStanga)
                            else:
                                self.segments[index+1].shape(self.colt_susDreapta)
                        
                        #x=constatn, y - se schimba, y_curent<y_urmatorul
                        elif x_segment==x_segment_next and y_segment<y_segment_next:
                            if x_segment>x_segment_previos:
                                self.segments[index+1].shape(self.colt_josDreapta)
                            else:
                                self.segments[index+1].shape(self.colt_josStanga)
                                
                        #caz x_curent == x_curent si y_curent == y_curent si directia capului sus|jos|stanga|dreapta  
                        elif ( (y_segment==y_segment_next and x_segment==x_segment_previos and head.direction=='down') or
                                (y_segment==y_segment_next and x_segment==x_segment_previos and head.direction=='up') or
                                (y_segment==y_segment_next and x_segment==x_segment_previos and head.direction=='left') or
                                (y_segment==y_segment_next and x_segment==x_segment_previos and head.direction=='right') ):
                            if y_segment==y_segment_next and x_segment==x_segment_previos:
                                if x_segment<x_segment_next:
                                    if y_segment<y_segment_previos:
                                        self.segments[index+1].shape(self.colt_josStanga)
                                    else:
                                        self.segments[index+1].shape(self.colt_susStanga)
                                elif y_segment<y_segment_previos:
                                        self.segments[index+1].shape(self.colt_josStanga)
                                else:
                                    self.segments[index+1].shape(self.colt_josDreapta)
                            else:
                                self.segments[index+1].shape(self.colt_josStanga)
                
                #== CODITA------------------------------------------------------------------------------
                x_pre_last_segment= self.segments[len(self.segments)-2].xcor() 
                y_pre_last_segment= self.segments[len(self.segments)-2].ycor() 

                x_last_segment= self.segments[len(self.segments)-1].xcor() 
                y_last_segment= self.segments[len(self.segments)-1].ycor() 
                
                #daca pren ultimul fragmen se afla interval pe axa X
                if x_last_segment>=x_pre_last_segment or x_last_segment<=x_pre_last_segment:
                    if x_last_segment<x_pre_last_segment:
                        self.segments[len(self.segments)-1].shape(self.tail_left)
                    elif x_last_segment>x_pre_last_segment:
                        self.segments[len(self.segments)-1].shape(self.tail_right)

                #daca pren ultimul fragmen se afla interval pe axa Y
                if y_last_segment>=y_pre_last_segment or y_last_segment<=y_pre_last_segment:
                    if y_last_segment<y_pre_last_segment:
                        self.segments[len(self.segments)-1].shape(self.tail_down)
                    elif y_last_segment>y_pre_last_segment:
                        self.segments[len(self.segments)-1].shape(self.tail_up)
                        
                #punere pozitie corecta la segmentul ce urmeaza dupa cap--------------------------------
                if head.direction == 'up' or head.direction == "down":
                    self.segments[0].shape(self.body_upDOWN)
                elif head.direction == 'left' or head.direction == "right":
                    self.segments[0].shape(self.body_left_right)
        #-----------------------------------------------------------------------------------------------

#============================================================================================================================
game = game_settings
game.play_background_sound("sounds/forest_wind_and_birds.mp3")
wind = game.create_game_window(600,600)

snake = MySnake(wind)
head = snake.create_snake_head()
head.hideturtle() #ascund capul, deoarece are 0 segmente

food = snake.create_snake_food()
food.goto(0, 100)
#==================================================================

#===  SETARE JOC FULLSCREEN SI INVERS ==========================================
#aflu rezolutia la monitor ---------------------------------------------------

my_monitor_width=0
my_monitor_height=0

for m in get_monitors():
    my_monitor_width=m.width
    my_monitor_height=m.height

#limitele campului la joc pentru fereastra 600x600
x_limit = 290 
y_limit = 290

def fullscreen():
    screenTk = wind.getcanvas().winfo_toplevel()
    screenTk.attributes("-fullscreen", True)
    wind.setup(width=my_monitor_width, height=my_monitor_height)

    #limitele campului la joc
    global x_limit, y_limit
    x_limit = my_monitor_width-970 #axa x #scad, deoarece se duce sarpele peste granita jocului
    y_limit = my_monitor_height-560 #axa y

    #adaugare pozitie de mancare noua
    x = random.randint(-(x_limit-20), x_limit-20)
    y = random.randint(-(y_limit-20), y_limit-20)      
    food.goto(x, y)
    head.goto(0,0)#pozitionare cap la centru la setare fullscreen

    game.check_what_level_is(game)
    game.write_current_score(game)

    wind.onkeypress(normal_screen,"space")

def normal_screen():
    screenTk = wind.getcanvas().winfo_toplevel()
    screenTk.attributes("-fullscreen", False)
    wind.setup(width=600,height=600, startx=650, starty=200)

    #limitele campului la joc pentru fereastra 600x600
    global x_limit, y_limit
    x_limit = 290
    y_limit = 290

    #adaugare pozitie de mancare noua
    x = random.randint(-270, 270)
    y = random.randint(-270, 270) 
    food.goto(x, y)
    head.goto(0,0)#pozitionare cap la centru dup iesire fullscreen

    game.check_what_level_is(game)
    game.write_current_score(game)

    wind.onkeypress(fullscreen,"space")
#===========================================================================================


#=================================================================================
# PAUSE THE GAME

def pause():
    if game.paused == False:
        head.direction = "stop"
        head.hideturtle()

        #ducem segmentele de la coada in inafara ecranului
        for segment in snake.segments:
            segment.goto(1000, 1000)
        snake.segments.clear()
        game.paused = True
    else:
        head.showturtle()
        for readding_segments in range(snake.nr_segments):
            snake.add_segment()
            readding_segments+=1
        head.direction = "up"
        head.goto(0,0)
        game.paused=False
        game.write_current_score(game)
#===============================================================================================

wind.listen()
wind.onkeypress(fullscreen,"space")
wind.onkeypress(snake.goup, "Up")
wind.onkeypress(snake.godown, "Down")
wind.onkeypress(snake.goleft, "Left")
wind.onkeypress(snake.goright, "Right")
wind.onkeypress(game.gobackToMenu, "Escape")
wind.onkeypress(pause, "BackSpace")
#===============================================================================================

#===============================================================================================
# Logica jocului -------------------------------------------------------------------------------
number_iteraions=0 #counter pentru pornire sunet cum sarpe se misca prin iarba peste X iteratii

while True:
    wind.update()

    # Oprire joc daca so ciocnit capul cu peretele ----------------------------------------------
    if head.xcor() > x_limit or head.xcor() < -x_limit or head.ycor() > y_limit or head.ycor() < -y_limit:
        game.if_lost_restart_the_game(game)
    #-------------------------------------------------------------------------------------------

    # Schimbarea niveluiui la un scor anumit ajuns ---------------------------------------------
    game.check_what_level_is(game)
    #------------------------------------------------------------------------------------------

    #cand va ajunge la X iteratii, atunci se va lansa sunetul, cum sarpele alearga prin iarba--
    #incep a numara iteratii numa atunci cand capu se afla intr-o oricare directie
    if head.direction=='up' or head.direction=='down' or head.direction=='left' or head.direction=='right':
        number_iteraions+=1
        if number_iteraions == 29:
            game.play_sound("sounds/running_in_grass.wav")
            number_iteraions=0
    #------------------------------------------------------------------------------------------


    # Adaugare segment nou la coada -----------------------------------------------------------
    if head.distance(food) < 20:
        game.play_sound("sounds/ate_food.mp3")
        #generarea aleatorie a locului unde va fi mancarea urmatoare
        if x_limit>290:
            x_food = random.randint(-(x_limit-40), x_limit-40)
            y_food = random.randint(-(y_limit-40), y_limit-40)      
        else:
            x_food = random.randint(-270, 270)
            y_food = random.randint(-270, 270)

        food.goto(x_food, y_food)

        # adaugare coada, daca am prins mancarea si score++
        snake.add_segment()
        snake.nr_segments+=1

        #adaugare scor
        game.score += 10
        if game.score > game.high_score:
            game.high_score = game.score
        game.write_current_score(game)
    #-------------------------------------------------------------------------------------------


    # adaugare segmente la coada, ca sa nu fie aratat doar capu ------------------------------
    if snake.initial_tail<5:
        if head.direction=='up' or head.direction=='down' or head.direction=='left' or head.direction=='right':
            head.showturtle()
            snake.add_segment()
            snake.nr_segments+=1
            snake.initial_tail+=1
    #------------------------------------------------------------------------------------------

    #aratare imagini segmente corect
    snake.display_snake_segments_images_correctly()

    #miscarea sarpelui, adica misc segmentele odata cu capul
    for index in range(len(snake.segments)-1, 0, -1):
        x = snake.segments[index-1].xcor()
        y = snake.segments[index-1].ycor()
        snake.segments[index].goto(x, y)
    if len(snake.segments) > 0:
        x = head.xcor()
        y = head.ycor()
        snake.segments[0].goto(x, y)
    snake.move()

    # Verificarea coliziunilor capului cu segmentele corpului --------------------------------------
    for segment in snake.segments:
        if segment.distance(head) < 20:
            game.if_lost_restart_the_game(game)
    
    time.sleep(game.delay)
#=====================================================================================

wind.mainloop()
