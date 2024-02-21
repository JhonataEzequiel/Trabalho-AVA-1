import json
import chardet
import statistics
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
    info_dict = {
        "PB": {},
        "RJ": {},
    }

    for uf, stats in info_dict.items():
        df, enc = load_csv(path.join(getcwd(), f"{uf}_DROPPED_MICRODADOS_ENEM_2022.csv"))

        present_first_day_filter = ((df["TP_PRESENCA_CH"] == 1) & (df["TP_PRESENCA_LC"] == 1))
        present_second_day_filter = ((df["TP_PRESENCA_CN"] == 1) & (df["TP_PRESENCA_MT"] == 1))

        df_present_fd = df[present_first_day_filter]
        num_presentes_pd = len(df_present_fd)
        num_ausentes_pd = len(df[~present_first_day_filter])

        df_present_sd = df[present_second_day_filter]
        num_presentes_sd = len(df_present_sd)
        num_ausentes_sd = len(df[~present_second_day_filter])

        notas_ch = df_present_fd["NU_NOTA_CH"].to_list()
        notas_lc = df_present_fd["NU_NOTA_LC"].to_list()
        notas_red = df_present_fd["NU_NOTA_REDACAO"].to_list()
        notas_cn = df_present_sd["NU_NOTA_CN"].to_list()
        notas_mt = df_present_sd["NU_NOTA_MT"].to_list()
        notas_red_comp1 = df_present_fd["NU_NOTA_COMP1"].to_list()
        notas_red_comp2 = df_present_fd["NU_NOTA_COMP2"].to_list()
        notas_red_comp3 = df_present_fd["NU_NOTA_COMP3"].to_list()
        notas_red_comp4 = df_present_fd["NU_NOTA_COMP4"].to_list()
        notas_red_comp5 = df_present_fd["NU_NOTA_COMP5"].to_list()

        num_notas_ch_0_199 = len([n for n in notas_ch if 0.0 <= n <= 199.9])
        num_notas_ch_200_399 = len([n for n in notas_ch if 200.0 <= n <= 399.9])
        num_notas_ch_400_599 = len([n for n in notas_ch if 400.0 <= n <= 599.9])
        num_notas_ch_600_799 = len([n for n in notas_ch if 600.0 <= n <= 799.9])
        num_notas_ch_800_1000 = len([n for n in notas_ch if 800.0 <= n <= 1000.0])
        num_notas_lc_0_199 = len([n for n in notas_lc if 0.0 <= n <= 199.9])
        num_notas_lc_200_399 = len([n for n in notas_lc if 200.0 <= n <= 399.9])
        num_notas_lc_400_599 = len([n for n in notas_lc if 400.0 <= n <= 599.9])
        num_notas_lc_600_799 = len([n for n in notas_lc if 600.0 <= n <= 799.9])
        num_notas_lc_800_1000 = len([n for n in notas_lc if 800.0 <= n <= 1000.0])
        num_notas_red_0_199 = len([n for n in notas_red if 0.0 <= n <= 199.9])
        num_notas_red_200_399 = len([n for n in notas_red if 200.0 <= n <= 399.9])
        num_notas_red_400_599 = len([n for n in notas_red if 400.0 <= n <= 599.9])
        num_notas_red_600_799 = len([n for n in notas_red if 600.0 <= n <= 799.9])
        num_notas_red_800_1000 = len([n for n in notas_red if 800.0 <= n <= 1000.0])
        num_notas_cn_0_199 = len([n for n in notas_cn if 0.0 <= n <= 199.9])
        num_notas_cn_200_399 = len([n for n in notas_cn if 200.0 <= n <= 399.9])
        num_notas_cn_400_599 = len([n for n in notas_cn if 400.0 <= n <= 599.9])
        num_notas_cn_600_799 = len([n for n in notas_cn if 600.0 <= n <= 799.9])
        num_notas_cn_800_1000 = len([n for n in notas_cn if 800.0 <= n <= 1000.0])
        num_notas_mt_0_199 = len([n for n in notas_mt if 0.0 <= n <= 199.9])
        num_notas_mt_200_399 = len([n for n in notas_mt if 200.0 <= n <= 399.9])
        num_notas_mt_400_599 = len([n for n in notas_mt if 400.0 <= n <= 599.9])
        num_notas_mt_600_799 = len([n for n in notas_mt if 600.0 <= n <= 799.9])
        num_notas_mt_800_1000 = len([n for n in notas_mt if 800.0 <= n <= 1000.0])

        media_notas_ch = statistics.mean(notas_ch)
        media_notas_lc = statistics.mean(notas_lc)
        media_notas_red = statistics.mean(notas_red)
        media_notas_cn = statistics.mean(notas_cn)
        media_notas_mt = statistics.mean(notas_mt)
        media_notas_red_comp1 = statistics.mean(notas_red_comp1)
        media_notas_red_comp2 = statistics.mean(notas_red_comp2)
        media_notas_red_comp3 = statistics.mean(notas_red_comp3)
        media_notas_red_comp4 = statistics.mean(notas_red_comp4)
        media_notas_red_comp5 = statistics.mean(notas_red_comp5)

        num_notas_mil_red = notas_red.count(1000.0)

        info_dict[uf] = {
            "stats": {
                "media_notas_ch": media_notas_ch,
                "media_notas_lc": media_notas_lc,
                "media_notas_red": media_notas_red,
                "media_notas_cn": media_notas_cn,
                "media_notas_mt": media_notas_mt,
                "media_notas_red_comp1": media_notas_red_comp1,
                "media_notas_red_comp2": media_notas_red_comp2,
                "media_notas_red_comp3": media_notas_red_comp3,
                "media_notas_red_comp4": media_notas_red_comp4,
                "media_notas_red_comp5": media_notas_red_comp5
            },
            "notas": {
                "num_notas_ch_0_199": num_notas_ch_0_199,
                "num_notas_ch_200_399": num_notas_ch_200_399,
                "num_notas_ch_400_599": num_notas_ch_400_599,
                "num_notas_ch_600_799": num_notas_ch_600_799,
                "num_notas_ch_800_1000": num_notas_ch_800_1000,
                "num_notas_lc_0_199": num_notas_lc_0_199,
                "num_notas_lc_200_399": num_notas_lc_200_399,
                "num_notas_lc_400_599": num_notas_lc_400_599,
                "num_notas_lc_600_799": num_notas_lc_600_799,
                "num_notas_lc_800_1000": num_notas_lc_800_1000,
                "num_notas_red_0_199": num_notas_red_0_199,
                "num_notas_red_200_399": num_notas_red_200_399,
                "num_notas_red_400_599": num_notas_red_400_599,
                "num_notas_red_600_799": num_notas_red_600_799,
                "num_notas_red_800_1000": num_notas_red_800_1000,
                "num_notas_cn_0_199": num_notas_cn_0_199,
                "num_notas_cn_200_399": num_notas_cn_200_399,
                "num_notas_cn_400_599": num_notas_cn_400_599,
                "num_notas_cn_600_799": num_notas_cn_600_799,
                "num_notas_cn_800_1000": num_notas_cn_800_1000,
                "num_notas_mt_0_199": num_notas_mt_0_199,
                "num_notas_mt_200_399": num_notas_mt_200_399,
                "num_notas_mt_400_599": num_notas_mt_400_599,
                "num_notas_mt_600_799": num_notas_mt_600_799,
                "num_notas_mt_800_1000": num_notas_mt_800_1000,
                "num_notas_mil_red": num_notas_mil_red
            },
            "num_presentes_pd": num_presentes_pd,
            "num_presentes_sd": num_presentes_sd,
            "num_ausentes_pd": num_ausentes_pd,
            "num_ausentes_sd": num_ausentes_sd,
        }

    print(info_dict)
    print('Salvando em "info.json"')
    with open("info.json", 'w') as json_file:
        json.dump(info_dict, json_file, indent=4)

if __name__ == '__main__':
    main()
