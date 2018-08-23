import MapReduce
import sys

"""
Problem 4
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: name
    # value: friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value, key)


def reducer(key, list_of_values):
    # key: name
    # value: list of friend counts
    #asymmetric friend name
    asy = []
    for friend in list_of_values:
        if friend in asy:
            asy.remove(friend)
            continue
        asy.append(friend)

    for friend in asy:
        mr.emit((key, friend))



# Do not modify below this line
# =============================
if __name__ == '__main__':
  #inputdata = open(sys.argv[1])
  inputdata = open("data/friends.json")
  mr.execute(inputdata, mapper, reducer)