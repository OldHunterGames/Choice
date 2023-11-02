define k = Character("Kristen")
define pc = Character("Me")

define doneOral = False
define doneVaginal = False
define doneAnal = False

init -10 python:
    import math
    import pygame
    def clamp(input, min, max):
        return input < min and min or input > max and max or input

    def map_range(current, in_min, in_max, out_min, out_max):
        mapped = (current - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

        return clamp(mapped, out_min, out_max)

    class TrackCursor(renpy.Displayable):

        def __init__(self, child, width, height, **kwargs):

            super(TrackCursor, self).__init__()

            self.child = renpy.displayable(child)
            self.x = 0
            self.y = 0
            self.actual_x = 0
            self.actual_y = 0
            self.actual_width = width
            self.actual_height = height

            self.last_st = 0

            self.x_diff = abs(config.screen_width - width)
            self.y_diff = abs(config.screen_height - height)
            print(self.y_diff, "self.y_diff")



        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)
            minimum_speed = 0.5
            maximum_speed = 3
            speed = 1 + minimum_speed
            mouse_distance_x = min(maximum_speed, max(minimum_speed, (self.x - self.actual_x)))
            mouse_distance_y = (self.y - self.actual_y)
            if self.x is not None:
                st_change = st - self.last_st

                self.last_st = st
                self.actual_x = math.floor(self.actual_x + ((self.x - self.actual_x) * speed * (st_change )))
                self.actual_y = math.floor(self.actual_y + ((self.y - self.actual_y) * speed * (st_change)))


                if mouse_distance_y <= minimum_speed:
                    mouse_distance_y = minimum_speed
                elif mouse_distance_y >= maximum_speed:
                    mouse_distance_y = maximum_speed

                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()

                render_x = map_range(self.actual_x, 0, config.screen_width, 0, self.x_diff)
                render_y = map_range(self.actual_y, 0, config.screen_height, 0, self.y_diff)
                print('self.y', self.y)
                print('render_y', render_y)
                rv.blit(cr, (render_x, render_y))



            renpy.redraw(self, 0)
            return rv

        def event(self, ev, x, y, st):
            hover = ev.type == pygame.MOUSEMOTION
            click = ev.type == pygame.MOUSEBUTTONDOWN
            mousefocus = pygame.mouse.get_focused()
            if hover:

                if (x != self.x) or (y != self.y) or click:
                    self.x = -x
                    self.y = -y

# The game starts here.
image kek = TrackCursor(Image(f"images/{persistent.graphic_mode}/checkout dance.png"), 1980, 2970)
image anal = "[persistent.graphic_mode]/full anal.png"
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bar
    show kek
    "Test"
    hide kek
    show anal

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

