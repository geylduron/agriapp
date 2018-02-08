// Copyright (c) 2017, sheerland and contributors
// For license information, please see license.txt

frappe.ui.form.on('Total Worked Hours', {
	to_time: function(frm,cdt,cdn) {
		
	sheer = frappe.model.get_doc(cdt,cdn);
	today = new Date();
	year = today.getFullYear();
	month = today.getMonth();
	currentDate = today.getDate();
	
	startDate = new Date(month + '-' + currentDate + '-' + year + ' ' + sheer.from_time);
	endTime = new Date(month + '-' + currentDate + '-' + year + ' ' + sheer.to_time);
	
	moment_SD = moment(startDate);
	moment_ED = moment(endTime);
	duration = moment.duration(moment_ED.diff(moment_SD));
	moment_seconds = duration.asSeconds();
	
	get_min = ((moment_seconds % 3600)/60);
	get_sec = moment_seconds % 60;
	get_hours = moment_seconds / 3600;
	
	
	get_sec = get_sec.toFixed(0);
	get_min = get_min.toFixed(0);
	get_hours = get_hours.toFixed(0);
	
	
	
	console.log(get_hours + " : " + get_min + " : " + get_sec);
	
	
	frm.set_value("total_hours", get_hours);
	// console.log(moment_hours);
	// console.log(startDate.getTime() + " : " + endTime.getTime());

	}
});
   