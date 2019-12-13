# Maak je eigen webpagina 

## HTML

Een HTML-pagina bestaat uit tags waarmee je aangeeft wat je op de pagina wil tonen en hoe dit eruit komt te zien. Een tag staat tussen een '<' en een '>' teken. Dit ziet er dan bijvoorbeeld zo uit: `<p>`. Dit is een begin-tag maar je hebt ook een eindtag. Die ziet er zo uit: `</p>`. Tussen de begin- en eindtag zet je de inhoud. Als je een paragraaf (een soort hoofdstuk) wil maken ziet dit er zo uit: `<p>Dit is een paragraaf met tekst</p>`

### Basispagina

Om onze webpagina te maken beginnen we met het toevoegen van de volgende tags:

```html
<!DOCTYPE html>
<html>
<body>

</body>
</html>
```

Hiermee maak je een lege pagina. Met `<!DOCTYPE html>` geef je aan wat het type html is. De `<html>` geeft aan dat hier de HTML begint. Met `<body>` geef je aan dat dit de inhoud van de pagina is.

### Tekst

Als je tekst toe wilt voegen kun je dit bijvoorbeeld in een paragraaf zetten. Dit kan door een `<p>` tag in de `<body>` tag te zetten. De HTML op de pagina komt er dan zo uit te zien:

```html
<!DOCTYPE html>
<html>
<body>
    <p>Dit is een paragraaf met tekst</p>
</body>
</html>
```

### Titels

Titels kun je toevoegen met de tags `<h1>` t/m `<h6>`. De 'h' staat voor heading en betekent titel of kop. De `<h1>` is de belangrijkste kop en is standaard het grootst. De `<h6>` is de minst belangrijkste kop en is standaard het kleinst. Een titel kan er bijvoorbeeld zo uitzien:

```html
<h1>Dit is de titel van de website</h1>
```

### Links toevoegen

Met een link kun je naar een andere pagina gaan. Een link kun je maken met de `<a>` tag. Tussen de begin- en eindtag zet je de naam van de link. Dit ziet er dan zo uit:

```html
<a>Zoeken met google<a>
```

Nu moeten we nog opgeven wat het adres is van webpagina waar we naartoe willen linken. Dit kan door een attribuut toe te voegen. Een attribuut zet je in de tag. Om het adres van de link op te geven gebruik je het `href` attribuut. Voor onze link naar google ziet dit er dan zo uit:

```html
<a href="https://www.google.com/">Zoeken met google</a>
```

### Plaatjes

Om een plaatje toe te voegen op een pagina kun je de `<img>` tag gebruiken. Deze tag heeft alleen maar een begin-tag omdat er niks tussen de tags kan komen te staan. Om aan te geven welke afbeelding je wil laten zien op je pagina kun je een `src` attribuut toevoegen met daarin het adres van de afbeelding. Dit ziet er dan zo uit:

```html
<img src="http://eenwebsite.nl/afbeelding.jpg">
```

### Youtube video toevoegen

Video's die op youtube staan kun je ook op je eigen webpagina zetten (Kan niet met alle video's). Ga hiervoor naar youtube en ga naar de video die je op de site wil zetten. Klik daarna op de knop 'delen' onder de video. Kies daarna voor 'Insluiten'. Nu zie je aan de rechterkant HTML verschijnen die we op onze webpagina kunnen zetten. Dit ziet er zo uit:

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/c7ROVdcyk7s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

### Andere tags

Op de volgende website kun je een Lijst van alle HTML tags vinden: https://www.w3schools.com/tags/

## CSS

Met CSS kun je aangeven hoe dingen op de pagina eruit moeten komen te zien. Om CSS toe te voegen gaan we eerst een `<style>` tag aan de HTML toevoegen. In deze tag komt de CSS te staan. Onze HTML ziet er dan zo uit:

```html
<!DOCTYPE html>
<html>
    <style>
            
    </style>
    <body>
        <p>Dit is een paragraaf met tekst</p>
    </body>
</html>
```

### Kleur van de tekst veranderen

In de `<style>` tag gaan we nu CSS toevoegen om de kleur van de tekst aan te passen. Met de CSS geef je eerst aan wat op de pagina aangepast moet worden. Dit gebeurt met de `p` en betekend dat we de paragrafen op de pagina willen aanpassen. Na de `p` zet je tussen accolades, een `{` en een `}` teken, hoe dit moet worden aangepast. 

Om de kleur van tekst aan te passen zet je `color` neer, dit is engels voor kleur. Daarna zet je een `:` teken neer zodat je daarna de kleur kan opgeven. Dit kan door de engelse naam van de kleur op te geven, voor blauw is dit `blue`. Onze `<style>` tag komt er dan zo uit te zien:

```html
<style>
    p {color: blue; }
</style>
```

### Achtergronden

Als je de achtergrondkleur van de pagina wil aanpassen kan dat met de eigenschap `background-color`. Deze kun je dan instellen voor de `body` tag. Als je de achtergrond groen wil maken kan dat op de volgende manier:

```html
<style>
    body { background-color: green; }
</style>
```

Het is ook mogelijk om een plaatje te gebruiken als achtergrond. Dit kan met de eigenschap `background-image`. Hierachter kun je de locatie (url) van een plaatje opgeven. Dit ziet er dan zo uit:

```html
<style>
    body { background-image: url('http://eenwebsite.nl/afbeelding.jpg'); }
</style>
```

### Lettergrote

Om letters groter te maken kun je gebruik maken van de eigenschap `font-size`. Dit kan bijvoorbeeld op de volgende manier

```html
<style>
    p { font-size: 50px; }
</style>
```

Nu hebben we voor paragrafen de grote van de letters 50 pixels gemaakt.

### Andere CSS-eigenschappen

Op de volgende website kun je een Lijst van alle CSS-eigenschappen vinden: https://www.w3schools.com/cssref/

## Javascript

Met javascript kun je een webpagina programmeren. Om javascript toe te voegen gaan we eerst een `<script>` tag aan de HTML toevoegen. In deze tag komt de javascript te staan. Onze HTML ziet er dan zo uit:

```html
<!DOCTYPE html>
<html>
    <script>
            
    </script>
    <body>
    </body>
</html>
```

### Raad een getal

Met javascript gaan we een klein spelletje maken dat je op de webpagina kan spelen. In het spel is het de bedoeling dat de speler een getal gaat raden.

De eerste stap is dat we een getal gaan bedenken en dat we deze opslaan. Dit gaan we doen in een variable. Dit gaat op de volgende manier:

```html
<script>
    var getal = 4;
</script>
```

We hebben nu een getal dat de speler moet gaan raden. Dit is nu altijd vier, maar dit gaan we later nog aanpassen.

De volgende stap is dat we een vraag gaan stellen aan de speler. Dit kan op de volgende manier:

```html
<script>
    var getal = 4;
    prompt("Raad een getal");
</script>
```

Met `prompt` kunnen een vraag stellen, en tussen de haakjes kan je opgeven wat de vraag moet zijn.

De volgende stap is dat we het antwoord van de speler willen opslaan in een variable. Hiervoor gaan we een nieuwe variable toevoegen met de naam 'antwoord'. Dit komt er zo uit te zien:

```html
<script>
    var getal = 4;
    var antwoord;

    antwoord = prompt("Raad een getal");
</script>
```

We hebben nu het antwoord van de speler opgeslagen. Nu gaan we kijken of het antwoord van de speler gelijk is aan het getal dat we hebben bedacht. Dit kan met een `if` wat engels is voor 'als'. Dit gaat op de volgende manier:

```html
<script>
    var getal = 4;
    var antwoord;

    antwoord = prompt("Raad een getal");

    if(antwoord == getal)
    {
        
    }
</script>
```

Tussen de haakjes van de `if` zet je wat je wil vergelijken. We vergelijken de variabelen 'antwoord' en 'getal'.  Als je iets wil vergelijken zet je twee '=' tekens neer (`==`). 

Tussen de accolades (`{` en `}` teken) kunnen we zetten wat er moet gebeuren als het getal gelijk is aan het antwoord. Hier willen we tegen de speler gaan zeggen dat het getal goed is geraden. Dit kunnen we doen met `alert`. Dit komt er zo uit te zien:

```html
<script>
    var getal = 4;
    var antwoord;

    antwoord = prompt("Raad een getal");

    if(antwoord == getal)
    {
        alert("Goed geraden");
    }
</script>
```

Ook hier kunnen we weer tussen de haakjes zetten wat we willen zeggen. We kunnen ook iets zeggen als de speler het fout heeft geraden. Dit kan met een `else` en dat is engels voor 'anders'. Onze code komt er dan zo uit te zien:

```html
<script>
    var getal = 4;
    var antwoord;

    antwoord = prompt("Raad een getal");

    if(antwoord == getal)
    {
        alert("Goed geraden");
    } else { 
        alert("Dat was helaas niet goed");
    }
</script>
```

De speler kan het getal nu een keer raden. De volgende stap is dat we ervoor zorgen dat de speler kan raden totdat het antwoord goed is. Dit kan door een herhaling toe te voegen. In javascript kan dit bijvoorbeeld met een `while`. We gaan de code op de volgende manier aanpassen:

```html
<script>
    var getal = 4;
    var antwoord;

    while (antwoord != getal) {
        antwoord = prompt("Raad een getal");

        if (antwoord == getal) {
            alert("Goed geraden");
        } else {
            alert("Dat was helaas niet goed");
        }
    }
</script>
```

Tussen de haakjes van de `while` kunnen we opgeven voor hoe lang de code herhaald moet worden. Zolang het antwoord niet gelijk is aan het getal wordt de code herhaalt. De tekens `!=` betekenen niet gelijk aan elkaar en is het tegenovergestelde van de tekens `==`. De code tussen de `{` en `}` na de `while` wordt nu herhaald.

Nu is het getal dat de speler moet raden altijd hetzelfde. De laatste stap is dat we dit getal willekeurig gaan maken. Dit kan met `Math.random()`. Om te zorgen dat dit een getal wordt van 0 tot en met 9 moeten we het eerst keer 10 doen en daarna nog afronden. Afronden kan met `Math.floor()` en om een getal keer tien te doen gebruik je `* 10`. Pas de code aan zodat het er zo uit komt te zien:

```html
<script>
    var getal = Math.floor(Math.random() * 10);
    var antwoord;

    while (antwoord != getal) {
        antwoord = prompt("Raad een getal");

        if (antwoord == getal) {
            alert("Goed geraden");
        } else {
            alert("Dat was helaas niet goed");
        }
    }
</script>
```

Goed gedaan! De eerste versie van ons spel is nu af.

> Uitdaging: Als je het fout hebt zeg dan of het getal hoger of lager is. Tip: Om te kijken of een getal hoger is kun je het `>` teken gebruiken in een `if`.

> Uitdaging: Zorg ervoor dat je maximaal 5 keer kan raden. Tip: Maak een nieuwe variabele om het aantal pogingen bij te houden.