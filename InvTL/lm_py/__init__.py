"""\
LM-PY, the Python Langugage Module for InvTS
"""
__version__ = "0.0.1"
#Set up pypy path here
import sys
import os
#sys.path.append(os.path.realpath(os.path.split(os.path.split(os.path.realpath(os.path.dirname(__file__)))[0])[0]+"/pypy-dist/pypy"))
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
from LM import LanguageModule
