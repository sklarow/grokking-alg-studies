from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = []
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]


def person_is_seller(person):
    return person.endswith("m")

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph.get(person, [])
                searched.add(person)
    return False

search("you")
