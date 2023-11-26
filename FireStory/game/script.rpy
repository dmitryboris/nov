# Определение персонажей игры.
define narrator = Character(what_italic=True)
define nvl_narrator = Character(kind=nvl)
define e = Character('OSEL', color="#c8ffc8")
define zhenya = Character('Женя', color="#13678A")
define zhenya_mad = Character('Женя', color="#13678A", what_size=38)
define mom = Character('Мама', color="#45C4B0")
define mom_mad = Character('Мама', color="#45C4B0", what_size=38)
define dad = Character('Папа', color="#9AEBA3")
define sm = Character('sm', color="#DAFDBA")
define teacher = Character('Учитель', color="FF0000")

define clockdissolve = Dissolve(3.0)
define characterdissolve = Dissolve(0.5)


label start:
    scene black
    show text "{size=50}{font=DejaVuSans-Bold.ttf}ентертеймент представляет...{/font}{/size}" with Dissolve(2.0)
    hide text with Dissolve(2.0)

label wake_up:
    scene start with clockdissolve
    play sound "clock.mp3"
    nvl_narrator "{cps=30}Женя с трудом открывает глаза.{/cps} \n"
    define menu = nvl_menu
    menu:
        nvl_narrator "{cps=30}Идти в школу совсем не хочется.{/cps}"
        "{u}Встать с постели{/u}.":

            nvl clear


    # hide text with Dissolve(2.0)


label on_kitchen:
    scene kitchen
    show mom at center
    mom "Женя, почему ты еще не в школе?"
    show zhenya at left with characterdissolve
    show mom at right with characterdissolve
    zhenya "Ну... я … это... проспал"
    mom "Проспал значит... давай бегом в школу!"

label at_school:
    scene classroom
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
    "евгений решил прогуляться"
    show zhenya_shocked
    zhenya "пупупу"


label at_home:
    scene hall
    show mom_mad at center # mom_mad
    mom_mad "Женя, ты опять ушел гулять, не сделав уроки?"
    show mom_mad at right with characterdissolve
    show zhenya at left
    zhenya "Ну... дааа"
    mom_mad "Иди делай, а я спать"

label fire:
    scene ignition
    show zhenya_shocked at left
    zhenya_mad "Пожар!"
    scene fire1
    "На маму падала горящая балка"
    show zhenya_shocked at right
    zhenya_mad "МАМА!"
    show dad at left
    dad "Уходим"
    zhenya_mad "отпусти!! надо помочь маме!"
    scene fire2
    "у вас мать сгорела"

label next_act:
    scene black
    show text "{size=50}{font=DejaVuSans-Bold.ttf}Акт второй{/font}{/size}" with Dissolve(2.0)
    hide text with Dissolve(2.0)


