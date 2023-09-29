define k = Character("Kristen")
define pc = Character("Me")

define doneOral = False
define doneVaginal = False
define doneAnal = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bar

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    "I'm in a night club looking for a date for a night"

    "I found a girl"

    pc "Hi there, I'm Anton"

    show kristen dress calm
    with dissolve

    "She is cheking me up"

    show kristen dress happy
    with dissolve

    k "Hello. I'm Kristen"

    "I bought her a drink and we have a chat for some time"

    k "Let's dance!"
   
    scene bg dancefloor

    show kristen dress shoked
    with dissolve

    "We are dancing"

    call screen viewport_screen

    "The song is over and we get back to a bar, to get two more shots"

    scene bg bar

    k "Do you whant to continue in my place?"

    pc "Shure! Let's go"

    scene bg parking

    "I call the taxi"

    "We going to the Kristen place"

    scene bg room

    pc "It's a nice place"

    k "Thanks!"

    pc "What we will do next?"

    k "You tell me! Take a choice, macho-man."

    pc "Actually I'm going to..."    

    menu:

        "Make love":
            jump make_love

        "Rape her":
            jump rape

    return

label make_love:

    pc "...kiss you!"

    "We are kissing"

    k "Sit down, Anton. I'll dance for you"

    "Kristen start ro dance"

    "Kristen takes off her dress"

    "And then her bra"

    "And finaly her painties"

    k "Sooo... do you enjoy the show?"

    pc "Come here and chek it yourself"

    "I'm taking my shirt off while Kristen comes closer, and gets down on her kennes. She unzips my pants"

    k "Oh... Looks like you really like it. Nice cook, by the way."

    jump sex_selector

    return

label sex_selector:
    menu:
        "Blowjob":
            if doneOral:
                jump cum_face
            $ doneOral = True      
            jump blowjob

        "Sex":
            if doneVaginal:
                jump cum_belly
            $ doneVaginal = True
            jump sex
        "Anal":
            if doneAnal:
                jump cum_back
            $ doneAnal = True
            jump anal
    return 

label blowjob:
    "Kristen blows my dick"
    jump sex_selector

    return

label sex:
    "I fuck her"
    jump sex_selector

    return

label anal:
    "I fuck her in the ass"
    jump sex_selector

    return

label cum_face:

    "My semen is all over her face"
    jump goodbye_kiss
    
    return

label cum_belly:

    "My semen is all over her belly"
    jump goodbye_kiss
    
    return

label cum_back:

    "My semen is all over her back"
    jump goodbye_kiss
    
    return

label goodbye_kiss:
    "I kissed her one more time and leave"

    "FIN"

    return

label rape: 

    pc "...rape you!"
    jump rape_selector

    return 

label rape_selector:
    menu:
        "Fuck her throat":
            if doneOral:
                jump cum_throat
            $ doneOral = True      
            jump throatfuck

        "Forced sex":
            if doneVaginal:
                jump impregnate
            $ doneVaginal = True
            jump forced_sex
        "Anal rape":
            if doneAnal:
                jump cum_ass
            $ doneAnal = True
            jump anal_rape
    return 

label throatfuck:
    "Kristen blows my dick"
    jump sex_selector

    return

label forced_sex:
    "I fuck her"
    jump sex_selector

    return

label anal_rape:
    "I fuck her in the ass"
    jump sex_selector

    return

label cum_throat:

    "My semen is all over her face"
    jump flee
    
    return

label impregnate:

    "My semen is all over her belly"
    jump flee
    
    return

label cum_ass:

    "My semen is all over her back"
    jump flee
    
    return

label flee:
    "She lying in a puddle of my semen. Time to get out!"

    "FIN"

    return

