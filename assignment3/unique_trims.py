import MapReduce
import sys

"""
Problem 5
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: trimmed nucleotides
    key = record[1]
    key = key[:-10]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: trimmed nucleotides
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  #inputdata = open("data/dna.json")
  mr.execute(inputdata, mapper, reducer)
