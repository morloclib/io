#!/usr/bin/env python

import sys
import subprocess
import json
from pymorlocinternals import (mlc_serialize, mlc_deserialize)
from collections import OrderedDict

sys.path = ["/home/z/.morloc/src"] + sys.path

from shell import *

def _morloc_foreign_call(args):
    try:
        sysObj = subprocess.run(
            args,
            stdout=subprocess.PIPE,
            check=True
        )
    except subprocess.CalledProcessError as e:
        sys.exit(str(e))

    return(sysObj.stdout.decode("ascii"))

def m1(x6, x7):
    a1 = mlc_deserialize(x7, ("str",None))
    a0 = mlc_deserialize(x6, ("list",(("str",None))))
    a2 = writeLinesF(a0, a1)
    a3 = mlc_serialize(a2, ("None",None))
    return(a3)
def m2(x8, x9):
    a1 = mlc_deserialize(x9, ("str",None))
    a0 = mlc_deserialize(x8, ("str",None))
    a2 = hasExtensionF(a0, a1)
    a3 = mlc_serialize(a2, ("bool",None))
    return(a3)
def m3(x10):
    a0 = mlc_deserialize(x10, ("list",(("str",None))))
    a1 = printL(a0)
    a2 = mlc_serialize(a1, ("None",None))
    return(a2)
def m4(x11):
    a0 = mlc_deserialize(x11, ("str",None))
    a1 = isGzipF(a0)
    a2 = mlc_serialize(a1, ("bool",None))
    return(a2)

if __name__ == '__main__':
    try:
        cmdID = int(sys.argv[1])
    except IndexError:
        sys.exit("Internal error in {}: no manifold id found".format(sys.argv[0]))
    except ValueError:
        sys.exit("Internal error in {}: expected integer manifold id".format(sys.argv[0]))
    try:
        dispatch = {
            1: m1,
            2: m2,
            3: m3,
            4: m4,
        }
        f = dispatch[cmdID]
    except KeyError:
        sys.exit("Internal error in {}: no manifold found with id={}".format(sys.argv[0], cmdID))

    result = f(*sys.argv[2:])

    print(result)
