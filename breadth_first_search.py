from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []



def is_mango_seller(person):
    return person.endswith("m")


def breadth_search():
    search_queue = deque()
    search_queue += graph["you"]
    
    while search_queue:
        print(search_queue)
        person = search_queue.popleft()
        if is_mango_seller(person):
            print("the mango seller is: ", person)
            return True
        else:
            search_queue += graph[person]
    return False
        
breadth_search()