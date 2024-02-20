import chardet
from datetime import datetime
from pandas import read_csv, isna, DataFrame
from os import path, getcwd

def load_csv(filepath : str):
    print(f"Reading {filepath}")
    enc = 'utf-8'
    try:
        df = read_csv(filepath, encoding=enc, sep=';')
    except:
        print("Couldn't encode with utf-8. Trying another encoding: ", end='')
        with open(filepath, 'rb') as f:
            result = chardet.detect(f.read(100000))
        enc = result['encoding']
        print(enc)
        df = read_csv(filepath, encoding=enc, sep=';')
    return df, enc

def main():
    filepath = path.join(getcwd(), "../DADOS/MICRODADOS_ENEM_2022.csv")
    start = datetime.now()
    df, enc = load_csv(filepath)
    end = datetime.now()
    print(f"Took: {end-start} (H:M:S)\n")

    pb_filter = (
        ((df["SG_UF_ESC"] == "PB") & ((df["SG_UF_PROVA"] == "PB") | isna(df["SG_UF_PROVA"]))) |
        ((df["SG_UF_PROVA"] == "PB") & isna(df["SG_UF_ESC"]))
    )
    rj_filter = (
        ((df["SG_UF_ESC"] == "RJ") & ((df["SG_UF_PROVA"] == "RJ") | isna(df["SG_UF_PROVA"]))) | 
        ((df["SG_UF_PROVA"] == "RJ") & isna(df["SG_UF_ESC"]))
    )

    pb_df = df[pb_filter]
    rj_df = df[rj_filter]
    pb_rj_df = df[pb_filter | rj_filter]

    uf_df_dict = {
        "PB": pb_df,
        "RJ": rj_df,
        "PB_RJ": pb_rj_df
    }

    for uf, df in uf_df_dict.items():
        DataFrame.to_csv(df, path.join(getcwd(), f"{uf}_MICRODADOS_ENEM_2022.csv"), encoding=enc, sep=';')
        print(f"Saved {uf} with {len(df)} rows")

if __name__ == '__main__':
    main()
