import numpy as np
import pandas as pd
import datetime as dt


def ReadCsv(PathCsv):
    df = pd.read_csv(f'{PathCsv}', sep=';').dropna()

    # Сортирую по дате
    df['time'] = df.Дата + ' ' + df.Время
    df['time'] = pd.to_datetime(df['time'], format='%d.%m.%Y %H:%M:%S')
    df.sort_values(['time'], inplace=True)
    df.drop(['Дата', 'Время'], axis='columns', inplace=True)

    df['col_median'] = df.groupby(['Пользов'])['time'].diff().dt.seconds
    df['col_median'] = np.where(df['col_median'] > 1200, np.nan, df['col_median'])
    df = df.groupby(by=['Операция'])['col_median'].median().apply(lambda x: str(dt.timedelta(seconds=x)))
    df.to_csv('answer.csv')


ReadCsv('test.csv')
