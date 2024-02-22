import pygame
from pygame.locals import *
import random

size = width, height = (1000, 800)
road_width = int(width / 1.6)
roadmark_width = int(road_width / 80)
right_lane = int(width / 2 + road_width / 4)
left_lane = int(width / 2 - road_width / 4)
speed = 1
pygame.font.init()
font = pygame.font.Font(None, 32)

pygame.init()
running = True
# Window size
screen = pygame.display.set_mode((size))
# Title
pygame.display.set_caption("Too Fast or Too Furious?")
# Background color
screen.fill((60,220,0))
# Update screen
pygame.display.update()

# Player vehicle
car = pygame.image.load("Car 1.png")
car_width = car.get_rect().width
car_height = car.get_rect().height
car_loc = car.get_rect()
car_loc.center = left_lane, height*0.85

# Oncoming vehicle
car2 = pygame.image.load("Police.png")
car2_width = car.get_rect().width
car2_height = car.get_rect().height
car2_loc = car.get_rect()
car2_loc.center = right_lane, height*0.3

counter = 0

while True:
    # Clear the screen at the start of each frame
    screen.fill((60,220,0))  # Green background
    #Increase speed of police car 
    counter += 1
    if counter == 1000:
        speed += 0.5
        counter = 0
        print("MORE POLICE ARE COMING!!!")
    # animate police car
    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:
            car2_loc.center= left_lane,-200
        else:
            car2_loc.center= right_lane,-200
    # End game if police car hits player car
    car_rect = pygame.Rect(car_loc[0], car_loc[1], car_width, car_height-160)
    car2_rect = pygame.Rect(car2_loc[0], car2_loc[1], car2_width, car2_height-160)
    # Check for a collision
    if car_rect.colliderect(car2_rect):
        print("THE POLICE GOT YOU!")
        print("Your score was", speed)
        break
    # Check for user input
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_LEFT, K_a]:
                car_loc = car_loc.move([-int(road_width/2+27), 0])
            if event.key in [K_RIGHT, K_d]:
                car_loc = car_loc.move([int(road_width/2+27), 0])
        
    # Check if car is off the road
    if car_loc[0] < (width/2 - road_width/2) or car_loc[0] > (width/2 + road_width/2 - car_width):
        print("You drove off the road!")
        print("Your score was", speed)
        break

 
    # Update score
    score_text = font.render(f'Score: {speed}', True, (0, 0, 0))

    # Build road
    pygame.draw.rect(screen, (50,50,50), (width/2 - road_width/2, 0, road_width, height))
    # Make separate lanes
    pygame.draw.rect(screen, (255,255,255), (width/2 - roadmark_width/2, 0, roadmark_width, height))
    # Yellow lines on the side of the road
    pygame.draw.rect(screen, (255,240,60), (width/2 - road_width/2 + roadmark_width*1, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255,240,60), (width/2 + road_width/2 - roadmark_width*2, 0, roadmark_width, height))

    car = pygame.transform.scale(car, (car_width / 1.5, car_height / 1.5))
    car2 = pygame.transform.scale(car2, (car2_width * 1.3, car2_height * 0.8))

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()

