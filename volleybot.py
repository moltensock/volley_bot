import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def send_message(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})

last = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
people = []

token = "6b1368a70a865a9f6307bfce834116c16aedad1ba47315f1a19d3cd4c363d51eac4519c81e6a90cb1f9a1"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        ed = 59181636 #100212567
        lesha = 560170062
        received_message = event.text
        rm = received_message.lower()
        sender = event.user_id
        if rm == "набор старт":
            i = 0
            people = []
            send_message(ed, "Набор на тренировку начался")
            send_message(lesha, "Набор на тренировку начался")
        if rm == "список":
            itog1 = ""
            a1 = 0
            for i in range(len(people)):
                itog1 += '{}. '.format(a1 + 1) + people[a1] + "\n"
                a1 += 1
            if itog != "":
                send_message(lesha, itog1)
            else:
                send_message(lesha, "Список пуст")
        if rm[:6] == 'секция':
            false = 0
            for i in range(len(people)):
                if received_message[7:] == people[i] or sender == last[i]:
                    send_message(sender, "Ты уже есть в списках!")
                    false = 1
                    break
                else:
                    i += 1
            if i == 16:
                send_message(sender, "⚠ Упс...\n\n• Набор на ДАННУЮ тренировку закончен, мест больше нет!\n\n✅ Следите за информацией о новых тренировках в группе секции: vk.com/ssk_alliance_volley")
                false = 1
            if false != 1:
                if i == len(people):
                    people.append(received_message[7:])
                    last[i] = sender
                    send_message(sender, "Твой порядковый номер: {}".format(i + 1))
                    a = 0
                    itog = ""
                    for i in range(len(people)):
                        itog += '{}. '.format(i + 1) + people[a] + "\n"
                        a += 1
                    if i == 15: 
                        send_message(ed, itog)
                        send_message(lesha, itog)
