import threading
import thread

import interleave.mocks
import interleave.core
import interleave.monkeypatch
from .stdlib_suite import py2_lock_tests as lock_tests

#interleave.monkeypatch.PatchEverywhere.DEBUG = True
ctx = interleave.mocks.mock_thread(
    interleave.core.SimpleGeneratorScheduler()
).__enter__()
print(threading.Lock)
print(thread.allocate_lock)
print(thread.start_new_thread)

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
