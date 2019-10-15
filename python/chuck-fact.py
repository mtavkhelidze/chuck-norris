#!/usr/bin/env python3

import ctypes

handle = ctypes.cdll.LoadLibrary("../.build/lib/libchuck-norris.dylib")
handle.chuck_fact_init.restype = ctypes.c_void_p
handle.chuck_fact_get.argtypes = [ctypes.c_void_p]
handle.chuck_fact_get.restype = ctypes.c_char_p

cf = handle.chuck_fact_init()
fact_bytes = handle.chuck_fact_get(cf)
fact = fact_bytes.decode("UTF-8")

print(fact)
