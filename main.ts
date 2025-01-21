input.onButtonPressed(Button.A, function () {
    for (let i = 0; i <= 9; i++) {
        basic.showNumber(9 - i)
        basic.pause(100)
    }
})
input.onButtonPressed(Button.B, function () {
    music.play(music.stringPlayable("C5 G B A F A C5 B ", 120), music.PlaybackMode.LoopingInBackground)
})
music.setVolume(1000)
basic.forever(function () {
	
})
