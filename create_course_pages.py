from __future__ import print_function
import json
import argparse
import pywikibot
site = pywikibot.Site()

parser = argparse.ArgumentParser()
parser.add_argument("--outdir",
                    default=".",
                    help="Output directory")
args = parser.parse_args()


course_details = json.load(open('./syllabus.json', 'r'))
for course in course_details[1:2]:
    course = dict(course)
    course_text = """
{{Infobox course
| course_code = %(Code)
| course_name = %(Name)
| department = [[%(Department)]]
| credits = %(Credits)
| ltp = %(LTP)
| professor =
| venue =
}}

=Syllabus=
==Syllabus mentioned in ERP==

%(Syllabus)


==Concepts taught in class==

===Student Opinion===

==How to Crack the Paper==

=Classroom resources=

=Additional Resources=
"""
    course_text = course_text % course
    course_page = pywikibot.Page(site, "{}: {}".format(course['Code'], course['Name']))
    course_page.text = course_text

    msg = "Created Page for {}".format(course['Name'])
    course_page.save(msg)
    print(msg)


"""

    {
        "Code": "ME41603",
        "Credits": "3",
        "Department": "Mechanical Engineering",
        "LTP": "3-0-0",
        "Name": "VIBRATION AND NOISE CONTROL",
        "Syllabus": "Prerequisite \u00e2Design of Machine ElementsFundamentals of Vibration Theory; Force\nTransmissibility, Design of Vibration Isolators and Absorbers and other passive\ndampers; Active Vibration control; Torsional Vibration; Basics of Acoustics,\nSolution of 1-D and 3-D wave equation, Sound Field Characterization, Sound\nSources, Principles of Noise Control, Reflection and Transmission of Sound\nWaves, Noise Control Materials: Absorbers, Barriers and Damping Materials,\nSilencers."
    }
 
"""
