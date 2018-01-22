screen = 'screen1'
start_loc = PVector(250, 600)
start_size = PVector(500, 100)
screen_number = 1
b_loc = PVector(50, 272)
b_size = PVector(35, 45)
a_loc = PVector(50, 172)
a_size = PVector(35, 45)
c_loc = PVector(50, 372)
c_size = PVector(35, 45)
back_loc = PVector(0, 0)
back_size = PVector(260, 100)


def setup():
    size(1000, 700)


def draw():

    global correct_screen
    global incorrect_screen
    global screen
    global screen1
    global screen_number
    global screen2
    global screen3
    global screen4
    global screen5

    if screen == 'screen1':
        background(0)
        fill(0)
        fill(51, 255, 255)
        rect(0, 0, 500, 800)
        fill(0)
        fill(0)
        rect(start_loc.x, start_loc.y, start_size.x, start_size.y)
        fill(51, 255, 255)
        fill(255)
        textSize(32)
        text("To win you must answer all the questions right, no cheating!!",
             30, 400)
        textSize(200)
        text("jeoPARTY", 30, 200)
        textSize(50)
        fill(51, 255, 255)
        text("START", 410, 675)

    if screen == 'screen2':
        font = loadFont("LucidaSans-TypewriterBold-48.vlw")
        textFont(font, 32)
        background(255, 0, 0)
        fill(255)
        # rect(50, 172, 35, 45)
        # rect(50, 272, 35, 45)
        # rect(50, 372, 35, 45)
        fill(0)
        textSize(20)
        text("Select the LETTER of the answer you think is correct", 50, 50)
        textSize(45)
        text("What is one plus one?", 50, 100)
        text("a) 7", 50, 200)
        text("b) 2", 50, 300)
        text("c) 6", 50, 400)

    if screen == 'screen3':
        background(255, 57, 57)
        fill(0)
        textSize(45)
        text("What is the capital city of England?", 23, 100)
        text("a) London", 50, 200)
        text("b) Manchester", 50, 300)
        text("c) Ottawa", 50, 400)

    if screen == 'screen4':
        background(255, 114, 114)
        fill(0)
        textSize(45)
        text("What is the sum of 2225 and 3476?", 23, 100)
        text("a) 5700", 50, 200)
        text("b) 5701", 50, 300)
        text("c) 5702", 50, 400)

    if screen == 'screen5':
        background(255, 102, 102)
        fill(0)
        textSize(45)
        text("What is the population of Canada?", 50, 100)
        text("a) 30 million", 50, 200)
        text("b) 40 million", 50, 300)
        text("c) 36 million", 50, 400)

    if screen == 'screen6':
        background(199, 255, 199)
        fill(0)
        textSize(40)
        text("What city has the largest population?", 10, 100)
        text("a) Toronto", 50, 200)
        text("b) London", 50, 300)
        text("c) Tokyo", 50, 400)

    if screen == 'screen7':
        background(171, 255, 171)
        fill(0)
        textSize(35)
        text("What is the most spoken language in the world?", 10, 100)
        text("a) Chinese", 50, 200)
        text("b) English", 50, 300)
        text("c) Russian", 50, 400)

    if screen == 'screen8':
        background(142, 255, 142)
        fill(0)
        textSize(40)
        text("What is the longest river in the world?", 10, 100)
        text("a) Nile", 50, 200)
        text("b) Amazon", 50, 300)
        text("c) Mississippi", 50, 400)

    if screen == 'screen9':
        background(114, 255, 114)
        fill(0)
        textSize(45)
        text("Which planet has the most moons?", 50, 100)
        text("a) Jupiter", 50, 200)
        text("b) Saturn", 50, 300)
        text("c) Earth", 50, 400)

    if screen == 'screen10':
        background(85, 255, 85)
        fill(0)
        textSize(35)
        text("What does PM in the context of time stand for?", 20, 100)
        text("a) Post Malone", 50, 200)
        text("b) Past Meridiem", 50, 300)
        text("c) Post Meridiem", 50, 400)

    if screen == 'screen11':
        font2 = loadFont("BodoniSvtyTwoOSITCTT-BookIt-48.vlw")
        textFont(font2, 32)
        background(102, 255, 102)
        fill(0)
        textSize(40)
        text("CONGRATS YOU BEAT THE IMPOSSIBLE jeoPARTY GAME!", 0, 300)

    if screen == 'screen12':
        font3 = loadFont("Charter-BlackItalic-48.vlw")
        textFont(font3, 50)
        background(255, 0, 0)
        fill(0)
        textSize(72)
        text("Sorry please try again.", 100, 300)
        fill(0)
        rect(back_loc.x, back_loc.y, back_size.x, back_size.y)
        textSize(23)
        fill(255)
        text("BACK TO MAIN MENU", 0, 50)


def mousePressed():
    global screen
    global screen_number
    global screen1
    global screen2
    global screen3
    global screen4
    global screen5
    global screen6
    global screen7
    global screen8
    global screen9
    global screen10
    global screen11
    global screen12

    if screen == 'screen1':
        if mouseX >= start_loc.x and mouseX <= start_loc.x + start_size.x:
            if mouseY >= start_loc.y and mouseY <= start_loc.y + start_size.y:
                screen_number += 1

    if screen == 'screen2':
        if mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x:
            if mouseY >= b_loc.y and mouseY <= b_loc.y + b_size.y:
                screen_number += 1
            elif mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x \
                or mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x \
                or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y \
                    or mouseY >= c_loc.y and mouseY <= c_loc.y + c_size.y:
                    screen_number += 10

    if screen == 'screen3':
        if mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x:
            if mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y:
                screen_number += 1
            elif mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x \
                    or mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x \
                    or mouseY >= b_loc.y and mouseY <= b_loc.y + b_size.y \
                    or mouseY >= c_loc.y and mouseY <= c_loc.y + c_size.y:
                screen_number += 9

    if screen == 'screen4':
        if mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x:
            if mouseY >= b_loc.y and mouseY <= b_loc.y + b_size.y:
                screen_number += 1
            elif mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x \
                or mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x \
                or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y \
                    or mouseY >= c_loc.y and mouseY <= c_loc.y + c_size.y:
                        screen_number += 8

    if screen == 'screen5':
        if mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x:
            if mouseY >= c_loc.y and mouseY <= c_loc.y + c_size.y:
                screen_number += 1
            elif mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x \
                or mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x \
                or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y \
                    or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y:
                        screen_number += 7

    if screen == 'screen6':
        if mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x:
            if mouseY >= c_loc.y and mouseY <= c_loc.y + c_size.y:
                screen_number += 1
            elif mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x \
                or mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x \
                or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y \
                    or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y:
                        screen_number += 6

    if screen == 'screen7':
        if mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x:
            if mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y:
                screen_number += 1
            elif mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x \
                or mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x \
                or mouseY >= b_loc.y and mouseY <= b_loc.y + b_size.y \
                    or mouseY >= c_loc.y and mouseY <= c_loc.y + c_size.y:
                        screen_number += 5

    if screen == 'screen8':
        if mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x:
            if mouseY >= b_loc.y and mouseY <= b_loc.y + b_size.y:
                screen_number += 1
            elif mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x \
                or mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x \
                or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y \
                    or mouseY >= c_loc.y and mouseY <= c_loc.y + c_size.y:
                        screen_number += 4

    if screen == 'screen9':
        if mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x:
            if mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y:
                screen_number += 1
            elif mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x \
                or mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x \
                or mouseY >= b_loc.y and mouseY <= b_loc.y + b_size.y \
                    or mouseY >= c_loc.y and mouseY <= c_loc.y + c_size.y:
                        screen_number += 3

    if screen == 'screen10':
        if mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x:
            if mouseY >= c_loc.y and mouseY <= c_loc.y + c_size.y:
                screen_number += 1
            elif mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x \
                or mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x \
                or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y \
                    or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y:
                        screen_number += 2

    if screen == 'screen11':
        if mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x:
            if mouseY >= c_loc.y and mouseY <= c_loc.y + c_size.y:
                screen_number += 1
            elif mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x \
                or mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x \
                or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y \
                    or mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y:
                        screen_number += 1

    if screen == 'screen12':
        if mouseX >= back_loc.x and mouseX <= back_loc.x + back_size.x:
            if mouseY >= back_loc.y and mouseY <= back_loc.y + back_size.y:
                screen_number -= 11

    screen = 'screen'
    screen = screen + str(screen_number)
