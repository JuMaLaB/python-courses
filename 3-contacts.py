
contacts = {
    'count': 3,
    'bastards': {
        'number one': {'name': 'Donald Trump', 'email': 'donald.trump@bastard.usa' },
        'number two': {'name': 'Vladimir Poutine', 'email': 'validimir.poutine@bastard.ru' },
        'number zero': {'name': 'Manu Macron', 'email': 'manu.macron@bastard.fr' }
    }
}

for key, values in contacts['bastards'].items():
    print(key, ': ', values)

print("Bastards emails:")
for key, values in contacts['bastards'].items():
    print(values['email'])