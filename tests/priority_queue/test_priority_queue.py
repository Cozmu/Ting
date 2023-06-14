from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():

    instance_priory_queue = PriorityQueue()
    instance_priory_queue.enqueue({"qtd_linhas": 6})
    instance_priory_queue.enqueue({"qtd_linhas": 3})

    assert instance_priory_queue.__len__() == 2
    assert instance_priory_queue.dequeue() == {"qtd_linhas": 3}

    with pytest.raises(IndexError):
        instance_priory_queue.search(-1)

    instance_priory_queue.enqueue({"qtd_linhas": 1})

    assert instance_priory_queue.search(0) == {"qtd_linhas": 1}
