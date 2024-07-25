class Contacts():
    def __init__(self):
        self.contacts = {}
        self.contact_freq = {}

    def add_contact(self, name, telf):
        self.contacts[name] = telf
        self.contact_freq[name] = 0

    def show_contact(self, name):
        print(f"{name} - phone: {self.contacts[name]}")

    def call_contact(self, name, x):
        self.contact_freq[name] += x

    def get_contact_frequency(self):
        def get_key(lst):
            return lst[1]

        contact_names = sorted(self.contact_freq.items(), key=get_key, reverse=True)
        return [ contact[0] for contact in contact_names ]

if __name__ == "__main__":
    contacts = Contacts()
    contacts.add_contact("Xavi", 677377362)
    contacts.add_contact("Elisa", 888888888)
    contacts.add_contact("Anna", 234543432)
    contacts.show_contact("Anna")
    contacts.call_contact("Xavi", 1)
    contacts.call_contact("Elisa", 4)
    contacts.call_contact("Xavi", 2)
    d = contacts.get_contact_frequency()
    print(d)
