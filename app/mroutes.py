import math

from flask import request, jsonify
from app import app

jsone = [{'name': 'Iron', 'qtty': '3', 'consumption': '1000', 'hours': '3'}, {'name': 'Iron', 'qtty': '3', 'consumption':'1000', 'hours':'3'}]


def adder(*args):
    return sum(*args)


@app.route('/power_consumption', method='POST')
def total_output_load():
    output = []
    data = request.get_json()
    for item in data:
        app_qtty = item['qtty']
        app_hours = item['hours']
        app_consumption = item['consumption']
        app_output = app_qtty * app_hours * app_consumption
        output.append(app_output)
    total_app_output = adder(output)
    result = {'status': 'oK', 'status_code': '200', 'total_power_consumption': total_app_output}
    return jsonify(result)


result_json = {'total_power': '1000', 'batt_type': 'lithium', 'batt_volt': '12v', 'solar_panel_power': '1000', 'total_watt':'1000'}


@app.route('/final_result', method='POST')
def calculated_result():
    data = request.get_json()
    sun_hours = 3.4
    load = data['total_power']
    output_load = data['total_power'] * 1.3
    panel_capacity_needed = output_load / sun_hours
    solar_panel_power = data['solar_panel_power']
    number_of_panels_needed = math.ceil(panel_capacity_needed / solar_panel_power)
    total_watt = data['total_watt']
    inverter_size = total_watt * 1.3
    battery_loss = 0.85
    depth_of_discharge = 0.6
    nominal_battery_voltage = data['batt_volt']
    days_of_autonomy = 3  # determined by user
    battery_required = (load * days_of_autonomy) / (battery_loss * depth_of_discharge * nominal_battery_voltage)
    result = {'status': 'oK', 'status_code': '200', 'number_of_panels_needed': number_of_panels_needed, 'inverter_size':inverter_size, 'battery_required': battery_required, }
    return jsonify(result)








