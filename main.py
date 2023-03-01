from utils import get_data, get_filtered_data, get_sorted, get_formatted


def main():
    OPERATIONS_URL = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677734654529&signature=IQ6QxNk5AUeHWNA7bwCDXtM7oe-EeXz8UsaF3vzl3kU&downloadName=operations.json"
    LAST_VALUES = 5
    NON_FROM = True

    data, info = get_data(OPERATIONS_URL)
    if not data:
        exit(info)
    #print(info)

    data = get_filtered_data(data, NON_FROM)
    data = get_sorted(data, LAST_VALUES)
    data = get_formatted(data)
    for line in data:
        print(line, end="\n\n")


if __name__ == "__main__":
    main()