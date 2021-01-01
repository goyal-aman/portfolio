from timeline.models import Card
import datetime
import json
def backup_cards():
    card_list = Card.objects.all()
    time = str(datetime.datetime.today())
    b = {}
    for index,card in enumerate(card_list):
        print(card)
        b[index] = [card.heading, card.body, str(card.date)]
    
    with open(f'backup_label_now.json', 'w') as wf:
        json.dump(b, wf)

def restore():
    with open('cards.json', 'r') as rf:
        data = json.load(rf)
    for key, val in data.items():
        try:
            Card.objects.create(
                heading = val[0],
                body = val[1],
                date = datetime.datetime.strptime(val[2], "%Y-%m-%d").date()
            )
            print(val, 'done')
        except Exception as e:
            print("ERROR", val, e)
