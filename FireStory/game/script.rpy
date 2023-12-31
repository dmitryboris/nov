﻿# Определение персонажей игры.
define narrator = Character(what_italic=True)
define nvl_narrator = Character(kind=nvl)
define e = Character('OSEL', color="#c8ffc8")
define max = Character('Максим', color="#13678A")
define max_mad = Character('Максим', color="#13678A", what_size=38)
define mom = Character('Мама', color="#45C4B0")
define mom_mad = Character('Мама', color="#45C4B0", what_size=38)
define dad = Character('Папа', color="#9AEBA3")
define misha = Character('Миша', color="#DAFDBA")
define team = Character('Команда', color="FF0000")

define scenedissolve = Dissolve(2.0)
define clockdissolve = Dissolve(3.0)
define characterdissolve = Dissolve(0.5)

label start:
    scene black
    show text "{size=50}{font=DejaVuSans-Bold.ttf}Cherti Entertainment presents{/font}{/size}" with Dissolve(2.0)
    hide text with scenedissolve
    show text "{size=50}{font=DejaVuSans-Bold.ttf}{cps=30}Акт 1. Начало{/cps]}{/font}{/size}" with Dissolve(2.0)
    hide text with scenedissolve


label beginning:
    play music forest fadein 1 volume 0.2
    scene house
    narrator "Мы видим красивый и уютный дом, где живет подросток Максим со своими мамой Еленой и \
              отцом Александром. Они счастливая семья. Максиму 15. Он интересуется \
              пожарной безопасностью, часто разговаривает с мамой о ее работе в МЧС."

    play sound clock
    nvl_narrator "{cps=30}Максим радостно открывает глаза.{/cps} \n"

    define menu = nvl_menu
    menu:
        nvl_narrator "{cps=30}Сегодня выходной, а значит не нужно идти в школу.{/cps}\n"
        "{u}Встать с постели{/u}.":

            nvl clear

    nvl_narrator "{cps=30}Максим садится на диван и решает дочитать книгу о пожарной безопасности.{/cps} \n"
    define menu = nvl_menu
    menu:
        nvl_narrator "{cps=30}Он начал ее читать только вчера.{/cps} \n"
        "{u}Открыть книгу{/u}.":

            nvl clear

    scene mainroom
    show max at left
    show mom at right with characterdissolve
    stop music fadeout 1
    play music witcher_relax fadein 1 volume 0.1
    max "Мама, я снова читаю о пожарной безопасности. Это на самом деле очень интересно."
    mom "Он снова погружен в книги. Что нового ты узнал, Максим?"
    max "Сейчас я читаю о том, как правильно пользоваться огнетушителем. Ты мне рассказывала, \
           что иногда приходится его использовать на работе, верно?"
    mom "Да, Максим, иногда приходится использовать огнетушители для тушения небольших пожаров, \
    чтобы не допустить их распространения. \nКакой еще полезной информации ты нашел?"
    max "Я узнал, что также очень важно знать, как покинуть дом в случае пожара. \
       Мы все дружно должны покинуть здание через ближайший выход и немедленно вызвать пожарных."

    show mom at center with characterdissolve
    show dad at right

    dad "О, о чем вы говорите?"
    mom "Максим читает о пожарной безопасности и делится своими новыми знаниями."
    dad "Отлично, сынок! Так важно быть готовым к чрезвычайным ситуациям. Вы и ваша мама знаете это лучше всего."
    max "Спасибо, папа. Я думаю, что это важно для всех, даже если мы не работаем в МЧС."
    mom "Абсолютно правильно, Максим! Пожарная безопасность – это наш общий интерес, потому что охрана нашей семьи и дома – наша первоочередная задача."
    dad "Мы – счастливая семья, и это, означает быть заботливыми друг к другу и гарантировать безопасность каждому члену."

    show dad at center with characterdissolve
    show mom at right with characterdissolve

    max "Я обещаю, что всегда буду следовать выученным правилам. Ведь знать, что делать в случае пожара – это крайне важно."
    mom "Мы верим в тебя, Максим. Ты уже вырос в ответственного и заботливого парня."
    dad "И помни, что мы всегда здесь, чтобы поддержать и помочь тебе в любой ситуации."
    max "Спасибо, мама и папа! Я очень рад, что у нас такая сильная и заботливая семья."
    stop music fadeout 1

label fire:
    scene main_menu with clockdissolve
    nvl_narrator "Однажды, в середине ночи, в доме происходит ужасный пожар. Все пытаются выбраться, \
    но огонь разгорается слишком быстро. Максим и его мама Елена оказываются в ловушке."
    nvl clear

    play music fire fadein 1 volume 0.2
    scene fire1
    show max_shocked at center
    show mom_mad at right

    max_mad "Мама, что мы делаем? Как выбраться отсюда?"
    mom_mad "Быстро, Максим! Нужно двигаться к окну! Закрой рот и нос полотенцем, чтобы не дышать ядовитым дымом. Следуй за мной!"
    max_mad "Но, мама, ты не можешь оставить меня здесь одного!"

    hide max_shocked
    show max at left with characterdissolve
    hide mom_mad
    show mom at center

    mom "Я никогда не смогу тебя оставить, мой малыш. Но сейчас самое важное - спасти тебя. Иди за мной, я создам проход сквозь огонь."
    max "Я боюсь, мама. Что, если мы не выберемся? Что, если ты останешься тут со мной?"
    mom "Дорогой, ты сильный и умный. Я верю в тебя. Просто следуй за моим голосом и не отступай от меня. Я буду рядом, пока мы не выберемся."
    max "Хорошо, мама. Я буду слушаться."
    mom "Вот идем, держись за меня крепче. Мы справимся вместе."

    narrator "Максим и Елена медленно идут сквозь густой дым, огонь и опасности. Елена удаляет горящие обломки и создает проход для них. Наконец, они достигают окна."

    max "Мама, мы почти там! Собери все свои силы!"
    mom "Сейчас... Спаса....йся"
    max_mad "Мама! МАМА!"

    stop music fadeout 1

    scene fire2
    narrator "Максим выбирается из окна, а затем обращает взор назад и видит, что Елена не смогла выбраться. Он понимает, что его мама погибла, спасая его."

label second_act:
    scene black
    show text "{size=50}{font=DejaVuSans-Bold.ttf}Акт 2. Путь к исполнению мечты{/font}{/size}" with Dissolve(2.0)
    hide text with scenedissolve

label yearning:
    scene forest with scenedissolve
    play music forest fadein 1 volume 0.2

    narrator "Максим остается с отцом Александром, который с грустью смотрит на своего сына, понимая, как сильно они оба переживают по поводу утраты."
    narrator "Максим решает стать пожарным, чтобы помогать другим людям и больше не приключалось таких ситуаций."

    show max at center
    show dad at right

    max "Отец, я решил. Я собираюсь стать пожарным. Я хочу помогать людям, уводить их от опасности и предотвращать подобные трагедии."
    dad "Мой сын, ты всегда был щедрым и отзывчивым, но это такая опасная и ответственная профессия. Я не хотел бы, чтобы ты подвергал себя опасности."
    max "Я понимаю, папа. Но я не могу просто смотреть, как люди теряют свои жизни и имущество из-за пожаров. Если я смогу помочь хотя бы одному человеку, я буду счастлив."
    dad "Я понимаю твое желание помогать другим, мой сын. Это благородно. Но я беспокоюсь о тебе. Жизнь пожарного может быть очень опасной, и я не хочу терять тебя."
    max "Папа, не волнуйся. Я буду тренироваться и стану самым лучшим пожарным, чтобы минимизировать риски. Я обещаю быть осторожным и заботиться о собственной безопасности."

    scene forest2
    show max at left
    show dad at center

    dad "Ты так похож на маму. Она тоже всегда помогала и заботилась о других. Я знаю, что я не могу остановить тебя от этого решения, и ты заслуживаешь поддержки."
    max "Спасибо, папа. Твоя поддержка значит для меня много. Я обещаю, что буду делать все, что в моих силах, чтобы помогать людям и предотвращать пожары."
    dad "Я верю в тебя, сынок. Будь осторожен и заботься о себе, а также о тех, кто находится в опасности. Ты сделаешь мир лучше."
    max "Я обещаю, папа. Благодаря тебе и маме я знаю, что я могу сделать это. Будь спокоен, я буду следовать своей мечте и помогать людям."
    stop music fadeout 1

label studying:
    scene black
    nvl_narrator "Максим безумно серьезно подходит к своей цели. Он тратит каждую свободную минуту \
    на учебу и тренировки. Максим хорошо сдает экзамены и поступает на обучение в УрФУ."
    nvl_narrator "А именно на направление Техносферная безопасность."

    nvl_narrator "Он погружается в интенсивные тренировки и учебу. Он учится разбираться с огнем, пользоваться экипировкой и работать в команде."
    nvl_narrator "Максим проходит испытания и тренировки со своими товарищами по университету, становится все сильнее и опытнее."

    nvl clear

    play music crowd fadein 1 volume 0.2
    scene urfu
    narrator "На одном из тренировочных занятий Максим работает в команде с Мишей, его близким другом из академии."

    show max at left
    show misha

    max "Это было что-то с чем-то! Я даже не мог себе представить, что обучение может быть таким трудынм."
    misha "Да, Максим, каждый день мы все сильнее и опытнее. Но это тот путь, который мы выбрали — стать лучшими и справиться с ответственностью, которая лежит на нас."
    max "Ты прав, Миша. Нам доверена возможность защищать себя и других людей. Не можем допустить, чтобы она попала в неправильные руки."
    misha "Согласен. Максим, ты с каждым днем становишься все сильнее и ловчее."
    max "Спасибо. Ты меня всегда поддерживал и наставлял на верный путь. Без тебя я бы не смог пройти через все эти испытания."
    misha "Помни, брат, мы — команда. Вместе мы сможем преодолеть любые трудности и добиться успеха."

    narrator "Максим и Миша обнимаются, продолжая улучшать свои навыки и прокладывая путь к успешному завершению академии."
    narrator "Их дружба и сотрудничество только укрепляются, и они смело вступают в свой следующий вызов, готовые преодолеть любые трудности, которые появятся у них на пути."
    stop music fadeout 1

label third_act:
    scene black
    show text "{size=50}{font=DejaVuSans-Bold.ttf}Акт 3. Герои нашего времени{/font}{/size}" with Dissolve(2.0)
    hide text with scenedissolve

label work:
    play music fire fadein 1 volume 0.2
    scene fire3
    narrator "Максим, Миша и их команда приходят на место возгорания, они одеты в защитные костюмы и снаряжены необходимым оборудованием."
    show max
    max "Все готовы, ребята? Это наш первый настоящий вызов, давайте покажем всем, на что мы способны!"
    team "Да, Максим, готовы с вами справиться с любой ситуацией!"
    max "Отлично! Давайте разделимся на команды – одна отвечает за спасение людей, а другая за тушение пламени. Пошли!"
    narrator "Команда начинает действовать. Одна группа выстраивается возле лестницы, чтобы эвакуировать людей, вторая группа направляется к источнику пожара с огнетушителями и шлангами."
    max "Проведите лестницу до окна на третьем этаже, дайте возможность людям покинуть здание!"

    narrator "В это время другая группа команды борется с огнем."
    hide max
    show misha
    misha "У нас есть дверь входа в горящее помещение. Давайте приступим к тушению, ребята!"
    team "Все в порядке, Владимир! Что насчет того, чтобы воспользоваться огнетушителем c газопенным составом?"
    show misha at left
    show max at right
    narrator "Команда продолжает тушить пламя, бущующее в здании. Максим активно координирует действия команды и следит за безопасностью всех."
    narrator "В тот день бригада проявляет большое мастерство и смелость. Они успешно справляются со своими обязанностями и спасают много жизней."

    stop music fadeout 1

label epilog:
    scene main_menu with scenedissolve
    nvl_narrator "Максим становится известным в своем городе и получает благодарность от всех, кого он спас. \
    Город узнает его имя и историю о том, как он потерял мать, но нашел силы помогать людям."
    nvl_narrator "Максим становится примером надежды и вдохновения для других. Он понимает, что он принес пользу\
     обществу и всегда будет помогать людям в трудных ситуациях."
    nvl clear

    play music witcher_relax fadein 1 volume 0.1
    scene street
    show max at center
    show dad at right

    dad "Максим, мой сын, я не могу объяснить, насколько я горжусь тобой. Ты не только стал мужчиной, но и примером истинной силы и сострадания."
    dad "Ты преодолел много испытаний и спас множество жизней. Я горжусь тобой."
    dad "Весь город говорит о тебе и думает о тебе как о герое. Ты - моя главная гордость."
    max "Спасибо, папа. Я никогда не считал себя героем, я просто делал то, что казалось правильным."
    max "Но видеть, как мои действия влияют на других, как я могу приносить радость и надежду в жизнь людей, - это непередаваемое чувство."
    max "Я понял, что помощь и сострадание - это то, что действительно приносит смысл и пользу в наше общество."
    stop music fadeout 1

label end:
    scene main_menu with scenedissolve
    show text "{size=100}{font=DejaVuSans-Bold.ttf}The end{/font}{/size}" with Dissolve(2.0)