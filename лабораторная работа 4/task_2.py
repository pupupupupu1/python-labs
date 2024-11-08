# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    pu = open(INPUT_FILENAME, "r")
    pi = open(OUTPUT_FILENAME, "w")

    reader = csv.DictReader(pu)
    po = []
    for i in reader:
        po.append(i)

    ...  # TODO Сериализовать в файл с отступами равными 4
    json.dump(po, pi, indent = 4)
    pi.close()
    pu.close()

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
