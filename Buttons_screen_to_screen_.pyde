
oldrect = True
newrect = False
def setup():
    size(400, 400)
    
def draw():
    global newrect
    global oldrect
    background(255)
    fill(0)
    if oldrect == True:
        rect(20, 20, 50, 60)
    if newrect:
        fill(0)
        rect(150, 150, 50, 60)
def mousePressed():
    global newrect, oldrect
    if mouseX >= 20 and mouseX <=70:
       if mouseY >= 20 and mouseY <= 80:
           newrect = True 
           oldrect = False
