# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class EquipmentandMaintenance(Document):

	def on_update(self):
		field = frappe.get_doc("Field",self.field_name)
		
		field.all_total = self.all_total
		field.save()
		
		#When update record we count qty
		#create new and delte Farming Stock record
		item_added = frappe.get_all("Farming Stock",
				fields=["name","item_name"], 
				filters={
					"parent" 	: "Equipment and Maintenance",
					"parent_name"	: self.name,
				}
        	)
	
		for item in item_added:
			frappe.delete_doc("Farming Stock", item.name)
			
		

		farmstock_added = frappe.get_all("Farming Stock",
				fields=["item_name","total_available"], 
				filters={
					"parent" 	: "Equipment and Maintenance",
				}
        	)
	
		# for item in farmstock_added:
			# frappe.insert_doc("Farming Stock Table", item.name)
			
		# Add new record Farming Stock
		for item in self.em_table: 
			stock = frappe.get_doc({
							"doctype"			: "Farming Stock",
							"qty" 		: item.quantity * (-1),
							"parent" 	: "Equipment and Maintenance",
							"parent_name"	: self.name,
							"item_name"				: item.equipment_name
						})
			
			stock.insert()
		
			