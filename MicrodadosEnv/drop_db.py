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
    pb_df = None
    rj_df = None
    pb_rj_df = None

    uf_df_dict = {
        "PB": pb_df,
        "RJ": rj_df,
        "PB_RJ": pb_rj_df
    }

    cols_to_keep = [
        "NU_NOTA_CN",
        "NU_NOTA_CH",
        "NU_NOTA_LC",
        "NU_NOTA_MT",
        "NU_NOTA_COMP1",
        "NU_NOTA_COMP2",
        "NU_NOTA_COMP3",
        "NU_NOTA_COMP4",
        "NU_NOTA_COMP5",
        "NU_NOTA_REDACAO",
        "TP_PRESENCA_CN",
        "TP_PRESENCA_CH",
        "TP_PRESENCA_LC",
        "TP_PRESENCA_MT",
        "SG_UF_ESC",
        "SG_UF_PROVA",
    ]

    for uf, df in uf_df_dict.items():
        uf_df_dict[uf], enc = load_csv(path.join(getcwd(), f"{uf}_MICRODADOS_ENEM_2022.csv"))
        uf_df_dict[uf] = uf_df_dict[uf][cols_to_keep]
        DataFrame.to_csv(uf_df_dict[uf], path.join(getcwd(), f"{uf}_DROPPED_MICRODADOS_ENEM_2022.csv"), encoding=enc, sep=';')

if __name__ == '__main__':
    main()
