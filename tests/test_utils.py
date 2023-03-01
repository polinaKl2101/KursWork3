import pytest
from utils import get_data, get_sorted, get_formatted, get_filtered_data


def test_get_data():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677734654529&signature=IQ6QxNk5AUeHWNA7bwCDXtM7oe-EeXz8UsaF3vzl3kU&downloadName=operations.json"
    data = get_data(url)
    assert get_data(url) is not None
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677734654529&signature=IQ6QxNk5AUeHWNA7bwCDXtM7oe-EeXz8UsaF3vzl3kU&downloadNam=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "WARNING: Ошибка - 400"


def test_get_sorted(test_data):
    data = get_sorted(test_data, last_values=5)
    assert data[0]['date'] == "2022-03-23T10:45:06.972075"
    assert len(data) == 5


def test_get_formatted(test_data):
    data = get_formatted(test_data[:1])
    assert data == ['26/08/2019 Перевод организации\nMaestro 1596 83** ****5199 -> Счёт **9589\n31957.58 руб.']
    data = get_formatted(test_data[3:4])
    assert data == ['23/03/2022 Открытие вклада\n[СКРЫТО]  -> Счёт **2431\n48223.05 руб.']


def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert len(data) == 5
    data = get_filtered_data(test_data, non_from=True)
    assert len(data) == 4

