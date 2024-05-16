#!/usr/bin/env python3
"""
Changs the topic of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Changs the topic of a school document based on the name
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
    )
