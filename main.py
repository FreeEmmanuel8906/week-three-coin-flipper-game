def on_button_pressed_a():
    if Math.random_boolean():
        basic.show_icon(IconNames.SKULL)
    else:
        basic.show_icon(IconNames.SQUARE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
