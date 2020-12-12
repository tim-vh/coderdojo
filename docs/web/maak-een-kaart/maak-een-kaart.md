# Maak een digitale kaart

## Inhoud van de kaart

Om onze kaart te maken beginnen we met het toevoegen van de volgende tags:

```html
<!DOCTYPE html>
<html>
<body>

</body>
</html>
```

Hiermee maak je een lege pagina. Met `<!DOCTYPE html>` geef je aan wat het type html is. De `<html>` geeft aan dat hier de HTML begint. Met `<body>` geef je aan dat dit de inhoud van de pagina is.

We gaan hier nu een tag aan toevoegen voor de kaart. Dit is de `<div>` tag. Deze tag gaan we ook een id meegeven zodat we de kaart later kunnen vinden met code. De code komt er dan zo uit te zien:

```html
<!DOCTYPE html>
<html>
<body>
 <div id="kaart">
 </div>
</body>
</html>
```

De volgende stap is dat we op de kaart een titel, een plaatje en een tekst gaan zetten.

### Titels

Titels kun je toevoegen met de tags `<h1>` t/m `<h6>`. De 'h' staat voor heading en betekent titel of kop. De `<h1>` is de belangrijkste kop en is standaard het grootst. De `<h6>` is de minst belangrijkste kop en is standaard het kleinst. Een titel kan er bijvoorbeeld zo uitzien:

```html
<h1>Dit is de titel van de website</h1>
```

We gaan de titel toevoegen aan de kaart en dit komt er zo uit te zien:

```html
<!DOCTYPE html>
<html>
<body>
 <div id="kaart">
  <h1>
   Fijne kerst
  </h1>
 </div>
</body>
</html>
```

### Plaatjes

Om een plaatje toe te voegen op een pagina kun je de `<img>` tag gebruiken. Deze tag heeft alleen maar een begin-tag omdat er niks tussen de tags kan komen te staan. Om aan te geven welke afbeelding je wil laten zien op je pagina kun je een `src` attribuut toevoegen met daarin het adres van de afbeelding. Dit ziet er dan zo uit:

```html
<img src="http://eenwebsite.nl/afbeelding.jpg">
```

Onder de titel gaan we nu een plaatje toevoegen. Voor het plaatje gaan we ook een breedte opgeven. Dit kunnen we doen met `width`. We gaan ervoor zorgen dat het plaatje half zo breed is als de kaart door hiervoor 50% op te geven.

```html
<!DOCTYPE html>
<html>
<body>
 <div id="kaart">
  <h1>
   Fijne kerst
  </h1>
  <img src="https://cdn.pixabay.com/photo/2016/11/15/19/25/santa-claus-1827265_1280.jpg" width="50%" />
 </div>
</body>
</html>
```

### Tekst

De tekst gaan we toevoegen door een `<p>` tag toe te voegen waarmee we een paragraag toevoegen. 

```html
<!DOCTYPE html>
<html>
<body>
 <div id="kaart">
  <h1>
   Fijne kerst
  </h1>
  <img src="https://cdn.pixabay.com/photo/2016/11/15/19/25/santa-claus-1827265_1280.jpg" width="50%" />
  <p>
        Hallo,
        Een fijne kerst een een gelukkig nieuw jaar.
        Groeten, Coderdojo
      </p>
 </div>
</body>
</html>
```

## Styling van de html pagina

We gaan er nu voor zorgen dat de kaart er nog wat mooier uit komt te zien. Dit gaan we doen door CSS toe te voegen. Hiermee kunnen we aangeven hoe de html die we hebben toegevoegd eruit komt te zien.

### Kleur van de tekst veranderen

Met de CSS geef je eerst aan wat op de pagina aangepast moet worden. Dit gebeurt met de `h1` en betekend dat we de kop op de pagina willen aanpassen. Na de `h1` zet je tussen accolades, een `{` en een `}` teken, hoe dit moet worden aangepast. 

Om de kleur van tekst aan te passen zet je `color` neer, dit is engels voor kleur. Daarna zet je een `:` teken neer zodat je daarna de kleur kan opgeven. Dit kan door de engelse naam van de kleur op te geven, voor groen is dit `green`. 

```html
h1 {
  color: green;
}
```

### Achtergrond afbeelding

Om een achtergrond afbeelding toe te voegen gaan we de CSS voor de body en de html tag toevoegen

```html
h1 {
  color: green;
}

html
{
  height: 100%;
}

body {
  background-image: url('https://cdn.pixabay.com/photo/2017/11/01/18/17/christmas-2908901_1280.jpg');
  background-size: cover;
}
```

De CSS voor de html zorgt dat de html pagina zo hoog wordt als het scherm. In de CSS voor de body geven we een url op voor het plaatje wat we willen toen. Dit doen we met `background-image`. Om ervoor te zorgen dat de achtergrond afbeelding zo groot wordt als de pagina zelf geven we op hoe groot de achtergrond moet worden met `background-size: cover;`

### Styling voor de kaart

Om de kaart in het midden van de pagina te zetten en de kleuren van de kaart aan te passen gaan we CSS voor de kaart toevoegen. Omdat we in de html de kaart een id hebben gegeven kunnen we in de CSS zeggen dat we alleen styling voor de kaart willen toevoegen. Als we een `#` teken neerzetten met daarachter het id geldt de opmaak alleen voor die html. Dit ziet er dan zo uit:

```html
h1 {
  color: green;
}

html
{
  height: 100%;
}

body {
  background-image: url('https://cdn.pixabay.com/photo/2017/11/01/18/17/christmas-2908901_1280.jpg');
  background-size: cover;
}

#kaart {
  margin: 0 auto;
  width: 50%;
  text-align: center;
  background-color: white;
  border: 20px solid red;
}
```

Met `margin: 0 auto;` zorgen we dat de kaart in het midden van de pagina wordt gezet. Om de breedte op te geven gebruiken we `width: 50%;`. Hierdoor wordt de kaart de helft van de pagina breed. Daarna zorgen we er nog voor de de tekst op de kaart in het midden komt te staan met `text-align: center;`.

Ook kunnen zorgen we er nog voor dat de kaart een witte achtergrond krijgt met `background-color: white;`. Als laatste voegen we een rand toe aan de kaar. Dit geberut met `border: 20px solid red;`, wat betekend dat de rand 20 pixels breed moet worden, van het type 'solid' is en een rode kleur krijgt.

