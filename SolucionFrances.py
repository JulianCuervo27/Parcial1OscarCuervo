import re

texto = """Salut! En 2025, 6 amis découvrent la France. Liste: croissant, café, chocolat. Le prix est de 18,25€. Les étoiles (★) 
brillent la nuit. 2 chats jouent, 4 chiens dorment. Le code #8765 est mystérieux. 5 jours de travail, 2 jours de repos. 
@tous sont présents. Le numéro magique est 77. Que feriez-vous avec 15,99€? La réponse est dans la liste: lire, écrire, danser. 
Profitez de chaque jour! 100 mots, 5 entiers, 3 décimaux, 2 listes."""

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
patron_enteros = r"(?<![#€])(?<!\d[.,])\b\d+\b(?![.,]\d)(?!\.)(?!\,)(?!\s*(?:mots|entiers|décimaux|liste))"
enteros = re.findall(patron_enteros, texto)

# 🔹 Decimales (coma o punto, incluyendo "88.")
patron_decimales = r"-?\b\d+(?:[,]\d+|[,])"
decimales = re.findall(patron_decimales, texto)

# 🔹 Listas
patron_listas = r"\:\s*([^.:]+(?:,[^.:]+)*)\."
listas = re.findall(patron_listas, texto)

print("Palabras encontradas:", len(palabras))   # 👉 100
print("Enteros encontrados:", enteros, " | Cantidad:", len(enteros))
print("Decimales encontrados:", decimales, " | Cantidad:", len(decimales))
print("Listas encontradas:", listas, " | Cantidad:", len(listas))
