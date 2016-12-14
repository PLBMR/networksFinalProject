#snapTutorial.py
#features the code that I wrote for the Snap.py tutorial, which is avaialble
#here http://snap.stanford.edu/snappy/doc/tutorial/tutorial.html

#imports

import snap

#general process
""" Basic Types:
    -TInt (int)
    -TFlt (float)
    -TStr (str)
    Note: TSR("") is not compatible with Python, so an empty string 
        literal will cause an error.
Vectors are sequences of values of the same type.
    -TIntV
    -TFltV
    -TStrV
"""

#empty vector of integers
v = snap.TIntV()
#add some values
for i in xrange(1,6):
    v.Add(i)
#fuck it, I'm just gonna do this tutorial from the python command line
#you can reference http://snap.stanford.edu/snappy/doc/tutorial/tutorial.html
""" Hash table types in Snap.py and SNAP use a naming convention of being named
    as <key_type_name><value_type_name>, followed by H. For example, TIntStrH.
    If <key_type_name> and <value_type_name> have the same type, only one type
    name might be used, such as TIntH.
"""
""" pairs contain two values. Each value has its own type. Naming convention is
    <type1><type2> folowed by Pr. For example, (integer,string) pair is named
    TIntStrPr. If <type1> and <type2> have the same type, only one type name
    might be use, such as TIntPr.
"""
"""see tutorial page for big list on the SNAP Types that are used in Snap.py.
"""
"""For graphs and networks, In general, if you need to call a class method, use 
    T and if you need to specify an instance type, use P. 
"""
