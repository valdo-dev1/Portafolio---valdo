# Diccionario Español - Sueco de Valdo - Proyecto para beca Suecia
diccionario = {
    "hola": "hej",
    "gracias": "tack",
    "amigo": "vän",
    "sol": "sol",
    "agua": "vatten",
    "casa": "hus",
    "escuela": "skola",
    "libro": "bok",
    "amor": "kärlek",
    "familia": "familj",
    "comida": "mat",
    "tiempo": "tid",
    "día": "dag",
    "noche": "natt",
    "mesa": "bord",
    "perro": "hund",
    "gato": "katt",
    "sí": "ja",
    "no": "nej",
    "adiós": "hej då",
    "por favor": "snälla",
    "buenos días": "god morgon",
    "te quiero": "jag älskar dig",
    "invierno": "vinter",
    "verano": "sommar",
    "nieve": "snö",
    "luz": "ljus",
    "ciudad": "stad",
    "feliz": "glad",
    "trabajo": "arbete"
}

print("mi diccionario espanol - sueco")
palabra = input("escribe tack, vän, sol, hej: ")
print(f"{palabra} es {diccionario.get(palabra, 'no encontrada')}")
print(f"Listo! {len(diccionario)} palabras")
