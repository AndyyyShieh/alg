import sys
import numpy as np

class Seq():
  def __init__(self, arr):
    self.arr = arr

  def is_arith(self):
    self.diffArr = np.diff(self.arr)
    return all(self.diffArr == self.diffArr[0])

  def get_diff_arr(self):
    return self.diffArr

  def get_diff_seq(self):
    tempArr = []
    for i in range(10):
      tempArr.append(self.arr[len(self.arr)-1] + self.diffArr[0]*(i+1))
    return tempArr

  def get_diff_diff_seq(self):
    return self.diffArr

  def is_fabo(self):
    return np.all(np.array(self.arr[:len(self.diffArr)-1]) == self.diffArr[1:])

  def get_fabo_seq(self):
    tempArr = []
    firstElem = self.arr[len(self.arr)-2]
    secondElem = self.arr[len(self.arr)-1]
    for i in range(10):
      tempElem = firstElem + secondElem
      tempArr.append(tempElem)
      firstElem = secondElem
      secondElem = tempElem
    return tempArr

  def is_geo(self):
    self.geoArr = []
    for i in range(len(self.arr)-1):
      self.geoArr.append(self.arr[i+1]/self.arr[i])
    return all(x==self.geoArr[0] for x in self.geoArr)

  def get_geo_seq(self):
    tempArr = []
    for i in range(10):
      tempArr.append(self.arr[len(self.arr)-1] * self.geoArr[0]*(i+1))
    return tempArr

  def get_repeat_seq(self):
    tempArr = []
    for i in range(10):
      tempArr.append(self.arr[i%len(self.arr)])
    return tempArr


if __name__ == '__main__':
  seq = Seq([int(i) for i in sys.argv[1:]])
  if seq.is_arith():
    print str(np.array(seq.get_diff_seq()))[1:-1]
  elif seq.is_fabo():
    print str(np.array(seq.get_fabo_seq()))[1:-1]
  elif seq.is_geo():
    print str(np.array(seq.get_geo_seq()))[1:-1]
  else:
    print str(np.array(seq.get_repeat_seq()))[1:-1]
    