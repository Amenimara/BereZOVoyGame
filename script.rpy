#(ГАЙД) чтобы запустить код надо скачать RenPy и добавить в папку проектов папку игры а потом запустить проект

#для себя
#звуки сделать (толпы там, улицы и т.д.)
#катсцены и фон площади
#ФОН МЕНЮ
#концовки
#gui customization

define gui.text_font = "AgcoopercyrItalic.ttf"

define n = Character("Нана", color = "#e769c1")
define m = Character('Майк', color="#6e6cec")
define vor = Character("Вор", color = "#3c2149")
define a = Character("###", color = "#0c0202")
define meh = Character("Механик", color = "#a6db44")
define f = Character("Фермер",color = "#dad60c")
define t = Character("Торговец", color = "#8a5d0b")
define mf = Character("Максим Фантомас", color = "#44db58")
define d = Character("Дмитрий Форбс", color = "#f0cc03")

#images
#Бекграунды
image bgcityview = "bg/bg1.png"
image bgstart = "bg/bg2.png"
image bgenter = "bg/bg3.png"
image bgcityinside = "bg/bg_enter.png"
image bgmehhome= "bg/bg_mehhome.png"
image bg_ship = "bg/bg_ship.png"
image bg_broadcast = "bg/bg_broadcast.png"
image bg_farm = "bg/bg_farm.png"
image bg_park1 = "bg/bg_park1.png"
image bg_park2 = "bg/bg_park2.png"
image bg_park3 = "bg/bg_park3.png"
image bg_park4 = "bg/bg_park4.png"
image bg_market1 = "bg/bg_market1.png"
image bg_market2 = "bg/bg_market2.png"
image bg_torghome = "bg/bg_torghome.png"
image bg_dhome = "bg/bg_mfhome.png"
image white = "bg/white.jpg"
image goodend1 = "bg/goodend1.png"
image goodend2 = "bg/goodend2.png"
image skip = "bg/skip.png"
image speech = "bg/speech.png"

#Иконки
image in1= "icon/nana.png"
image pes = "icon/pes.png"

#Спрайты
#механик
image meh1 = "sprites/meh1.png"
image meh2 = "sprites/meh2.png"
image meh3 = "sprites/meh3.png"
#фермер
image f1 = "sprites/fermer1.png"
image f2 = "sprites/fermer2.png"
#Вор
image vor1 = "sprites/voruga1.png"
image vor2 = "sprites/voruga2.png"
# торгаш
image t = "sprites/lapa.png"
#ФАНТОМАС
image mf = "sprites/mf.png"
#богатый 
image d = "sprites/vasyan.png"


#variables
init: 
    $ fermer = 0
    $ torg = 0
    $ fant = 0
# DAY 1

label start:
    scene black
    play music "siren.mp3" fadein 1 fadeout 1
    pause 1.0
    n "О нет…{w} Что-то случилось с нашим кораблем!"
    scene bgstart with dissolve
    #звук сирены
    
    show in1 with dissolve
    n "Майк, проверь как можно быстрее датчики! "
    hide in1

    show pes with dissolve 
    m "Гав! {w}Тут показано, что у нас совсем не осталось топлива!!!{w} Если мы не приземлимся как можно скорее, то мы навсегда тут останемся и станем КОСМИЧЕСКИМ МУСОРОМ!"
    hide pes

    show in1 with dissolve 
    n "Тогда нам незамедлительно нужно найти ближайшую планету!"
    hide in1

    show pes with dissolve 
    m "НАШЕЛ! Самая близкая - это Кристалис!"
    hide pes
        
    show in1 with dissolve 
    n "Тогда летим к ней"
    hide in1
    stop music fadeout 1
    play sound "babah.mp3" fadein 1 fadeout 2
    
    scene black with dissolve
    pause 5
    jump cityview

label cityview:

    scene bg_ship with dissolve
    stop sound fadeout 1
    show in1 with dissolve 
    n "Какой ужас… Майк! У нас не только топливо закончилось, но и сломалось 4 модуля у корабля!"
    hide in1
    
    show pes with dissolve 
    m "Что же нам делать!? Неужели мы никогда от сюда не выберемся?{w} А как же мер?{w} Мы же должны быть там через 5 дней, чтобы получить землю за наш с тобой упорный труд, но если мы не вернемся, то все было зря!"
    
   
    m "Я не хочу тут оставаться…{w}Гав…"
    hide pes

    scene black with dissolve
    pause 0.5

    scene bgcityview with dissolve

    show in1 with dissolve 
    n "Так! Без паники! Я вижу там недалеко город! {w}Там должен быть Механик, который поможет нам с кораблем и мы сможем вернуться домой"
    hide in1

    show pes with dissolve 
    m "Гав"
    hide pes
    scene black with dissolve
    pause 0.5

    jump cityenter

label cityenter:


    scene bgcityinside with dissolve
    play music "maintheme.mp3" 
    show in1 with dissolve 
    n "Хмм… Я думаю можно спросить у местных жител..{w}.{w}{cps=5} ..АААААА….{/cps}"
    hide in1

    show pes with dissolve 
    m "ГАВ!{w} ГАВ!{w} ГАВ!"
    hide pes

    show vor2 with dissolve
    vor "{cps=5}НЕТ, НЕТ, НЕТ!{/cps} Я БОЛЬШЕ НЕ БУДУ ВОРОВАТЬ! ТОЛЬКО НЕ БЕЙТЕ!"

    show in1 with dissolve 
    n "Что? Я ничего не понимаю"
    hide in1

    hide vor2
    show vor2 at left
    show meh1 with dissolve
    meh "ПОПАЛСЯ! ТАК ТЕБЕ И НАДО, НЕГОДНИК! {w}Спасибо добрые люди, что помогли поймать этого воришку. Пошлите хоть чаем напою, да угощу Вас чем-нибудь вкусненьким!"

    show in1 with dissolve 
    n "Спасибо! Мы как раз проголодались после долгой дороги"
    hide in1

    show pes with dissolve 
    m "ГАВ"
    hide pes
    hide meh1 with dissolve
    hide vor2 with dissolve
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.5

    jump mehhome

label mehhome:

    show text "нана рассказала все о том, как она тут оказалась" at truecenter with dissolve 
    pause 1 
    hide text with dissolve

    scene bg_mehhome with dissolve
    play music "hometheme.mp3"
    show meh1 with dissolve
    meh "Мдаа… {w}Ну ремонт выйдет вам недешево. За то, что вы помогли в поимке вора я возьму только 500 флориумов"
    hide meh1
    show meh2 with dissolve
    show in1 with dissolve
    n "А как же мы сможем их заработать? Мы ведь ничего тут не знаем, да и мы должны вернутся на нашу планету через 5 дней"
    hide in1

    hide meh2
    show meh3 with dissolve
    meh "У нас есть местный рынок, где каждый день вывешивают объявления с работенкой, за которую можно получить флориумы. Он как раз находится недалеко от сюда!"

    show in1 with dissolve
    n "Хорошо! Майк, я знаю чем мы с тобой займемся"
    hide in1
    hide meh3 with dissolve
    stop music fadeout 1
    scene black with dissolve
    pause 0.5

    
    jump broadcast

label broadcast:

    scene bg_broadcast with dissolve
    play music "maintheme.mp3" fadein 1.0
    pause 1

    show in1 with dissolve
    n "Хмммм... тут написано, что фермеру нужна помощь в планировке бюджета для покупки семян и улучшений"
    hide in1
    #объявление Нужна срочная помощь в планировки бюджета для покупки семян и  улучшений!

    menu:
        "Помочь фермеру?":
            
            show in1 with dissolve
            n "О! Это отличная возможность заработать флориумы и помочь фермеру!"
            hide in1

            $ fermer += 1
            stop music fadeout 1.0
            scene black with dissolve
            pause 0.5
            

            jump ifhelp

        "Пойти дальше":

            show in1 with dissolve
            n "Мы можем оставшуюся часть дня погулять по городу и отдохнуть от всего!"
            hide in1 

            show pes with dissolve 
            m "Но разве нам не нужно починить корабль? У нас же совсем мало времени!"
            hide pes

            show in1 with dissolve
            n "Ну мы же должны хоть немного отдохнуть? {w}Мы столько пережили за сегодняшний день! Пошли лучше в парке посидим"
            hide in1
            stop music fadeout 1.0
            scene black with dissolve
            pause 0.5
            

            jump ifnothelp

label ifhelp:

    scene bg_farm with dissolve
    play music "hometheme.mp3" fadein 1.0
    show pes with dissolve
    m "Вроде бы пришли"
    hide pes

    show in1 with dissolve
    n "Хммм… И вправду, все выглядит как то грустно… Здесь есть кто нибудь?"
    hide in1

    f "Да, да, я тут!"
    show f1 with dissolve

    show in1 with dissolve
    n "Мы пришли Вам помочь.{w} Мои родители работают в банке и являются очень образованными людьми, которые с самого детства обучали меня и рассказывали много полезной информации в сфере финансов!"
    hide in1

    hide f1
    show f2 with dissolve
    f "{cps=20}Охх… {w}Даже не знаю с чего начать.. {w}Я из года в год пытаюсь заработать состояние, но мои не знания в планировании бюджета для покупок семян и его улучшений, рушат все планы{/cps}"

    show in1 with dissolve
    n "Хммм… Ну смотрите, весь этот процесс требует системного подхода.{w} Вот несколько шагов, которые могут помочь:"

    n "1-е - Оценка потребностей. Вы должны определить, какие культуры планируете выращивать и в каких объемах, а так же изучить требования к семенам, включая сорт, количество и качество."

    n "2-е -Анализ затрат. Собрать информацию о стоимости семян. Кроме того, оценить дополнительные расходы, связанные с улучшениями, такими как удобрения, средства защиты растений, полив. "

    n "3-е- Планирование доходов. Вы должны оценить потенциальный доход от продажи урожая. Учитывая  рыночные цены на выбранные культуры. И рассмотрите возможность получения грантов или субсидий, которые могут помочь в финансировании!"
    hide in1

    hide f2
    show f1 with dissolve
    f "{cps=20}Звучит здорово! Спасибо вам огромное! Я безумно рад, что встретил таких людей, как вы! Могу я вас чем нибудь отблагодарить?{/cps}"

    show pes with dissolve
    m "Гав! Гав!"
    hide pes

    hide f1
    show f2 with dissolve
    f "{cps=20}Точно!Я слышал у вас нет где переночевать ? Можете остаться у меня, я совсем не против, а, и еще! Возьмите пожалуйста 120 флориумов. Это за помощь! Я уверен, что благодаря вашим советам, я смогу научиться планировать свой бюджет!{/cps}"
    
    show in1 with dissolve
    n "Спасибо большое! Как хорошо же жить в мире с добрыми и людьми, не так ли Майк??"
    hide in1

    show pes with dissolve 
    m "Так точно!{w} ГАВ!"
    hide pes

    hide f2 
    show f1 with dissolve
    f "Чего ж вы стоите на улице до сих пор? Заходите быстрее!!!"

    show in1 with dissolve 
    n "уже идем!" 
    hide in1 with dissolve
    hide f1 with dissolve
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.5

    jump transition1

label ifnothelp:

    scene bg_park1 with dissolve
    play music "maintheme.mp3" fadein 1.0
    show pes with dissolve
    m "Как же хорошо гулять по парку и ничего не делать! Иногда так хочется просто полениться…"
    hide pes
    show in1 with dissolve 
    n "Дааа.{w} Я такого же мнения"
    hide in1

    show meh1 with dissolve
    meh "Чего ж вы тут сидите? Пошлите скорее в дом! Я приючу вас ненадолго!"

    show pes with dissolve
    m "Спасибо Вам огромное, как же хорошо, что на этой планете живут добрые и отзывчивые люди!"
    hide pes
    show in1 with dissolve
    n "Согласна с тобой, Майк! Пошли уже скорее домой!"
    hide pes

    hide meh1 with dissolve
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.5

    jump transition1

#день 2 другой скрипт

#АААААААААААААААААААААААААААААААААААААААААА ТУТ НАДО РАЗДЕЛЕНИЕ СДЕЛАТЬ БЛЯТЬ ААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААААА
#похуй
# DAY 2

label transition1: 
    #тут кароче анимка как она скипает ночь 
    scene skip with dissolve
    pause 1 
    scene black with dissolve
    jump secondday1
    
label secondday1:
    
    scene bg_mehhome with dissolve
    play music "hometheme.mp3" fadein 1.0
    show in1 with dissolve 
    n "Ох… {w}Вот как же хорошо спалось! Майк, ты как?"
    hide in1
    show pes with dissolve
    m "Гав!"
    hide pes
    menu:
        "Пойти на рынок":
            show in1 with dissolve 
            n "Замечательно! {w}Тогда пошли на рынок, Механик же сказала, что каждый день там новое объявление, с помощью которого мы сможем заработать флориумы!"
            hide in1
            show pes with dissolve
            m "Хорошо"
            hide pes
            stop music fadeout 1.0
            scene black with dissolve
            pause 0.5

            jump market

        "Пойти в парк":
            show in1 with dissolve 
            n "Замечательно! {w}Тогда может мы пойдем в парк аттракционов? Я слышала, что там очень интересно и весело"
            hide in1
            show pes with dissolve
            m "Хорошо"
            hide pes
            stop music fadeout 1.0
            scene black with dissolve
            pause 0.5

            jump park1
            #не идет на рынок а сразу в парк

label market:

    scene bg_broadcast with dissolve
    play music "maintheme.mp3" fadein 1.0
    pause 0.5

    show in1 with dissolve
    n "Тут объявление!"

    n"На объявлении написано: Ищу помощника, который является образованный и классифицированным в установлении цен на товары"
    hide in1 


    menu:
        "Помочь":

            show in1 with dissolve 
            n "Думаю будет весело, а главное мы ему поможем! А ты как думаешь?"
            hide in1
            show pes with dissolve
            m "ГАВ!{w} Я тоже так думаю! Тогда идем же быстрее"
            hide pes
            $ torg += 1

            scene black with dissolve
            pause 0.5
            stop music fadeout 1.0

            jump trader1

        "Пойти в парк": 
            show in1 with dissolve 
            n "Хмм… {w}Даже не знаю. {w}Может мы лучше пойдем в парк аттракционов? "
            hide in1
            show pes with dissolve
            m "Хорошо, я не против!"
            hide pes
            stop music fadeout 1.0
            scene black with dissolve
            pause 0.5

            jump park1

label trader1:

    scene bg_market1 with dissolve
    play music "tolpa.mp3" fadein 1.0
    show in1 with dissolve 
    n "Вроде бы пришли"
    hide in1

    show t with dissolve
    t "{cps=20}Эх… {w}Как же много бумаг… {w}Я совсем ничего не понимаю!{/cps}"
    show pes with dissolve
    m "Мы пришли Вам помочь!"
    hide pes

    t "{cps=20}Да? Но как же?{/cps}"
    show in1 with dissolve 
    n "Хм... {w}Чтобы установить правильно цену, нам 1-е, что нужно сделать это - {i}Анализ затрат"
    hide in1

    t "{cps=20}Звучит логично! Я совсем про это не подумал{/cps}"

    show pes with dissolve
    m "Анализ затрат - это очень важно! Ведь нам нужно определить все затраты, связанные с товаром:"

    m "производственные, транспортные, налоги, аренду,  а так же убедиться, что он учитывает все переменные и фиксированные затраты"
    hide pes
    hide t
    show t with dissolve
    t "{cps=20}Ух, какие умные гости к нам пожаловали!{/cps}"
    show in1 with dissolve 
    n "Хах, спасибо!{w} Но это не все! Мы так же должны изучить рынок!"
    hide in1
    show pes with dissolve
    m "Гав!  Нам нужно провести  исследование конкурентов:"

    m "узнать, какие цены они устанавливают на аналогичные товары, а так же определить целевую аудиторию и их платежеспособность" 
    hide pes
    show in1 with dissolve 
    n "Но и это еще не все! Мы так же должны выбрать стратегию ценообразования!{w} То есть, себестоимость + наценка! Нам нужно добавить определенный процент к себестоимости товара"
    hide in1

    hide t
    show t with dissolve
    t "{cps=20}Так чего ж мы ждем!{w} Давайте скорее все разбирать! {/cps}"
    hide t 

    scene black with dissolve
    show text "Прошло 5 часов" at truecenter with dissolve 
    pause 1.5
    hide text with dissolve
    scene bg_market2 with dissolve

    show in1 with dissolve 
    n "Фухх…{w} Вроде бы все!"
    hide in1
    
    show t with dissolve
    t "{cps=20}Спасибо Вам, Добрые люди! Если бы не вы, то даже не знаю, что могло бы произойти! {/cps}"
    
    show pes with dissolve
    m "Та не за что!{w} Мы всегда рады помочь, ведь помогая людям, мы делаем мир лучше!"
    hide pes

    hide t
    show t with dissolve
    t "{cps=20}Вы можете остаться ночевать у меня, пока не почините свой корабль! Места у меня много, хватит на всех!{w} А я поговорю с механиком, он мой лучший друг, думаю снизит вам цену! {/cps}"

    show in1 with dissolve 
    n "Спасибо Вам огромное!"
    hide in1
    show pes with dissolve
    m "Гав!{w} Гав!"

    hide pes 
    hide t with dissolve
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.5
    
    jump perehod

label perehod:
    
    scene bg_park4 with dissolve
    play music "maintheme.mp3" fadein 1.0
    show in1 with dissolve
    n "Так, я думаю, теперь можно сходит и в парк"
    hide in1 

    show pes with dissolve
    m"Отличная идея, {w} Гав!"
    hide pes
    stop music fadeout 1.0
    jump park1

label park1:

    scene bg_park1 with dissolve
    play music "maintheme.mp3" fadein 1.0
    show in1 with dissolve 
    n "{cps=10}Ура! {/cps}{w}Мы наконец-то пришли! Но как тут странно…!"
    hide in1
    show pes with dissolve
    m "Гав!{w} Гав!"
    hide pes

    show mf with dissolve
    mf "Эхх… Все-таки настал тот момент, когда прийдется тебя закрыть…"
    
    show in1 with dissolve 
    m "ЗАКРЫТЬ?{w} А что случилось? Может мы сможем Вам помочь?"
    hide in1

    hide mf 
    show mf with dissolve
    mf "Мой парк работал многие годы… {w}Но что то пошло не так и я стал терять прибыль с него… "
    mf "Теперь прийдется его закрыть, ведь я совсем не знаю что делать"

    show in1 with dissolve 
    n "Вам очень повезло, что вы встретили нас!" 
    hide in1 

    mf "Да? Тогда все внимательно слушаю! Возможно тогда парк будет работать, как раньше!"

    show in1 with dissolve 
    n "Улучшение маркетинга точно Вам поможет!"
    n "Вы должны создать привлекательные рекламные кампании и использовать социальные сети, чтобы привлекать новую аудиторию и удерживать существующих клиентов! " 
    hide in1

    mf "Звучит здорово!{w} Ведь тогда не только с нашего города будут приходить, но и приезжать и с других городов"

    show pes with dissolve
    m "Оценка ценовой политики, так же играет важную роль! Вам стоит пересмотреть цены на входные билеты и аттракционы. {w}Возможно, стоит сделать их более доступными для широкой аудитории"
    hide pes

    hide mf 
    show mf with dissolve
    mf "Как же я сам до этого не догадался! {w}Возьмите пожалуйста 150 флориумов! К сожалению больше у меня нет… "

    show in1 with dissolve 
    n "Спасибо! {w}Я думаю у вас все обязательно получится!"
    hide in1

    $ fant += 1

    hide mf with dissolve
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.5
    
    jump transition2

# DAY 3

label transition2:

    scene skip with dissolve
    pause 1 
    scene black with dissolve

    jump day3


label day3:

    if torg > 0 and fermer > 0 and fant > 0:

        scene bg_torghome with dissolve
        play music "hometheme.mp3" fadein 1.0

        show in1 with dissolve 
        n "Осталось 3 дня, за которые мы должны успеть вернуться обратно домой!{w} Но денег по-прежнему не хватает… Даже не знаю что делать…"
        hide in1

        show pes with dissolve
        m "Мы можем организовать финансовый семинар для местных жителей! Он будет очень полезен для мирного населения!"
        hide pes

        show in1 with dissolve 
        n "А что? Звучит Здорово! {w}Если мы соберем большое количество людей, то туда помогут прийти очень богатые люди, которые смогут стать нашими спонсорами!{w} И тогда мы точно сможем улететь домой"
        hide in1

        show pes with dissolve
        m "Гав!{w} Гав!"
        hide pes

        show t with dissolve
        t "{cps=20}Я вам помогу! {/cps}"

        hide t 
        show t at left
        show f1 with dissolve
        f "Я тоже!"    

        show in1 with dissolve 
        n "Спасибо, вам большое! Вы настоящие друзья! {w}Только как нам это сделать?"
        hide in1 

        show pes with dissolve
        m "Мы можем заказать рекламу у рекламного агенства! Это нам поможет собрать достаточное количество людей!"
        hide pes

        hide f1 
        show f2 with dissolve
        f "Так держать! Я вместе с торговцем тогда отправлюсь заказать рекламу, а вы  оставайтесь здесь!"

        show in1 with dissolve 
        n "Хорошо! Мы тогда сделаем листовки и расклеим их по всему городу, где будет все подробно расписано!"
        hide in1

        show pes with dissolve
        m "Гав!{w} Гав!{w} Отличная идея!"
        hide pes
        hide t with dissolve
        hide f1 with dissolve
        stop music fadeout 1.0
        scene black with dissolve
        pause 0.5

        jump cutscene1

    else:
        
        scene bg_torghome with dissolve
        play music "hometheme.mp3" fadein 1.0
        show in1 with dissolve 
        n "Осталось 3 дня, за которые мы должны успеть вернуться обратно домой! {w}Но денег по прежнему не хватает… {w}Даже не знаю что делать…"
        hide in1

        show pes with dissolve
        m "Мы можем организовать финансовый семинар для местных жителей! Он будет очень полезен для мирного населения!"
        hide pes

        show in1 with dissolve 
        n "А что? Звучит Здорово! Если мы соберем большое количество людей, то туда помогут прийти очень богатые люди, которые смогут стать нашими спонсорами!{w} И тогда мы точно сможем улететь домой!"
        hide in1

        show pes with dissolve
        m "Гав!{w} Гав!{w} Мы можем заказать рекламу у рекламного агенства! Это нам поможет собрать достаточное количество людей!"

        m "Я тогда отправлюсь заказать рекламу, а ты оставайся здесь!" 
        hide pes

        show in1 with dissolve 
        n "Хорошо! Тогда, я сделаю листовки и расклею их по всему городу, где будет все подробно расписано!"
        hide in1

        show pes with dissolve
        m "Гав!{w} Гав!"
        hide pes
        stop music fadeout 1.0
        scene black with dissolve
        pause 0.5

        jump cutscene2


label cutscene1:

    # (ФОТО ЛИСТОВКИ)
    # (ФОТО ГДЕ ОНА НАКЛЕЕНА)
    # (ФОТО ГДЕ ПО ТЕЛЕКУ ПОКАЗАНА РЕКЛАМА, КОТОРУЮ ЗАКАЗАЛ ФЕРМЕР И ТОРГОВЕЦ)
    scene black 
    jump day3torg

label cutscene2:

    #2(ФОТО ЛИСТОВКИ)
    #3(ФОТО ГДЕ ОНА НАКЛЕЕНА)
    #4(ФОТО ГДЕ ПО ТЕЛЕКУ ПОКАЗАНА РЕКЛАМА, КОТОРУЮ ЗАКАЗАЛ ФЕРМЕР И ТОРГОВЕЦ)
    #5(ФОТО НА СЦЕНЕ)
    scene black
    jump day3street

label day3torg:
    scene bg_torghome with dissolve
    play music "hometheme.mp3" fadein 1.0
    #( в доме у торговца)
    
    show in1 with dissolve 
    n "Я так волнуюсь… {w}А если никто не прийдет…"
    hide in1

    show pes with dissolve
    m "Ты что! У нас все получиться! Главное верить!"
    hide pes

    show f2 with dissolve
    f "Да! Главное не впадать в отчаяние!{w} А теперь спать!{w} Утро вечера мудрене́е"
    
    show in1 with dissolve 
    n "Хорошо!"
    hide in1

    hide f2 with dissolve
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.5

    jump transition3

label day3street:
    
    scene speech with dissolve
    play music "tolpa.mp3" fadein 1.0

    show in1 with dissolve 
    n "Я так волнуюсь… А если никто не прийдет…"
    hide in1

    show pes with dissolve
    m "Ты что! У нас все получиться! Главное верить!"
    hide pes

    show in1 with dissolve 
    n "Ты прав!"
    hide in1
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.5

    jump transition3
    
label transition3:

    scene skip with dissolve
    pause 1 
    scene black with dissolve

    jump day4start

# DAY 4    
    
label day4start:

    scene speech with dissolve
    play music "tolpa.mp3" fadein 1.0
    show in1 with dissolve 
    n "Майк, что-то я очень сильно сильно переживаю…"
    hide in1 

    show pes with dissolve
    m "Так, хватит переживать! У нас все получиться! {w}Тут уже как раз все начали собираться, смотри как много людей пришло!"
    hide pes

    show in1 with dissolve 
    n "Ого… Они вправду пришли послушать меня?"
    hide in1

    show f1 with dissolve
    if torg > 0 and fermer > 0 and fant > 0:
        f "Конечно!{w} Они все наслышаны, как ты помогала нам!{w} Ого…сюда даже пришел самый богатый житель нашего города"
    else:
        f "Вы слышали? Самый богатый житель города лично пришел посмотреть!"
    show in1 with dissolve 
    n "Так, кажется я кое-что придумала"
    hide in1
    hide f1 with dissolve
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.5

    jump day4speech

label day4speech:

    scene speech with dissolve
    play music "tolpa.mp3" fadein 1.0
    show in1 with dissolve 
    n "Дорогие жители! Спасибо, что нашли время встретиться со мной сегодня. Я очень ценю вашу возможность услышать меня! "
    n "Как вы, возможно, знаете, финансовая грамотность – это основа для достижения ваших жизненных целей. "
    n "Она помогает не только лучше понимать, как работают деньги, но и принимать обоснованные решения в различных ситуациях. "
    n "Мы все сталкиваемся с финансовыми вопросами: от планирования бюджета до инвестиций, и понимание этих основ поможет нам избежать возможных ошибок"

    n "Сегодня мы рассмотрим несколько ключевых тем:"
    n "1) Основы финансовой грамотности."
    n "2) Как составить личный бюджет"
    n "3) Способы накопления и инвестиций"
    n "4) Создание финансовой подушки безопасности"

    n "Личный бюджет — это план доходов и расходов.{w} Ведение бюджета помогает контролировать финансы, избегать долгов и достигать финансовых целей"
    n "Для того, что составить личный бюджет нужно: {w}1. Ведение тетради учета. Записывайте все доходы и расходы.{w}  2. Использование приложений. Приложения для финанализа упрощают учет{w}  3. Составление бюджета. Устанавливайте лимиты на категории расходов."
   
    n "Вы можете открыть Сберегательные счета, которые обеспечивают стабильный доход с низким риском. Облигации, то есть долговые ценные бумаги с фиксированным доходом. А так же ПИФы. {w}Вы можете инвестировать в фонды, даже с небольшими суммами."
    n "Финансовая подушка защищает от непредвиденных расходов. Откладывайте 3-6 месячных расходов на свой сберегательный счет"

    n "Так же я написала вам книгу, в которой более подробно рассказано про финансовую грамотность!{w} Всем спасибо! Надеюсь я Вам помогла!"
    hide in1
    stop music fadeout 1.0
    scene black with dissolve
    pause 0.5

    jump day4dialog

label day4dialog:

    scene bg_dhome with dissolve
    play music "hometheme.mp3" fadein 1.0 
    if torg > 0 and fermer > 0 and fant > 0:

        show d with dissolve
        d "Меня очень впечатлила ваша речь на семинаре! Я стал более лучше понимать в сфере финансов, что является для меня очень важной частью в моей жизни!"
        d "Так же вы помогли нашему городу стать более образованным, за что я вам очень сильно благодарен.{w} Я хочу стать спонсором, ведь вы помогли нам, а я помогу вам"

        show in1 with dissolve 
        n "Спасибо вам большое! Я вам очень благодарна! Наконец-то я смогу заплатить за корабль и улететь к себе домой!"
        hide in1

        f "Нана, спасибо тебе за все, что ты сделала для нашего города! Мы тебе все очень сильно благодарны! Если бы не ты, то не знаю к чему бы наша необразованность привела!"

        hide d 
        show d at left
        show t with dissolve
        t "Полностью согласен с фермером! Прилетайте к нам еще как-нибудь!"
        show in1 with dissolve 
        n "Спасибо вам огромное!{w} Без Вас бы у меня ничего не получилось, поэтому те деньги, которые у меня остались я хочу отдать городу на его развитие!{w} Всем пока!{w} До новых встреч!"
        hide in1

        show pes with dissolve
        m "Гав!{w} Гав!"
        hide pes
        hide d with dissolve
        hide t with dissolve
        stop music fadeout 1.0

        jump goodend

    else:

        show d with dissolve
        d "{cps=10}Меня, к сожалению, не впечатлила ваша речь на семинаре!{w} Тем более многие говорили, что Вы не помогали нашим жителям.{/cps}"
        d "{cps=10}Я думаю, что Вы решили организовать весь этот спектакль ради того, чтобы получить мои деньги!{w} {i}Так что до свидания!{/cps}"

        hide d with dissolve
        show in1 with dissolve 
        n "{cps=5}О нет...{/cps}"
        hide in1
        
        show pes with dissolve
        m "{cps=5}Что же нам делать!{w} Мы не успеем уже вернутся домой.{w}.{w}.{/cps}"
        hide pes

        stop music fadeout 1.0  
        scene black with dissolve
        pause 0.5

        jump badend

label goodend:

    scene bg_dhome 
    play music "maintheme.mp3" fadein 1.0
    show in1 with dissolve
    n "Отлично, теперь нам хватает денег для починки корабля!"
    hide in1

    show meh1 with dissolve
    meh "Я в деле!"

    pause 0.5
    hide meh1

    scene black with dissolve
    pause 0.5
    scene bg_ship with dissolve
    show meh2 with dissolve
    show in1 with dissolve
    n "Отлично, теперь мы можем лететь домой!"
    hide in1 

    meh "Удачи вам и спасибо за помощь!"

    show pes with dissolve
    m "Гав{w} Гав!"
    stop music fadeout 2.0
    hide pes
    hide meh2
    
    pause 2
    scene bgstart with dissolve
    pause 3
    scene goodend1 with dissolve
    pause 3
    scene goodend2 with dissolve
    pause 3
    scene black with dissolve
    show text "The end" at truecenter with dissolve
    pause 2.0
    return

label badend:

    scene bg_dhome
    show pes with dissolve
    m "Ты уже забыла? у тебя зарядился артефакт, который возвращает нас на 4 дня назад"
    hide pes
    show in1 with dissolve
    n "Точно, тогда используем его!"
    play sound "warp.mp3" fadein 1.0
    hide in1

    pause 1.0
    #sound 

    scene white with dissolve

    pause 1.0

    scene black with dissolve
    jump start
     

return