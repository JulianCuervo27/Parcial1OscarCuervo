import re

texto = """En el año 2025, 8 personas viajan por el mundo. ¡Hola! ¿Qué tal? El cielo azul, las estrellas (★) brillan. 
4 niños juegan, 3.14 horas de alegría. Lista: libro, lápiz, cuaderno. El costo es $20.50. ¿Sabías que el código #5678 es famoso? 
La vida es aventura, @todos disfrutan. El tiempo corre, 5 días laborales. ¡Éxito! El número especial es 99. 
¿Qué harías con 12.75 dólares? La respuesta está en la lista: viajar, aprender, reír. ¡Vive intensamente! 
100 palabras, 6 enteros, 3 decimales, 2 listas."""

# 🔹 Palabras y símbolos especiales
palabras = palabras = (
    re.findall(r'\b[A-Za-zÁÉÍÓÚáéíóúÑñüÜ]+\b', texto) +   # Palabras normales
    re.findall(r'\b[$#@¿!(]\d+', texto) +                   # inician con caracter especial
    re.findall(r'\d+\b[?!,.):]', texto) +                   # inician con caracter especial
    re.findall(r'\d+\.\d+', texto) +                     # Decimales completos
    re.findall(r'(?<=\b)\d+(?=\.\d+)', texto) +          # Parte entera decimal
    re.findall(r'(?<=\.)\d+\b', texto) +                 # Parte decimal
    re.findall(r'(?<=#)\d+', texto) +                    # Número de hashtag
    re.findall(r'★', texto) +                            # Estrella
    re.findall(r'(?<![#@.])\b\d+\b(?!\.\d)', texto)      # Enteros aislados
)

# 🔹 Enteros (incluye #5678, pero excluye 100, 6, 3, 2 del final)
patron_enteros = r"(?:#)?(?<!\$)(?<!\d\.)\b\d+\b(?!\.\d)(?!\s*(?:palabras|enteros|decimales|listas))"
enteros = re.findall(patron_enteros, texto)

# 🔹 Decimales (excluye los del final)
patron_decimales = r"\b\d+\.\d+\b(?!\s*(?:palabras|enteros|decimales|listas))"
decimales = re.findall(patron_decimales, texto)

# 🔹 Listas
patron_listas = r"\:\s*([^.:]+(?:,[^.:]+)*)\."
listas = re.findall(patron_listas, texto)

print("Palabras encontradas:", len(palabras))   # 👉 100
print("Enteros encontrados:", enteros, " | Cantidad:", len(enteros))   # 👉 6
print("Decimales encontrados:", decimales, " | Cantidad:", len(decimales))   # 👉 3
print("Listas encontradas:", listas, " | Cantidad:", len(listas))   # 👉 2)
