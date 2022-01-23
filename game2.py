from pygame import *

init()

screen = display.set_mode([500, 500])

a = True
while a:
    for e in event.get():
        if e.type == QUIT:
            a = False

    screen.fill((0, 0, 0))

    draw.circle(screen, (255, 255, 255), (250, 250), 250)
    draw.rect(screen, (0, 0, 0), (0, 250, 500, 250))

    display.flip()

quit()
