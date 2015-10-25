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


prof_details = json.load(open('./prof_details.json', 'r'))
for prof in prof_details:
    prof = dict(prof)
    prof["field"] = "| ".join(prof["field"])
    prof_text = """
{{Infobox Professor
| department = %(dept)s
| research_areas = {{ubl| %(field)s}}
| year_joined = %(year)s
}}
"""
    prof_text = prof_text % prof
    prof_page = pywikibot.Page(site, prof['name'])
    prof_page.text = prof_text

    msg = "Creat Page for {}".format(prof['name'])
    prof_page.save(msg)
    print(msg)
