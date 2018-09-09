import sys

import github.overfl0.stack_overflow_import.stackoverflow as so
del sys.meta_path[0]
# sys.modules['stackoverflow'] = so

# from stackoverflow import quicksort

from github.overfl0.stack_overflow_import.stackoverflow import quicksort

args = [1, 3, 2, 5, 4]
#print(quicksort.quick_sort(None, args))
