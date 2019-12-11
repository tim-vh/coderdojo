# Maak je eigen webpagina 

## HTML

Een HTML-pagina bestaat uit tags waarmee je aangeeft wat je op de pagina wil tonen en hoe dit eruit komt te zien. Een tag staat tussen een '<' en een '>' teken. Dit ziet er dan bijvoorbeeld zo uit: `<p>`. Dit is een begin-tag maar je hebt ook een eindtag. Die ziet er zo uit: `</p>`. Tussen de begin- en eindtag zet je de inhoud. Als je een paragraag met tekst wil maken ziet dit er zo uit: `<p>Dit is een paragraaf met tekst</p>`

### Basispagina

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

Titels kun je toevoegen met de tags `<h1>` t/m `<h6>`. De 'h' staat voor heading en betekent titel of kop. De `<h1>` is de belangrijkste kop en is standaard het grootst. De `<h6>` is de minst belangrijkste kop en is standaard het kleinst.

### Links toevoegen

### Plaatjes

### Youtube video toevoegen

### Een lijst maken

### Andere tags

Lijst van alle tags: https://www.w3schools.com/tags/

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

In de `<style>` tag gaan we nu CSS toevoegen om de kleur van de tekst aan te passen. Onze `<style>` tag komt er dan zo uit te zien:

```html
<style>
    p {color: blue; }
</style>
```

Met de CSS geef je eerst aan wat op de pagina er aangepast moet worden. Dit gebeurt met de `p` en betekend dat we de paragraven op de pagina willen aanpassen. Na de `p` zet je tussen accolades, een `{` en een `}` teken, hoe dit moet worden aangepast. Om de kleur van tekst aan te passen zet je `color` neer, dit is engels voor kleur. Daarna zet je een `:` teken neer zodat je daarna de kleur kan opgeven. Dit kan door de engelse naam van de kleur op te geven, voor blauw is dit `blue`.

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

### Lettertype en lettergrote

### Andere CSS-eigenschappen

Lijst van alle CSS-eigenschappen: https://www.w3schools.com/cssref/