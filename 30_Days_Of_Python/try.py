class Website:
    def __init__(self):
        self.links = {
            'youtube': 'https://www.youtube.com',
            'facebook': 'https://www.facebook.com'
        }
        self.shortcuts = {
            'yt': 'youtube',
            'fb': 'facebook'
        }

    def get_link(self, shortcut):
        name = self.shortcuts.get(shortcut)
        return self.links.get(name, "Das weiß ich leider nicht!")
    
    def add_link(self, shortcut, link_name):
        # Füge die neue Abkürzung zur shortcuts-Dictionary hinzu
        self.shortcuts[shortcut] = link_name
        # Füge den neuen Link zur links-Dictionary hinzu
        self.links[link_name] = f"https://www.{link_name}.com"

# Nutzung der Klasse
website = Website()
while True:
    mode = input("\ng = get\nl = list\na = add\nr = remove\ne = exit\nBitte Auswahl eingeben: ")
    if mode == "e":
        break
    if mode == 'g':
        print("\nOption 'get' ausgewählt.")
        eingabe = input("Shortcut>>> ")
        print(website.get_link(eingabe))
    elif mode == 'l':
        print("\nOption 'list' ausgewählt.")
        print("Shortcuts:")
        for shortcut, name in website.shortcuts.items():
            print(f"{shortcut} -> {name}: {website.links[name]}")
    elif mode == 'a':
        print("\nOption 'add' ausgewählt.")
        new_shortcut = input("Gib eine neue Abkürzung ein: ")
        new_link_name = input("Gib die neue Verknüpfung ein: ")
        website.add_link(new_shortcut, new_link_name)
        print(f"Neue Verknüpfung hinzugefügt: {new_shortcut} -> {new_link_name}")
    elif mode == 'r':
        
        print("\nOption 'remove' ausgewählt.")
    else:
        print("Ungültige Auswahl!")