input.onGesture(Gesture.TiltRight, function () {
    if (tiempo < 60) {
        ax = x
        ay = y
        x += 1
        if (x == 5) {
            x = 0
            ax = 4
        }
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    if (tiempo < 60) {
        ax = x
        ay = y
        x += -1
        if (x == -1) {
            x = 4
            ax = 0
        }
    }
})
input.onGesture(Gesture.LogoDown, function () {
    if (tiempo < 60) {
        ax = x
        ay = y
        y += -1
        if (y == -1) {
            y = 4
            ay = 0
        }
    }
})
input.onGesture(Gesture.LogoUp, function () {
    if (tiempo < 60) {
        ax = x
        ay = y
        y += 1
        if (y == 5) {
            y = 0
            ay = 4
        }
    }
})
let puntos = 0
let y = 0
let ay = 0
let x = 0
let ax = 0
let tiempo = 0
let Obj_x = randint(0, 4)
let Obj_y = randint(0, 4)
loops.everyInterval(1000, function () {
    tiempo += 1
})
basic.forever(function () {
    led.plotBrightness(Obj_x, Obj_y, 37)
    if (tiempo < 60) {
        led.unplot(ax, ay)
        led.plot(x, y)
        if (x == Obj_x && y == Obj_y) {
            music.play(music.tonePlayable(932, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            led.unplot(Obj_x, Obj_y)
            puntos += 1
            Obj_x = randint(0, 4)
            Obj_y = randint(0, 4)
            while (x == Obj_x && y == Obj_y) {
                Obj_y = randint(0, 4)
                Obj_x = randint(0, 4)
            }
            led.plotBrightness(Obj_x, Obj_y, 37)
            if (x == Obj_x && y == Obj_y) {
                Obj_x = randint(0, 4)
                Obj_y = randint(0, 4)
            }
        }
    } else {
        music.play(music.tonePlayable(175, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        led.unplot(Obj_x, Obj_y)
        led.unplot(x, y)
        basic.showNumber(puntos)
    }
})
