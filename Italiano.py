import re

texto = """Salve! Nel 2025, 7 amici visitano Milano. Lista: risotto, pane, vino. Il prezzo è €14,30. 
Le stelle (★) brillano sopra la città. 3 gatti saltano, 2 cani giocano. Il codice #6789 è segreto. 
6 giorni di lavoro, 1 giorno di riposo. @tutti sono invitati. Il numero magico è 88. 
Cosa faresti con 11,25€? La risposta è nella lista: leggere, scrivere, ballare. Vivi ogni giorno! 
100 parole, 6 interi, 3 decimali, 2 liste."""

# 🔹 Palabras y símbolos especiales
palabras = (
    re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ']+-[A-Za-zÀ-ÖØ-öø-ÿ']+", texto) +
    re.findall(r"\b[A-Za-zÀ-ÖØ-öø-ÿ']+[!¡?¿]", texto) +
    re.findall(r"\b[A-Za-zÀ-ÖØ-öø-ÿ']+\b", texto) +
    re.findall(r"\b[A-Za-zÀ-ÖØ-öø-ÿ]+'", texto) +
    re.findall(r"(?<=')[A-Za-zÀ-ÖØ-öø-ÿ']+", texto) +
    re.findall(r"(?:€\d+,\d+|\d+,\d+€)", texto) +
    re.findall(r"\d+,\d+(?=€)", texto) +
    re.findall(r"(?<=\b)\d+(?=,)", texto) +
    re.findall(r"(?<=,)\d+\b", texto) +
    re.findall(r"€", texto) +
    re.findall(r"#\d+", texto) +
    re.findall(r"(?<=#)\d+", texto) +
    re.findall(r"@\w+", texto) +
    re.findall(r"(?<=@)\w+", texto) +
    re.findall(r"★", texto) +
    re.findall(r"(?<![,])\b\d+\b(?![,])", texto) +
    re.findall(r"\b[Ll]ista:", texto) +
    re.findall(r"\?", texto)+
    re.findall(r'\b[$#@¿!(]\d+', texto) +                   # inician con caracter especial
    re.findall(r'\d+\b[?!,.):]', texto)                 # inician con caracter especial
)

# 🔹 Enteros (sin #, sin €, sin partes de decimales y sin números terminados en punto)
patron_enteros = r"(?<![#€])(?<!\d[.,])\b\d+\b(?![.,]\d)(?!\.)(?!\s*(?:parole|interi|decimali|liste))"
enteros = re.findall(patron_enteros, texto)

# 🔹 Decimales (coma o punto, incluyendo "88.")
patron_decimales = r"-?\b\d+(?:[.,]\d+|[.])"
decimales = re.findall(patron_decimales, texto)

# 🔹 Listas
patron_listas = r"\:\s*([^.:]+(?:,[^.:]+)*)\."
listas = re.findall(patron_listas, texto)

print("Palabras encontradas:", len(palabras))   # 👉 100
print("Enteros encontrados:", enteros, " | Cantidad:", len(enteros))
print("Decimales encontrados:", decimales, " | Cantidad:", len(decimales))
print("Listas encontradas:", listas, " | Cantidad:", len(listas))
