def count_sheeps(arrayOfSheeps):
    """With True meaning sheep present, count the number of sheep in a list."""
    count = 0
    for i in arrayOfSheeps:
        if i == True:
            count += 1
    return count


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]

print count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1)