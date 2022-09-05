#!/usr/bin/python3
from models.base_model import BaseModel
"""
    Module that contains state class
    inherits from base.
"""


class State(BaseModel):
    """
        Class define information about States
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
