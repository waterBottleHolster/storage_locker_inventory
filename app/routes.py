from flask import render_template, flash
from app import app
from app.forms import ItemForm
from app.templates.item_dict import genny_function
import os, json

with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "r") as f:
	data = json.load(f)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html", data=data)

@app.route("/remove_item/<item_url>", methods=["GET","POST"])
def remove_item(item_url):
	# find the list index of the item being deleted
	for i, item in enumerate(data):
		if item["url"] == item_url:
			# delete the html template
			os.remove("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/items/"+item_url+".html")
			# remove the dict from data object
			del data[i]

	# now write the updated info the json
	with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
		json.dump(data, outfile, indent=2)

	# call the genny functions to update routes and html templates
	genny_function()

	return render_template("remove_item.html", deleted_item=item_url)

@app.route("/add_item", methods=["GET", "POST"])
def add_item():
	form = ItemForm()

	if form.validate_on_submit():
		# This route will add a new item into the json file
		# First check that the item isn't already in there.
		dupe_marker = False
		for item in data:
			if item["url"] == form.url.data:
				flash("An item with that title is already in the JSON!")
				dupe_marker = True

		if dupe_marker == False:
		#this means the item is new
			temp_dict = {
				"title": form.title.data,
				"plan": form.plan.data,
				"category": form.category.data,
				"url": form.url.data,
				"description": form.description.data,
				"comments": [
					["", ""]
				]
			}
			data.append(temp_dict)

			# now update the json
			with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
				json.dump(data, outfile, indent=2)

			# call the genny functions to update routes and html templates
			genny_function()

			# finally, flash a success message to user
			flash("Item successfully added to JSON file!")

	return render_template("add_item.html", form=form)


@app.route("/snowboard", methods=["GET", "POST"])
def snowboard():
	form = ItemForm()
	if form.validate_on_submit():
		# update the data dict with the info submitted from the form
		for item in data:
			if item["title"] == "Snowboard":
				item["plan"] = form.plan.data
				item["category"] = form.category.data
				item["description"] = form.description.data

			# update the json with the new info
			with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
				json.dump(data, outfile, indent=2)

	return render_template("items/snowboard.html", data=data, form=form)

@app.route("/snowboard_helmet", methods=["GET", "POST"])
def snowboard_helmet():
	form = ItemForm()
	if form.validate_on_submit():
		# update the data dict with the info submitted from the form
		for item in data:
			if item["title"] == "Snowboard Helmet":
				item["plan"] = form.plan.data
				item["category"] = form.category.data
				item["description"] = form.description.data

			# update the json with the new info
			with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
				json.dump(data, outfile, indent=2)

	return render_template("items/snowboard_helmet.html", data=data, form=form)

@app.route("/socket_set", methods=["GET", "POST"])
def socket_set():
	form = ItemForm()
	if form.validate_on_submit():
		# update the data dict with the info submitted from the form
		for item in data:
			if item["title"] == "Socket Set":
				item["plan"] = form.plan.data
				item["category"] = form.category.data
				item["description"] = form.description.data

			# update the json with the new info
			with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
				json.dump(data, outfile, indent=2)

	return render_template("items/socket_set.html", data=data, form=form)

@app.route("/east_of_eden", methods=["GET", "POST"])
def east_of_eden():
	form = ItemForm()
	if form.validate_on_submit():
		# update the data dict with the info submitted from the form
		for item in data:
			if item["title"] == "East of Eden":
				item["plan"] = form.plan.data
				item["category"] = form.category.data
				item["description"] = form.description.data

			# update the json with the new info
			with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
				json.dump(data, outfile, indent=2)

	return render_template("items/east_of_eden.html", data=data, form=form)

@app.route("/grapes_of_wrath", methods=["GET", "POST"])
def grapes_of_wrath():
	form = ItemForm()
	if form.validate_on_submit():
		# update the data dict with the info submitted from the form
		for item in data:
			if item["title"] == "Grapes of Wrath":
				item["plan"] = form.plan.data
				item["category"] = form.category.data
				item["description"] = form.description.data

			# update the json with the new info
			with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
				json.dump(data, outfile, indent=2)

	return render_template("items/grapes_of_wrath.html", data=data, form=form)

@app.route("/flask_web_textbook", methods=["GET", "POST"])
def flask_web_textbook():
	form = ItemForm()
	if form.validate_on_submit():
		# update the data dict with the info submitted from the form
		for item in data:
			if item["title"] == "Flask Web Textbook":
				item["plan"] = form.plan.data
				item["category"] = form.category.data
				item["description"] = form.description.data

			# update the json with the new info
			with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
				json.dump(data, outfile, indent=2)

	return render_template("items/flask_web_textbook.html", data=data, form=form)

@app.route("/alberta_road_atlas", methods=["GET", "POST"])
def alberta_road_atlas():
	form = ItemForm()
	if form.validate_on_submit():
		# update the data dict with the info submitted from the form
		for item in data:
			if item["title"] == "Alberta Road Atlas":
				item["plan"] = form.plan.data
				item["category"] = form.category.data
				item["description"] = form.description.data

			# update the json with the new info
			with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
				json.dump(data, outfile, indent=2)

	return render_template("items/alberta_road_atlas.html", data=data, form=form)

@app.route("/sask_road_atlas", methods=["GET", "POST"])
def sask_road_atlas():
	form = ItemForm()
	if form.validate_on_submit():
		# update the data dict with the info submitted from the form
		for item in data:
			if item["title"] == "Sask Road Atlas":
				item["plan"] = form.plan.data
				item["category"] = form.category.data
				item["description"] = form.description.data

			# update the json with the new info
			with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
				json.dump(data, outfile, indent=2)

	return render_template("items/sask_road_atlas.html", data=data, form=form)

@app.route("/bc_road_atlas", methods=["GET", "POST"])
def bc_road_atlas():
	form = ItemForm()
	if form.validate_on_submit():
		# update the data dict with the info submitted from the form
		for item in data:
			if item["title"] == "BC Road Atlas":
				item["plan"] = form.plan.data
				item["category"] = form.category.data
				item["description"] = form.description.data

			# update the json with the new info
			with open("/home/kirk/Documents/flask_projects/storage_locker_inventory/app/templates/item_dict.json", "w") as outfile:
				json.dump(data, outfile, indent=2)

	return render_template("items/bc_road_atlas.html", data=data, form=form)

