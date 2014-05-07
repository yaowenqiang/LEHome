#!/usr/bin/env python
# encoding: utf-8
from util.log import *
from lib.model import Callback


class logical_callback(Callback.Callback):
    def callback(self, aValue, bValue):
        DEBUG("logical callback invoke.")
        return aValue and bValue
