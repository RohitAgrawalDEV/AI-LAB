def bfs(src, target):
queue = []
queue.append(src)

exp = []

while len(queue) > 0:
source = queue.pop(0)
exp.append(source)

   print(source)

   if source == target:
       print("success")
       return

   poss_moves_to_do = []
   poss_moves_to_do = possible_moves(source, exp)

   for move in poss_moves_to_do:

       if move not in exp and move not in queue:
           queue.append(move)
def possible_moves(state, visited_states):

Find index of empty spot and assign it to b
b = state.index(-1)

'd' for down, 'u' for up, 'r' for right, 'l' for left - directions array
d = []

Add all possible direction into directions array - Hint using if statements
if b not in [0, 1, 2]:
d.append('u')
if b not in [6, 7, 8]:
d.append('d')
if b not in [0, 3, 6]:
d.append('l')
if b not in [2, 5, 8]:
d.append('r')
