# Czech / Česky
## Popis 
Jedna z nejjednoduších a zároveň velmi neefektivních implementací 
[Voroného diagramu](https://cs.wikipedia.org/wiki/Voroného_diagram). 

V budoucnu možná bude podporovat i různé effektivnější algoritmy, 
prozatím však bude stačit jen agloritmus, který bube počítat vzdálenost
pro každý pixel zvlášť

## Nápad
Nápad jsem ukradl od rekreačního programátora a streamera [Tsoding](https://www.youtube.com/watch?v=kT-Mz87-HcQ). (doporučuju shlédnout - en kanál)

## Provedení
Prozatimní plán je vytvořit jednoduchou aplikaci v [Pythonu](https://www.python.org) 
s pomocí modulu [PyGame](https://www.pygame.org), ve které se bude zobrazovat 
aktuální diagram a uživatel bude moct přidávat další záchytné body.

## Plány do budoucna
Effektivnější algoritmy, ukládání obrázků, přepis do C, nastavení rozlišení.
Přidávání bodů pomocí konzole?

## Requirements (cz)
Programováno s Pythonem 3.11.1 (mělo by fungovat i na starších a novějších).
 - bohužel díky nové verzi Pythonu jsem pracoval na dev verzi PyGame, pozdeji 
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

Working on gui and first aloritm.

## Idea
Idea stolen from recreational programmer and streamer [Tsoding](https://www.youtube.com/watch?v=kT-Mz87-HcQ). I can recommend his YT or twitch channel.
## Provedení

## Future plans
Better algorithms, saving pictures, rewriting in C, custom resolution.

## Requirements (en)
Coded with Python 3.11.1 (should work even on other versions).
 
Note: In the developement of this mini project there is no full version
of PyGame to use with Python 3.11.1, so I'm using the dev version.
```
pip install -r requirements.txt
```

Coded on Windows 10.

## Run
```
python main.py
```

