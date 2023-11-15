"""This is my implementation of simple breadth-first search
"""


def mango_seller(name):
    return "m" in name


def search(graph):
    """ Find the closes friends that sell mango. mango seller is defined
    with a person with the 'm' char in their name
    """

    queue = []
    queue += graph["you"]
    visited = set()
    visited.update(graph["you"])
    while queue:
        print("current queue: ", queue)
        current_friend = queue[0]
        del queue[0]

        if mango_seller(current_friend):
            return current_friend
        else:
            for friend in graph[current_friend]:
                if friend not in visited:
                    queue.append(friend)
                    visited.add(friend)
    return -1


if __name__ == '__main__':

    graph = {
        "you": ["bob", "claire", "alice",],
        "bob": ["anuj", "peggy"],
        "claire": ["thom", "jonny"],
        "alice": ["peggy"],
        "peggy": [],
        "thom": [],
        "jonny": [],
        "anuj": [], }
    print(search(graph))