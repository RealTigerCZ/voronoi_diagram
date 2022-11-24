# Czech / Česky
## Popis 
Jedna z nejjednoduších a zároveň velmi neefektivních implementací 
[Voroného diagramu](https://cs.wikipedia.org/wiki/Voroného_diagram). 

V budoucnu možná bude podporovat i různé effektivnější algoritmy, 
prozatím však bude stačit jen agloritmus, který bube počítat vzdálenost
pro každý pixel zvlášť

## Nápad
Nápad jsem ukradl od rekreačního programátora a streamera [Tsoding](https://www.youtube.com/watch?v=kT-Mz87-HcQ). (doporučuju shlédnout - en kanál)

## Dodatečné informace
Aktuální implementace je velmi pomalá. Pro její zrychlení jsem použil měřítko,
abych snížil počet pixelů. Největším bottleneckem je aktuálně 
[pygame.Surface.set_at()](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_at), který je relativně pomalýa je velmi často volán. 
Dalším faktorem je samotný algoritmus, který zvlášt vypočítává barvu
pro každý pixel a přiřazuje ji po jednom. Avšak jako první prototyp to zatím postačí.

S přibývajícím počtem bodů se program také velmi rychle zpomaluje.
Pro rozlišení 400x300px na mém počítači se jedná asi o 700 ms pro set_at() a
cca 100 ms pro každý bod (kromě prvního).

## Provedení
Prozatimní plán je vytvořit jednoduchou aplikaci v [Pythonu](https://www.python.org) 
s pomocí modulu [PyGame](https://www.pygame.org), ve které se bude zobrazovat 
aktuální diagram a uživatel bude moct přidávat další záchytné body.

## Plány do budoucna
Effektivnější algoritmy, ukládání obrázků, přepis do C, nastavení rozlišení.
Přidávání bodů pomocí konzole?

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

Working on gui and first aloritm.

## Idea
Idea stolen from recreational programmer and streamer [Tsoding](https://www.youtube.com/watch?v=kT-Mz87-HcQ). I can recommend his YT or twitch channel.

## Aditional info
This implementation is very slow. To speed up things I've used image
scaling. The biggest bottleneck now is [pygame.Surface.set_at()](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_at) function.
This function isn't the fastest and you are not supposed to call it 10 of
thousands of times. The other slow thing is the algorithm alone. It is 
computing for every pixel on screen distance from every point.

But why am I publishing it? I just wanted to try it and then maybe 
optimise it. 

Some numbers for my pc (resolution is set to 400x300px):
about 700 ms takes to set_at all pixels
about 100 ms takes to calculate for all pixels distance from one point

## Actual plan
is to make some easy app in [Python](https://www.python.org) with help of
[PyGame](https://www.pygame.org), that can display the current diagram 
and the user will be able to add additional reference points by clicking.

## Future plans
Better algorithms, saving pictures, rewriting in C, custom resolution.

## Requirements (en)
Coded with Python 3.11.1 (should work even on other versions).
 
Note: In the moment there is no full version
of PyGame to use with Python 3.11.1, so I'm using the dev version.
```
pip install -r requirements.txt
```

Coded on Windows 10.

## Run
```
python main.py
```

# Ukázky / screenshots

![Alt text](./screenshot.png?raw=true "Screenshot 1")


