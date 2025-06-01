import math

print("Erweiterter Taschenrechner mit sqrt, sin, cos, tan")
print()
print("Funktionen:")
print()
print("Addition: +")
print("Subrtakion: -")
print("Multiplikation: *")
print("Division: /")
print("Potenzen: **")
print("Wurzel: sqrt()")
print("Tangens: tan()")
print("Sinus: sin()")
print("Cosinus: cos()")
print("Lorgarithmen: log(), log10()")
print("mathematisches pi: pi")
print("mathimatisches e: e")
print()
print("Gib 'exit' ein zum Beenden.")

# Erlaubte Funktionen und Konstanten:
erlaubt = {
    "sqrt": math.sqrt,
    "sin": lambda x: math.sin(math.radians(x)),  # Grad in Radiant umrechnen
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "pi": math.pi,
    "e": math.e,
    "log": math.log,
    "log10": math.log10,
    "__builtins__": {}  # verbietet gefährliche Funktionen
}

while True:
    ausdruck = input(">>> ")
    if ausdruck.lower() == "exit":
        break
    try:
        ergebnis = eval(ausdruck, erlaubt)
        print("Ergebnis:", ergebnis)
    except Exception as e:
        print("Fehler:", e)
