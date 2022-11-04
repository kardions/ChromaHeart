# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jax")
define r = Character("Ra3n")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene dystopian_bg with wiperight
    play music raen
    show raen_smile at right with dissolve

    # These display lines of dialogue.

    r "You're finally awake!"

    r "Or should I say 'finally entered the Dreamscape'?"

    r "C'mon! There's so much I need to show you!"

    show raen_normal at right with dissolve

    menu:

        "How should I respond?"

        "Wait...Who are you?! And where am I?!":

            jump yes

        "Say nothing":

            jump no

    label yes:

        show raen_awkward at right with dissolve

        r "Oh, right, haha."
        r "There's a lot you've missed since going to sleep."
        r "You see, you're in a simulation. Don't freak out! You'll be waking up again soon... ish."
        r "Hold on--"
        r "Before I continue, do you remember your name?"

    menu:

        "DO I remember my name?"

        "Yes; tell him your name.":

            jump yesr1

        "No; tell him you do not remember your name.":

            jump nor1

    label no:

        show raen_awkward at right

        r "Hmm... I remember you being more talkative."
        r "This time DID have more complications, though... so I guess it makes sense."
        r "There's a lot you've missed since going to sleep."
        r "You see, you're in a simulation. Don't freak out! You'll be waking up again soon... ish."
        r "Hold on--"
        r "Before I continue, do you remember your name?"


        show raen_awkward at right

    menu:

        "DO I remember my name?"
        
        "Yes; tell him your name.":

            jump yesr1

        "No; tell him you do not remember your name.":

            jump nor1


    label yesr1:
        scene dystopian_bg
        show raen_smile at right

        r "Perfect! I'm so glad you're here in one piece, then!"


    return


    label nor1:
        scene dystopian_bg
        show raen_awkward at right

        r "Right. Okay, so I guess it didn't work then."
        r "Don't worry, you'll remember soon enough!"

    return
