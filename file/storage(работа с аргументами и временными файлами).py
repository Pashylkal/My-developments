import os
import tempfile
import argparse
import json

BeforeUp = dict()
StrUp = str()

# Получение аргументов, key и val название свойств аргументов
parser = argparse.ArgumentParser()
parser.add_argument('--key', type=str)
parser.add_argument('--val', type=str)
getArgs = parser.parse_args()
# Создание файла, в котором будут хранится ключи и их значения
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.isfile(storage_path) is True:
    with open(storage_path, 'r') as f:
        for line in f:
            StrUp += str(line)
        if StrUp != "":
            BeforeUp.update(json.loads(StrUp))

# Логика работы скрипта при нужном введении аргументов

if getArgs.val is None and getArgs.key in BeforeUp.keys():
    for values in BeforeUp[getArgs.key][:-1]:
        print(values, end=', ')
    print(BeforeUp[getArgs.key][-1])
    exit()
elif getArgs.val is None and getArgs.key not in BeforeUp.keys():
    print(None)
    exit()
elif getArgs.val is None and os.path.isfile(storage_path) is False:
    print(None)
    exit()
else:
    if getArgs.key in BeforeUp.keys():
        BeforeUp[getArgs.key].append(getArgs.val)
    else:
        BeforeUp[getArgs.key] = [getArgs.val]

with open(storage_path, 'w') as f:
    f.write(str(json.dumps(BeforeUp)))

