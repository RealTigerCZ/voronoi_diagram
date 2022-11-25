# Czech / Česky
## Popis 
Jedna z nejjednoduších a zároveň velmi neefektivních implementací 
[Voroného diagramu](https://cs.wikipedia.org/wiki/Voroného_diagram). 

V budoucnu možná bude podporovat i různé effektivnější algoritmy, 
prozatím však bude stačit jen agloritmus, který bube počítat vzdálenost
pro každý pixel zvlášť

## Nápad
Nápad jsem ukradl od rekreačního programátora a streamera [Tsoding](https://www.youtube.com/watch?v=kT-Mz87-HcQ). (doporučuju shlédnout - en kanál)

## Milník
 - [x] První algoritmus
 - [x] GUI a přidávání bodů klikáním
 - [x] Lehká optimalizace prvního algoritmu
 - [x] Nastavení (config.ini)

 - [ ] Lepší algoritmus
 - [ ] Ukládání výstupu
 - [ ] Přepis do C


## Dodatečné informace
Aktuální implementace je pomalá. Pro její zrychlení jsem použil měřítko,
abych snížil počet pixelů. Avšak provedl jsem jsité optimalizace. Pro každý
pixel se stále počítá vzdálenost, ale jen od naposledy přidaného bodu.

Poté se přepíší jen pixely, kterým se minimální vzdálenost změnila.

Aktualizované odezvy (rozlišení 400x300px):
 * První bod  -> cca 1 ms
 * Druhý bod  -> cca 450 ms
 * Další body -> cca 300 ms

## Provedení
Prozatimní plán je vytvořit jednoduchou aplikaci v [Pythonu](https://www.python.org) 
s pomocí modulu [PyGame](https://www.pygame.org), ve které se bude zobrazovat 
aktuální diagram a uživatel bude moct přidávat další záchytné body.


## Requirements (cz)
Programováno s Pythonem 3.11.0 (mělo by fungovat i na starších a novějších).
 - bohužel díky nové verzi Pythonu jsem pracoval na dev verzi PyGame, později 
 updatuju na normální full verzi 
```
pip install -r requirements.txt
```

Programováno na Windows 10.

## Spuštění
```
python main.py
```


# English

## Description
Easy and not effective implementation of [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram). 

Working on improving the algorithm.

## Idea
Idea stolen from recreational programmer and streamer [Tsoding](https://www.youtube.com/watch?v=kT-Mz87-HcQ). I can recommend his YT or twitch channel.

## Milestones
 - [x] First Algorithm
 - [x] GUI and adding points by clicking
 - [x] Slight optimalization of algorithm
 - [x] Settings (config.ini)

 - [ ] Better algorithms
 - [ ] Output saving
 - [ ] Rewrite to C

## Aditional info
This implementation is slow. To speed up things I've used image
scaling. I've done some otimalizations and now it is computing 
only distances from the last added point. 

Updated comutation time (resolution 400x300px):
 * First point  -> about 1 ms
 * Second point -> about 450 ms
 * Other points -> about 300 ms  

But why am I publishing it? I just wanted to try it and then maybe 
optimise it (working on in :D). 


## Actual plan
is to make some easy app in [Python](https://www.python.org) with help of
[PyGame](https://www.pygame.org), that can display the current diagram 
and the user will be able to add additional reference points by clicking.


## Requirements (en)
Coded with Python 3.11.1 (should work even on other versions).
 
Note: In the moment there is no full version
of PyGame to use with Python 3.11.0, so I'm using the dev version.
```
pip install -r requirements.txt
```

Coded on Windows 10.

## Run
```
python main.py
```

# Ukázky / screenshots

![screenshot1](/screenshot1.png?raw=true "Screenshot 1")
![screenshot2](/screenshot2.png?raw=true "Screenshot 2 - many points")


