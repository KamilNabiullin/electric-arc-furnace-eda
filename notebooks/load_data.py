import pandas as pd
import os

data_dir = 'data'

files = [
    'basket_charged.csv',
    'inj_mat.csv',
    'eaf_transformer.csv',
    'ladle_tapping.csv',
    'ferro.csv',
    'eaf_temp.csv',
    'lf_added_materials.csv',
    'eaf_gaslance_mat.csv',
    'eaf_final_chemical_measurements.csv',
    'lf_initial_chemical_measurements.csv',
    'eaf_added_materials.csv'
]

dataframes = {}

file_configs = {
    'basket_charged.csv': {
        'parse_dates': ['DATETIME'],
        'decimal_columns': ['CHARGED_AMOUNT'],
        'date_format': '%Y-%m-%d %H:%M:%S'
    },
    'inj_mat.csv': {
        'parse_dates': ['REVTIME'],
        'decimal_columns': ['INJ_AMOUNT_CARBON', 'INJ_FLOW_CARBON'],
        'date_format': '%Y-%m-%d %H:%M:%S,%f'
    },
    'eaf_transformer.csv': {
        'parse_dates': ['STARTTIME'],
        'decimal_columns': ['MW'],
        'date_format': '%Y-%m-%d %H:%M:%S'
    },
    'ladle_tapping.csv': {
        'parse_dates': ['DATETIME'],
        'decimal_columns': [],
        'date_format': '%Y-%m-%d %H:%M:%S'
    },
    'ferro.csv': {
        'parse_dates': [],
        'decimal_columns': [
            'Nb', 'Ta', 'Mo', 'V', 'Ca', 'Al', 'Mg', 'P', 'S', 'Ash', 'Moisture',
            'C', 'Si', 'Mn', 'Cr', 'Ti', 'Cu', 'Zn', 'Ni', 'Pb', 'Sn', 'Al2O3',
            'CaO+MgO', 'CaO', 'SiO2', 'MgO', 'FeO', 'Fe2O3', 'Cr2O3', 'TiO2', 'Na+K', 'TiO', 'As', 'SiC', 'Zr'
        ],
        'date_format': None
    },
    'eaf_temp.csv': {
        'parse_dates': ['DATETIME'],
        'decimal_columns': ['TEMP', 'VALO2_PPM'],
        'date_format': '%Y-%m-%d %H:%M:%S'
    },
    'lf_added_materials.csv': {
        'parse_dates': ['FILTER_KEY_DATE'],
        'decimal_columns': [],
        'date_format': '%Y-%m-%d %H:%M:%S'
    },
    'eaf_gaslance_mat.csv': {
        'parse_dates': ['REVTIME'],
        'decimal_columns': ['O2_AMOUNT', 'GAS_AMOUNT', 'O2_FLOW', 'GAS_FLOW'],
        'date_format': '%Y-%m-%d %H:%M:%S,%f'
    },
    'eaf_final_chemical_measurements.csv': {
        'parse_dates': ['DATETIME'],
        'decimal_columns': ['VALC', 'VALSI', 'VALMN', 'VALP', 'VALS', 'VALCU', 'VALCR', 'VALMO', 'VALNI', 'VALAS', 'VALSN', 'VALN'],
        'date_format': '%Y-%m-%d %H:%M:%S'
    },
    'lf_initial_chemical_measurements.csv': {
        'parse_dates': ['DATETIME'],
        'decimal_columns': ['VALC', 'VALSI', 'VALMN', 'VALP', 'VALS', 'VALCU', 'VALCR', 'VALMO', 'VALNI'],
        'date_format': '%Y-%m-%d %H:%M:%S'
    },
    'eaf_added_materials.csv': {
        'parse_dates': ['DATETIME'],
        'decimal_columns': [],
        'date_format': '%Y-%m-%d %H:%M:%S'
    }
}

def load_file(filename, parse_dates=None, decimal_columns=None, date_format=None):
    file_path = '../' + os.path.join(data_dir, filename)
    try:
        df = pd.read_csv(file_path, decimal=',', parse_dates=parse_dates or [], date_format=date_format)

        if decimal_columns:
            for col in decimal_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

        return df
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None


for file in files:
    config = file_configs.get(file, {'parse_dates': [], 'decimal_columns': [], 'date_format': None})
    df = load_file(file, config['parse_dates'], config['decimal_columns'], config['date_format'])
    if df is not None:
        df_name = file.split('.')[0]
        dataframes[df_name] = df

