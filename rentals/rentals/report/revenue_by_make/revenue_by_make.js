// Copyright (c) 2026, BWH and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue By Make"] = {
	"filters": [
		{
			"fieldname":"make",
			"label": "Make",
			"fieldtype": "Data",
			"width": 400
		},
		{
			"fieldname":"total_revenue",
			"label": "Total Revenue",
			"fieldtype": "Currency",
			"width": 400
		},
		{
			"fieldname":"make_count",
			"label": "Number of rides",
			"fieldtype": "Int",
			"width": 400
		}

	]
};
