screen_2 = False
screen_1 = True 
screen_3 = False
start_loc = PVector(250, 600)
start_size = PVector(500, 100)
easy_loc = PVector(25, 200)
easy_size = PVector(400, 50)
def setup():
    size(1000, 800)
def draw():
    global screen_2
    global screen_1
    global screen_3
    if screen_1 == True:
        background(255)
    fill(0)
    rect(0, 0, 500, 800)
    fill(255, 255, 255)
    rect(100, 400, 300, 100)
    fill(0)
    rect(600, 400, 300, 100)
    fill(255, 0, 0)
    textSize(32)
    text("P1:", 125, 460)
    fill(0, 0, 255)
    textSize(32)
    text("P2:", 620, 460)
    fill(51, 255, 255)
    textSize(200)
    text("jeoPARTY",30 , 200)
    rect(start_loc.x, start_loc.y, start_size.x, start_size.y)
    textSize(50)
    fill(0)
    text("START", 410, 675)
        
    if screen_2 == True:
        background(255)
        fill(0)
        textSize(100)
        text("Select a level:", 25, 100)
        rect(25, 200, 400, 50)
        textSize(32)
        fill(255)
        text("Easy", 175, 230)
        fill(0)
        rect(25, 300, 400, 50)
        textSize(32)
        fill(255)
        text("Moderate", 175, 330)
        fill(0)
        rect(25, 400, 400, 50)
        textSize(32)
        fill(255)
        text("Hard", 175, 430)   
    if screen_3 == True:
        background(255)
        fill(0)
        textSize(32)
        text("What is one plus one?", 50, 100)
        text("a) 7", 50, 200)
        text("b) 2", 50, 300)
        text("c) 6", 50, 400)
    


def mousePressed():
    global screen_2
    global screen_1
    global screen_3
    if mouseX >= start_loc.x and mouseX <= start_loc.x + start_size.x:
        if mouseY >= start_loc.y and mouseY <= start_loc.y + start_size.y:
            screen_2 = True
            screen_1 = False
            screen_3 = False


    if mouseX >= easy_loc.x and mouseX <= easy_loc.x + easy_size.x:
        if mouseY >= easy_loc.y and mouseY <= easy_loc.y + easy_size.y:
            screen_1 = False
            screen_2 = False
            screen_3 = True







