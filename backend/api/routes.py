from flask import Blueprint, request, jsonify
import sqlite3

api = Blueprint('api', __name__)

def get_db_connection():
    conn = sqlite3.connect('instance/medical.db')
    conn.row_factory = sqlite3.Row
    return conn

@api.route('/get_advice', methods=['POST'])
def get_advice():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', '').lower().strip()

        if not symptoms:
            return jsonify({'success': False, 'message': 'Please enter your symptoms.'})

        conn = get_db_connection()
        c = conn.cursor()

        c.execute('''SELECT symptom, remedy, advice, severity 
                     FROM symptoms_remedies 
                     WHERE LOWER(symptom) LIKE ?''', ('%' + symptoms + '%',))

        results = c.fetchall()
        conn.close()

        if results:
            response = [{
                'symptom': row['symptom'],
                'remedy': row['remedy'],
                'advice': row['advice'],
                'severity': row['severity']
            } for row in results]
            return jsonify({'success': True, 'results': response})
        else:
            return jsonify({'success': False, 'message': 'No matching symptoms found. Please consult a healthcare professional.'})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})