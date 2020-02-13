#!/usr/bin/python

#Nicholas Campbell
#2/13/2020
#I pledge my Honor that I have abided by the Stevens Honor System


"""
Python Core object Types
"""

import math

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551"
    print(x)

    # Assign a string "Stevens" to a variable y
    y = "Stevens"
    print(y)

    # Repeat variable y 5 times
    5*y
    # What is the length of z?
    z = 'z'
    length = len('z')
    print(length)
    # Concatenate variable y with string " is good"
    y = y+" is good"
    print(y)
    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    m = "good"
    m = "awesome"
    n = m
    return x, y, z, length, m, n


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings
    n = n.split(" ")
    print(n)
    # Get all the items past the first of the third substring
    p = n[2][1:]
    print (p)
    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    r = [[1,4,5],[6,10,11],[12,17,38]]
    print(r)
    # Collect the items in the last column of matrix A using list comprehension
    c = r[0][2]
    d = r[1][2]
    e = r[2][2]
    print (c,d,e)
    # Collect only the even items of the diagonal of matrix A using list comprehension
    f = r[0][0]
    g = r[2][2]
    h = r[0][2]
    i = r[2][0]
    print (f,g,h,i)
    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    d = "Stevens"
    c = len(d)
    o = []
    r = 0
    for x in range (0,c):
        p = d[r]
        r = r+1
        o = o+[ord(p)]
        
    print (o)    
    return p, r, c, d, o, e, f, g, h, i


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    a = {
        "fruit": "apple",
        "quantity": 4,
        "color": "green"
    }
    # Get the item in dictionary f that the key "fruit" maps to
    f = a["fruit"]
    print (f)
    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    f = a["quantity"]+1
    print (f)
    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    p = {
        "name": {
            "first_name": "Grace",
            "last_name": "Hopper"
        },
        "jobs": ["scientist", "engineer"],
        "age": 85

    }
    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    p["jobs"] = p["jobs"] + ["programmer"]
    print (p["jobs"])
    # Get the third job Grace has that you recently added
    print (p["jobs"][2])
    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    k = [key for key in p.keys()]
    k.sort()
    print (k)
    return a, f, p, k

numbers_and_strings()
lists()
dictionaries()





