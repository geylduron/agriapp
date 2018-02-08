# Copyright (c) 2013, sheerland and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	
	columns = get_columns()
	data = get_fields(filters)
	
	return columns, data
	

def get_columns():
	return [
		"Division::150",
		"Field::150"
	]

def get_fields(filters):
	conditions = get_conditions(filters)

	data = []
	
	fields = frappe.db.sql ("""SELECT company, field_name from `tabField` order by company asc """, as_list=1)
	
	division = ''
	for j in range(0,len(fields)):
		
		if division != fields[j][0]:
			division = fields[j][0]
			name = division
		else: 
			name = ""
			
		data.append([name, fields[j][1]])
		
	return data
	
		
def get_conditions(filters):
	conditions = ""

	return conditions	
