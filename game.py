import pygame
import time
import random

#initializing the pygame library
pygame.init()

dis_width = 800
dis_hei = 600
speed = 8
snake_size = 10

dis=pygame.display.set_mode((dis_width,dis_hei))
pygame.display.update()
pygame.display.set_caption("Welcome to Snake game")

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255, 0, 0)
yellow = (255,255,102)
green = (0, 255, 0)

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_size, snake_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[100 , 125])


def gameLoop():
    game_over = False
    game_close = False

    #Position Parameters
    x1 = dis_width/2
    y1 = dis_hei/2

    x2 = 0
    y2 = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, dis_width - snake_size)/10.0) * 10.0
    foody = round(random.randrange(0, dis_hei - snake_size)/10.0) * 10.0


    # Setting the button functions:
    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("You lost! Press Q-quit \n  P-Play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        # for event in pygame.event.get():
        #     # print(event)
        #
        #     if event.type == pygame.QUIT:
        #         game_over = True
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             x2 = -10
        #             y2 = 0
        #         elif event.key == pygame.K_RIGHT:
        #             x2 = 10
        #             y2 = 0
        #         elif event.key == pygame.K_UP:
        #             x2 = 0
        #             y2 = -10
        #         elif event.key == pygame.K_DOWN:
        #             x2 = 0
        #             y2 = 10

        if not game_close:
            print("entered")

            x1 = x1 + 10
            y1 = 0

            while x1:
                x1 = x1 + 10
                y1 = 0



        # #Free boundary method:
        # if x1 >= 500:
        #     x1 = 0
        # if y1 >= 400:
        #     y1 = 0
        # if x1 < 0:
        #     x1 = 500
        # if y1 < 0:
        #     y1 = 400

        #Restricted boundary method:
        if x1> dis_width or x1 < 0 or y1> dis_hei or y1 < 0:
            game_close = True

        # Setting the parameters for snake element movement:
        x1 += x2
        y1 += y2
        dis.fill(white)
        print(x1,y1)
        pygame.draw.rect(dis, green,[foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list)> snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_size, snake_list)
        pygame.display.update()
        # pygame.draw.rect(dis,blue,[x1,y1,snake_size,snake_size])
        # pygame.display.update()


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_hei - snake_size) / 10.0) * 10.0
            snake_length += 1
        clock.tick(speed)


    pygame.quit()
    quit()

# def searching_algo():
#     if (x1 < (dis_width/2)) and (y1 < (dis_hei/2)):
#
#
#     else if (x1 > (dis_width/2)) and (y1 > (dis_hei/2)):


def main():
    gameLoop()

main()