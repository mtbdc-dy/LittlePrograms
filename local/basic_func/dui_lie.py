from collections import deque

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = []
graph['anuj'] = []
graph['peggy'] = []

search_queue = deque()
search_queue += graph['you']

while search_queue:
    person = search_queue.popleft()
    print(person)
    search_queue += graph[person]



