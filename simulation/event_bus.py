"""
Event bus to track queue of events
"""

from collections import defaultdict


class EventBus:
    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_type, callback):
        self.listeners[event_type].append(callback)

    def publish(self, event):
        for callback in self.listeners[type(event)]:
            callback(event)
