from pygame import *
window = display.set_mod((500,700))
display.set_caption('Доганялки')
background = transform.scale(image.load('jason-edwards-patrickstar-house (1).jpg'), (700, 500))
clock = time.Clock()
fps = 60
run = True
x1 = 100
y1 = 350
sprite1 = transform.scale(image.load('vydZVBUvMR8l9h5sPc7fXuLfevAjYQhnoPKGvLRN.jpeg.png'), (100,100))
x2 = 400
y2 = 350
sprite2 = transform.scale(image.load('sprite2.png'))
while run:
    window.blit(background, (0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprit2, (x2,y2))
# while True:
#     window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
           run = False
    keys_pressd = key.get_pressed()
    if keys_pressd[k_LEFT] and x1>5:
        x1 -= 10
    if keys_pressed[K_RIGHT] and x1< 595:
        x1 += 10
    if keys_pressd[K_UP] and y1 > 5:
        y1 -= 10
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 +=10
    display.update()
    clock.tick(FPS)