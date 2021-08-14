# Lagre bilder med Turtle Graphics

Når vi har lagd et kunstverk med Turtle, så har vi gjerne lyst til å lagre det som et bilde. Innebygd i Turtle, så kan vi lagre kunsten vår som *PostScript*-filer. PostScript er en type fil som historisk ble brukt mye for print, men i dag er det dessverre ikke mange program som støtter dette filformatet. I denne guiden vil vi derfor vise hvordan dere lagrer turtle-kunst som PostScript filer, og tre måter dere kan konvertere disse postscript-filene til *vanlige*-bildeformat som PNG (som vi anbefaler fremfor JPG).



## Lagre turtle-kunst som PostScript



Når du har tegnet noe med turtle, så kan du lagre bildet som er i Turtle-vinduet som en PostScript fil med kommandoen

````python
turtle.getscreen().getcanvas().postscript(file="filnavn.eps")
````

Kommandoen over vil ta det som er tegnet i Turtle-vinduet og lagre det i filen "filnavn.eps". 
La oss se hvordan dette vil virke i praksis med å lagre et bilde av en firkant

````python
import turtle

penn = turtle.Turtle()
for side in range(4):
    penn.forward(50)
    penn.right(90)

turtle.getscreen().getcanvas().postscript(file="skilpaddekunst.eps")
````

Med dette vil vi lagre en fil "skilpaddekunst.eps", som inneholder bildet av firkanten vår. Neste steg er å lagre dette som en PNG-fil (PNG er bedre enn JPG, siden JPG-komprimeringen ikke egner seg for Turtle-kunst).

## Tre måter å konvertere EPS til PNG
### Gjennom Spyder (eller Anaconda prompt)

Det første vi må gjøre er å aktivere GhostScript-funksjonaliteten i Anaconda. GhostScript er et lite program som kan lese og konvertere postscript og PDF filer til andre formater. I Spyder kan aktivere denne funksjonaliteten med denne kommandoen (som du skriver i Python vinduet nede i høyre hjørne):
```
!conda install ghostscript -y -c conda-forge
```
Nå som GhostScript er aktivert, kan vi bruke det for å konvertere PostScript-filen til en PNG fil. Det gjør du med å skrive denne kommandoen i kommandovinduet:
```
!gs -dSAFER -dNOPAUSE -dBATCH -r300 -sDEVICE=pngalpha -sOutputFile=skilpaddekunst.png skilpaddekunst.eps
```
Denne kommandoen vil laste inn filen "skilpaddekunst.eps" og konvertere den til filen "skilpaddekunst.png".

Noe av det som er så praktisk med Spyder er at man kan putte slike "ekstrakommandoer", som ikke er gyldig Pythonkode inne i Python-scriptene våre. Hvis vi gjør det, så må programmet kjøres gjennom Spyder (eller strengt tatt IPython, som Spyder bruker for å kjøre Python-kode). Vi kan altså ha et script som ser slik ut som vil lagre både en PostScript fil og en PNG fil:


````python
import turtle

penn = turtle.Turtle()
for side in range(4):
    penn.forward(50)
    penn.right(90)

turtle.getscreen().getcanvas().postscript(file="skilpaddekunst.eps")
!gs -dSAFER -dNOPAUSE -dBATCH -r300 -sDEVICE=pngalpha -sOutputFile=skilpaddekunst.png skilpaddekunst.eps
````

### Ved å bruke internettkonverterere

Det finnes en rekke nettsider som kan konvertere EPS-filer til PNG-filer. De er ofte gratis å bruke for noen bilder om dagen (f.eks. 25), også kan man få mulighet til å konvertere flere bilder ved å betale en liten sum. Her er noen slike nettsider:

 * https://cloudconvert.com/ps-to-png
 * https://psviewer.org/convertpstopng.aspx
 * https://www.aconvert.com/image/ps-to-png/
 * https://www.docspal.com/convert/ps-to-png


### Ved å bruke GhostScript gjennom IrfanView

IrfanView er et utrolig bra program som man kan bruke for å se på og konvertere bilder med. Det er gratis for undervisning og eget bruk, og hvis man har installert GhostScript (det fulle programmet) kan det åpne PostScript filer og lagre de som PNG filer. Du kan laste ned PostScript herfra:https://www.ghostscript.com/download/gsdnld.html og IrfanView herfra: https://www.irfanview.com/64bit.htm (du må installere både IrfanView og plugin-pakken). Når du har installert IrfanView så starter du programmet og trykker på "Open" knappen i øvre venstre hjørne. Naviger deg til der du kjørte Turtle-programmet ditt og åpne filen "skilpaddekunst.eps" (hvis du ikke ser den, så må du velge "All files (*.*)" i dropdown-menyen "Files of type"). 