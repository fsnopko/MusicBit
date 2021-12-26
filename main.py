def on_button_pressed_a():
    basic.show_leds("""
        # . # . #
                . # # # .
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.pause(1000)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.clear_screen()
    basic.show_string("Netras ma!!!")
    basic.show_icon(IconNames.CONFUSED)
    for index in range(6):
        basic.show_leds("""
            . . . . #
                        . . . . #
                        . . . . #
                        . . . . #
                        . . . . #
        """)
        basic.show_leds("""
            . . . # #
                        . . . # #
                        . . . # #
                        . . . # #
                        . . . # #
        """)
        basic.show_leds("""
            . . # # #
                        . . # # #
                        . . # # #
                        . . # # #
                        . . # # #
        """)
        basic.show_leds("""
            . # # # #
                        . # # # #
                        . # # # #
                        . # # # #
                        . # # # #
        """)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        basic.show_leds("""
            # # # # .
                        # # # # .
                        # # # # .
                        # # # # #
                        # # # # .
        """)
        basic.show_leds("""
            # # # . .
                        # # # . .
                        # # # . .
                        # # # # .
                        # # # . #
        """)
        basic.show_leds("""
            # # . . .
                        # # . # .
                        # # . . .
                        # # # . .
                        # # . # #
        """)
        basic.show_leds("""
            # . . . .
                        # . # . #
                        # . . . .
                        # # . . .
                        # . # # #
        """)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
        """)
        basic.show_leds("""
            . . . . .
                        # . # . .
                        . . . . .
                        . . . # .
                        # # # . .
        """)
        basic.show_leds("""
            . . . . .
                        . # . . .
                        . . . . .
                        . . # . .
                        # # . . .
        """)
        basic.show_leds("""
            . . . . .
                        # . . . .
                        . . . . .
                        . # . . .
                        # . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
                        . . . . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_icon(IconNames.HEART)
        basic.show_string("WOW")
    basic.show_icon(IconNames.YES)
    basic.show_icon(IconNames.HAPPY)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_string("Databaza on.")
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.SMALL_HEART)
    basic.show_icon(IconNames.YES)
    basic.show_icon(IconNames.NO)
    basic.show_icon(IconNames.HAPPY)
    basic.show_icon(IconNames.SAD)
    basic.show_icon(IconNames.CONFUSED)
    basic.show_icon(IconNames.ANGRY)
    basic.show_icon(IconNames.ASLEEP)
    basic.show_icon(IconNames.SURPRISED)
    basic.show_icon(IconNames.SILLY)
    basic.show_icon(IconNames.FABULOUS)
    basic.show_icon(IconNames.MEH)
    basic.show_icon(IconNames.TSHIRT)
    basic.show_icon(IconNames.ROLLERSKATE)
    basic.show_icon(IconNames.DUCK)
    basic.show_icon(IconNames.HOUSE)
    basic.show_icon(IconNames.TORTOISE)
    basic.show_icon(IconNames.BUTTERFLY)
    basic.show_icon(IconNames.STICK_FIGURE)
    basic.show_icon(IconNames.GHOST)
    basic.show_icon(IconNames.SWORD)
    basic.show_icon(IconNames.GIRAFFE)
    basic.show_icon(IconNames.SKULL)
    basic.show_icon(IconNames.UMBRELLA)
    basic.show_icon(IconNames.SNAKE)
    basic.show_icon(IconNames.RABBIT)
    basic.show_icon(IconNames.COW)
    basic.show_icon(IconNames.QUARTER_NOTE)
    basic.show_icon(IconNames.EIGTH_NOTE)
    basic.show_icon(IconNames.PITCHFORK)
    basic.show_icon(IconNames.TARGET)
    basic.show_icon(IconNames.TRIANGLE)
    basic.show_icon(IconNames.LEFT_TRIANGLE)
    basic.show_icon(IconNames.CHESSBOARD)
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_icon(IconNames.SCISSORS)
    basic.show_string("End")
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
                . # # # .
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    basic.clear_screen()
    basic.show_string("Pustim pesnicku.")
    basic.pause(1000)
    basic.show_icon(IconNames.EIGTH_NOTE)
    music.set_built_in_speaker_enabled(True)
    soundExpression.giggle.play()
    music.play_melody("C5 G A G A F D G ", 303)
    music.play_melody("C5 G A G A F D G ", 303)
    music.play_melody("A G F A G F F B ", 303)
    music.play_melody("A G F A G F F B ", 303)
    music.play_melody("A G F A G F F B ", 303)
    soundExpression.giggle.play()
    basic.show_string("Koniec.")
    basic.show_icon(IconNames.HAPPY)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

music.set_volume(255)
basic.show_string("Ahoj!")
basic.show_leds("""
    . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
""")
basic.pause(1000)
basic.show_leds("""
    . # # # .
        # . . . #
        # # . # #
        # . . . #
        . # # # .
""")
basic.pause(1000)
basic.show_leds("""
    . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
""")
basic.pause(1000)
basic.show_leds("""
    . # # # .
        # . . . #
        # # # # #
        # . . . #
        # . . . #
""")
basic.pause(1000)
basic.show_leds("""
    . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
""")
basic.pause(1000)
basic.show_leds("""
    # . . . .
        # . . . .
        # # # . .
        # . . # .
        # # # . .
""")
basic.pause(1000)
basic.show_leds("""
    . . # . .
        . # . # .
        # # # # #
        . # . # .
        . . # . .
""")
basic.show_icon(IconNames.HAPPY)
basic.pause(5000)
basic.clear_screen()
basic.show_string("Music:Bit by Filip Snopko")
basic.show_string("Serial nm.:" + str(control.device_serial_number()))
basic.show_string("Name:" + control.device_name())
basic.show_icon(IconNames.HAPPY)