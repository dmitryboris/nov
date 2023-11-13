# Определение персонажей игры.
define narrator = Character(what_italic=True)
define e = Character('OSEL', color="#c8ffc8")
define zhenya = Character('Женя', color="#13678A")
define mom = Character('Мама', color="#45C4B0")
define dad = Character('Папа', color="#9AEBA3")
define sm = Character('sm', color="#DAFDBA")
define teacher = Character('Учитель', color="FF0000")

define clockdissolve = Dissolve(3.0)
define characterdissolve = Dissolve(0.5)

  
label start:
    scene black
    show text "{size=50}{font=DejaVuSans-Bold.ttf}кто-то там представляет...{/font}{/size}" with Dissolve(2.0)
    hide text with Dissolve(2.0)
    
label wake_up:
    scene clock with clockdissolve
    # queue sound "tower_clock.ogg"
    # queue sound "tower_clock.ogg"
    # queue sound "tower_clock.ogg"
    "опять в школу(("
     

label on_kitchen:
    scene kitchen
    show mom at center
    mom "Женя, почему ты еще не в школе?"
    show zhenya at left with characterdissolve
    show mom at right with characterdissolve
    zhenya "Ну... я … это... проспал"
    mom "Проспал значит... давай бегом в школу!"

label at_school:
    scene class
    show zhenya at right with characterdissolve
    show teacher at center with characterdissolve
    hide zhenya
    teacher "Почему опоздал?"
    hide teacher
    show zhenya at right with characterdissolve
    zhenya "Хз"
    show teacher
    teacher "Раньше спать ложиться надо, все иди на место"

label go_home:
    scene street
    zhenya "пупупу"


label at_home:
    scene hall with fade
    show mom at center # mom_mad
    mom "Женя, ты опять ушел гулять, не сделав уроки?"
    show mom at right with characterdissolve
    show zhenya at left
    zhenya "Ну... дааа"
    mom "Иди делай, а я спать"

label fire:
    return
    
