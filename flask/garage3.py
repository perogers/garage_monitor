from flask import Flask, jsonify
from flask import render_template
from flask import send_file

from w1thermsensor import W1ThermSensor

app = Flask(__name__)

@app.route("/door/image", methods=['GET'])
def getImage():
    return send_file('static/garage/image.jpg')

@app.route("/door/camera", methods=['GET'])
def cam():
    templateData = {
	'cam' : 'garage_open.jpg'
    }
    return render_template('door_camera.html', **templateData)

# TODO : add GPIO code with door switch
@app.route("/door/state", methods=['GET'])
def hello():
    templateData = {
        'status' : 'OPEN'
    }
    return render_template('garage.html', **templateData)

@app.route("/", methods=['GET'])
@app.route("/garage/temperature", methods=['GET'])
def getTemperature():
	sensor = W1ThermSensor()
	temperature = sensor.get_temperature(W1ThermSensor.DEGREES_F)
	templateData = {
	   'temperature' : temperature,
	   'scale' : 'fahrenheit'
	}
	return jsonify(templateData)
	#return render_template('temperature.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
