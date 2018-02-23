import json


class ContactList(object):
    storagefile = 'storage.json'
    data = {}

    def __init__(self):
        self.loadData()

    def loadData(self):
        storageFile = open(self.storagefile, 'r')
        storageFileData = storageFile.read()
        self.data = json.loads(storageFileData)
        storageFile.close()

    def listContacts(self):
        for i in range(0, len(self.data['contacts'])):
            print(
                '{} - Name: {} - Phone Number: {}'.format(
                    i + 1,
                    self.data['contacts'][i]['name'],
                    self.data['contacts'][i]['phone']
                )
            )

    def persist(self):
        with open(self.storagefile, 'w') as outfile:
            json.dump(self.data, outfile)

    def add(self, name, phone):
        contact = {
            "name": name,
            "phone": phone
        }
        self.data['contacts'].append(contact)
        self.persist()

    def update(self, index, contact):
        try:
            self.data['contacts'][index] = contact
            self.persist()
            return True
        except IndexError:
            return False

    def remove(self, index):
        print(index)
        del self.data['contacts'][index]
        self.persist()
