# Snake handleiding 

## Basisspel
We gaan eerst de kop van de slang toevoegen. Ga naar uiterlijken en kies voor 'Tekenen'.

![Image](afbeeldingen/sprite-tekenen.png)

Teken nu een hoofd met twee ogen erin.

![Image](afbeeldingen/sprite-kop-slang.png)

Nu gaan we er voor zogen dat de slang kan bewegen Voeg hiervoor de volgende gebeurtenis toe:

![Image](afbeeldingen/wanneer-op-vlag-wordt-getikt.png)

Dit blok zorgt ervoor dat er code wordt uitgevoerd als het spel start. Nu kunnen we hier het volgende blok aan vast maken:

![Image](afbeeldingen/neem-twee-stappen.png)

Als het spel start beweegt de slang nu 2 stappen. Om ervoor te zorgen dat de slang blijft bewegen gaan we een herhaal toevoegen:

![Image](afbeeldingen/herhaal-stappen.png)

Nu blijft de slang bewegen tot hij bij de rand is. De volgende stap is dat we ervoor gaan zorgen dat we de slang kunnen besturen. Eerst gaan we de slang omhoog laten bewegen als we op 'pijltje omhoog' drukken. Voeg hiervoor de volgende gebeurtenis toe:

![Image](afbeeldingen/wanneer-omhoog-wordt-ingedrukt.png)

Dit blok voert code uit als er op een toets wordt gedrukt. Om de slang omhoog te laten bewegen maken we hier het volgende blok aan vast:

![Image](afbeeldingen/richt-naar-0.png)

Nu moeten we er nog voor zorgen dat de slang ook de andere kanten op kan bewegen. Voeg hiervoor de volgende code toe:

![Image](afbeeldingen/richt-naar.png)

Nu kunnen we alle kanten op bewegen! De volgende stap is het lichaam van de slang steeds langer te laten worden. Dit gaan we doen door een lijn te tekenen. Hiervoor moeten we eerst de 'pen' uitbreiding toevoegen aan Scratch:

![Image](afbeeldingen/scratch-uitbreidingen.png)

Met deze uitbreiding krijgt de sprite een pen waarmee hij lijnen kan tekenen als hij beweegt. Om de pen aan te zetten kunnen we het volgende blok toevoegen:

![Image](afbeeldingen/pen-neer.png)

Om het lijf van de slang dikker te maken kunnen we de pendikte aanpassen met de volgende code:

![Image](afbeeldingen/pen-dikte.png)

Ook willen we dat het lijf dezelfde kleur krijgt als de kop. Dit kan met het volgende blok:

![Image](afbeeldingen/maak-penkleur.png)

Om precies dezelfde kleur te kiezen als de slang kun je op het onderste icoontje klikken en daarna op de kop van de slang in het spel klikken.

Het is handig dat elke keer dat het spel start de lijf van de slang weer verdwijnt en de slang in het midden van het spel begint. Dit kunnen we doen met de volgende code:

![Image](afbeeldingen/reset-pen-en-positie.png)

Nu kunnen we het spel leuker gaan maken door ervoor te gaan zorgen de we punten kunnen verdienen. Dit gaan we doen door de slang appels te laten eten. Voor elke appel krijg je een punt. Hiervoor gaan we een nieuwe sprite toevoegen:

![Image](afbeeldingen/sprite-toevoegen.png)

Eerst gaan we ervoor zorgen dat de appel op een willekeurige plek in het spel verschijnt met de volgende code:

![Image](afbeeldingen/ga-naar-willekeurige-positie.png)

Ook willen we dat de appel wat kleiner wordt:

![Image](afbeeldingen/verander-grootte.png)

Nu gaan we elke keer dat de slang beweegt kijken of hij de appel raakt:

![Image](afbeeldingen/als-raak-ik-slang.png)

Nu moeten we gaan zorgen dat we een score kunnen gaan bijhouden. Dit kunnen we gaan doen moet een variable. Een variable kun je een waarde geven, bijvoorbeeld een getal, die je met code kan veranderen. Voeg een variable 'score' toe:

![Image](afbeeldingen/variable-toevoegen.png)

Nu kunnen we zorgen dat we een punt krijgen als de slang de appel raak met de volgende code:

![Image](afbeeldingen/verander-score.png)

Nu krijgen we elke keer dat de slang de appel raak er een punt bij. Om ervoor te zorgen dat de score niet heel snel optelt gaan we de appel verplaatsen als we een punt scoren door de volgende code toe te voegen:

![Image](afbeeldingen/ga-naar-willekeurige-positie-als-geraakt.png)

Nu gaan we het spel nog wat moeilijker maken door ervoor te zorgen dat de slang niet mag botsen met de rand of met zichzelf. Eerst gaan we kijken of de slang de rand raakt met de volgende code:

![Image](afbeeldingen/als-raak-ik-rand.png)

Elke keer als de slang beweegt kijken we of de rand wordt geraakt. Als dit zo is gaan we er nu voor zorgen dat het spel stopt en de slang zegt dat het spel is afgelopen:

![Image](afbeeldingen/raak-rand-game-over.png)

Nu gaan we nog kijken of de slang zichzelf raakt. Dit gaan we doen door eerst een 'of' blok toe te voegen. Hiermee kijken we of we de rand raken of het lijf van de slang:

![Image](afbeeldingen/raak-ik-rand-of.png)

Om te kijken of de slang zichzelf raak kijken we of de ogen het lichaam van de slang raakt door te kijken naar de kleuren:

![Image](afbeeldingen/raakt-kleur-ogen-kleur-lijf.png)

Maak de eerste kleur gelijk aan de kleur van de ogen en de andere kleur gelijk aan de kleur van het lijf. Doe dit in deze volgorde anders werkt het niet! De eerste versie van ons spel is nu af! Maar je kan het spel natuurlijk nog verder uitbreiden.