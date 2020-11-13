# Maak een klok in JavaScript
In deze workshop gaan we een klok maken. Hierbij maken we gebruik van een beetje HTML en veel JavaScript.

# Basispagina in html

Om onze webpagina te maken beginnen we met het toevoegen van de volgende tags:

```html
<!DOCTYPE html>
<html>
	<head>
		<title>Klok</title>
	</head>
	<body>

	</body>
</html>
```

Hiermee maken we een lege html pagina met een titel en een plekje voor de stijl-elementen die we later willen toevoegen.

## Canvas
Om een klok te kunnen maken gaan we tekenen in JavaScript, hiervoor hebben we een canvas nodig. Tussen de body-elementen van de webpagina maken we daarom een canvas aan. We geven het canvas ook een unieke naam mee, die we zometeen vanuit JavaScript kunnen gebruiken.

```html
	<body>
		<canvas id="klok">
		</canvas>
	</body>
```

## Javascript container
Naast een plek om te tekenen hebben we ook een plek nodig om onze JavaScriptcode in te zetten, dat doen met met een script-tag in html. Script zetten we altijd netjes in de head van de pagina. We geven in de script-tag ook netjes aan om welk soort script het gaat.

```html
	<head>
		<title>Klok</title>
		<script type="text/javascript">

		</script>
	</head>
```

# JavaScript
JavaScript is een taal waarmee je webpagina's interactief kan maken, je kan er zelfs hele programma's in bouwen.

## Object
In JavaScript werk je met objecten, dat houdt in dat alle stukjes code die we maken eigenschappen hebben en acties kunnen uitvoeren. Een klok heeft bijvoorbeeld de eigenschap dat deze rond is, dat deze wijzers heeft. Een actie van een klok is dat deze een wijzer kan laten bewegen en dat deze de tijd aangeeft. Voor een object heb je een blauwdruk, of mal nodig dat we een klasse noemen. Met een klasse kan je objecten maken. Als je een object maakt doe je dat met een methode die constructor heet. Dat is een functie die een nieuw object voor je bouwt.

Ken jij voorbeelden van een blauwdruk of mal?

Een klasse maak je als volgt:
```html
		<script type="text/javascript">
			class Clock {
			}
		</script>
```

## Constructor
We moeten nu verzinnen wat voor eigenschappen een klok heeft, de minimale eigenschappen waarvan wij vinden dat een klok een klok maakt die nemen we op als eigenschappen in de constructor.

1. We moeten weten waar de klok geplaatst moet worden dus geven we het id van het canvas mee.
2. We willen weten hoe groot de ruimte is waar de klok komt te staan, dus geven we een breedte en een hoogte mee. Omdat de klok rond is gaan we later uitrekenen hoe groot die moet worden om op het canvas te passen.

```javascript
			class Clock {
				constructor (id, width, height) {
					this.id = id;
					this.width = width;
					this.height = height;
				}
			}
```

## this
Weet jij wat this betekent?

Alle eigenschappen van een object kan je in dat object benaderen met this. Het object vraagt eigenlijk iets aan zichzelf. In de constructor kunnen we al dingen gaan doen, zoals het uitrekenen hoe groot de klok wordt.

```html
			class Clock {
				constructor (id, width, height) {
					this.id = id;
					this.width = width;
					this.height = height;
					
					// uitrekenen hoe groot de klok wordt, de radius is een halve doorsnee en dat moeten we bepalen door de kortste kant door twee te delen
					if (this.width < this.height) {
						this.radius = this.width / 2;
					} else {
						this.radius = this.height / 2;
					}
				}
			}
```
Maar hoe moet ik dat nu lezen? Een vishaakje betekent groter of kleiner dan. Een < lijkt op een stukje van de K en betekent kleiner dan. De > betekent dus groter dan. 
Hier staat dus eigenlijk in code: als mijn breedte kleiner is dan mijn hoogte dan is mijn radius mijn breedte gedeeld door twee, anders is mijn radius mijn hoogte gedeeld door twee.

## Starten
Omdat we nu een stukje code hebben willen we eigenlijk gelijk weten of het juist is geschreven. We doen dit door de de klok aan te roepen.

```html
		<script type="text/javascript">
			class Clock {
				...
			}
			
			window.onload = function () {
				let clock = new Clock("klok", 300, 300);
			};
		</script>
```
Als we dit aanroepen dan gebeurt er niet iets dat we kunnen zien. We kunnen wel zien of we een fout hebben gemaakt, maar we kunnen nog niet zien of we het goed hebben gedaan. We gaan er dus even vanuit dat zolang het niet fout is dan is het goed.

## canvas aanpassen
We moeten nu ons tekenvel nog aanpassen zodat onze klok er op past. Hiervoor gaan we een methode toevoegen die het canvas inricht.
```html
			class Clock {
				constructor (id, width, height) {
					...
				}
				
				canvas () {
					this.canvas = document.getElementById(this.id);
					this.canvas.width = this.width;
					this.canvas.height = this.height;
					this.context = this.canvas.getContext("2d");
				}
			}
```
Deze methode haalt het canvas-html-element op en geeft dat element dan een breedte en een hoogte. Vervolgens moeten we een eigenschap van het canvas ophalen en bewaren zodat we kunnen gaan tekenen. Tekenen doen we op basis van de context.

## cirkel tekenen
Deze klok heeft een rand, zodat deze goed zichtbaar is op het canvas. De rand is een cirkel, die moeten we dus gaan tekenen.
```html
			class Clock {
				constructor (id, width, height) {
					...
				}
				
				canvas () {
					...
				}
				
				circle() {
					this.context.beginPath();
					this.context.arc(
						this.canvas.width / 2,
						this.canvas.height / 2,
						this.radius,
						0,
						Math.PI*2
					);
					
					this.context.lineWidth=1;
					this.context.stroke();
				}
			}
```

Om een cirkel te tekenen moeten we beginnen met een pen op het canvas zetten, een pad (paadje) maken met path. Daarna zeggen we dat we een boog willen maken, dat noemen we een arc. Je kan zien dat arc een methode is van het object context. Die methode heeft parameters nodig. Parameters zijn waardes die we aan het object geven zodat die er iets mee kan doen. Bij de methode arc geven we vijf parameters mee:
1. x-coordinaat van het centrum van de cirkel: de helft dus van de totale breedte
2. y-coordinaat van het midden van de cirkel: de helft van de totale hoogte
3. r: de radius van de cirkel
4. start punt: we starten op rad 0 
5. eind punt: we eindigen aan het einde van de cirkel (dat is de totale omtrek in dit geval: 2*PI*r)

Nadat we de boog hebben bepaald stellen we de dikte van de cirkel in op 1. Daarna tekenen we de cirkel met stroke.

## Resultaat
Om het resultaat van onze oefeningen te kunnen bekijken gaan we de aanroep een beetje aanpassen. In eerste instantie hadden we alleen een clock object gemaakt, nu gaan we ook het canvas en de cirkel functie aanroepen.

```html
		<script type="text/javascript">
			class Clock {
				...
			}
			
			window.onload = function () {
				let clock = new Clock("klok", 300, 300);
				clock.canvas();
				clock.circle();
			};
		</script>
```
We moeten nu een cirkel om het scherm kunnen zien. Deze cirkel is misschien niet helemaal perfect omdat deze precies even groot is als het canvas en daarom lijkt het alsof deze een beetje van het scherm valt. Voor nu vinden we dat niet erg, je kan zelf later uitzoeken hoe je dat mooier kan maken (tip: dit heeft met de grootte van de cirkel en de grootte van het canvas te maken).

# Tijd in JavaScript
Tijd in JavaScript kan je niet tellen zoals je dat met een horloge doet. Je moet eigenlijk met JavaScript zo nu en dan kijken hoe laat het is. Dat doe je met een timeout. Een timeout is een soort kookwekker die na een aantal milliseconden kijkt hoe laat het is. Voor de klok gaan we dan ook elke seconde kijken hoe laat het is en tekenen we de klok opnieuw.

```html
		<script type="text/javascript">
			class Clock {
				...
				
				show() {
					this.circle();
					
					var that = this;
					setTimeout(function() {
						that.show();
					}, 1000);
				}
			}
			
			...
		</script>
```
De timer is nu gemaakt, nu moet deze worden aangeroepen. De window.onload functie moet daarvoor worden aangepast.
```html
			window.onload = function () {
				let clock = new Clock("klok", 300, 300);
				clock.canvas();
				clock.show();
			};
```
We hebben circle in show veranderd. Bij het laden wordt nu een canvas getekend, dan wordt er een timer gezet die elke seconde de cirkel opnieuw tekent.  Als je goed lijkt wordt de cirkel steeds dikker. Dat komt omdat we voordat we gaan tekenen ons canvas niet schoon maken. Voor een cirkel is dat geen probleem, maar zometeen als we wijzers gaan tekenen gaat het wel fout. Let maar op.

## Wijzers
Wijzers zijn eigenlijk lijnen, een klok heeft drie lijnen: een voor de uren, een voor de minuten en een voor de seconden. We gaan dus als handigheid een methode maken die een lijn tekent en die methode gaan we dan drie keer aanroepen. Een uurlijn is kort en dik en zwart. Een minutenlijn is lang en dun en zwart. Een secondenlijn is lang en dun en rood. Een lijn moet dus alle drie deze eigenschappen bevatten.

```html
		<script type="text/javascript">
			class Clock {
				...
								
				line(x, y, params) {
					this.context.beginPath();
					this.context.moveTo(this.canvas.width / 2, this.canvas.height / 2);
					this.context.lineTo(x, y);
					this.context.lineWidth = params.width ? params.width : 1;
					this.context.strokeStyle = params.colour ? params.colour : 'black';
					this.context.stroke();
				}
			}
		</script>
```

Bovenstaande methode tekent voor ons een lijn. We beginnen met tekenen in de context, daarna gaan we naar het midden met moveTo en dan gaan we een lijn tekenen naar de x en y coordinaten op de rand van de cirkel. Daarna geven we ook aan hoe dik de lijn moet zijn (behalve als we dat niet weten dan wordt de lijn 1 dik) en we geven de kleur aan (behalve als we dat niet weten dan wordt de lijn rood). En als laatste tekenen we de lijn met stroke.

## Wijzers op de juiste plek
We hebben nu wijzers maar we weten niet waar x en y zijn. We moeten dus eigenlijk de echte tijd weten en die vertalen naar een plekje op de cirkel van de klok.

```html
		<script type="text/javascript">
			class Clock {
				...
								
				draw(dt, params) {
					var angle = this.sec2radian(dt);
					var point = this.point(
						this.canvas.width / 2,
						this.canvas.height / 2,
						params.length ? params.length * this.radius: this.radius,
						angle
					);
					
					this.line(point[0], point[1], params);
				}			

				sec2radian(sec) {
					return (2 * Math.PI / 60 * sec) - (Math.PI / 2);
				}
				
				point(x, y, r, angle) {
					return [x + Math.cos(angle) * r, y + Math.sin(angle) * r];
				}
			}
		</script>
```
Je ziet hier drie methoden. De eerste is om de eerder gemaakte line methode aan te roepen. De tweede is om de hoek te bepalen. Laten we het even stap voor stap doornemen en we beginnen bij de tweede methode. Een stukje cirkel dat even lang is als de straal of radius noem je een radian. Een cirkel is altijd 2*PI*radius groot. Een rondje is 60 seconden. We berekenen dus op welke plek van de cirkel we moeten zijn op het huidige aantal seconden. Let op dat een radius altijd op kwart over / drie uur begint. Een kwart cirkel is gelijk aan een halve pi, daarom corrigeren we met een halve pi.

De eerste methode draw krijgt als parameter de tijd mee en een paar instellingen. De tijd gebruiken we om de hoek te berekenen waarin we de lijn van de wijzers moeten zetten. Daarna gaan we het punt op de cirkel bepalen waar we de lijn vanaf het midden naartoe moeten tekenen. Dat punt berekenen we met de derde methode; de parameters zijn de x en y coordinaten op het canvas waar we moeten beginnen. Daarna de radius en daarna de hoek (die hadden we al eerder met de tweede methode uitgerekend). De methode point geeft een lijstje terug met op de eerste plaats de x en op de tweede plaats de y coordinaat op de cirkel waar de lijn van de wijzer naar toe moet worden getekend. Draw roept nu de eerdere methode line aan om de lijn te tekenen in de juiste dikte en met de juiste kleur.

## Teken de wijzers
We gaan de show methode aanpassen en wijzers tekenen.

```html
				show() {
					this.circle();
					
					// get the time and draw the hands
					var date = new Date();
					this.draw(date.getSeconds(), {colour: 'red', length: 0.9});
					this.draw(date.getMinutes(), {width: 2, length: 0.8});
					this.draw(date.getHours() * 5, {width: 3, length: 0.6});
					
					var that = this;
					setTimeout(function() {
						that.show();
					}, 1000);
				}	
```
Als je nu je pagina bekijkt zie je een wijzerplaat en er verschijnt steeds een nieuwe wijzer. Dat ziet er best gek uit. Wat we nog moeten doen is elke keer dat we de klok tekenen even het canvas schoonmaken.

## Opschonen
```html
		<script type="text/javascript">
			class Clock {
				...
				
				clean() {
					this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);				
				}
			
				show() {
					this.clean();
					this.circle();
					...
			}
		</script>
```
We hebben een clean methode toegevoegd die het canvas schoonmaakt. Vervolgens roepen we deze methode in show aan.

# Klaar!
Nu heb je als het goed is een werkende klok. Kan je deze nu pimpen?
