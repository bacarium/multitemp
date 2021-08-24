def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(input.temperature() * 9 / 5 + 32)
input.on_button_pressed(Button.B, on_button_pressed_b)
