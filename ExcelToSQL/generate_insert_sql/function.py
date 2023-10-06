import pandas as pd
import numpy as np


def get_table_name():
    pass



def generate_insert_sql(target_physical=""):

    if target_physical:
        # Read Excel form
        file_path = 'table_data.xlsx'
        sheet_name = 'table_name'

        table_name_df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)
        # print(table_name_df)
        # target_physical = "分荷データ"
        # Use the .loc method to find the corresponding "logical" value
        logical_value = table_name_df.loc[table_name_df['physical'] == target_physical, 'logical'].values
        # print(logical_value)

        data_df = pd.read_excel(file_path, sheet_name=target_physical, header=0)
        # print(data_df)

        # Get column name and data type
        column_names = data_df.iloc[0].tolist()
        data_types = data_df.iloc[1].tolist()
        # print(column_names)
        # print(data_types)
        data_df.columns = column_names
        data_df = data_df[2:]
        data_df.index = np.arange(len(data_df))
        # print(data_df)
        # Generate SQL insert syntax
        if "AUTO_INCREMENT" in data_types:
            insert_sql = f"INSERT INTO public.{logical_value[0]} ({', '.join(column_names[1:])}) VALUES "
        else:
            insert_sql = f"INSERT INTO public.{logical_value[0]} ({', '.join(column_names)}) VALUES "
        print(insert_sql)
        for index, row in data_df.iterrows():
            values_placeholder = "("
            if "AUTO_INCREMENT" in data_types:
                row_list = row.tolist()[1:]
                row_data_types = data_types[1:]
            else:
                row_list = row.tolist()
                row_data_types = data_types[:]
            for i in range(len(row_list)):
                if row_data_types[i] == "integer":
                    values_placeholder += f"{row_list[i]}"
                else:
                    values_placeholder += f'"{row_list[i]}"'
                if i != len(row_list)-1:
                    values_placeholder += ", "
                else:
                    values_placeholder += ")"
            # print(values_placeholder)
            # insert_sql += values_placeholder
            if index == len(data_df) - 1:
                values_placeholder += ";"
            else:
                values_placeholder += ","
            print(values_placeholder)
    else:
        print("target_physical is null.")
