from flask import Flask, request, jsonify
import threading
import calc

app = Flask(__name__)
calculation_status = {"status": "Idle"}

@app.route('/startcalculation', methods=['POST'])
def start_calculation():
    data = request.json
    calculation_key = data.get('key')

    if calculation_status["status"] == "Idle":
        calculation_status["status"] = "Berechnung läuft"
        thread = threading.Thread(target=calc.run_calculation, args=(calculation_key, calculation_status))
        thread.start()
        return jsonify({"message": "Berechnung gestartet"}), 200
    else:
        return jsonify({"message": "Eine Berechnung läuft bereits"}), 400

@app.route('/statuscalculation', methods=['GET'])
def status_calculation():
    return jsonify({"status": calculation_status["status"]})

if __name__ == '__main__':
    app.run(debug=True)
