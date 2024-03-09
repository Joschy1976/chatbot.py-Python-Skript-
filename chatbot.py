class Chatbot:
    def __init__(self):
        self.antworten = {
            "Hallo": "Hallo! Wie kann ich dir helfen?",
            "Wie geht es dir?": "Mir geht es gut, danke!",
            "Wer bist du?": "Ich bin ein einfacher Chatbot.",
            "Erzähle mir einen Witz": "Warum hat der Python-Programmierer keine Freunde? Weil er immer `null` setzt!",
            # Hier können weitere Fragen und Antworten hinzugefügt werden
        }

    def antworten_auf_frage(self, frage):
        frage = frage.capitalize()  # Standardisiere die Eingabe
        antwort = self.antworten.get(frage, "Entschuldigung, ich verstehe die Frage nicht.")
        return antwort

if __name__ == "__main__":
    chatbot = Chatbot()

    while True:
        benutzerfrage = input("Benutzer: ")
        if benutzerfrage.lower() == "exit":
            print("Chatbot wird beendet.")
            break

        antwort = chatbot.antworten_auf_frage(benutzerfrage)
        print(f"Chatbot: {antwort}")