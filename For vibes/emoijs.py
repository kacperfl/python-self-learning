# Emoji vertaler
# Vraag een zin aan de gebruiker en vervang woorden als “blij”, “boos”, “slapen” door 😄 😡 😴 etc.
# 👉 oefent .replace(), if, stringbewerking.


user_input = input("Hey hoe voel je je nu, wat is jou emotie? ").strip().lower()

match user_input:
    case "blij":
        aanpassing = user_input.replace("blij", "😄")
        print(aanpassing)
    case "boos":
        aanpassing = user_input.replace("boos", "😡")
        print(aanpassing)    
    case "slapen":
        aanpassing = user_input.replace("slapen", "😴")
        print(aanpassing)     
