"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
from Tasks.a1_my_queue import Queue


class PriorityQueue:
    def __init__(self):
        self.queue_priority = []  # todo для очереди можно использовать python dict

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :param priority: element priority
        :return: Nothing
        """
        item = {
            "elem": elem,
            "priority":priority
        }

        if not self.queue_priority:
            self.queue_priority.append(item)
            return None

        for index, cur_item in enumerate(self.queue_priority):
            if cur_item["priority"] <= item["priority"]:
                self.queue_priority.insert(index, item)
                break
        else:
            self.queue_priority.append(item)


    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.queue_priority:
            return None

        return self.queue_priority.pop()["elem"]

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """

        return self.queue_priority[-ind -1]["elem"]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.queue_priority.clear()
        return None
