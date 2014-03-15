# Music Tutor

Тренировка чтения нот: программа показывает ноту на нотном стане,
нужно нажать на клавиатуре соответствующую клавишу.

Тренировка распознования нот на слух: программа проигрывает ноту,
нужно нажать на клавиатуре соответствующую клавишу.

Без подключенного к компьютеру синтезатора или MIDI-клавитуры смысла в ней мало.
[Как подключить синтезатор к компьютеру](http://tanalin.com/articles/midikb2pc/).


## Мое окружение

В котором я разрабатываю и использую (в другом окружении не пробовал):
 -  Ноутбук Thinkpad T520
 -  Ubuntu 13.04
 -  Синтезатор YAMAHA PSR R300
 -  USB-MIDI переходник CL036

Зависимости:
 - Python 2.7
 - pygtk 2.0
 - aseqdump


## Как читать midi данные с синтезатора

Устройство /dev/snd/midi* у меня /dev/snd/midiC1D0

Можно читать тупо утилитой *cat* (с флагом -v, иначе она игнорирует бинарные данные)

    cat -v /dev/snd/midiC1D0

Умнее утилита *amidi*, может показывать бинарные данные, идущие с MIDI-порта:

    yura ~ $ amidi -l
    Dir Device    Name
    IO  hw:1,0,0  USB2.0-MIDI MIDI 1
     O  hw:1,0,1  USB2.0-MIDI MIDI 2

    yura ~ $ amidi -d -p hw:1,0,0
    F8
    90 48 25
    F8
    F8
    90 48 00

Еще лучше утилита *aseqdump*, она интерпретирует данные и показывает MIDI-события:

    yura ~ $ aseqdump -l
     Port    Client name                      Port name
      0:0    System                           Timer
      0:1    System                           Announce
     14:0    Midi Through                     Midi Through Port-0
     20:0    USB2.0-MIDI                      USB2.0-MIDI MIDI 1

    yura ~ $ aseqdump -p 20:0
    Waiting for data. Press Ctrl+C to end.
    Source  Event                  Ch  Data
     20:0   Clock
     20:0   Active Sensing
     20:0   Clock
     20:0   Clock
     20:0   Note on                 0, note 62, velocity 66
     20:0   Clock
     20:0   Clock
     20:0   Note on                 0, note 60, velocity 49
     20:0   Clock
     20:0   Active Sensing
     20:0   Note off                0, note 64


## Инфа по теме

[MIDI Commands](http://computermusicresource.com/MIDI.Commands.html)
[Как подключить синтезатор к компьютеру](http://tanalin.com/articles/midikb2pc/)
[Использование синтезатора в качестве компьютерной клавиатуры](http://habrahabr.ru/post/143893/)
