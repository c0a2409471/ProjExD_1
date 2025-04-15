import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    gb_image=pg.transform.flip(bg_img,True,False)
    tmr = 0
    images=pg.image.load("fig/3.png")
    images=pg.transform.flip(images,True,False)
    images_rct=images.get_rect()
    images_rct.center= (300,200)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            images_rct.move_ip((0, -1))
        if key_lst[pg.K_RIGHT]:
            images_rct.move_ip((1, 0))
        if key_lst[pg.K_LEFT]:
            images_rct.move_ip((-1, 0))
        if key_lst[pg.K_DOWN]:
            images_rct.move_ip((0, 1))


        x=tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(gb_image, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(images,images_rct)
        pg.display.update()
        tmr += 1 
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()