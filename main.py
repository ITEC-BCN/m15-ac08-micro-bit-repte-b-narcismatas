def on_button_pressed_a():
    music.play(music.string_playable("G F G A - F E D ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play(music.string_playable("E A F E D C G E ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    music.change_tempo_by(input.rotation(Rotation.PITCH))
basic.forever(on_forever)
