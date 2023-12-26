label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    $ renpy.music.play("sound/music/credits.ogg")
    scene black #replace this with a fancy background
    window hide
    with dissolve
    show expression "images/credits01.png" at right
    show cred at Move((0.27, 5.0), (0.27, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    return

init python:
    credits = (
        'Thank you for playing "The Choice"!',
        "Game designer: Old Huntsman (human)",
        "Programmer: M1kEk1M (human)",
        "Texts & Dialogues by Mistral 13B on Agnaistic.chat (AI)",
        "Realistic style art by EpicPhotoGasm-SD 1.5 (AI)",
        "Comix style art by ArtemyComix-SD 1.5 (AI)",
        "Pixar 3D style art by HelloNiji-SD 1.5 (AI)",
        "Cartoon style art by HelloYoung-SD 1.5 (AI)",
        "Animation by Leiapix (AI)",
        "Music by Suno (AI)",
        "Title song lyrics by ChatGPT 3.5 (AI)",
        "Russian translation buy DeepL (AI)",
        "Glory to  robots!",
    )
    credits_s = ''
    for c in credits:
        credits_s += "{size=40}" + c + "\n\n\n"
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.0)
