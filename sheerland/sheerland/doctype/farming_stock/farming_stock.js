// Copyright (c) 2017, sheerland and contributors
// For license information, please see license.txt

cur_frm.add_fetch("item_name","quantity", "total_available");
cur_frm.add_fetch("item_name","price", "price");

frappe.ui.form.on('Farming Stock', {
	refresh: function(frm) {

	},
	qty: function(frm, cdt, cdn){
		stock = frappe.model.get_doc(cdt,cdn);
		
		if(stock.total_available == 0){
			frm.set_value("total_available", stock.qty);
			refresh_field("total_available");
		}else{
			var total = stock.total_available;
			var qty = stock.qty;
			var update;
			
			update = flt(total) + flt(qty);
			
			frm.set_value("total_available", update);
			refresh_field("total_available");
		}
	}
});
