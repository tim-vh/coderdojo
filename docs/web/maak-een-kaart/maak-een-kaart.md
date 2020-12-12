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

```css
h1 {
  color: green;
}
```

### Achtergrond afbeelding

Om een achtergrond afbeelding toe te voegen gaan we de CSS voor de body en de html tag toevoegen

```css
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

```css
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

## Programmeren met javascript

We gaan aan onze kaart toevoegen dat iemand zijn naam kan opgeven, zodat we dit in de tekst van de kaart kunnen zetten. Om dit te kunnen doen gaan we eerst een formulier aan de html toevoegen. Dit formulier zetten we boven de kaart in de `<body>` tag van de html. Dit kan op de volgende manier.

```html
...
<div id="form">
  <label for="naam">Wat is je naam</label>
  <input id="naam" type="text" />
  <button id="create">
    Maak kaart
  </button>
</div>
...
```

Om het er wat mooier uit te laten zien voegen we de volgende css toe voor het formulier:

```css
...
#form {
  background-color: white;
  margin: 0 auto;
  width: 50%;
  padding: 20px;
}
...
```

Nu gaan we de javascript toevoegen waarmee we de kaart programmeren. We gaan eerst een functie toevoegen. In de functie gaan we neerzetten wat er moet gebeuren. De functie ziet er zo uit:

```javascript
function create() {

}
```

We willen de functie uitvoeren als we op de knop van het formulier drukken. Hiervoor gaan we de html als volgt aanpassen

```html
...
    <div id="form">
      <label for="naam">Wat is je naam</label>
      <input id="naam" type="text" />
      <button id="create" onclick="create()">
        Maak kaart
      </button>
    </div>
...
```

In `<button>` tag is er een 'event' toegevoegd. Deze ziet er zo uit `onclick="create()"`. Dit betekend dat als er op de knop wordt geklikt de functie 'create' wordt aangeroepen.

We gaan testen of de knop en de functie goed werken. We gaan hiervoor eest een stuk code aan de functie toevoegen:

```javascript
function create() {
  alert('test');
}
```

Als je nu op de knop drukt zie je ongeveer het volgende:

![Image](afbeeldingen/alert.png)

Nu gaan we de code aanpassen zodat de naam uit het formulier op de kaart wordt gezet. Om dit te doen moeten we eerst in de html zetten waar de naam moet komen. Daarvoor gaan we een `<span>' tag toevoegen met een id zodat we de tag kunnen vinden met code. Dit komt er zo uit te zien in de html:

```html
...
<p>
  Hallo <span id="naam-tekst"></span>,
  Een fijne kerst en een gelukkig nieuw jaar.
  Groeten, Coderdojo
</p>
...
```

Nu kunnen we code gaan toevoegen om de naam op te halen uit het formulier. Dit kan op de volgende manier:

```javascript
function create() {
	var naam = document.getElementById('naam').value;  
}
```

Met deze code maken we een variabele en die vullen we met de waarde die in het invoerveld met het id 'naam' staat.

Nu gaan we ervoor zorgen dat de naam in de tekst komt te staan. Dit kan op de volgende manier:

```javascript
function create() {
  var naam = document.getElementById('naam').value;
  document.getElementById('naam-tekst').innerHTML = naam;
}
```

We hebben nu een regel toegevoegd die eerst de plek in de html ophaalt waar de naam moet komen te staan. Daarna vullen we de plek met de waarde van de variable naam.