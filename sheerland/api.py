import frappe
from frappe import _

@frappe.whitelist()
def updateqtybystock(doc, method):
		# sum qty of item
		item_name = doc.item_name
		query = """ SELECT SUM(qty) as sum_qty FROM `tabFarming Stock`
		WHERE item_name = '%s'""" %(item_name)
		
		quantity = frappe.db.sql(query)[0][0]
		
		if not quantity :
			quantity = 0
		
		item = frappe.get_doc("Item for Farming",item_name)
		
		item.quantity = quantity
		item.save()


@frappe.whitelist()
def updateqtybyfield(doc, method):

		stocks = frappe.get_all("Farming Stock",
				fields=["name","item_name"], 
				filters={
					"parent" 	: "Equipment and Maintenance",
					"parent_name"	: doc.name,
				}
        	)
		
		for stock in stocks:
			frappe.delete_doc("Farming Stock", stock.name)
			