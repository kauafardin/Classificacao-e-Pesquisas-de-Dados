from bubble_sort import *
from insertion_sort import *
from selection_sort import *
from merge_sort import *
from quick_sort import *
from shell_sort import *

print("TEMPOS ABAIXO:\n")
import time
start_time = time.time()
teste_bubble()
end_time = time.time()
tempo_bubble = end_time - start_time
print(f"Tempo bubble: {tempo_bubble:,.6f} segundos!\n")

start_time = time.time()
teste_insertion()
end_time = time.time()
tempo_insertion = end_time - start_time
print(f"Tempo insertion: {tempo_insertion:,.6f} aegundos!\n")

start_time = time.time()
teste_selection()
end_time = time.time()
tempo_selection = end_time - start_time
print(f"Tempo selection: {tempo_selection:,.6f} segundos!\n")

start_time = time.time()
teste_merge()
end_time = time.time()
tempo_merge = end_time - start_time
print(f"Tempo merge: {tempo_merge:,.6f} segundos!\n")

start_time = time.time()
teste_quick()
end_time = time.time()
tempo_quick= end_time - start_time
print(f"Tempo quick: {tempo_quick:,.6f} segundos!\n")

start_time = time.time()
teste_shell()
end_time = time.time()
tempo_shell = end_time - start_time
print(f"Tempo shell: {tempo_shell:,.6f} segundos!\n")

