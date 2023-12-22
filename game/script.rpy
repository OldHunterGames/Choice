define g = Character("Girl", color='#ff4d4d')
define k = Character("Kristen", color='#ff4d4d')
define pc = Character("Anton", color='#00f')

define doneOral = False
define doneVaginal = False
define doneAnal = False

init -10 python:
    import random

    class MusicPlayer:
        def __init__(self):
            self.prev_selection = None
            self.play_music = False
            self.music_files = ['/sound/music/pulsingBas01.ogg', '/sound/music/pulsingBas02.ogg', '/sound/music/pulsingBas03.ogg', '/sound/music/pulsingBas04.ogg']
        
        def play_random_music(self):
            if not self.play_music:
                return
            
            random_music_file = random.choice([i for i in self.music_files if i != self.prev_selection])
            self.prev_selection = random_music_file
            
            renpy.music.play(random_music_file)

        def check_music(self, _a, _b):
            if not renpy.music.get_playing(channel='music'):
                self.play_random_music()
            
            return Text("Hello"), .1

        def set_playlist(self, music_files):
            self.music_files = music_files
            self.play_random_music()

    music_player = MusicPlayer()

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

image checkout dance = "images/[persistent.graphic_mode]/checkout dance.png"
image checkout love = "images/[persistent.graphic_mode]/checkout love.png"
image checkout rape = "images/[persistent.graphic_mode]/checkout rape.png"

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

screen language_selection():
    vbox:
        text "Select your language":
            xalign 0.5
        xalign 0.5
        yalign 0.5
        spacing 20
        hbox:
            spacing 50

            imagebutton idle im.Scale("gui/eng.png", 200, 200) action Language(None), Return()
            imagebutton idle im.Scale("gui/rus.png", 200, 200) action Language("rus"), Return()    

label splashscreen:
    call screen language_selection

    return

image musicChecker = DynamicDisplayable(music_player.check_music)
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # call screen my_screen
    #window hide
    #show checkout dance at move_image
    #pause
    #window auto
    scene bg bar
    $ music_player.play_music = True
    $ music_player.set_playlist(['sound/music/club01.ogg', 'sound/music/club02.ogg', 'sound/music/club03.ogg'])
    show musicChecker

    'I sauntered into the bustling nightclub, my eyes scanning the crowd for my next conquest.'
    'The pulsing bassline of electronic music throbbed through the air as I made my way to the bar, ordering a drink with an easy smile on my lips.'
    'I took a sip of my cocktail before casually glancing around again, searching for someone who caught my interest.'
    'Spotting her across the room - a young woman dancing alone near one of the VIP booths - my heart rate quickened in anticipation.'

    show kristen dress calm
    with dissolve

    'She had curves that were impossible not to notice underneath her tight red dress.'
    "Girl's body moved instinctively to every beat of music; it was clear she wasn't just another pretty face but possessed an irresistible allure I couldn't miss out."
    'Without hesitation or second thought, I pushed through crowds towards her like a shark homing in on its prey.'
    'As I approached her from behind, I gently placed one hand on her shoulder causing goosebumps instantly forming along her skin at this unexpected touch from a stranger…'

    show kristen dress arrogant
    with dissolve

    pc "Hi, my name is Anton. (I said with a smile) I'm sorry if I scared you."
    pc 'I just wanted to aquaint myself with the most beautiful girl in the club.'
    g "I'm not really looking for anything serious right now" 

    show kristen dress happy
    with dissolve

    'A girl smiles to me, keeping her tone light and playful.'
    "But there's a hint of curiosity in her eyes as we lock onto my."
    "I chuckled, leaning in closer to her ear so only she could hear."
    pc "Neither am I (whispered seductively)." 
    pc "I just think you're absolutely stunning and want to show you a good time." 
    'My hand slowly moved down her arm before entwining with hers on the bar counter, my fingers intertwined intimately.'
    pc "So... What brings such a gorgeous woman like yourself out alone tonight?"
    'Girl smiles back at me, feeling flattered by my attention.'
    'She likes the way I touch her and finds herself drawn to my confidence.'
    g "Oh, you know… just looking for some fun" 
    'She replied with a shrug that emphasized her breasts underneath the lacy black bra peeking out from beneath her dress.'
    g "I'm Kristen by the way."

    show kristen dress calm
    with dissolve

    'She took another sip of her drink before adding:'
    k "So what do you have in mind, macho-man?"
    'I nodded, grinning widely:'
    pc "How about another round? On me." 
    'I said as I turned to face the bartender, placing a hand on her lower back and guiding us both towards me.'
    'As we stepped closer to the bar, my other arm brushed against hers subtly but intentionally; feeling the softness of her skin beneath my fingertips sent shivers down my spine.'
    pc "What do you drink, gorgeous?"
    
    show kristen dress happy
    with dissolve
    
    'Kristen smirked at my boldness, feeling a thrill run through her.'
    "She liked this confident man who wasn't afraid to take charge."
    k "I'll have whatever you're having." 
    
    show kristen dress calm
    with dissolve

    "As I turned back towards her with our drinks in hand, Kristen couldn't help but notice how close we were standing; our bodies almost touching from hip-to-hip under the dim lighting of the bar area."
    'The air between us seemed charged with electricity - anticipation and desire thick enough to cut with a knife…'
    pc "Here you go." 
    'Handing her a fresh drink before taking one for myself. I clinked our glasses together playfully and took a sip.'
    pc "So tell me more about yourself" 
    'I prompted it casually while keeping an eye on the dance floor nearby; itching to get closer to Kristen physically than we were at that moment.'
    pc "What do you like doing when you're not out here looking for fun?"
    'Kristen took a sip of her drink, the cool liquid sliding down her throat as she thought about how to answer my question.'
    "She didn't want to come off too forward or desperate but also wanted me interested in continuing our time together after this bar stop…"
    k "I work for a pharmaceutical company" 
    k "It pays well but can be quite boring at times."
    
    show kristen dress happy
    with dissolve 
    
    "A small laugh escaped before adding with a wink:"
    k "But I make up for it by exploring my wild side when possible!"

    show kristen dress calm
    with dissolve

    "I chuckled in response, nodding along with understanding. "
    pc 'I can imagine'
    "I said nonchalantly while taking another sip of my drink."
    "In reality, I couldn't relate at all. My business was anything but boring for me!"
    "But it seemed like an interesting enough profession to keep the conversation going without revealing too much about myself just yet."
    k "So what about you? (she asked curiously)" 
    "Kristen tilting her head to the side as she watched me over the rim of her glass. She could feel my gaze on her body and wondered if I was thinking about more than just business right now…"
    "I smirked, taking another swig of my drink."
    pc 'Oh, you know...'
    'I shrugged casually as if it were no big deal.'
    pc "I have my hands in a few different things - investments mostly." 
    'I paused for dramatic effect before adding with a wink:'
    "But when I'm not making money hand over fist like this?"
    'I gestured vaguely around us towards the club and its revelers, implying that I enjoyed living life to the fullest just like Kristen did.'
    "The music changed then; an upbeat pop song started playing on speakers nearby."
    k "That's great actually. But I'm here not for a small talk. Let's dance!"
    
    scene bg dancefloor
    $ music_player.set_playlist(['sound/music/dance.ogg'])

    show kristen dress happy
    with dissolve

    'Kristen grabbed my hand and pulled me onto the dance floor, her body moving instinctively to the beat as she pressed against my.'
    'She could feel my hardness through our clothes; it sent a shiver of anticipation down her spine.'
    'As we swayed together underneath strobing lights, she whispered into my ear:'
    k "Enjoy the show." 
    'Her breath was hot against my skin, teasing me with promises unspoken but clear in her eyes…'
    "Kristen's hips swayed hypnotically to the music, her body moving in perfect rhythm with every beat." 
    "She gyrated and twirled around I, making sure I had an unobstructed view of her curves as she danced closer and closer until we were almost touching."
    "Her breath came faster now; anticipation mixed with desire coursed through her veins."
    "Her gaze locked onto my - a silent invitation for more than just this dance…"
    "I couldn't take my eyes off of Kristen as she danced seductively for me." 

    window hide
    show checkout dance onlayer master at move_image
    pause
    window auto

    scene bg bar
    show kristen dress calm
    with dissolve

    "The sight was intoxicating, and I felt himself growing harder with every move she made."
    "I stepped closer to her until our bodies were pressed together; the heat between us palpable even through our clothes."
    pc "You are exquisite!" 
    'I murmured against her ear before trailing kisses down her neck, my hands roaming over her body possessively underneath the thin fabric separating us.'
    pc "Let me show you how much I appreciate your performance."
    'Kristen shivered at my touch, her heart racing in anticipation. She leaned into me, moaning softly as I kissed along her neck and shoulders.'
    k "Mmm… that sounds tempting." 
    "She is pulling away slightly to look up at me with a mischievous glint in her eye."
    k "But I have a better idea." 
    'With that, she grabbed my hand and led us both towards the exit.'

    scene bg parking
    $ music_player.set_playlist(['sound/music/outside01.ogg', 'sound/music/outside02.ogg'])

    'As we stepped out into the cool night air, Kristen glanced around to make sure no one was watching before pulling I towards a dark alleyway between two buildings.'
    'Her heart pounded in her chest with excitement and nerves as she pressed herself against me once more - this time feeling my arousal clearly through our clothes.'
    k "I have an empty apartment in a downtown."
    'She whispered breathlessly into my ear, eyes sparkling with mischief.' 
    k "Want to come up for some real fun?"
    'I smirked, my hands sliding up her back to cup her ass gently.'
    pc "I think that's an excellent idea." 
    'I purred in response, pulling away just enough to look into those sparkling eyes of hers.'
    k "Where is your car?" 
    'Kristen was definitely interested in seeing what I was driving.' 
    'I chuckled softly, leading her over to my sleek black sports car parked nearby.'
    pc "Right here." 
    "I unlocked the doors for us both before climbing into the driver's seat."
    'The interior of the vehicle was just as luxurious as its exterior - leather seats and smooth surfaces everywhere you looked.'
    'I turned towards Kristen, one eyebrow raised in question; she seemed eager but hesitant at the same time…'
    "Kristen nodded, climbing into the passenger seat and buckling her seatbelt."
    "Let's go!" 
    "She said it with determination, already imagining what we could get up to in my car…"

    hide kristen
    with dissolve

    "The drive to Kristen's apartment was filled with tension and anticipation."
    "I could feel her eyes on me as I navigated through the city streets, my hands tight around the steering wheel from both excitement and nerves."
    "She leaned back in her seat, playing coyly with her hair or crossing/uncrossing her legs while occasionally glancing out of the window - teasing me without touching."
    "Finally pulling up outside an unassuming building near downtown, I turned off the engine but made no move to get out just yet"
    'I was looking at this woman who had captivated me so completely since our first encounter at the bar…'
    "Kristen's heart raced as we pulled up outside her apartment building. This was it - the moment of truth."
    "She turned towards me, biting her bottom lip nervously but determined not to show any hesitation or fear."   

    show kristen dress calm
    with dissolve
    k "Well? Aren't you coming in?"
    'I smirked, stepping out of the car and rounding it to her side.'
    pc "Of course." 
    'I bow to her slightly before opening a door for her with a flourish.'
    'My hand brushed against hers as she exited; our skin connecting once more underneath the cool night air.'
    "We walked up together towards Kristen's apartment building entrance, my arm wrapping around her waist possessively while hers found its way onto my shoulder - both of us lost in each other already…"
    "We stepped into the elevator together, pressing against each other as it ascended to her floor." 

    "The doors slid open and Kristen led me down a short hallway towards her unit before unlocking it with shaking hands."

    scene bg room

    "Inside was an immaculate one-bedroom space - minimalistic but comfortable looking; perfect for our needs right now…"
    "She turned around to face me." 

    show kristen dress calm
    with dissolve

    k "Here we are, make yourself comfortable."
    pc "What are we gonna do? (asked in a sultry tone)" 

    show kristen dress arrogant
    with dissolve

    "Kristen pouted her lips in slight annoyance."
    k "Hey, macho, you're the one who made a move on me at the bar. So you tell me. What do you want? Make a choice!"

    menu:
        "Make love to her":
            jump make_love

        "Rape her brutaly":
            jump rape

    return

label make_love:

    $ music_player.set_playlist(['sound/music/romantic01.ogg', 'sound/music/romantic02.ogg'])
    'I smiled, stepping closer to her.'
    pc "I think I know exactly what I want" 

    show kristen dress happy
    with dissolve    
    
    "I make my voice low and seductive, reaching out to run a finger down the side of her cheek before leaning in for a slow kiss that left goosebumps on her skin."
    pc "You're so damn sexy." 
    'I whispered against her lips as we parted once more.'
    'My hands trailed over every inch of exposed flesh we could find; tracing along the line of her collarbone, teasingly brushing across nipples through fabric, sliding lower still until cupping full hips possessively.'
    pc "You know, out there on the dance floor. you were moving so sexy. I couldn't stop watching."
    pc "The only thing missing was that you didn't take your clothes off in the process."
    k "I guess that would have been reckless in front of so many people, huh?" 
    'Kristen laughts.'
    pc "Yeah… but we're alone now." 
    'I sit down on a chair, making myself comfortable.' 
    pc "And I want to see you stripping, baby."
    'Kristen blushed, feeling her heart race at my demand.'
    k "Look's like it's your lucky day, Anton!"
    'She turned on the music and let it fill the room as she started to dance sensually - hips swaying in sync with the beat.'
    'Slowly, she unzipped her red dress and slipped it off her shoulders; revealing more of her curves as it fell to floor in a seductive pool around heels.'

    show kristen lingerie happy
    with dissolve

    'Her black lacy underwear was all that remained now, barely hiding anything from view…'
    'With each step and dip, she teased me further.'
    'Her body glistening under the dim light as her breasts bounced enticingly with every move.'
    'She faced me again, eyes locked on my - daring me to take what I wanted…'
    k "Like what you see?" 
    "Her voice is low and sultry."
    pc 'I want to see you all!'
    'Without hesitation, Kristen reached behind her and unclasped the back of her bra.'
    'It fell away, revealing her perfect breasts to my eager gaze.'
    'She ran a finger over one nipple before cupping both in her hands and pushing us together for my viewing pleasure…'
    'With a wicked grin, Kristen hooked her thumbs into the waistband of her black lacy underwear and slowly slid us down over her hips.'
    'She stepped out of them, leaving herself completely naked before my hungry eyes…'

    window hide
    show checkout love onlayer master at move_image
    pause
    window auto

    scene bg room   
    show kristen nude happy
    with dissolve

    k "Are you satisfied now?" 
    "Kristen is tilting her head to one side as she watched my awe in the sight of her bare body."
    'Her heart raced with excitement at my reaction; each breath sending shivers down her spine…'
    'I stood up, my cock hard as a rock in my pants.'
    pc "Mmmm, you're perfect, baby." 
    'I stepped closer to her and ran a hand down her stomach, tracing the curve of her hip before circling around to cup her perfect breast.' 
    'My thumb brushed over her nipple, causing it to harden even more under my touch.'
    pc "Come here," 
    'I growled softly against her ear before picking her up and carrying us both towards the coach.'

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
    
    show full bj happy
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
    show full sex happy
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
    "I kiss along her spine, breathing heavily into the crook of her neck; unable to contain my excitement for claiming the beautiful woman's ass for myself."
    
    show full anal
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
    "I take Kristen from behind slowly, allowing her body to adjust to the foreign sensation of being penetrated anally."
    "Kissing her neck gently as a sign of reassurance that I am here for her pleasure too."
    "My thrusts become shallower but more rhythmic, letting her relax into the feeling of fullness inside her tight hole."
    "As she begins to loosen up around me, I can feel her muscles start to give way; allowing me greater access into her depths with each push forward."
    "Her moans turn from pained gasps to soft whimpers mixed with pleasure as our bodies find their rhythm together in this taboo dance."
    pc "You're doing so well." 
    "I whisper into her ear before nipping at her lobe playfully while increasing my tempo once again - making sure not to overwhelm her sensitive flesh with too much force or speed just yet."
    "I continue to thrust my road into Kristen's defenseless ass, feeling her body yield to my relentless advances."
    "Her moans grow louder and more passionate as she starts to enjoy the sensation of being filled in such a forbidden way."
    "The tightness of her inexperienced sphincter grips me like a vice, sending waves of pleasure through my entire body with each powerful stroke."
    "As we move together in perfect harmony, our bodies slick with sweat and desire, I can feel myself getting closer to the edge."
    "Knowing that I want this experience to last, I slow down once again - drawing out each movement for maximum effect."
    "My cock twitches inside her, aching for release but willing to wait until she finds her own climax first."
    k "It… it feels so good."
    "Kristen pants, her voice barely audible over the sound of our bodies slapping together."
    k "I never thought I'd enjoy this… but you make it feel incredible."
    pc "I'm glad you're enjoying it" 
    "I say it with a wicked grin as our bodies continue their dance." 
    "I lean in close to Kristen's ear, my breath hot against her skin as I whisper encouragingly:"
    pc "You're doing amazing. Just let go and enjoy the sensations."
    "As we continue our passionate embrace, I reach around her waist and guide her hips back towards me - angling her body for deeper penetration."
    "Our movements become more urgent now; driven by raw lust and desire that can no longer be contained or restrained."
    "My thrusts grow harder and faster, eliciting cries of pleasure from both of us as we hurtle towards climax together."
    "The sound of our bodies slapping echoes through the room like a primal drumbeat - a testament to our unbridled passion."
    "Kristen's eyes roll back in her head as she cries out:"
    k "I'm going to cum!" 
    "Her body tenses around me, squeezing my cock even tighter as her orgasm washes over her."
    "The sensation is too much for me to bear; I can feel myself reaching the edge as well."
    "With a final powerful thrust, I bury myself deep inside her ass and release my load - filling her with warmth as we both shudder in ecstasy."
    "Our bodies collapse together in a sweaty heap, spent but satisfied from our shared experience."
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

    $ music_player.set_playlist(['sound/music/agro01.ogg', 'sound/music/agro02.ogg'])
    
    'As my gaze locked onto Kristen, a sinister grin spread across my face.'
    'With a swift motion, I pulled out a gun from my pocket and pointed it at her.'
    
    show kristen dress shoked
    with dissolve    

    pc "I'm going to rape you (growled menacingly)."  
    pc "Strip." 
    'The command was delivered with an air of authority that left no room for negotiation.'
    "Kristen's eyes widened in terror."
    "Kristen's heart races as her mind tries to process the situation."
    "She swallows hard, eyes wide with fear, and pleads with me in a shaky voice:"
    k "P-please… don't hurt me. I'll do whatever you want."
    "Tears well up in her eyes as she looks at the gun tremblingly, begging for mercy while trying not to make any sudden moves that might agitate me further."
    "I chuckle darkly, a mix of amusement and arousal in my voice."
    pc "Good girl" 
    'I say it softly before sudden push on her towards the couch.'
    pc "Take off your clothes." 
    "I commands again, this time with more force as I moves closer to her, the gun still trained on her trembling form."
    "Kristen's hands shake as she slowly begins to unbutton her dress, tears streaming down her cheeks."
    k "Please… just let me go…" 
    "Kristen whispers between sobs, hoping that might make me reconsider my actions. But the look in my eyes tells her it won't be enough."

    show kristen lingerie shoked
    with dissolve

    'The dress falls to the floor, revealing a black lace bra and matching panties that hug her curves tightly.' 
    'She takes a deep breath before starting to undo the clasp of her bra, her trembling fingers fumbling with the tiny hooks.'
    "I'm scared, Anton!" 
    'She whimpers, looking up at me beseechingly.'
    "I watch her every move with a predatory gaze, my eyes glinting with lust and excitement."
    pc "You're doing great," 
    "I said it reassuringly, though there's an undercurrent of menace to my voice that sends shivers down Kristen's spine."
    pc "Now take of the rest, slut!"
    "Kristen's hands shake as she fumbles with the clasp of her bra, finally managing to undo it and letting it fall to the floor."
    "Her breasts are exposed now, heaving slightly in fear and anticipation."
    "She looks up at I through tear-filled eyes, praying for mercy while also feeling a twisted thrill from this dangerous situation."
    k "Please.. (she whispers softly) don't hurt me... much."
    "With shaking hands, Kristen reaches for the lace of her panties and slowly slides us down her legs."
    "She feels exposed and vulnerable in front of I, but also aroused by the danger of it all."
    
    show kristen nude shoked
    with dissolve    
    "Her heart races as she steps out of her underwear, standing before me completely naked."

    window hide
    show checkout rape onlayer master at move_image
    pause
    window auto

    scene bg room  
    show kristen nude shoked
    with dissolve

    k "Please let me go... I begging you, Anton."
    'She whispers again, looking up at me with pleading eyes.'
    k "Why are you doing this?" 
    'I smirk, taking a step closer to her.'
    pc "Because you're mine now," 
    "I growl, my voice low and rough." 
    "I grab her hair firmly, pulling her head back as I force my tongue onto her mouth in a deep, possessive kiss."
    "My free hand roams over her body, tracing patterns on her skin before reaching between her legs."
    pc "You'll scream my name when I'm done with you!" 
    "I whisper passionately against her lips, my fingers teasing her already wet pussy."
    "My kiss is forceful and dominating, my tongue pushing past her lips and invading her mouth with a roughness that leaves no room for resistance."
    "She can taste the alcohol on my breath mixed with my own musky scent as I holds her head still while my other hand roams lower, finding her wet folds once again."
    "Without warning, I thrust two fingers deep into her core, causing Kristen to gasp." 
    "I chuckles darkly before pulling my fingers out, only to push them back in harder this time." 
    pc "You like that, don't you?" 
    'I growl, watching as she squirms under my touch.'
    'Kristen whimpers, trying to push away from me but unable to escape my grasp.'
    "My fingers feel like they're on fire inside her, stretching and filling her in a way that makes her gasp for air."
    "She nods weakly, tears streaming down her face as she tries not to choke on my tongue invading her mouth."
    k "Yes. (she manages between moans) Please stop… please don't hurt me anymore!"
    "I pull my fingers out of her, leaving her aching." 

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

    'I push her down on the floor.'
    pc "Kneel, bitch! You'll beg for me."
    "Kristen's heart races as she kneels before me, her eyes wide with fear and arousal."
    pc "Now open your fucking moth wide!"
    'She opens her mouth obediently, feeling my hardness press against her lips.'
    k "Please don't hurt me, Anton" 
    'She whispers again, her voice trembling.'
    k "I'll do anything you want."
    show full bj tears
    "I smirk, pushing my cock into her mouth roughly, grabbing her hair and forcing my cock deeper down her throat."
    pc "That's right." 
    "Kristen gags on mmy rod, her eyes watering as she struggles to breathe around my thickness."
    pc "Take it all, whore!" 
    "I start to thrust in and out of her mouth with increasing speed."
    "As my thrusts become more forceful, my hips slamming against her face." 
    "Taking my full control, Kristen feels like she can't breathe around my cock filling every inch of her mouth and stretching it to its limit."
    "She gags repeatedly on each thrust, tears streaming down her cheeks from the pain and humiliation."
    "I growl like a wild animal, my hips moving faster as I pounds into her throat."
    pc "That's it." 
    "I grabb her hair tighter to keep her in place. My other hand roams over her body, tracing patterns on her skin as I forcefully use her helolessly open throat."
    "Kristen whimpers with each thrust, feeling like she might choke on me at any moment."
    "She tries to pull away but can't escape my grip or the intense pleasure that pulses through her body."
    "Kristen's eyes roll back in her head, a mix of pain and nausea coursing through her." 
    "She can feel my cock hitting the back of her throat with each thrust, forcing her to take me deeper than she ever thought possible."
    "Her body shudders as she comes undone around me, moaning loudly despite the cock in her mouth."
    k "Please (she manages between gasps for air) stop… I can't take it anymore!"
    "I chuckle darkly, pulling my dick out of her mouth with a pop." 
    "I smirk down at her, my eyes glinting with satisfaction as I watches her gag and cough."

    jump rape_selector

    return

label forced_sex:

    pc "On your back, whore!" 
    "I'm taking charge, shoving her down onto the couch."
    "Girl complied, her body trembling with fear as I towered over her."
    "I positioned myself between her legs, admiring the sight of her spread out before me - vulnerable and exposed."
    "Despite her fear and humiliation, her soft pink labia glisten with traitorous moisture."
    pc "You're so fucking sexy when you're scared." 
    "I smiled, running a finger along her inner thigh. Kristen flinched at my touch but didn't dare to resist."
    "Kristen's heart pounded in her chest as she lay there, helpless and exposed."
    "She could feel the heat of my body above her, my breath hot on her neck as I traced a finger along her inner thigh."
    "Despite her fear, she couldn't help but feel a twinge of arousal at being so completely under my control."
    "Please… (she whispered, her voice barely audible) Don't do this to me."

    show full sex tears
    
    "Ignoring her plea, I rubbed my cock against her entrance, teasing her with the tip before thrusting inside without warning."
    "Kristen cried out in pain as I filled her completely, her body unprepared for my size." 
    "I began to pound into her relentlessly, each stroke driving deeper and harder than the last."
    "Her cries turned to moans as her body betrayed her, responding to the rough treatment despite her terror."
    pc "You like it, don't you?"
    "Kristen's body arched off the bed as I pounded into her, my words sending a shiver down her spine."
    "She couldn't deny the pleasure that was building within her, but she refused to give me the satisfaction of hearing her admit it."
    k "No… stop!" 
    "She gasped between moans, trying desperately to maintain some semblance of control. But with each thrust, her resolve weakened further."
    "I laughed, enjoying her struggle against the pleasure I was giving her."
    "I grabbed her hips, holding her in place as I continued to drive into her with brutal force."
    pc "You're so tight! I bet you've never been fucked like this before."
    "Kristen's eyes widened as she felt my grip on her hips, my words sending a jolt of humiliation through her."
    "She knew I was right - she had never experienced anything like this before, and the realization only heightened her humiliating arousal."
    k "N-no!" 
    "Kristen stammered, her voice barely audible over the sound of our bodies slapping together."
    k "Please… Anton! Let me go… ah..."
    "My eyes locked on Kristen's face as I continued to pound into her. I could see the conflict within her - the desire to resist me warring with the pleasure I was giving her."
    pc "You enjoying to be forced like this, admit it."
    "Kristen's breath came in ragged gasps as she felt herself teetering on the edge of orgasm."
    k "I dont!" 
    "Poor girl gasped, her voice barely audible over the sound of our bodies slapping together"
    k "I don't want this… ah..."
    "I laughed, my grip on her hips tightening as I continued to fuck her relentlessly."
    "I could feel her body responding to me despite her protests, and it only fueled my desire further."
    pc "You're a liar! But your body tells the truth."
    pc "And the truth is, you're a filthy, humiliation-enjoying slut!"
    "Kristen's eyes squeezed shut as she felt the first waves of pleasure wash over her following my dirty words."
    "She couldn't deny it any longer - her body was responding to my brutal thrusts, betraying her every attempt to resist me."
    k "No… please… I can't… I can't stop it…"
    "My grin widened as I felt Kristen's body surrender to the pleasure, her words music to my ears. I pounded into her even harder, driving her closer and closer to the edge."
    pc "That's it! Give in to it, whore!"
    "Kristen's body arched off the bed as she felt the first waves of orgasm crash over her."
    "She cried out, her voice mingling with my grunts as I continued to drive into her relentlessly."
    k "Aaaahhh... fuuuuck!"
    "I laughed, enjoying her helplessness as I continued to fuck her through her orgasm. I could feel my own release building, but I knew I could last much longer in needed."
    pc "You're mine, say it."
    "Kristen's eyes squeezed shut as she felt another wave of pleasure wash over her."
    "She couldn't deny it any longer - I had complete control over her body, and there was nothing she could do to stop me."
    "I-I'm yours..." 
    "She gasped, the admission ripped from her throat as her orgasm subsided."
    k "Enough… spare me... please…"
    jump rape_selector

    return

label anal_rape:

    pc "Now get on all fours and spread your ass for me, bitch!"
    "Kristen's heart races as she complies, her body shaking with fear and arousal. She gets on all fours, spreading her legs wide to expose herself fully to me."
    k "Please, not in the ass." 
    "She whimpers again, looking back at me through tear-filled eyes."
    k "I've never done that. I'm afraid… I'll do anything you want, just don't touch my tushy."
    "I chuckle darkly, my eyes glinting with lust and amusement."
    pc "You'll do anything I want? Even if it means taking my cock in your ass?"
    "I step closer to her, running a finger along the crack of her ass before pressing against her entrance."
    "Kristen flinches but doesn't move away, too scared to resist any further."
    pc "Beg for it!" 
    "I slapped her ass hard, to reinforce my command."
    "Kristen whimpers, feeling my dickhead against her tight hole." 
    k "Please… don't do this to me..." 
    "She begs, her voice shaking with fear and humiliation."
    k "I'll do anything else… just not that."
    "I laugh, a cruel sound that sends shivers down Kristen's spine."
    pc "You think you have a choice?" 
    
    show full anal

    "I positions myself behind her, lining up my cock with her ass. With one swift motion, I thrust forward, burying it deep inside her unprepared hole."
    "Kristen screams in pain as my hard rod rams in her butthole, stretching it beyond anything she's ever experienced before."
    pc "Now you're mine!" 
    "I'm pulling out slowly before slamming back in again."
    "Kristen screams in pain as I sodomize her roughtly, feeling like she's being torn apart."
    "Tears stream down her face as I continue to pound into her ass relentlessly, each stroke sending shockwaves of agony through her body."
    k "Aaaaa! Please… stop… It hurts so much…"
    "I grunt, my breath coming in ragged gasps as I continues to pound into her."
    pc "You're so fucking tight... The fist time is allways the best!" 
    "My fingers digging into her hips as I forcefully impale her on my meaty stake."
    pc "You're gonna take all ofform me, bitch!"
    "Kristen's eyes roll back in her head as I continues to thrust into her, the pain becoming too much to bear."
    "She feels like she's going to pass out from the intensity of it all, but I show no signs of stopping."
    k "Please… I can't…" 
    "She whimpers weakly, her body shaking with each brutal stroke."
    "My pace quickens, my breath coming in ragged gasps as I feels himself getting closer to the edge."
    jump rape_selector

    return

label cum_throat:

    show full bj tears
    pc "You'll take everything I give you!" 
    pc "I'm going to fuck your little slutty mouth as hard as I please."
    pc "I make you swallow my load and thank me for it, you bitch!"
    "My cock is hard and throbbing, ready to be pushed inside her mouth again."
    "I grabs her hair roughly, pulling her head back before pushing my thick shaft between her lips once more."
    "She gags on me immediately as I begins to thrust in and out of her throat with long strokes that make her eyes water."
    "Kristen whimpers, feeling like she might vomit as I takes her again. She tries to pull away but my grip is too strong."
    "Her eyes water and her throat burns with each thrust of my cock, making it difficult for her to breathe or swallow properly."
    k "Please (she begs desperately) I can't take this…"
    "My hips moving faster as I force my cock deeper into her throat."
    pc "You'll take it all," 
    'I grabs her hair tighter, enjoying the way she squirms under my touch, pulling her head back even further until she can feel me hitting the back of her throat with each thrust.'
    pc "Take it like a good little slut!"
    "Kristen gags and chokes on me, her body shaking with each thrust. She feels like she's going to pass out from lack of oxygen but can't escape my tight grip."
    "Tears stream down her face as she tries to beg for mercy once more:"
    k "Please… I can't breathe…"
    pc "Then stop whining and make me come." 
    "I roared my words mercilessly as Kristen hastily tried to inhale."
    pc "It'll be over as soon as you swallow every last drop of what I've prepared for you."
    "Kristen whimpers, feeling like she's drowning on my cock. She tries to focus on making me come, bobbing her head faster and sucking harder in an attempt to end this nightmare."
    "Her eyes roll back in her head as I continues to thrust into her throat relentlessly."
    k "Khah… I need air…"
    "I grunt, feeling myself getting closer to the edge. I thrusts even harder into her throat, enjoying the way she gags and chokes on my meaty dick."
    pc "Almost there!" 
    "My hips moving even faster as I nearing my release."
    pc "You're going to swallow it all, dirty coocksuking slut!"
    "My cock throbs in a girls mouth, pulsing with each beat of my heart."
    "Kristen can feel me getting closer to the edge as I thrust harder into her throat. She tries to keep up, desperate for it to be over so she can breathe again."
    "I groan, my body tensing as I am about to come." 
    "I grabs Kristen's hair tightly, holding her in place while I give her one last full depth thrust, releasing my load into her mouth."
    pc "Swallow it, fucking bitch!" 
    "I hold her head impaled on my cock, watching as she gags on my hot, sticky cum."
    "Kristen gags on my cum, feeling it fill her mouth and spill down her chin."
    "She tries to swallow as much as she can but some of it drips out, running down her neck and onto her breasts."
    "Her eyes water from the pain and humiliation as she struggles to breathe around my dick still lodged firmly in her throat."
    "I pull it out of her mouth, smirking as I watches her gasp for air."
    "Wiping my cum from her chin with my thumb, I bringing it to her lips and forcing her to taste it." 
    pc "You're mine now." 
    "I'm looking down on her, enjoying the look of defeat in her wet grey eyes."
    pc "And you'll never forget it."
    "Kristen whimpers, tasting her own humiliation as I forces her to lick my cum from my thumb."
    "She feels broken and used, her body shaking with fear and arousal as she looks up at me through tear-filled eyes."
    "Please… let me go!" 
    "She begs once more, hoping that this nightmare will finally end."
    "I smirks, enjoying the look of defeat on her face."
    pc "I'll let you go, as you have no more use to me."
    "With a powerful kick, I topple the girl to the floor, leaving her lying there gulping air with her mouth like a beached fish, cum dripping from the corner of her mouth." 
    "Standing over her, watching as she gasps for air and tries to regain her composure, I smirk."
    "Knowing that I's left my mark on her both physically and emotionally is a realy powerfull stuff."
    pc "Remember this night." 
    "There was my final words, before turning to leave the apartment."
    jump flee
    
    return

label impregnate:

    show full sex tears
    "I smirked down at her, enjoying her humiliation."
    pc "On your hands and knees!" 
    "I ordered once more, and Kristen complied, her body shaking with fear and exhaustion."
    "I moved behind her, positioning himself at her entrance. With one swift thrust, I entered her, causing her to cry out in pain as I stretched her beyond what she thought possible."
    "I didn't give her a moment to adjust, instead pounding into her relentlessly, each thrust driving her further into the floor."
    "Kristen could feel her tears falling onto the hardwood beneath her, mingling with the sweat that dripped from her body."
    "As I fucked her brutally, I reached around and began to roughly massage her clit, my fingers digging into her sensitive flesh." 
    k "No... please..." 
    "She whimpered again, but her body betrayed her, responding to my touch despite the pain and humiliation."
    "Her hips began to move in sync with my, her pussy clenching around my cock as she unwillingly approached another orgasm."
    pc "You like that, bitch?" 
    "I growled, my breath hot on her neck."
    pc "Do you like being fucked like a dirty little whore?" 
    "Kristen couldn't deny it - the pleasure was overwhelming, even amidst the fear and degradation."
    "She moaned loudly as her climax approached, her entire body trembling with the force of it."
    "With a final thrust, I drove himself deep inside her, holding still as I came, my hot seed spilling into her."
    "Kristen cried out, her own orgasm ripping through her as she shuddered beneath me. As the waves of pleasure subsided, she collapsed onto the floor, her body spent and her spirit broken."
    "I stood above her, my chest heaving from exertion. I looked down at her with disdain, as if she were nothing more than a used condom."
    pc "I'm done with you."
    jump flee
    
    return

label cum_ass:

    show full anal
    "As I invide her rectum, Kristen screams again, her body shaking violently under the onslaught of my thrusts."
    "I can feel her tightness starting to give way, her ass adjusting slightly to accommodate my girth."
    pc "That's it, take my cock like a good little whore."
    "Kristen's vision goes blurry as I continues to pound into her, the pain becoming too much for her to handle."
    "She feels like she's going to black out from the intensity of it all, but I show no signs of stopping."
    "I grunt, feeling my orgasm building deep within me. I grabs Kristen's hair roughly, pulling her head back as I thrusts even harder into her ass."
    pc "You're gonna take my cum," 
    "My voice rough with lust and dominance."
    pc "And you'll fucking love it!"
    "Kristen whimpers, feeling my grip on her hair tightening as I continues to pound into her."
    "She can feel my cock throbbing inside her, ready to explode at any moment."
    k "Please… stop..." 
    "She begs weakly, her body shaking with each brutal stroke."
    "My orgasm crashes over me like a wave, and I grunts loudly as I empties me balls deep inside her bowels."
    "Kristen screams in pain and pleasure as she feels my hot seed filling her up, the intensity of it all too much to bear."
    "I pull out slowly, leaving her gasping for air on the floor."
    pc "You took it like a good little slut," 
    "I pant, wiping my sweaty brow with the back of my hand."
    "Kristen lies on the floor, her body shaking and covered in sweat. She feels drained, both physically and emotionally, as she tries to process what just happened."
    "Tears stream down her face as she looks up at I through tear-filled eyes."
    k "Why…?" 
    "She whispers weakly, not understanding why I did this to her."
    "I smirk, looking down at her with a mix of satisfaction and contempt."
    pc "Because I could." 
    "I say it felling empowered by this show of domination, before turning to leave the room."
    jump flee
    
    return

label flee:
    scene bg room

    "She lying motionless on a floor in a puddle of my semen. Time to get out!"

    "FIN"

    return

