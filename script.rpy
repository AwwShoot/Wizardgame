# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("") #Nameless character for narration
define y = Character("You") #You moment
define r = Character("Recruiter") # Recruiter at the booth. Only exists for the starting scene.
define e = Character("Esteban") # Muscle wizard.
define a = Character("Anin") # Prankster alchemist
define b = Character("Belladonna") # Dommy mommy

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    y "(Ah, the Great Scribe Seminar, I'm finally here. This is where the best of the best scribes, clerics, and authors gather to discuss all things writing.)"
    y "(With any luck, I can finally get a high-paying gig here. No more copying menus for McTaverns from here on out!)"
    y "(I still sometimes write their slogan in my sleep... *Shudders*)"

    n 'You try to blot out promotional offers for "The new dragon nuggets! Now 25% less likely to start a barfight!" from your memory as you scan the booths'
    n "libraries, academies, and political publishers line the wall, each one offering a competitive rate for a professional scribe like yourself."

    n "But the one thing that catches your eye is a blue and gold booth for what appears to be a wizard academy."

    y "(I've always wanted to work with wizards! What an honor it would be to help write studies about real magic.)"

    n "You approach the booth hopefully. The recruiter catches your eye and waives you over."

    r "Hello! Are you interested in copying and reprinting the manuscripts of one of our wizards?"

    y "More than anything else! but, erm, why don't the wizards copy their manuscripts with magic?"

    r "Using magic to copy magical notes can have some... unintended side effects. I mean, just look at Esteban over there."

    show esteban

    e "huh?"

    y "He doesn't seem that bad... In fact, I've never seen wizard be so fit."

    e "Thanks nerd."

    n "Esteban grabs an unnocupied chair and begins lifting it like a dumbell"

    hide esteban

    r "*qiuetly laughs* anyways... we need scribes like you. We can offer you twice as much as anyone else here, plus you'll have living arrangements with your client."
    r "You'll be staying with the wizard you decide to work with so they can look over your work and make sure it fits our standards."

    y "Living with a wizard AND copying their magical notes!? This sounds too good to be true!"

    r "Well we are expecting one hundred high quality copies from you. This is not a job that you can do one the side or quit partway through. Are you sure you want to sign up?"

    y "totally!"

    n "As you finish the contract, the recruiter chuckles ominously."

    r "THE CONTRACT IS SEALED."

    y "(Why does every employer do that?)"

    r "You've seen Esteban now, here are the other two wizards who are looking for a scribe currently."

    show anin happy

    r "This is Anin, an alchemist."

    a "Nice to meet you."

    n "Anin holds out their right hand. You shake it without hesitation to find it seems to be rather sweaty. You try to wipe your hand off on your shirt, but it just sticks to you."
    n "Anin quietly laughs."

    r "And this is Bella."

    show belladonna angry

    b "That's Lady Belladonna to you. I will expect nothing less than perfection in my manuscript."

    y "Can do!"

    r "I'm sure you can. Anyways, you signed away your right to back out of the deal now, so just pick one."

    y "But I barely even know who they are, much less what they actually study!"

    r "Go ahead then, ask a few questions."

    jump question_hub:

    label question_hub:
        menu:
            "What do you all study?":
                jump study

            "What are your manuscripts like?":
                jump manuscripts

            "What are your living arrangements like?":
                jump living

            "No more questions":
                jump pre_interview_hub







    label: study
        show esteban

        e "Wouldn't you like to know, nerd!"

        y "Yes... I would..."

        show anin mischeivious

        a "Here, take my business card"

        n "Anin holds out a minimalistic, red card. He seems to be grinning mischeivously"
        n "You get the feeling this card will do more harm than good."

        y "I'm fine for now, thank you."

        show Belladonna angry

        b "I study the the natural magical properties of all toxic plants. My manuscript catalogues each and every known naturally occuring plant toxin."
        b "Ordered by method of delivery, lethality, then alphabetically. "
        b "Do you understand?"

        y "Uh, I think so."

        b "I expected better than 'thinking so' from you."

        y "(Geez what did I sign myself up for?)"

        jump question_hub

    label manuscripts
        show anin neutral

        a "You'll need to copy my alchemical formulae perfectly, we can't have any accidents, can we?"

        show belladonna neutral

        b "I expect you to faithfully recreate my writing and illustrations. Your penmanship must be flawless, not one stray mark."

        show esteban

        e "You'll have to touch it up on your own. It better be nice and organized when you're done."

        y "(is that even copying or am I just rewriting your manuscript at that point?)"

        jump question_hub

    label living
        show belladonna happy

        b "You will spend your time working with me in my greenhouse. It's full of the most delightful flowers..."
        b "If you want to live, don't touch any of them!"

        y "(What!? Am I getting hazard pay?)"

        show esteban

        e "The library's also where I work out. I'm not gonna stop my routine just to look over your shoulder."

        show anin happy

        a "I actually have a clean study room for you, unlike the other two."

        y "(Great.. why does living with a wizard suddenly sound less whimsical and magical?)"

    # End of the introduction. On to the meat of the game!

    label pre_interview_hub:
        r "Alrighty, now pick one. Pick someone to spend the next few years living with and working under."

        y "Wait! Can't I get to know them a little bit more? I've spent like five minutes with each wizard."

        r "What? Like a date?"

        y "Huh? no! I want to interview them!"

        r "Sure you do..."

        n "You leave the symposium confused, a little terrified, and with your hand still stuck to your shirt..."

        default anin_interviewed = False
        default bella_interviewed = False
        default esteban_interviewed = False
        jump interview_hub


    label interview_hub:
        y "Now who should I interview..."

        menu:
            "Anin":
                jump anin

            "Bella":
                jump bella

            "Esteban":
                jump esteban

            "I suppose I should just pick one now...":
                jump endings


    label anin:
        $ anin_interviewed = True
        default anin_outwitted = False
        default anin_good_ending = False
        bg anin study

        n "You set up an appointment to interview Anin, and today's the day. Their study is a modest building separated from the rest of the academy."
        n "Several chimneys rise out from the roof, and one side of the building lacks a wall, making it an open-air laboratory."
        n "You cautiously knock on the door, and are promptly geeted by Anin."

        show anin happy

        a "Hey! You made it! Come on in! Welcome to my lab."

        show anin flustered

        a "By the way, sorry about getting your hand stuck to your shirt the other day. It was an honest alchemical mistake..."

        n "Anin ushers you inside and leads you to his study. It's a rather tidy space. The walls are arrayed with ingredients and potions on shelf after shelf."
        show anin happy
        a "So, you want to interview me? Ask away!"
        jump anin_questions:

        label anin_questions:
            menu:
                "May I see your manuscript?":
                    jump anin_manuscript

                "Do you have any hobbies?":
                    jump anin_hobbies

                "What's with the floating bottles around you?":
                    jump anin_bottles

                "No more questions. Do you have any questions for me?"
                    jump anin_interview_end


        label anin_manuscript:
            a "Sure! Be careful though, I've had a few spills in the process of writing it."

            n 'They hand you a somewhat stained binder labelled "Acids, Adhesives, and all things affected". The binder is thick with pages upon pages of notes.'
            n "With some effort you manage to separate a few pages and get a good look at their contents. They are dense with complex alchemical symbols and instructions."

            a "I'll be happy to have a clean copy, that's for sure. The rest of the copies you make will be distributed to my colleagues."
            show anin neutral
            a "You might have to go deliver some of them for me as well. I'm not quite popular among other alchemists."

            menu:
                "Why not?"
                jump anin_manuscript_answer

                "(That's not my business)"
                jump anin_manuscript_no_answer

            label anin_manuscript_answer:
                show anin mischeivious
                a "Not all alchemists share my sense of humor. Of course that's not my problem..."
                a "But I seem to be awfully accident prone when they try to get back at me."
                a "I tend to spill acid when people get in my face to lecture me on professionalism."

                y "(Yikes!)"
                jump anin_manuscript_no_answer

            label anin_manuscript_no_answer:
                y "*ahem* anyways..."
                jump anin_questions

            label anin_hobbies:
                show anin neutral
                a "I don't really have any hobbies. I just focus on my studies."

                menu:
                    "Really? Well I love playing pranks on people.":
                        jump anin_hobbies_pranks

                    "You really don't have any spare time?"
                        jump anin_hobbies_no_pranks

                label anin_hobbies_pranks:
                    show anin happy
                    a "Oh? What kinds of pranks do you like? Should I be worried? haha."

                    menu:
                        "(Tell them about a harmless prank to a fellow scribe.)":
                            jump anin_hobbies_pranks_harmless

                        "(Make up a story about a more advanced prank)""
                            jump anin_hobbies_pranks_lie

                    label anin_hobbies_pranks_harmless:
                        y "Well, one time I jammed the quill of another scribe so badly that it snapped and leaked ink everywhere when he tried to use it."

                        a "Ha! That's pretty good! Just don't try that here. You might cause some hazardous chemical to spill and react."
                        a "Is there anything else you'd like to know about me?"
                        jump anin_questions

                    label anin_hobbies_pranks_lie:
                        $ anin_outwitted = True
                        y "Well, once I got a colleague's desk stuck closed with a full bottle of ink attatched to the inside."
                        y "When he finally yanked it open, the bottle spilled everywhere! His clothes were stained for a week!"

                        show anin angry

                        a "That wouldn't work at all! Common ink is to viscous to splash out of a container that much!"
                        a "Even if he yanked the drawer with all of his strength, it probably wouldn't even ruin the documents inside, much less spread to his clothes."

                        y "You sure know a lot about pranks."

                        a "Certainly more than you. You've already fallen for one of the simplest pranks that exist back in the symposium."

                        y "Aha! So that wasn't an accident!"

                        show anin surprised

                        a "What? No I was... uhm... another prank on another person or-"

                        y "Gotcha."

                        show anin flustered

                        a "Dammit! You're clever. I'll give you that."

                        y "so you're not going to prank me while I'm writing for you, right?"

                        show anin mischeivious

                        a "Certainly not~"

                        y "(It was worth a shot...)"
                        y "Anyways, I still have an interview to conduct."
                        jump anin_questions

        label anin_bottles:
            a "These? They're some of my more caustic experiemnts."

            y "Why on earth do you keep them hovering next to you at all times?"

            a "I need to keep an eye on them. If they turn unstable I need to be around so I can neutralize them before something happens."

            show anin mischevious

            a "Besides, people tend not to get in your face when they know you could accidentally spill acid on them at any moment."

            y "How often do people get in your face for you to need to threaten them with acid!?"

            a "You know alchemists... they really can't take a joke."

            y "(How bad are your jokes!?)"
            y "erm... maybe let's move on to another question"

            jump anin_questions

        label anin_interview_end
            a "Actually I do have one."

            show anin neutral

            a "Could you show me your handwriting? I need to know if you can cleanly recreate all of the formula symbols I use."
            a "There's some paper in the top compartment of my desk and I keep an ink bottle on top for you to use."
            a "Be careful though, my ink likes to bleed through the paper."

            n "True enough, there is a fresh bottle of ink sitting atop the desk."
            n "As you take a sheet of paper from the desk you see another ink bottle. The sides are stained with ink like it's already been used a lot."

            menu:
                "(No need to rummage around, I'll use the fresh ink bottle.)":
                    jump anin_interview_end_pranked

                "(This is fishy. I'll use the older ink bottle in case the new one is a trap.)":
                    jump anin_interview_end_not_pranked

            label anin_interview_end_pranked:
                n "As you trace over a few alchemical symbols, you suddenly feel something dripping on your leg."
                n "You shift your chair back to reveal that the ink not only bled through the paper, but the table itself to stain your pants."

                y "*Sigh* this interview is over"

                n "You stand up and leave while most of your dignity is intact and your pants aren't too stained."
                $ anin_good_ending = True
                jump interview_hub

            label anin_interview_end_not_pranked:
                n "You hear Anin quietly sigh as you pull out the spare ink bottle. You trace over the alchemical symbols with ease."

                if anin_outwitted:
                    a "Not bad."

                    y "My writing? Or the fact that I avoided your little prank."

                    show anin flustered

                    a "Damn, you're good. Your handwriting, that is. I'd be happy to have you copy my manuscript"

                    y "So you won't prank me if I work for you?"

                    show anin mischevious

                    a "I never said that."

                    y "It's time I left anyways. I have other interviews to conduct."

                else:
                    a "Your symbols are alright. I suppose I wouldn't mind you copying my manuscripts..."

                    y "Thanks. I'll keep you in mind."
                    n "You walk out of the laboratory. Was that fresh bottle of ink really trapped? Or did you just use their spare bottle for no reason."
                    jump interview_hub

    label bella:
        default bella_good_ending = False
        default flowers_picked = False
        default red_flowers = False
        default blue_flowers = False
        default purple_flowers = False
        n "Greenhouses and gardens line the botanical wing of the academy. Beautifully sweet fragrances fill the air."
        n "A particularly long stretch of flowers remains between you and Belladonna's greenhouse."
        menu:
            "(There are so many flowers here, surely a few won't be missed.)"
                jump bella_flowers

            "(I should not mess with the garden.)"
                jump bella_approach.

        label bella_flowers:
            n "Within the field, several flowers stand out to you as particularly pretty."
            n "There are some blue flowers with very broad petals. Each bloom seems to expand out to be as big as your hand."
            n "Adjacent to the blue flowers is a row of bright crimson poppies. Perhaps their medicinal properties will be useful."
            n "Further down the row is a bed of enchanting indigo flowers. Each bloom is small and unimpressive, but the sheer number of petals catching the sun makes for a dazzling display."
            n "In front of the purple flower beds appears to be a warning sign to inform readers that the plants may contain a mild poison in their petals."

            menu:
                "(The blue flowers seem impressive. I'll take some of those.)":
                    $ blue_flowers = True
                    n "You pick a particularly large specimen and continue to Belladonna's greenhouse."
                    jump bella_approach
                "(The poppies may come in handy. It couldn't hurt to take a few)"
                    $ red_flowers = True
                    n "You take a handful of poppies. Perhaps Belladonna can help you get their extract."
                    jump bella_approach
                "(Girls love poisonous flowers, right?)"
                    $ purple_flowers = True
                    n "With some hesitation, you grab a few indigo blooms. Your hands itch where the petals brushed against them."
                    jump bella_approach
        label bella_approach:
            n "You approach Belladonna's greenhouse. It's just as beautiful as the rest. Inside it, vibrant purple flowers line the insides."
            n "As you open the door, the gardener stands up from tending to her flowers and looks down at you coldly."

            show bella angry


    return
