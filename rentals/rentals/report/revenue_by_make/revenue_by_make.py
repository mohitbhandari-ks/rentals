# Copyright (c) 2026, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import cint, flt


def execute(filters=None):

	filters = filters or {}

	columns = [{
		"fieldname": "make",
		"label": "Make",
		"fieldtype": "Data",
		"width": 400
	}, {
		"fieldname": "total_revenue",
		"label": "Total Revenue",
		"fieldtype": "Currency",
		"width": 400
	}, {
		"fieldname": "make_count",
		"label": "Number of rides",
		"fieldtype": "Int",
		"width": 400
	}]
	data = frappe.get_all("Ride Booking", fields=["sum(total_amount) as total_revenue", "vehicle.make","count(*) as make_count"], filters={"docstatus": ("=", 1)}, group_by="make")

	# make/total_revenue/make_count only exist after the join + aggregation,
	# so they can't be pushed down as WHERE conditions - filter in Python instead.
	if filters.get("make"):
		data = [d for d in data if filters["make"].lower() in (d.make or "").lower()]
	if filters.get("total_revenue"):
		data = [d for d in data if d.total_revenue == flt(filters["total_revenue"])]
	if filters.get("make_count"):
		data = [d for d in data if d.make_count == cint(filters["make_count"])]

	chart = {
		"type": "donut",
		"data": {
			"labels": [d.make for d in data],
			"datasets": [{
				"name": "Total Revenue",
				"values": [d.total_revenue for d in data],
			}]
		},
		# "colors": ["#ff6384", "#36a2eb", "#ffce56", "#4bc0c0", "#9966ff", "#ff9f40"],
		"title": "Revenue by Make",
	}

	return columns, data, "Here is the message summary", chart


def execute_snapshot_report(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for snapshot report. When 'Synced
	Report' is enabled in report, framework will call this method
	every time the report is refreshed or a filter is updated. It
	accepts the same filters as normal execute. But a utility method -
	get_latest_sync, is also imported.

	"""
	from frappe.database.duckdb.database import get_latest_sync

	columns, data = [], []
	return columns, data
