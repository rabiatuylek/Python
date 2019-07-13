a = [1,2,3,]
b = ["a","b","c"]
for c in zip(a,b):
    print(c)

  #  (1, 'a')
  #  (2, 'b')
  #  (3, 'c')

word = "abcde"
for item in enumerate(word):
    print(item)
   # (0, 'a')
   # (1, 'b')
   # (2, 'c')
   # (3, 'd')
   # (4, 'e')


#elimizdeki string degerini karakterlerine ayırarak teslim eder.