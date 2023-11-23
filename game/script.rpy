define k = Character("Kristen", color='#ff4d4d')
define pc = Character("Anton", color='#00f')

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
# image kek = TrackCursor(Image(f"images/{persistent.graphic_mode}/checkout dance.png"), 1980, 2970)
# image anal = "[persistent.graphic_mode]/full anal.png"

image checkout dance = f"images/{persistent.graphic_mode}/checkout dance.png"
image checkout love = TrackCursor(Image(f"images/{persistent.graphic_mode}/checkout love.png"), 1980, 2970)
image checkout rape = TrackCursor(Image(f"images/{persistent.graphic_mode}/checkout rape.png"), 1980, 2970)

image bg bar = "[persistent.graphic_mode]/bg bar.png"
image bg dancefloor = "[persistent.graphic_mode]/bg dancefloor.png"
image bg parking = "[persistent.graphic_mode]/bg parking.png"
image bg room = "[persistent.graphic_mode]/bg room.png"
image full anal = "[persistent.graphic_mode]/full anal.png"
image full happy = "[persistent.graphic_mode]/full happy.png"
image full tears = "[persistent.graphic_mode]/full tears.png"
image full sex happy = "[persistent.graphic_mode]/full sex happy.png"
image full sex tears = "[persistent.graphic_mode]/full sex tears.png"
image kristen dress calm = "[persistent.graphic_mode]/kristen dress calm.png"
image kristen dress arrogant = "[persistent.graphic_mode]/kristen dress arrogant.png"
image kristen dress happy = "[persistent.graphic_mode]/kristen dress happy.png"
image kristen dress shoked = "[persistent.graphic_mode]/kristen dress shoked.png"
image kristen lingerie happy = "[persistent.graphic_mode]/kristen lingerie happy.png"
image kristen lingerie shoked = "[persistent.graphic_mode]/kristen lingerie shoked.png"
image kristen nude happy = "[persistent.graphic_mode]/kristen nude happy.png"
image kristen nude shoked = "[persistent.graphic_mode]/kristen nude shoked.png"

transform move_image:
    yalign 0.0
    linear 6.0 yalign 1.0
    linear 6.0 yalign 0.0
    linear 6.0 yalign 1.0
    linear 6.0 yalign 0.0

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bar
    # call screen my_screen
    window hide
    show checkout dance at move_image
    pause
    window auto
    scene bg bar
    # show kek onlayer master
    # hide kek

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

    window hide
    show checkout dance onlayer master
    pause
    window auto
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

    window hide
    show checkout love onlayer master
    pause
    window auto
    
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
    'I took a step closer to her, my eyes burning with desire as I ran my hands up and down her naked body.'
    pc "You're even more beautiful without your clothes on."
    'Kristen felt her cheeks flush at my compliment, her nipples hardening under my touch.' 
    'She looked up at me with shiny gray eyes, a small smile playing on her lips as she waited for my next move.' 
    'I pulled away slightly, giving Kristen a sly grin. I turned back around slowly, giving Kristen time to admire my ass which flexed enticingly beneath those tight jeans' 
    'With one swift movement, I removed them along with boxers revealing a thick cock already half-hard from anticipation alone'
    'Kristen gulped audibly when she saw how big it was; bigger than most men she had been with previously...'
    '... but not intimidating enough to make her hesitate anymore because now all thoughts were focused solely on pleasuring me'
    "As I turned back around, Kristen couldn't help but let out a soft moan of desire."
    "She had never seen such a formidable cock before - thick and veiny, pulsing with need for her mouth." 
    "Without another word, she dropped to her knees in front of me, taking my throbbing member into her hands and gently stroking it up and down the shaft as she leaned forward to take the head between her lips."
    'Her tongue flicked over the sensitive tip, tasting the pre-cum that had already gathered there.'
    'She closed her eyes tightly, savoring the taste as she began to bob her head up and down on my shaft, sucking deeper each time.'
    'Her slurping sounds echoed through the room while she worked her magic, using every ounce of skill she possessed to make this blowjob unforgettable.'
    pc "Oh, fuck... You're natural!"
    'I groaned loudly, my hands finding their way into her hair as I gripped tightly.'
    'My hips thrusting forward involuntarily against her skilled mouth. This was better than anything I could have imagined!'
    "As Kristen continued her blowjob, she could feel my cock growing harder and heavier in her mouth."
    'She took more of it each time, swallowing around him when he reached the back of her throat.'
    'Her eyes remained closed as she focused on pleasing me completely - tasting every inch, feeling my moans vibrate against her face.'
    pc "You're amazing, baby!" 
    'I groaned out between gasps for air.' 
    pc "I've never had a woman suck like this before." 
    "My words only fueled Kristen's determination to make this night one I would never forget!"
    "With renewed vigor, she increased the speed and pressure of her bobbing head."
    'Kristen felt a rush of pride hearing those words from me, but she knew there was more to come.'
    "She slowed her pace slightly, teasing me with gentle sucks and licks around the head before taking me back into her mouth again."
    'Her hands wandered down my thighs, tracing patterns on my skin as she waited for my next command.'
    
    jump sex_selector

    return

label sex:
    
    show full sex happy
    'I swiftly moved forward, pressing my lean yet ripped body against her soft curves.'
    'My hands glide over every inch of her supple skin, trailing up towards her firm large breasts that jiggle enticingly under my touch.'
    'With a deft movement, I couped one in each hand and gently squeeze them before lowering my head to capture a throbbing nipple between my lips.'
    'Kristen moans softly as she throws back her head onto the rack of their shoulders, allowing me greater access while arching her spine towards me for more contact.'
    'I suck greedily at it with practiced skill even as the other hand slides downward along her taut stomach and lower until I reach the wetness between her thighs...'
    '...finding it already eagerly awaiting me!'
    'As we neck deep into the intimate dance of desire and lust on the couch beneath us in silence broken only by our heavy breathing and occasional gasps of pleasure.'
    "I slowly push two fingers deep into tender folds soaking wet with desire - searching out Kristen's sweet spot effortlessly despite being unfamiliar territory thus far"
    'A shudder runs through both our bodies when I finally find what I seek'
    'Thrusting those digits rhythmically inside making sure not miss any part of the hidden treasure trove which causes goosebumps all over both flesh & bones alike!'
    'While fucking herself on those invading digits relentlessly now Kristen is frustrated by lack proximity alone wanting full cock instead'
    'Now craving release more than anything else world could'
    k 'Oh, Anton! Fuck me! (moans impatiently) I want you cock in my slit… please fuck me!'
    'Feeling the heat and need emanating from Kristen, I pull away from her plump lips reluctantly.'
    'My strong hands grip her thighs as I slowly stand up to tower over her aching form.'
    'With a wicked smirk, I watch as she spreads herself wide in anticipation of my entry.'
    'I waste no time stepping between those legs and pressing the crown of my cock against her entrance'
    'Teasingly grazing it back and forth before finally thrusting my dick deep within with one powerful motion that causes both our bodies to shudder'
    'As our hips grind together instinctively seeking friction, I take control by wrapping an arm around her waist pulling me closer while using the other hand for leverage'
    'This angle allows for deeper penetration each time we connect intimately.'
    "The sound of slapping flesh echoes throughout the room along with whimpers from Kristen's lips parted in a plea for more - begging me not to stop tmy pleasure!"
    k "Ahh… fuck! (Kristen moans) I feel it… so deep inside me… Please, don't stop. Fuck me harder!"
    "I grin at Kristen's begging, my deep black eyes reflecting the passion within me as I start to pump my hips in a steady rhythm that matches our entwined breaths."
    'Each thrust drives my dick deeper inside before pulling out just enough to tease and taunt before plunging back in again.'
    'My strong yet gentle grip on her waist holds her close as we sway together like dancers lost in an intimate waltz under the haze of lustful desire.'
    'Kristen arches her back off the couch in pure ecstasy feeling every inch of my manhood slide against sensitive walls within'
    'Clawing at anything she can reach for purchase to keep herself grounded during these moments of primal bliss'
    'Fucking harder and faster until sweat beads form along their skin from exertion alone!'
    'Her breasts bounce enticingly against my chest with each movement adding another layer of heightened stimulation between us both'
    'Moans and groans echo off every surface signaling how close we are getting not only physically but also emotionally!'
    jump sex_selector

    return

label anal:

    show full anal
    'With a smooth confidence, I take the lead by wrapping my strong arms around her waist and pulling her body close to my own.'
    'I wmyper softly into her ear'
    pc "You really are stunningly beautiful"
    "My voice sending shivers down Kristen's spine."
    "She melts into my embrace, unable to resist the power of my charm as I nuzzle against her neck while gently sucking on her earlobe."
    "Our tongues dance together in an erotic dance that leaves us both panting for more intimacy."
    "Ever so gently, I guide Kristen towards the coach as I position her body to bend over it."
    'My intentions are clear - I gonna fuck her in the ass.'
    'Taking my time, I fetch a small bottle of lubricant and slowly uncaps it before approaching her sensitive anus.'
    'Unsure but intrigued by my actions, Kristen watches nervously as I dabble some lube onto my fingers and tease her opening with them.'
    'As anticipation builds within me.'
    'Bracing herself for any discomfort that may come, Kristen feels my lubricated finger penetrate her anal ring slowly.'
    'The tightness around it causes a slight twinge of pain; she winces slightly but bears through it out of trust for me.'
    'As I introduce another digit and begins to stretch her opening, she finds herself pleading softly'
    k "I… haven't done thus before. Be gentle please." 
    'Her voice quivers with fear mixed with arousal as she continues to beg me to cease the unfamiliar act.'
    'I kiss her shoulder reassuringly while wmypering soothing assurances in her ear'
    pc "I won't hurt you. I promise." 
    'My other hand slides down between our bodies rubbing against the hot wetness between her legs, teasing both of their budding desires.'
    'I gently thrust my fingers deeper into her anus until they reach deep within where we meet resistance from the sensitive walls surrounding my knuckles before pulling back...'
    '...and pushing again!'
    'Despite her unease, Kristen feels a building desire within herself that matches my.'
    "She can't help but moan as I continues to penetrate her tight hole with each thrust of my fingers."
    "The sensation brings an entirely new level of pleasure she hadn't experienced before - one that ignites a fire within her core."
    "Her hips buck against me, craving more contact as we both struggle for release."
    "I kiss along her spine, breathing heavily into the crook of her neck; unable to contain my excitement for claiming tmy beautiful woman's ass for myself."
    "I pull back slightly and position myself at her entrance before slowly pushing into the depths with just the head of my cock"
    "Pausing momentarily due to resistance from her anal muscles squeezing around me tightly like velvet gloves around steel rod." 
    'With determination burning through any last vestiges of hesitation, I push deeper until I feel our hips meet flush together joining them in one sinful motion'
    "As I begin to thrust gently inside of Kristen's now stretched and swollen anus, I feels a rush of pleasure unlike any other."
    "It's clear she's tight yet accommodating - her walls clenching around my cock tightly, driving me wild with desire." 
    'I start off slowly but find it difficult to control my urge for harder pounding due to the intensity of need coursing through my veins.'
    "The sight alone sends chills down my spine as I watch my cock disappear into her rectum; each successive thrust pushing deeper into her virgin depths."
    k "Ah… It's a strange feeling… (moans) Don't push it so much… it hurts!"
    jump sex_selector

    return

label cum_face:

    show full bj happy
    'I gripped her hair tighter, pulling her off just enough to look into those shiny gray eyes.'
    pc "You're killing me. (growled playfully) I want you to take all of this cock." 
    pc '(paused for a moment before continuing softly) Show me what you can do with your throat.'
    "Kristen couldn't hide the excitement in her voice as she nodded eagerly."
    'She opened wide, taking my dick back into her mouth until its entire length was buried deep within it once again'
    'Moaning around my shaft as if it were filling up every orifice instead.' 
    'Her hands moved up my torso now, fisting in my shirt and pulling me closer still as she began bobbing faster than ever before!'
    "I couldn't hold back any longer" 
    "I began thrusting my hips forward, fucking her mouth with a fervor that left no doubt about who was in control now!"
    'Every time I pulled and pushed in and out, she took more of my lenght eagerly, sucking and licking every inch as it slid past her lips.'
    'Her cheeks hollowed out from the force of each powerful stroke, but she welcomed the sensation - this was exactly what she had been waiting for!'
    pc "Fuck yeah, (groaned, feeling himself getting closer to the edge) Get it all the way in, like a good girl." 
    'My hands gripped her head tightly, holding her in place as I used her body like a personal pleasure device.'
    pc "I'm close, (I warned her hoarsely between pants for air) Don't stop now!"
    'Kristen felt her throat stretching to its limits, the gag reflex threatening to take over as my cock hit the back of her mouth with each powerful thrust.'
    'She tried desperately not to choke on it, taking short breaths in between sucks and licks when she could manage it.'
    "Her eyes were watering now from the effort but never once did they leave his gaze - she wouldn't give up until I came!"
    pc "Fuck... I can feel it. (muttered through clenched teeth) Suck it, suck it, suuuck!" 
    "I pulled out just enough for her to get a breath before slamming back into that wet warmth again, driving a cock deeper than ever before!"
    'Kristen groaned around him, feeling every vein bulge against her tongue and cheeks as she worked harder than ever to please me completely!' 
    'My hips bucked wildly, my cock throbbing in her mouth as I neared orgasm.'
    'Kristen could feel it building inside of her - the warmth and pressure growing stronger with each passing second.'
    'She increased the speed of her bobbing head, taking more of a dick into that tight throat until she felt him pulse violently against her tongue!'
    pc "Oh fuck!" 
    'I cry out loudly, shooting ropes of hot cum down her throat as she swallowed every drop greedily!'
    'Kristen pulled back slowly from my softening member, licking around the crown to clean off any remaining traces of cum' 
    'She is looking up at me with pride etched across those shiny gray eyes.' 

    jump goodbye_kiss
    
    return

label cum_belly:

    show full sex happy
    'I lean down capturing one plump nipple between my teeth as moan vibrates through it.'
    'Sending shivers through entire body line causing waves after wave crash over us both sweeping away any lingering thoughts or worries'
    'Leaving only raw need slow building towards imminent climax.' 
    'Feeling the increasing rhythm of my movements, Kristen realizes that I am close to orgasm'
    k "Please don't come yet! (pleads desperately) I'm so close. Ah… ah! Harder. Please! Just don't stop!!! Don't stop!"
    'I feel the raging waves of pleasure building up within me, my muscles tensing as I fights to hold back my release.'
    "The sensation of Kristen's warmth enveloping me and her moans echoing through the room are enough to drive me wild with need."
    'With a growl that mirrors my impending orgasm, I increases the intensity of my thrusts without mercy - pounding into her over and over again'
    'I move like a man possessed by desire itself.'
    'Kristen gasps for air between each cry of pleasure, feeling every inch of my powerful frame against hers as we dance tmy erotic waltz towards ecstasy.'
    'Her tight channel grips at me eagerly while she arches her back begging for more; closer to that elusive peak we both crave so dearly!'
    'She can feel it building deep inside; becoming unbearable almost… but not quite yet ready just when I give an audible groan signaling imminent climax!'
    pc 'Ahhhh... yes, yes, yessss...'
    "In response, Kristen's nails dig into my shoulders drawing blood as she pulls herself closer on reflex alone trying anything possible keep from being left behind in momentary bliss!"
    'The world around us melts away into pure sensation creating an indescribable connection so intense neither could resist much longer now…'
    'My hips buck wildly, pouring every ounce of my energy into each thrust as I nears my climax.'
    'I grit my teeth, feeling the familiar burn building deep within me.'
    'Kristen feels it too—the telltale signs that I is about to spill my seed inside her.'
    'Her body tightens around me in anticipation, welcoming the oncoming release with open arms.'
    'With a primal roar, I finally unleash my hot cum within her trembling womb.'
    'My powerful member throbs and pulses as a sticky white liquid fills every nook and cranny.' 
    'She clamps down on me instinctively at first before succumbing to overwhelming pleasure herself.'
    k "Oh, I'm cuming! I'm cuming!!!"
    'She screams out in ecstasy as wave after wave washes over us both like an ocean tide crashing onto a rocky shore - our passion so intense it feels almost tangible!'
    "Our bodies become one glowing entity bathed in sweat and satisfaction under the torrent of raw emotion while their hearts race against each other's chests" 
    'I pull out of Kristen with a soft groan, my cock still twitching from the intense release.'
    'A thick string of cum oozes out from her entrance, leaving a wet trail behind as it leaks onto the couch.'
    'I watche in fascination as she gathers some on her fingers and brings it to her lips, savoring the taste with closed eyes and parted mouth'
    "This is revealing just how much pleasure she's found in this encounter."
    'With shaky hands we both sit up straight trying to catch our breath; leaning against one another for support.'
    'Kristen runs gentle fingers along my abs feeling every ripple beneath before finally letting go allowing me space explore surroundings somewhat numbly'

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

    k '"Was that good for you?"'
    'Her voice hoarse from our intense encounter. A small smile played on her lips as she waited for my answer.'
    'I nodded, still catching my breath.'
    pc '"Fuck yeah," I managed to get out between pants. "You are amazing."' 
    'I pulled her into a tight embrace, nuzzling my face into her neck.'
    pc '"I gotta say," I said, running my fingers through her hair. "That was one hell of a way to kick off my night."'
    'I grabbed my clothes from where they had been discarded earlier and began dressing himself once again.'
    'The encounter with Kristen had been incredible, but there were more girls waiting for me at the bar - eager eyes looking for their own chance at an unforgettable experience like hers!'
    "I couldn't help but feel a twinge of excitement as I thought about it all."
    pc '"You take care now," I said over my shoulder, not wanting to make things too awkward between us. "And thanks for the night."'

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

    window hide
    show checkout rape onlayer master
    pause
    window auto

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

