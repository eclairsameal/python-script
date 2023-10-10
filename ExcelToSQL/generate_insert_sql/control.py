import sys
import function

# print(sys.argv)

for arg in sys.argv[1:]:
    function.generate_insert_sql(arg)
