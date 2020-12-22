# %%
import pandas as pd
import numpy as np
import datetime
import copy
from tqdm import tqdm

# %%
kpp = pd.read_excel('kpp.xlsx', header=4, sheet_name='Лист1')

% % time
# первичные преобразования
kpp = kpp[['Таб. №', 'Дата и время', 'Зона доступа']]
kpp['Дата и время'] = pd.to_datetime(kpp['Дата и время'])
kpp['Таб. №'] = kpp['Таб. №'].astype(str).apply(lambda x: '0' * (8 - len(x)) + x)
kpp = kpp[(kpp['Таб. №'].str.startswith('0107')) |
          (kpp['Таб. №'].str.startswith('0109'))]

# %%

% % time
skype = pd.read_csv('skype.csv', delimiter=';')

# %%

% % time
# первичные преобразования
skype = skype[(skype['User1'].str.contains('@severstal-ssc')) |
              (skype['User2'].str.contains('@severstal-ssc'))]
skype['InviteTime'] = pd.to_datetime(skype['InviteTime'])
skype['EndTime'] = pd.to_datetime(skype['EndTime'])
skype = pd.concat([skype[['User1', 'InviteTime', 'EndTime']].rename(columns={'User1': 'User'}),
                   skype[['User2', 'InviteTime', 'EndTime']].rename(columns={'User2': 'User'})], sort=False)
skype['User'] = skype['User'].str.lower()

# %%

# совмещаем фреймы
kpp = kpp.rename(columns={'Таб. №': 'empl', 'Дата и время': 'timestamp', 'Зона доступа': 'zone'})
kpp['source'] = 'kpp'
skype = skype.rename(columns={'InviteTime': 'timestamp'})
skype['source'] = 'skype'

df = pd.concat([kpp, skype], sort=False)

# %%

# задаем инетерсующий период
sdate = datetime.date(2020, 1, 1)
edate = datetime.date(2020, 3, 31)
delta = edate - sdate

# строим матрицу даты и времени
matrix = dict()
for d in range(delta.days + 1):
    for h in range(0, 24 * 2):
        date = datetime.datetime.combine(sdate + datetime.timedelta(days=d),
                                         datetime.time(h // 2, h % 2 * 30))
        matrix[date] = {'kpp': bool(), 'skype': bool()}

# %%

# создаем матрицу для каждого человека, который есть в проходках или в skype
main = dict()
for empl, data in tqdm(df.groupby('empl')):
    # берем массив для ускорения вычислений
    k = data[data['source'] == 'kpp'].to_numpy()
    s = data[data['source'] == 'skype'].to_numpy()
    main[empl] = copy.deepcopy(matrix)
    # сверяем каждые полчаса
    for date in main[empl]:

        # получаем последний проход человека в последние 9 часов
        prev = k[np.where(((k[:, 1] >= date - datetime.timedelta(hours=9)) &
                           (k[:, 1] <= date + datetime.timedelta(minutes=30))))]
        # если это был вход, то ставим True
        if len(prev) != 0 and prev[-1][2] == 1: main[empl][date]['kpp'] = True

        # получаем последние сессии skype общения
        prev = s[np.where(((s[:, 1] <= date + datetime.timedelta(minutes=30)) &
                           (s[:, 5] >= date)))]
        # если человек пообщался недавно, то ставим True
        if len(prev) > 0: main[empl][date]['skype'] = True

# %%

# преобразуем в табличку
res = list()

for empl in main:
    for date in main[empl]:
        for source in main[empl][date]:
            res.append({'empl': empl, 'date': date, 'source': source, 'value': main[empl][date][source]})

res = pd.DataFrame(res)

# %%

# экспортируем в excel
res.to_csv('result.csv', index=False)



