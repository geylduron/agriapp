from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("HR"),
			"items": [
				{
					"type": "doctype",
					"name": "Employee",
				},
				{
					"type": "doctype",
					"name": "Salary Slip",
				},
				{
					"type": "doctype",
					"name": "Salary Structure",
				},
				{
					"type": "doctype",
					"name": "Contracts",
				},
			]
		},
		{
			"label": _("Agriculture"),
			"items": [
				{
					"type": "doctype",
					"name": "Division",
				},
				{
					"type": "doctype",
					"name": "Field",
				},
				{
					"type": "doctype",
					"name": "Agricultural Tools",
				},
				{
					"type": "doctype",
					"name": "Machinery List",
				},
				{
					"type": "doctype",
					"name": "Crop Maintenance",
				},
			]
		},
		{
			"label": _("Analysis"),
			"items": [
				{
					"type": "doctype",
					"name": "Soil Analysis",
				},
				{
					"type": "doctype",
					"name": "Water Analysis",
				},
			]
		},
		{
			"label": _("Stock"),
			"items": [
				{
					"type": "doctype",
					"name": "Farming Stock",
				},
				{
					"type": "doctype",
					"name": "Harvest",
				},
			]
		},
		{
			"label": _("Activities"),
			"items": [
				{
					"type": "doctype",
					"name": "Project for Farming",
				},
					{
					"type": "doctype",
					"name": "Project",
				},
			]
		}
	]