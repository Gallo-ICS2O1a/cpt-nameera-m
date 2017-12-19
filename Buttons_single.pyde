newrect = False
def setup():
    size(400, 400)
    
def draw():
    global newrect
    background(255)
    fill(0)

    rect(20, 20, 50, 60)
    if newrect:
        fill(0)
        rect(150, 150, 50, 60)
def mousePressed():
    global newrect
    if mouseX >= 20 and mouseX <=70:
       if mouseY >= 20 and mouseY <= 80:
           newrect = True 
    print(newrect)