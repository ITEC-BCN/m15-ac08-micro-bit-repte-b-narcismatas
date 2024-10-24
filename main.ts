input.onButtonPressed(Button.A, function () {
    music.play(music.stringPlayable("G F G A - F E D ", 120), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    music.play(music.stringPlayable("E A F E D C G E ", 120), music.PlaybackMode.UntilDone)
})
basic.forever(function () {
    music.changeTempoBy(input.rotation(Rotation.Pitch))
})
