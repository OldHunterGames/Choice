label credits:
    $ credits_speed = 40 #scrolling speed in seconds
    $ renpy.music.play("sound/music/credits.ogg")
    scene black #replace this with a fancy background
    window hide
    with dissolve
    show expression "images/credits01.png" at right
    #show cred at Move((0.27, 4.0), (0.27, 0.5), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show cred at Move((0.27, 3.5), (0.27, 0.5), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    $ renpy.pause(credits_speed * 100, hard=True)
    return

init python:
    credits = (
        __('Thank you for playing "The Choice"!'),
        __("Game designer: Old Huntsman (human)"),
        __("Programmer: M1kEk1M (human)"),
        __("Texts & Dialogues by Mistral 13B on Agnaistic.chat (AI)"),
        __("Realistic style art by EpicPhotoGasm-SD 1.5 (AI)"),
        __("Comix style art by ArtemyComix-SD 1.5 (AI)"),
        __("Pixar 3D style art by HelloNiji-SD 1.5 (AI)"),
        __("Cartoon style art by HelloYoung-SD 1.5 (AI)"),
        __("Animation by Leiapix (AI)"),
        __("Music by Suno (AI)"),
        __("Title song lyrics by ChatGPT 3.5 (AI)"),
        __("Russian translation by DeepL (AI)"),
        __("Glory to robots!"),
        "\n",
        "\n"
    )
    credits_s = ''
    for c in credits:
        credits_s += "{size=40}" + c + "\n\n\n"
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = VBox(
        Text(credits_s, text_align=0.0), 
        TextButton(__("Get more games by Old Huntsman"), action=OpenURL("https://peakd.com/adultgames/@oldhuntsman/the-choice-10x-actualization-page ")),
        TextButton(__("Make another Choice!"), action=MainMenu(confirm=False)),
    )
