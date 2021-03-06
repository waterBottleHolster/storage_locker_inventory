
# Each item gets a dictionary, then they are all compiled into a big 
# list at the end.
#    - item title and item plan are self-explanatory
#    - category is what kind of item it is (wanted this to separate 
#       out books easily)
#    - description is a couple basic notes about the item
#    - comments are lists of tuples (element 0 is date, element 1 
#       is comment itself)


# list of categories
#category_list = [
#    books,
#    fitness,
#    tools
#]


# The point of storing the info in here is that it's easier to
# navigate/edit than a database. These dictionaries will be used
# to dynamically update html templates. You can update the info here
# and the changes will be carried through to the templates without 
# you having to navigate to each of them.

import json

def genny_function():
    #start by getting an up to date json file
    with open('/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json', 'r') as f:
        master_list = json.load(f)

    # generate the routes.py file
    fp = "/home/kirk/Documents/flask_projects/storage_locker_inventory/app/routes.py"
    with open(fp, 'w') as f:
        f.write('from flask import render_template, flash\n')
        f.write('from app import app\n')
        f.write('from app.forms import ItemForm\n')
        f.write('from app.templates.item_dict import genny_function\n')
        f.write('import os, json\n')
        f.write('\n')
        f.write('with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "r") as f:\n')
        f.write('\tdata = json.load(f)\n')
        f.write('\n')
        f.write('@app.route("/")\n')
        f.write('@app.route("/index")\n')
        f.write('def index():\n')
        f.write('\treturn render_template("index.html", data=data)\n')
        f.write('\n')
        f.write('@app.route("/remove_item/<item_url>", methods=["GET","POST"])\n')
        f.write('def remove_item(item_url):\n')
        f.write('\t# find the list index of the item being deleted\n')
        f.write('\tfor i, item in enumerate(data):\n')
        f.write('\t\tif item["url"] == item_url:\n')
        f.write('\t\t\t# delete the html template\n')
        f.write('\t\t\tos.remove("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/items/"+item_url+".html")\n')
        f.write('\t\t\t# remove the dict from data object\n')
        f.write('\t\t\tdel data[i]\n')
        f.write('\n')
        f.write('\t# now write the updated info the json\n')
        f.write('\twith open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:\n')
        f.write('\t\tjson.dump(data, outfile, indent=2)\n')
        f.write('\n')
        f.write('\t# call the genny functions to update routes and html templates\n')
        f.write('\tgenny_function()\n')
        f.write('\n')
        f.write('\treturn render_template("remove_item.html", deleted_item=item_url)\n')
        f.write('\n')       
        f.write('@app.route("/add_item", methods=["GET", "POST"])\n')
        f.write('def add_item():\n')
        f.write('\tform = ItemForm()\n')
        f.write('\n')
        f.write('\tif form.validate_on_submit():\n')
        f.write('\t\t# This route will add a new item into the json file\n')
        f.write('\t\t# First check that the item isn\'t already in there.\n')
        f.write('\t\tdupe_marker = False\n')
        f.write('\t\tfor item in data:\n')
        f.write('\t\t\tif item["url"] == form.url.data:\n')
        f.write('\t\t\t\tflash("An item with that title is already in the JSON!")\n')
        f.write('\t\t\t\tdupe_marker = True\n')
        f.write('\n')
        f.write('\t\tif dupe_marker == False:\n')
        f.write('\t\t#this means the item is new\n')
        f.write('\t\t\ttemp_dict = {\n')
        f.write('\t\t\t\t"title": form.title.data,\n')
        f.write('\t\t\t\t"plan": form.plan.data,\n')
        f.write('\t\t\t\t"category": form.category.data,\n')
        f.write('\t\t\t\t"url": form.url.data,\n')
        f.write('\t\t\t\t"description": form.description.data,\n')
        f.write('\t\t\t\t"comments": [\n')
        f.write('\t\t\t\t\t["", ""]\n')
        f.write('\t\t\t\t]\n')
        f.write('\t\t\t}\n')
        f.write('\t\t\tdata.append(temp_dict)\n')
        f.write('\n')
        f.write('\t\t\t# now update the json\n')
        f.write('\t\t\twith open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:\n')
        f.write('\t\t\t\tjson.dump(data, outfile, indent=2)\n')
        f.write('\n')
        f.write('\t\t\t# call the genny functions to update routes and html templates\n')
        f.write('\t\t\tgenny_function()\n')
        f.write('\n')
        f.write('\t\t\t# finally, flash a success message to user\n')
        f.write('\t\t\tflash("Item successfully added to JSON file!")\n')
        f.write('\n')
        f.write('\treturn render_template("add_item.html", form=form)\n')
        f.write('\n')
        f.write('\n')

        # give each item in the master_list a route too
        for item in master_list:
            f.write('@app.route("/'+item["url"]+'", methods=["GET", "POST"])\n')
            f.write('def '+item["url"]+'():\n')
            f.write('\tform = ItemForm()')
            f.write('\n')
            f.write('\tif form.validate_on_submit():\n')
            f.write('\t\t# update the data dict with the info submitted from the form\n')
            f.write('\t\tfor item in data:\n')
            f.write('\t\t\tif item["title"] == "'+item["title"]+'":\n')
            f.write('\t\t\t\titem["plan"] = form.plan.data\n')
            f.write('\t\t\t\titem["category"] = form.category.data\n')
            f.write('\t\t\t\titem["description"] = form.description.data\n')
            f.write('\n')
            f.write('\t\t\t# update the json with the new info\n')
            f.write('\t\t\twith open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:\n')
            f.write('\t\t\t\tjson.dump(data, outfile, indent=2)\n')
            f.write('\n')
            f.write('\treturn render_template("items/'+item["url"]+'.html", data=data, form=form)\n')
            f.write('\n')
        
    # Generate all the html files that correspond to the items in the
    # master_list.
    for item in master_list:
        fp = "/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/items/"+item["url"]+".html"
        with open(fp, 'w') as f:
            f.write('{% extends "base.html" %}\n')
            f.write('\n')
            f.write('{% block title %}'+item["title"]+'{% endblock %}\n')
            f.write('\n')
            f.write('{% block page_content %}\n')
            f.write('\n')
            f.write('<a href="{{ url_for("index") }}"><h1 class="text-light display-4 my-3">'+item["title"]+'</h1></a>\n')
            f.write('\n')
            f.write('<form action="{{ url_for("'+item["url"]+'") }}" method="POST">\n')
            f.write('\t{{ form.hidden_tag() }}\n')
            f.write('\t{{ form.url }}\n')
            f.write('\t{% for item in form %}\n')
            f.write('\t\t{% if item.name != "csrf_token" %}\n')
            f.write('\t\t\t{% if item.name != "submit" %}\n')
            f.write('\t\t\t\t{% if item.name == "url" %}\n')
            f.write('\t\t\t\t\t<div class="form-group mb-3">\n')
            f.write('\t\t\t\t\t\t{{ item.label(class="text-light") }}\n')
            f.write('\t\t\t\t\t\t<p class="text-white" id="url-stand-in"></p>\n')
            f.write('\t\t\t\t\t</div>\n')
            f.write('\t\t\t\t{% else %}\n')
            f.write('\t\t\t\t\t<div class="form-group mb-3">\n')
            f.write('\t\t\t\t\t\t{{ item.label(class="text-light") }}\n')
            f.write('\t\t\t\t\t\t{# find the element in the json for this page #}\n')
            f.write('\t\t\t\t\t\t{% for element in data %}\n')
            f.write('\t\t\t\t\t\t\t{% if element["title"] == "'+item["title"]+'" %}\n')
            f.write('\t\t\t\t\t\t\t\t{{ item(class="form-control", value=element[item.name]) }}\n')
            f.write('\t\t\t\t\t\t\t{% endif %}\n')
            f.write('\t\t\t\t\t\t{% endfor %}\n')
            f.write('\t\t\t\t\t</div>\n')
            f.write('\t\t\t\t{% endif %}\n')
            f.write('\t\t\t{% endif %}\n')
            f.write('\t\t{% endif %}\n')
            f.write('\t{% endfor %}\n')
            f.write('\t<div style="display: flex; justify-content: space-between;">\n')
            f.write('\t\t<a type="button" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#comments-modal">Comments</a>\n')
            f.write('\t\t<div style="display: flex; justify-content: flex-end;">\n')
            f.write('\t\t\t<input type="reset" class="btn btn-warning mx-3" />\n')
            f.write('\t\t\t{{ form.submit(class="btn btn-success mx-3") }}\n')
            f.write('\t\t</div>\n')
            f.write('\t</div>\n')
            f.write('</form>\n')
            f.write('\n')
            f.write('<div class="modal fade" id="comments-modal" tabindex="-1" aria-labelledby="comments-modal-label" aria-hidden="true">\n')
            f.write('\t<div class="modal-dialog">\n')
            f.write('\t\t<div class="modal-content">\n')
            f.write('\t\t\t<div class="modal-header">\n')
            f.write('\t\t\t\t<h5 class="modal-title" id="comments-modal-label">Chronilogical Comments</h5>\n')
            f.write('\t\t\t\t<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>\n')
            f.write('\t\t\t</div>\n')
            f.write('\t\t\t<div class="modal-body">\n')
            f.write('\t\t\t\t<table class="table table-bordered table-dark" id="snowboard-comments-table">\n')
            f.write('\t\t\t\t\t<colgroup>\n')
            f.write('\t\t\t\t\t\t<col span="1" style="width: 20%;">\n')
            f.write('\t\t\t\t\t\t<col span="1" style="width: 70%;">\n')
            f.write('\t\t\t\t\t</colgroup>\n')
            f.write('\t\t\t\t\t<thead>\n')
            f.write('\t\t\t\t\t\t<tr>\n')
            f.write('\t\t\t\t\t\t\t<th>Date</th>\n')
            f.write('\t\t\t\t\t\t\t<th>Comment</th>\n')
            f.write('\t\t\t\t\t\t</tr>\n')
            f.write('\t\t\t\t\t</thead>\n')
            f.write('\t\t\t\t\t<tbody id="comments-table-content">\n')
            f.write('\t\t\t\t\t\t<tr>\n')
            f.write('\t\t\t\t\t\t\t<td>2022-02-13</td>\n')
            f.write('\t\t\t\t\t\t\t<td>Moved to storage locker.</td>\n')
            f.write('\t\t\t\t\t\t</tr>\n')
            f.write('\t\t\t\t\t</tbody>\n')
            f.write('\t\t\t\t</table>\n')
            f.write('\t\t\t</div>\n')
            f.write('\t\t\t<div class="modal-footer">\n')
            f.write('\t\t\t\t<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>\n')
            f.write('\t\t\t\t<form id="modal-form" action="#">\n')
            f.write('\t\t\t\t\t<button type="submit" class="btn btn-success">Save</button>\n')
            f.write('\t\t\t\t</form>\n')
            f.write('\t\t\t</div>\n')
            f.write('\t\t</div>\n')
            f.write('\t</div>\n')
            f.write('</div>\n')
            f.write('\n')
            f.write('<script>\n')
            f.write('\twindow.addEventListener("load", (event) => {\n')
            f.write('\t\traw_title = document.getElementById("title").value;\n')
            f.write('\t\tlowercase_title = raw_title.toLowerCase();\n')
            f.write('\t\ttreated_title = lowercase_title.replaceAll(" ", "_");\n')
            f.write('\t\tdocument.getElementById("url").value = treated_title;\n')
            f.write('\t\tdocument.getElementById("url-stand-in").innerText = treated_title;\n')
            f.write('\t});\n')
            f.write('\tdocument.getElementById("title").addEventListener("input", (event) => {\n')
            f.write('\t\traw_title = document.getElementById("title").value;\n')
            f.write('\t\tlowercase_title = raw_title.toLowerCase();\n')
            f.write('\t\ttreated_title = lowercase_title.replaceAll(" ", "_");\n')
            f.write('\t\tdocument.getElementById("url").value = treated_title;\n')
            f.write('\t\tdocument.getElementById("url-stand-in").innerText = treated_title;\n')
            f.write('\t});\n')
            f.write('</script>\n')
            f.write('\n')
            f.write('{% endblock %}')
            

if __name__ == "__main__":
    genny_function()