## Персонажи
define n = Character(None, kind=nvl)
define blake = Character('{b}Блэйк{/b}', color="#DDA0DD")
define none = Character('{b}???{/b}', color="#FFFFFF")


## Переменные
### Переменные осмотра местности
#### Палата Блэйка
define room_blake = 0
define v_1_1 = False
define v_1_2 = False
define v_1_3 = False

## Анимации персонажей
### Анимация Блэйка
#### Моргает в спокойном состоянии
image ch blake normal blink:
    "ch blake normal"
    choice:
        pause 5
    choice:
        pause 8
    choice:
        pause 12
    "ch blake normal closed"
    pause 0.1
    repeat
    
### Говорит в спокойном состоянии
image ch blake normal speech:
    "ch blake normal"
    pause 0.2
    "ch blake normal mouth 1"
    pause 0.2
    "ch blake normal mouth 2"
    pause 0.2
    "ch blake normal mouth 3"
    pause 0.2
    repeat
