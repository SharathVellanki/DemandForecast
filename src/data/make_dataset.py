import pandas as pd

def main():
    train = pd.read_csv('data/raw/train.csv', parse_dates=['Date'], low_memory=False)
    store = pd.read_csv('data/raw/store.csv')
    df = train.merge(store, on='Store', how='left')

    df['CompetitionDistance'] = df['CompetitionDistance'].fillna(df['CompetitionDistance'].median())
    df['CompetitionOpenSinceMonth'] = df['CompetitionOpenSinceMonth'].fillna(1)
    df['CompetitionOpenSinceYear'] = df['CompetitionOpenSinceYear'].fillna(df['Date'].dt.year.min())
    df['Promo2SinceWeek'] = df['Promo2SinceWeek'].fillna(0)
    df['Promo2SinceYear'] = df['Promo2SinceYear'].fillna(0)
    df['PromoInterval'] = df['PromoInterval'].fillna('')

    df = df[(df.Open == 1) & (df.Sales > 0)].copy()
    df.sort_values(['Store', 'Date'], inplace=True)

    df.to_csv('data/processed/clean.csv', index=False)
    print(f'Wrote cleaned data ({len(df)} rows) to data/processed/clean.csv')

if __name__ == '__main__':
    main()
