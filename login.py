
The following Python code has a bug.

Issue:
The login function crashes when password is None.
The code should check for None before validating credentials.

Code:

The following Python code has a bug.

Issue:
The login function crashes when password is None.
The code should check for None before validating credentials.

Code:
def login(username, password):

    # BUG: password can be None
    if password is None or password == "":
        return "Password cannot be empty"

    if username == "admin" and password == "admin123":
        return "Login successful"

    return "Invalid credentials"


# test
print(login("admin", None))


Return the corrected version of the code only.

# Test it out:
def login(username, password):

    if password == "admin123":
        return "Login successful"

    return "Password cannot be empty"

def login(username, password):

    if password == None or password == "":
        return "Password cannot be empty"

    return "Login successful"

def login(username, password):

    # BUG: password can be None
    if password is None or password == "":
        return "Password cannot be empty"

    return "Login successful"

# test:
print(login("admin", None))
print(login("admin", "admin123"))
print(login("admin", "admin"))

"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 08:54:52 2020

@author: lalitha
"""

import pykml.etree as parse
import kml_functions as kf
import argparse

def parse_kml(kml_path, return_type, **kwargs):


Return the corrected version of the code only.

# Test it out:
if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="""
                                     This code gets the latitude and longitude data from a kml file
                                     and converts it into the coordinate form of
                                     a folium map. By default it saves the map as a map and the name of the
                                     output file as a map file. It can also save the folium map in the map dir.

                                     Arguments:
                                          --path kml_path  --return_type json  --map_file map_file.json --name map_file.png
    -----------------------------------------------------------------------------------
    example:
    python kml_to_folium.py -path/path/file.kml  -output/location.map     --map_file map_file.png

    """
                                    )
    parser.add_argument('--path', metavar='path', dest='kml_path', nargs=1,
                        default='',