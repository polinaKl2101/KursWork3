import requests
from datetime import datetime


def get_data(url):
    """получаем данные по удаленной ссылке"""

    response = requests.get(url)

    """проверяем получение данных"""

    if response.status_code == 200:
        return response.json(), "INFO: we did it!"
    return None, f"WARNING: Ошибка - {response.status_code}"


def get_filtered_data(data, non_from=False):
    """фильтруем значение по ключу state, если он равен executed, оставляем их"""

    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']

    if non_from:
        """фильтруем полученные значения на остутствие отправителя, если его нет, убираем их"""
        data = [x for x in data if 'from' in x]

    return data


def get_sorted(data, last_values):
    """сортируем данные по дате и возвращаем 5 последних"""

    data = sorted(data, key=lambda x: x['date'], reverse=True)

    return data[:last_values]


def get_formatted(data):
    completed_data = []
    for line in data:
        """ переводим дату """
        time = datetime.strptime(line['date'], '%Y-%m-%dT%H:%M:%S.%f')
        new_time = time.strftime('%d/%m/%Y')

        description = line['description']
        if 'from' in line:
            """ проверяем на наличие отправителя """
            send_from = line['from'].split()
            sender_bill = send_from.pop(-1)
            sender_bill = f'{sender_bill[:4]} {sender_bill[4:6]}** ****{sender_bill[-4:]}'
            sender_info = ' '.join(send_from)
            """ если нет, выводим надпись СКРЫТО """
        else:
            sender_bill, sender_info = '', '[СКРЫТО]'
        """ выводим данные счета получателя """

        recipient_bill = line['to'].split().pop(-1)
        recipient_bill = f'**{recipient_bill[-4:]}'
        """ выводим сумму отправления """

        amount = f"{line['operationAmount']['amount']} {line['operationAmount']['currency']['name']}"

        """ пополняем список данными"""
        completed_data.append(f"{new_time} {description}\n{sender_info} {sender_bill} -> Счёт {recipient_bill}\n{amount}")
    """ выводим укомплектованный список с операциями"""

    return completed_data


