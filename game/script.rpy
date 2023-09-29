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

    show kristen dress happy
    with dissolve

    "We are dancing"

    #call screen viewport_screen

    "The song is over and we get back to a bar, to get two more shots"

    scene bg bar

    show kristen dress calm
    with dissolve

    k "Do you whant to continue in my place?"

    pc "Shure! Let's go"

    scene bg parking

    "I call the taxi"

    "We going to the Kristen place"

    scene bg room

    pc "It's a nice place"

    show kristen dress calm
    with dissolve    

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

    show kristen dress happy
    with dissolve    

    "We are kissing"

    k "Sit down, Anton. I'll dance for you"

    "Kristen starts to dance"

    show kristen lingerie happy
    with dissolve

    "Kristen takes off her dress"
    
    show kristen nude happy
    with dissolve

    "And then her bra underware"

    k "Sooo... do you enjoy the show?"

    pc "Come here and chek it yourself"

    "I'm taking my shirt off while Kristen comes closer, and gets down on her kennes. She unzips my pants"

    k "Oh... Looks like you really like it. Nice cook, by the way."

    jump sex_selector

    return

label sex_selector:

    scene bg room

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

    show full bj happy
    "Kristen blows my dick"
    jump sex_selector

    return

label sex:
    
    show full sex happy
    "I fuck her"
    jump sex_selector

    return

label anal:

    show full anal
    "I fuck her in the ass"
    jump sex_selector

    return

label cum_face:

    show full bj happy
    "My semen is all over her face"
    jump goodbye_kiss
    
    return

label cum_belly:

    show full sex happy
    "My semen is all over her belly"
    jump goodbye_kiss
    
    return

label cum_back:

    show full anal
    "My semen is all over her back"
    jump goodbye_kiss
    
    return

label goodbye_kiss:
    scene bg room
    show kristen nude happy
    with dissolve

    "I kissed her one more time and leave"

    "FIN"

    return

label rape: 
    
    pc "...rape you!"
    
    show kristen dress shoked
    with dissolve    

    "I grab my gun and point in on her"

    pc "Now, take of you fucking clothes, bitch!"

    k "Please don't shot me! I'll do anything you want..."

    "Kristen starts to unress"

    show kristen lingerie shoked
    with dissolve

    "She is unressing reluctantly"
    
    show kristen nude shoked
    with dissolve

    "And now she is standing nude and fearful in front of me"

    jump rape_selector

    return 

label rape_selector:
    scene bg room

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

    show full bj tears
    "I shove my dick in a slut's mouth"
    jump rape_selector

    return

label forced_sex:

    show full sex tears
    "I fuck her hard"
    jump rape_selector

    return

label anal_rape:

    show full anal
    "I fuck her in the ass forcefully"
    jump rape_selector

    return

label cum_throat:

    show full bj tears
    "My semen is all over her face"
    jump flee
    
    return

label impregnate:

    show full sex tears
    "I'm cumming in her womb"
    jump flee
    
    return

label cum_ass:

    show full anal
    "I cum deep in her asshole"
    jump flee
    
    return

label flee:
    scene bg room

    "She lying in a puddle of my semen. Time to get out!"

    "FIN"

    return

