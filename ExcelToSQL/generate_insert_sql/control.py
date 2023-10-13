import sys
import function

# print(sys.argv)

if sys.argv[1] == "help":
    str = """
    control.py tl [excel_file]
        [excel_file]: excel file name does not contain file extension
        result:       View the table list in excel file
        Ex:           tl table_data_m
    control.py tl [excel_file] [*index]
        [excel_file]: excel file name does not contain file extension
        [*index]:     index of table
        result:       table insert command
        Ex:           table_data_m 0 1 2 3
    """
    print(str)

elif sys.argv[1] == "tl":
    print(function.get_table_name(sys.argv[2]))

else:
    for arg in sys.argv[2:]:
        function.generate_insert_sql(sys.argv[1], arg)
