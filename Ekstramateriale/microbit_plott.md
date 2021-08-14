# Mini-guide til plotting av data fra en Micro:bit

Micro:bit-er ikke pensum for dette kurset, men for de interesserte har vi lagd en kort mini-guide for plotting av data fra en Micro:bit.

Her er en lenke til et lite eksempelskript som logger informasjon fra Micro:bit-en: [https://makecode.microbit.org/_HrAXkkPqFhoW](https://makecode.microbit.org/_HrAXkkPqFhoW).
For å bruke scriptet må du bruke en Chromium-basert nettleser (altså ikke Firefox eller gamle versjoner av Microsoft Edge/Internet Explorer).
Når du har åpnet nettsiden, trykker på "Edit"-knappen oppe i høyre hjørne, og så på Download knappen. Følg instruksjonene for å overføre programmet til Micro:bit-en.
For å lagre CSV-filen trykker du på "Show console   Device"-knappen — da vil du få et plott som viser vinkelen til Micro:bit-en.
Oppe i høyre hjørne av dette plottet er det en blå knapp (Export data), og hvis du trykker på denne knappen vil du kunne laste ned måledatene i form av en CSV-fil.

Når du har lastet ned denne filen så kan vi plotte den med Python.
Under er en liten eksempelkodesnutt som viser hvordan du kan laste inn fila med Pandas og plotte målingene med matplotlib:

```python
import pandas as pd
import matplotlib.pyplot as plt

filnavn = "microbit-data-14-2021-19-03-25-0200.csv"
data = pd.read_csv(filnavn, delimiter="\t", skiprows=1)
# Vi setter delimiter til "\t" siden det er et "Tab"-tegn som brukes for å separarere kolonnene
# Vi setter skiprows til 1 siden den første linja i fila kun beskriver hvilket tegn vi bruker for å skille kolonnene
print(data.head())  # Vis de første fem radene av tabellen

plt.plot(data["time (source1)"], data["data.heading"])
plt.xlabel("Tid [s]")
plt.ylabel("Vinkel i grader")
plt.savefig("vinkelplott.png")
plt.show()
```
