# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("Aetheria")
define m = Character("Marcus")
define j = Character("Jax")
define r = Character("Ra3n")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    play music glitter volume 0.5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show aetheria normal at left
    show marcus normal at right

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    m "Once you add a story, pictures, and music, you can release it to the world!"

    e "This is more placeholder text before the next scene."

    m "Let's start the game, shall we?"

    scene space_bg with wipeleft
    show aetheria normal at right
    show marcus normal at left

    m "this is more placeholder text"

    e "we're testing stuff out"

    m "please bear with us"

    scene space_bg with dissolve
    play music aunt volume 0.5
    show jax_normal at left with wipeleft

    j "i'm a new character"

    j "i'm here to help test out using new images and audio"

    show jax_sad at left with dissolve

    j "that's all from me now!"

    show jax_mischief at left with dissolve

    j "bye!"

    scene space_bg with pushright
    play music raen volume 0.5
    show raen_normal at right with dissolve

    r "hey... the name's Ra3n. It's pronounced 'Rain'."

    show raen_awkward at right with dissolve

    r "I'm the anxious alien character"

    r "LOL bye"

    # This ends the game.

    return
