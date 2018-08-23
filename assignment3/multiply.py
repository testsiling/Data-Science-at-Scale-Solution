import MapReduce
import sys

"""
Problem 6
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
def mapper(record):
    # key: (i, j)
    # value: [matrix name, value]
    if record[0] == "a":
        for i in range(5):
            key = (record[1], i)
            value = record
            mr.emit_intermediate(key, value)
    elif record[0] == "b":
        for i in range(5):
            key = (i, record[2])
            value = record
            mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: new matrix position
    # value: original matrix information
    value = [0, 0, 0, 0, 0]
    for i in range(5):
        a = b = 0
        for item in list_of_values:
            if (item[0] == "a") and (item[2] == i):
                a = item[3]
            if (item[0] == "b") and (item[1] == i):
                b = item[3]
        value[i] = a*b

    mr.emit((key[0], key[1], sum(value)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    #inputdata = open("data/matrix.json")
    mr.execute(inputdata, mapper, reducer)
