input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # . # . #
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.pause(1000)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    basic.showString("Netras ma!!!")
    basic.showIcon(IconNames.Confused)
    for (let index = 0; index < 6; index++) {
        basic.showLeds(`
            . . . . #
            . . . . #
            . . . . #
            . . . . #
            . . . . #
            `)
        basic.showLeds(`
            . . . # #
            . . . # #
            . . . # #
            . . . # #
            . . . # #
            `)
        basic.showLeds(`
            . . # # #
            . . # # #
            . . # # #
            . . # # #
            . . # # #
            `)
        basic.showLeds(`
            . # # # #
            . # # # #
            . # # # #
            . # # # #
            . # # # #
            `)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.showLeds(`
            # # # # .
            # # # # .
            # # # # .
            # # # # #
            # # # # .
            `)
        basic.showLeds(`
            # # # . .
            # # # . .
            # # # . .
            # # # # .
            # # # . #
            `)
        basic.showLeds(`
            # # . . .
            # # . # .
            # # . . .
            # # # . .
            # # . # #
            `)
        basic.showLeds(`
            # . . . .
            # . # . #
            # . . . .
            # # . . .
            # . # # #
            `)
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
        basic.showLeds(`
            . . . . .
            # . # . .
            . . . . .
            . . . # .
            # # # . .
            `)
        basic.showLeds(`
            . . . . .
            . # . . .
            . . . . .
            . . # . .
            # # . . .
            `)
        basic.showLeds(`
            . . . . .
            # . . . .
            . . . . .
            . # . . .
            # . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showIcon(IconNames.Heart)
        basic.showString("WOW")
    }
    basic.showIcon(IconNames.Yes)
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Databaza on.")
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.SmallHeart)
    basic.showIcon(IconNames.Yes)
    basic.showIcon(IconNames.No)
    basic.showIcon(IconNames.Happy)
    basic.showIcon(IconNames.Sad)
    basic.showIcon(IconNames.Confused)
    basic.showIcon(IconNames.Angry)
    basic.showIcon(IconNames.Asleep)
    basic.showIcon(IconNames.Surprised)
    basic.showIcon(IconNames.Silly)
    basic.showIcon(IconNames.Fabulous)
    basic.showIcon(IconNames.Meh)
    basic.showIcon(IconNames.TShirt)
    basic.showIcon(IconNames.Rollerskate)
    basic.showIcon(IconNames.Duck)
    basic.showIcon(IconNames.House)
    basic.showIcon(IconNames.Tortoise)
    basic.showIcon(IconNames.Butterfly)
    basic.showIcon(IconNames.StickFigure)
    basic.showIcon(IconNames.Ghost)
    basic.showIcon(IconNames.Sword)
    basic.showIcon(IconNames.Giraffe)
    basic.showIcon(IconNames.Skull)
    basic.showIcon(IconNames.Umbrella)
    basic.showIcon(IconNames.Snake)
    basic.showIcon(IconNames.Rabbit)
    basic.showIcon(IconNames.Cow)
    basic.showIcon(IconNames.QuarterNote)
    basic.showIcon(IconNames.EigthNote)
    basic.showIcon(IconNames.Pitchfork)
    basic.showIcon(IconNames.Target)
    basic.showIcon(IconNames.Triangle)
    basic.showIcon(IconNames.LeftTriangle)
    basic.showIcon(IconNames.Chessboard)
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.Square)
    basic.showIcon(IconNames.SmallSquare)
    basic.showIcon(IconNames.Scissors)
    basic.showString("End")
    basic.showIcon(IconNames.Happy)
})
input.onSound(DetectedSound.Loud, function () {
    basic.clearScreen()
    basic.showString("Music:Bit by Filip Snopko")
    basic.showString("Serial nm.:" + control.deviceSerialNumber())
    basic.showString("Name:" + control.deviceName())
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        `)
    basic.clearScreen()
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.clearScreen()
    basic.showString("Pustim pesnicku.")
    basic.pause(1000)
    basic.showIcon(IconNames.EigthNote)
    music.setBuiltInSpeakerEnabled(true)
    soundExpression.giggle.play()
    music.playMelody("C5 G A G A F D G ", 303)
    music.playMelody("C5 G A G A F D G ", 303)
    music.playMelody("A G F A G F F B ", 303)
    music.playMelody("A G F A G F F B ", 303)
    music.playMelody("A G F A G F F B ", 303)
    soundExpression.giggle.play()
    basic.showString("Koniec.")
    basic.showIcon(IconNames.Happy)
})
input.setSoundThreshold(SoundThreshold.Loud, 150)
music.setVolume(255)
basic.showString("Ahoj!")
basic.showLeds(`
    . . # . .
    . # # # .
    # . # . #
    . . # . .
    . . # . .
    `)
basic.pause(1000)
basic.showLeds(`
    . # # # .
    # . . . #
    # # . # #
    # . . . #
    . # # # .
    `)
basic.pause(1000)
basic.showLeds(`
    . . # . .
    . # . . .
    # # # # #
    . # . . .
    . . # . .
    `)
basic.pause(1000)
basic.showLeds(`
    . # # # .
    # . . . #
    # # # # #
    # . . . #
    # . . . #
    `)
basic.pause(1000)
basic.showLeds(`
    . . # . .
    . . . # .
    # # # # #
    . . . # .
    . . # . .
    `)
basic.pause(1000)
basic.showLeds(`
    # . . . .
    # . . . .
    # # # . .
    # . . # .
    # # # . .
    `)
basic.pause(1000)
basic.showLeds(`
    . . # . .
    . # . # .
    # # # # #
    . # . # .
    . . # . .
    `)
basic.pause(1000)
basic.showIcon(IconNames.Happy)
