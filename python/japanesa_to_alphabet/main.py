import pandas as pd
from pykakasi import kakasi

kks = kakasi()


def main():
    df = pd.read_excel('ローマ字変換.xlsx', sheet_name='変換', index_col=None)

    df['平仮名'] = df['変換対象'].apply(lambda ja: kks.convert(ja)[0].get('hira'))
    df['カタカナ'] = df['変換対象'].apply(lambda ja: kks.convert(ja)[0].get('kana'))
    df['ヘボン'] = df['変換対象'].apply(lambda ja: kks.convert(ja)[0].get('hepburn').capitalize())
    df['訓令'] = df['変換対象'].apply(lambda ja: kks.convert(ja)[0].get('kunrei').capitalize())
    df['パスポート'] = df['変換対象'].apply(lambda ja: kks.convert(ja)[0].get('passport').capitalize())

    df.to_excel('ローマ字変換.xlsx', sheet_name='変換', index=False)


if __name__ == '__main__':
    main()
