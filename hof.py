from functools import reduce
def is_present(lst,x):
 return list(map(lambda a: 1 if a == x else 0, lst))

def count_occ(lst,target):
  return reduce(lambda a,b: a +1 if b == target else a, lst, 0)

def uniq(lst):
  return reduce(lambda a,h: a+[h] if count_occ(a,h) == 0 else a ,lst,[])

def find_max(matrix):
  reduce(lambda a,b: max(a,reduce(lambda c,d: max(c,d),b,a)),matrix,0)

def count_ones(matrix):
  raise Exception("Unimplemented")

def addgenerator(x):
  return lambda a: a + x

def apply_to_self():
 return lambda a,b: a + b(a)

def ap(fns,args):
  raise Exception("Unimplemented")

def map2(matrix,f):
  raise Exception("Unimplemented")


#reduce(lambda: a,h: a + h, [1,2,3],0)