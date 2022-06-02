from __future__ import annotations
from typing import Callable, List, Optional


class Node:  # create a class Node
    def __init__(self, callback: Optional[Callable] = None, name: Optional[str] = None):  # initialize the Node with a callback and a name
        self.children: List[Node] = []
        self.parent: Optional[Node] = None
        self.callback: Optional[Callable] = callback
        self.name: Optional[str] = name

    async def run(self, *args, **kwargs):
        if self.callback:  # check that the callback is defined
            await self.callback(*args, **kwargs)  # run the callback

    def add_child(self, child: Node):
        child.parent = self  # set the child's parent to the current node
        self.children.append(child)  # add a child to the Node (like a tree)

    async def __call__(self, *args, **kwargs):
        await self.run(*args, **kwargs)  # make possible to use a Node instance as a function (node = Node(); node())

    def __getattr__(self, item):
        return next((child for child in self.children if child.name == item), None)  # return the first child found by name

    def __getitem__(self, item):  # make possible to use a Node instance as a list or a dictionary (node = Node(); node[0]; node['name'])
        if isinstance(item, int):  # if the item is an integer
            return self.children[item]  # return the child at the index (like a list)
        elif isinstance(item, str):  # if the item is a string
            return self.__getattr__(item)  # return the child by name (like a dictionary) (see __getattr__)
        else:
            raise TypeError(f"{type(item)} is not supported")  # raise an error if the item is not an integer or a string
