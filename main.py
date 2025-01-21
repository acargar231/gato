
def on_forever():
    pass
def on_button_pressed_a():
    for i in range(10):
            basic.show_number(9-i)
            basic.pause(100)

input.on_button_pressed(Button.A, on_button_pressed_a)
music.set_volume(1000)
def on_button_pressed_b():

    music.play(music.string_playable("C D E ", 120), music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.forever(on_forever)
