from bubble_sort import *
from insertion_sort import *
from selection_sort import *
from merge_sort import *

import time

start_time = time.time()
teste_bubble
end_time = time.time()
tempo_bubble = end_time - start_time
print(f"Tempo bubble: {tempo_bubble:,.2f}\n")

start_time = time.time()
teste_insertion
end_time = time.time()
tempo_insertion = end_time - start_time
print(f"Tempo insertion: {tempo_insertion}\n")

start_time = time.time()
teste_selection
end_time = time.time()
tempo_selection = end_time - start_time
print(f"Tempo selection: {tempo_selection}\n")

start_time = time.time()
teste_merge()
end_time = time.time()
tempo_merge = end_time - start_time
print(f"Tempo merge: {tempo_merge}\n" )





