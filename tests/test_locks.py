import threading

import interleave.mock_thread
import interleave.core
from .stdlib_suite import py2_lock_tests as lock_tests


def gen():
    while True:
        for i in xrange(10):
            yield i
for patcher in interleave.mock_thread.get_patchers():
    patcher.__enter__()
sched = interleave.core.GeneratorScheduler(gen())


class LockTests(lock_tests.LockTests):
    locktype = staticmethod(threading.Lock)

class RLockTests(lock_tests.RLockTests):
    locktype = staticmethod(threading.RLock)

class EventTests(lock_tests.EventTests):
    eventtype = staticmethod(threading.Event)

class ConditionAsRLockTests(lock_tests.RLockTests):
    # An Condition uses an RLock by default and exports its API.
    locktype = staticmethod(threading.Condition)

class ConditionTests(lock_tests.ConditionTests):
    condtype = staticmethod(threading.Condition)

class SemaphoreTests(lock_tests.SemaphoreTests):
    semtype = staticmethod(threading.Semaphore)