class Website:
    def __init__(self):
        self.links = {
            'youtube': 'https://www.youtube.com',
            'instagram': 'https://www.instagram.com',
            'facebook': 'https://www.facebook.com'
        }
        self.shortcuts = {
            'yt': 'youtube',
            'ig': 'instagram',
            'fb': 'facebook'
        }

    def get_link(self, shortcut):
        name = self.shortcuts.get(shortcut)
        return self.links.get(name, "Das weiß ich leider nicht!")

# Nutzung der Klasse
website = Website()
while True:
    eingabe = input("Your Input>>> ")
    if eingabe == "exit":
        break
    print(website.get_link(eingabe))