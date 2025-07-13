import pandas as pd

def add_date_parts(df):
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['WeekOfYear'] = df['Date'].dt.isocalendar().week
    df['IsWeekend'] = df['DayOfWeek'].isin([5, 6]).astype(int)
    return df

def add_lag_features(df, lags=[7, 14, 28]):
    for lag in lags:
        df[f'Sales_Lag_{lag}'] = df.groupby('Store')['Sales'].shift(lag)
    return df

def add_rolling_features(df, windows=[7, 14]):
    for window in windows:
        df[f'Sales_RollMean_{window}'] = df.groupby('Store')['Sales'].shift(1).rolling(window).mean().reset_index(0, drop=True)
    return df

def main():
    df = pd.read_csv('data/processed/clean.csv', parse_dates=['Date'])
    df = add_date_parts(df)
    df = add_lag_features(df)
    df = add_rolling_features(df)
    df.dropna(inplace=True)
    df.to_csv('data/processed/features.csv', index=False)
    print(f'Saved features to data/processed/features.csv (n={len(df)})')

if __name__ == '__main__':
    main()
