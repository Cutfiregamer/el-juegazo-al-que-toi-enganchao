def on_gesture_tilt_right():
    global ax, ay, x
    if tiempo < 60:
        ax = x
        ay = y
        x += 1
        if x == 5:
            x = 0
            ax = 4
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_tilt_left():
    global ax, ay, x
    if tiempo < 60:
        ax = x
        ay = y
        x += -1
        if x == -1:
            x = 4
            ax = 0
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_logo_down():
    global ax, ay, y
    if tiempo < 60:
        ax = x
        ay = y
        y += -1
        if y == -1:
            y = 4
            ay = 0
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_gesture_logo_up():
    global ax, ay, y
    if tiempo < 60:
        ax = x
        ay = y
        y += 1
        if y == 5:
            y = 0
            ay = 4
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

puntos = 0
y = 0
ay = 0
x = 0
ax = 0
tiempo = 0
Obj_x = randint(0, 4)
Obj_y = randint(0, 4)
led.plot_brightness(Obj_x, Obj_y, 37)

def on_every_interval():
    global tiempo
    tiempo += 1
loops.every_interval(1000, on_every_interval)

def on_forever():
    global puntos, Obj_x, Obj_y
    if tiempo < 60:
        led.unplot(ax, ay)
        led.plot(x, y)
        if x == Obj_x and y == Obj_y:
            music.play(music.tone_playable(932, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            led.unplot(Obj_x, Obj_y)
            puntos += 1
            Obj_x = randint(0, 4)
            Obj_y = randint(0, 4)
            led.plot_brightness(Obj_x, Obj_y, 37)
            if x == Obj_x and y == Obj_y:
                Obj_x = randint(0, 4)
                Obj_y = randint(0, 4)
    else:
        music.play(music.tone_playable(175, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        led.unplot(Obj_x, Obj_y)
        led.unplot(x, y)
        basic.show_number(puntos)
basic.forever(on_forever)
