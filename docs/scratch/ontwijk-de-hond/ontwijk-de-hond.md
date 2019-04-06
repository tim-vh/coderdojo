# Ontwijk de hond handleiding 

## Inhoud
- [Ontwijk de hond handleiding](#ontwijk-de-hond-handleiding)
  - [Inhoud](#inhoud)
  - [Basisspel](#basisspel)
  - [Uitbreidingen](#uitbreidingen)
    - [Levens](#levens)
    - [Laat de kat sprinten](#laat-de-kat-sprinten)
    - [Muren toevoegen](#muren-toevoegen)
  
## Basisspel

Voeg de volgende gebeurtenis toe: 

![Image](afbeeldingen/gebeurtenis-vlag.png)
 
Hiermee kun je code uitvoeren als het spel begint. Je kan bijvoorbeeld de kat laten bewegen. Voeg de volgende code toe aan de gebeurtenis om de kat te laten bewegen: 

![Image](afbeeldingen/verander-x.png)
 
Als je het spel start neemt de kat 10 stappen naar rechts. Nu willen we dat de kat blijft lopen als het spel begint. Dit kan door een herhaling toe te voegen:

![Image](afbeeldingen/herhaal.png)
 
Nu blijft de kat bewegen totdat de rand van het spel wordt geraakt. De volgende stap is dat we de kat kunnen besturen met de pijltjestoetsen. Om dit te doen willen we dat kat alleen beweegt als we op een toets drukken. Dit kan door een 'als' blok toe te voegen met daarin een blok die kijkt of er op een toets wordt gedrukt:   

![Image](afbeeldingen/als-leeg.png)
![Image](afbeeldingen/als-toets-rechts.png)

Nu beweegt de kat alleen als pijltje naar rechts wordt ingedrukt. Nu willen we ervoor zorgen dat de kat ook de andere kanten op kan bewegen:

![Image](afbeeldingen/beweeg-met-pijtjes-toetsen.png)
 
Nu is er voor elke richting een toets toegevoegd. Wanneer x veranderd gaat de kat naar links of naar rechts. En wanneer y veranderd gaat de kat naar boven of naar beneden. Door een minteken ('-') voor het getal te zetten zorg je ervoor dat de kat bijvoorbeeld naar links gaat in plaats van naar rechts. 

De volgende stap is dat we een hond toevoegen. Voeg hiervoor een nieuwe sprite toe: 

![Image](afbeeldingen/sprite-toevoegen.png)

Nu gaan we code toevoegen om de hond te laten bewegen. Klik hiervoor op de hond bij sprites en voeg de volgende code toe: 

![Image](afbeeldingen/neem-10-stappen.png)

Nu beweegt de hond als het spel start. Nu gaan we ervoor zorgen dat als de hond de rand van het spel raak hij in de richting van de kat beweegt: 

![Image](afbeeldingen/als-raak-ik-kat.png)

Om ervoor te zorgen dat de hond naar een andere plek in het spel gaat als de kat geraakt wordt voegen we nog een 'als' blok toe. In dit blok wordt een willekeurig getal gekozen zodat de hond elke keer naar een ander plek gaat: 

![Image](afbeeldingen/ga-naar-willekeurige-plek.png)

De eerste versie van ons spel is nu af! Maar je kan het spel natuurlijk nog verder uitbreiden. Bijvoorbeeld met de onderstaande onderdelen. Maar je kan natuurlijk ook zelf iets verzinnen. 

- Levens 
- Laat de kat sprinten 
- Muren toevoegen 
- .....

## Uitbreidingen

In de volgende hoofdstukken staat uitgelegd hoe je deze uitbreidingen zou kunnen maken. 

### Levens 

Ga naar Variabelen en kies voor 'Maak een variabele'. 

![Image](afbeeldingen/maak-variabele.png)

Noem de variabele 'levens'. 

![Image](afbeeldingen/maak-levens-variabele.png)

Een variabele is een blok die je een bepaalde waarde kan geven. Met dit blok gaan we het aantal levens van de kat bijhouden. Aan het begin van het spel willen we dat de kat 9 levens heeft. Dit kan op de volgende manier. 

![Image](afbeeldingen/maak-levens-9.png)

Nu gaan we ervoor zorgen dat wanneer de kat geraakt wordt de levens minder worden. Bij de code voor de hond wordt al gekeken of de kat wordt geraakt. Hier gaan we nu een blok toevoegen dat ervoor zorgt dat het aantal levens minder wordt. 

![Image](afbeeldingen/verminder-aantal-levens.png)

Wanneer de hond de kat raakt wordt er nu een leven afgehaald. We gaan er nu nog voor zorgen dat als het aantal levens '0' is het spel stopt. Dit kan door nog een 'als' blok toe te voegen. 

![Image](afbeeldingen/stop-spel.png)

Door dit blok toe te voegen wordt er gekeken of het aantal levens nul is. Als dat zo is wordt alle code gestopt. 

 
### Laat de kat sprinten 

Ga naar Data en kies voor 'Maak een variabele'. 

![Image](afbeeldingen/maak-variabele.png)

Noem de variabele 'snelheid'

![Image](afbeeldingen/maak-snelheid-variabele.png)

Een variabele is een blok die je een bepaalde waarde kan geven. Wij gaan de variabele de waarde '5' geven zodat de kat met die snelheid kan bewegen.  Dit kunnen we doen door het volgende blok toe te voegen. 

![Image](afbeeldingen/maak-snelheid-5.png)

Nu gaan we het blok 'snelheid' gebruiken op de plek waar we bewegen. Verander je code op de volgende manier. 

![Image](afbeeldingen/verander-x-met-snelheid.png)

Nu moeten we er nog voor zorgen dat de kat de goede kant opgaat voor naar links en naar beneden. Voor deze getallen stond eerst een min teken('-'). Dit kunnen we op de volgende manier doen. 

![Image](afbeeldingen/snelheid-omdraaien-voor-liks-en-omlaag.png)

Door de snelheid keer -1 te doen gaat de kat weer de goede kant op. We hebben nu de snelheid van de kat in een variabele gestopt. Nu kunnen we de snelheid van de kat aanpassen met code. We gaan er nu voor zorgen dat de kat sneller gaat wanneer je op spatie drukt. 

![Image](afbeeldingen/ga-sneller.png)

De kat heeft nu de snelheid '10' wanneer je op spatiebalk drukt. Nu gaan we er nog voor zorgen dat de snelheid weer terug wordt gezet naar de normale snelheid. Dit kan met de volgende code. 

![Image](afbeeldingen/zet-snelheid-terug-na-3-seconden.png)

De snelheid wordt nu na 3 seconden weer normaal. 

### Muren toevoegen 

We gaan de code van de kat aanpassen zodat wanneer de kat iets zwarts raakt hij niet beweegt. Hierdoor kan de kat niet door zwarte dingen heen. Eerst gaan we onze achtergrond aanpassen door hier een zwarte muur op te tekenen. Ga eerst naar 'speelveld': 

![Image](afbeeldingen/ga-naar-speelveld.png)

Ga daarna naar 'achtergronden': 

![Image](afbeeldingen/ga-naar-achtergronden.png)

Nu kunnen we de achtergrond aanpassen door er bijvoorbeeld een zwarte lijn op te tekenen: 

![Image](afbeeldingen/teken-lijn.png)

Nu gaan we de code van de kat aanpassen zodat hij niet door de lijn kan. Voeg het volgende 'als' blok toe aan de code: 

![Image](afbeeldingen/niet-door-lijn-voor-naar-rechts.png)

Zorg dat de kleur in het blok 'raak ik kleur?' zwart wordt. Dit kan door helderheid op 0 te zetten door de schuifknop onder 'Helderheid' helemaal naar links te slepen. Als de kat nu naar rechts beweegt en de zwarte lijn raakt wordt hij weer naar links verplaatst zodat hij niet beweegt. Nu moeten we hetzelfde doen voor de andere richtingen. Pas de code op de volgende manier aan: 

![Image](afbeeldingen/niet-door-lijn-voor-alle-richtingen.png)

Nu kan de kat niet meer door de zwarte lijnen. Je kan de achtergrond nu eventueel verder aanpassen door meer lijnen toe te voegen.  