from frappe import _

def get_data():
	return {
		'fieldname': 'field_name',
		'transactions': [
			{
				'label': _('Soil Analysis'),
				'items': ['Soil Analysis']
			},
			{
				'label': _('Water Analysis'),
				'items': ['Water Analysis']
			},
			{
				'label': _('Harvest'),
				'items': ['Item']
			},
			{
				'label': _('Create Project'),
				'items': ['Project']
			},
		]
	}