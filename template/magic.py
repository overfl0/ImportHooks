import sys

import github.overfl0.stack_overflow_import.stackoverflow as stackoverflow

# Workaround: if the module name starts with 'github.[...]' the github import
# hook will fire for each subpackage
# To prevent that, we rename the module to look like a top level module
stackoverflow.__name__ = 'stackoverflow'  # Was: 'github. [...] .stackoverflow'
sys.modules['stackoverflow'] = stackoverflow

from stackoverflow import quicksort
args = [1, 3, 2, 5, 4]

# print('Sorting array:', args)
# print('Result:', quicksort.quick_sort(None, args))
