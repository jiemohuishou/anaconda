#!/usr/bin/env python


_globalKvm = 0
_globalCdms = 0

def getKvmAndCdmsFlags():
    global _globalKvm, _globalCdms
    return _globalKvm, _globalCdms

def setKvmFlags(kvm):
    global _globalKvm
    _globalKvm = kvm

def setCdmsFlags(cdms):
    global _globalCdms
    _globalCdms = cdms
