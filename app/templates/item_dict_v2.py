# This file can probably be deleted soon. It just helps me test
# how to get into and out of a json file with python.
import sys, json
with open('/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json', 'r') as f:
  data = json.load(f)

# Data at this point is a list of dictionaries. Each dict is an object 
# in the master_list

print(data)
sys.exit()
if __name__ == "__main__":
    # generate the routes.py file
    fp = "/home/kirk/Documents/flask_projects/storage_locker_inventory/app/routes.py"
    with open(fp, 'w') as f:
        f.write('from flask import render_template\n')
        f.write('from app import app\n')
        f.write('from app.templates.item_dict import master_list\n')
        f.write('\n')
        f.write('@app.route("/")\n')
        f.write('@app.route("/index")\n')
        f.write('def index():\n')
        f.write('\treturn render_template("index.html", master_list=master_list)\n')
        f.write('\n')
        # give each item in the master_list a route too
        for item in master_list:
            f.write('@app.route("'+item["url"]+'")\n')
            f.write('def '+item["url"]+'():\n')
            f.write('\treturn render_template("items/'+item["url"]+'", master_list=master_list)\n')
        f.write('\n')
        
    # Generate all the html files that correspond to the items in the
    # master_list.
    for item in master_list:
        fp = "/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/items/"+item["url"]
        with open(fp, 'w') as f:
            f.write('{% extends "base.html" %}\n')
            f.write('\n')
            f.write('{% block title %}'+item["title"]+'{% endblock %}\n')
            f.write('\n')
            f.write('{% block page_content %}\n')
            f.write('\n')
            f.write('<h1 class="text-light">'+item["title"]+'</h1>\n')
            f.write('\n')
            f.write('\n')
            f.write('\n')
            f.write('\n')