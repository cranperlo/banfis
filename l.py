while True:
    from turtle import*

    speed(0)
    penup()
    goto(-400, 250)
    pendown()
    a=input("Enter country name")

    if a == "India":
        color("orange")
        begin_fill()
        forward(800)
        right(90)
        forward(167)
        right(90)
        forward(800)
        end_fill()
        left(90)
        forward(167)

        color("green")
        begin_fill()
        forward(167)
        left(90)
        forward(800)
        left(90)
        forward(167)
        end_fill()
    
        penup()
        goto(70,0)
        pendown()
        color("navy")
        begin_fill()
        circle(70)
        end_fill()

        penup()
        goto(60, 0)
        pendown()
        color("white")
        begin_fill()
        circle(60)
        end_fill()

        penup()
        goto(-57, -8)
        pendown()
        color("navy")
        for i in range(4):
            begin_fill()
            circle(3)
            end_fill()
            penup()
            forward(15)
            right(15)
            pendown()
    
        penup()
        goto(20, 0)
        pendown()
        begin_fill()
        circle(20)
        end_fill()

        penup()
        goto(0, 0)
        pendown()
        pensize(2)
        for i in range(24):
            forward(60)
            back(60)
            left(15)
    
    elif a == "Japan":
        forward(800)
        right(90)
        forward(501)
        right(90)
        forward(800)
        right(90)
        forward(501)

        penup()
        color("red")
        begin_fill()
        goto(70,0)
        circle(70)
        end_fill()

    elif a=="Poland":
        color("white")
        begin_fill()
        forward(800)
        right(90)
        forward(250)
        right(90)
        forward(800)
        end_fill()
    
        color("red")
        begin_fill()
        forward(800)
        right(90)
        forward(250)
        right(90)
        forward(800)
        end_fill()

    else:
        break



    mainloop()