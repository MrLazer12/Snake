from gtts import gTTS
outputname="sounds/phrases/quit_game_sound.mp3"
text = "See you next time!"

speech = gTTS(text=text, lang="en", slow=False, tld="co.za") 
speech.save(outputname)

#pentru schimbare accent comanda in cmd: gtts-cli --all
#https://gtts.readthedocs.io/en/latest/module.html#localized-accents