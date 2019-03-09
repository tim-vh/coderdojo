# Snake handleiding 

## Basisspel
We gaan eerst de kop van de slang toevoegen. Ga naar uiterlijken en kies voor 'Tekenen'.

Teken nu een hoofd met twee ogen erin.

Nu gaan we er voor zogen dat de slang kan bewegen

Voeg hiervoor de volgende gebeurtenis toe:

[wanneer op (vlag) is gedrukt]

Dit blok zorgd ervoor dat er code wordt uitgevoerd als het spel start. Nu kunnen we hier het volgende blok aan vast maken:

[neem 2 stappen]

Als het spel start beweegt de slang nu 2 stappen. Om ervoor te zorgen dat de slang blijft bewegen gaan we een herhaal toevoegen:

[herhaal]

Nu blijft de slang bewegen tot hij bij de rand is. De volgende stap is dat we ervoor gaan zorgen dat we de slang kunnen besturen. Eerst gaan we de slang omhoog laten bewegen als we op 'pijltje omhoog' drukken. Voeg hiervoor de volgende gebeurtenis toe:

[Wanneer pijltje omhoog is ingedrukt]

Dit blok voert code uit als er op een toets wordt gedrukt. Om de slang omhoog te laten gaan maken we hier het volgende blok aan vast:

[richt naar 0 graden]

Nu moeten we er nog voor zorgen dat de slang ook de andere kanten op kan bewegen. Voeg hiervoor de volgende code toe:

[richt naar 90 graden]
[richt naar 180 graden]
[richt naar -90 graden]

Nu kunnen we alle kanten op bewegen!

De volgende stap is het lichaam van de slang steeds langer te laten worden. Dit gaan we doen door een lijn te tekenen. Hiervoor moeten we eerst de 'pen' uitbreiding toevoegen aan scratch:

[toevoegen pen uitbreiding]

Met deze uitbreiding krijgt de sprite een soort pen waarmee hij lijnen kan tekenen als hij beweegt. Om de pen aan te zetten kunnen we het volgende blok toevoegen:

[pen neer]

Om het lijf van de slang dikker te maken kunnen we de pendikte aanpassen met de volgende code:

[maak pendikte 4]

Ook willen we dat het lijf dezelfde kleur krijgt als de kop. Dit kan met het volgende blok:

[maak penkleur (kleur)]

Het is handig dat elke keer dat het spel start het lijf van de slang weer verdwijnt en de slang in het midden van het spel begint. Dit kunnen we doen met de volgende code:

[wis alles]
[ga naar x: 0 y:0]

Nu kunnen we het spel leuker gaan maken door ervoor te gaan zorgen de we punten kunnen verdienen. Dit gaan we doen door te slang appels te laten eten. Voor elke appel krijg je een punt. Hiervoor gaan we een nieuwe sprite toevoegen:

[sprite toevoegen]

Eerst gaan we ervoor zorgen dat de appel op een willekeurige plek in het spel verschijnt met de volgende code:

[wanneer op (vlag) wordt geklikt]
[ga naar willekeurige positie]

Ook willen we dat de appel wat kleiner wordt:

[maak grootte 30%]

Nu gaan we elke keer dat de slang beweegt kijken of hij de appel raakt:

[herhaal]
[als raak ik slang]

Nu moeten we gaan zorgen dat we een score kunnen gaan bijhouden. Dit kunnen we gaan doen moet een variable. Een variable kun je een waarde geven, bijvoorbeeld een getal, die je met code kan veranderen. Voeg een variable 'score' toe:

[maak variable score]

Nu kunnen we zorgen dat we een punt krijgen als de slang de appel raak met de volgende code:

[verander score met 1]

Nu krijgen we elke keer dat de slang de appel raak er een punt bij. Om ervoor te zorgen dat de score niet heel snel optelt gaan we de appel verplaatsen als we een punt scoren door de volgende code toe te voegen:

[ga naar willekeurige positie]

Nu gaan we het spel nog wat moeilijker maken door ervoor te zogen dat de slang niet mag botsen met de rand of met zichtzelf. Eerst gaan we kijken of de slang de rand raak met de volgende code:

[als raak ik rand]

Elke reek als de slang beweegt kijken we of de rand wordt geraakt. Als dit zo is gaan we er nu voor zorgen dat het spel stopt en de slang zegt dat het spel is afgelopen:

[zeg game over! 2 sec]
[stop alle]

Nu gaan we nog kijken of de slang zichtzelf raakt. Dit gaan we doen door eerst een 'of' blok toe te voegen. Hiermee kijken we of we de rand raken of de slang:

[als raak ik rand of]

Om te kijken of de slang zichtzelf raak kijken we of de ogen het lichaam van de slang raakt door te kijken naar de kleuren:

[raakt kleur (kleur ogen) kleur (kleur lijf)]

Maak de eerste kleur gelijk aan de kleur van de ogen en de andere kleur gelijk aan de kleur van het lijf. Doe dit in deze volgorde anders werkt het niet!

