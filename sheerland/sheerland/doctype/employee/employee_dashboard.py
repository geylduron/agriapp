from frappe import _

def get_data():
	return {
		'fieldname': 'employee_name',
		'transactions': [
			{
				'label': _('Contracts'),
				'items': ['Contracts']
			}
		]
	}