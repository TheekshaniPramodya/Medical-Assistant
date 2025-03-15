from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate
from config import DATABASE_URL, SECRET_KEY
import logging



# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

# Initialize database
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Define model
class SymptomRemedy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptom = db.Column(db.String(100), nullable=False)
    remedy = db.Column(db.String(255), nullable=False)
    advice = db.Column(db.String(255), nullable=False)
    severity = db.Column(db.String(10), nullable=False, default='mild')

# Create database tables before handling requests
@app.before_request
def setup():
    db.create_all()
    if not SymptomRemedy.query.first():  # Populate DB if empty
        initial_data = [
            SymptomRemedy(symptom="headache", remedy="Take acetaminophen or ibuprofen",
                          advice="Rest in a quiet, dark room. Apply a cold or warm compress.", severity="mild"),
            SymptomRemedy(symptom="fever", remedy="Take acetaminophen or ibuprofen",
                          advice="Rest, stay hydrated, and monitor temperature.", severity="moderate"),
            SymptomRemedy(symptom="chest pain", remedy="Seek immediate medical attention",
                          advice="This could be serious. Call emergency services.", severity="severe"),
        ]
        db.session.bulk_save_objects(initial_data)
        db.session.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_advice', methods=['POST'])
def get_advice():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', '').lower()

        if not symptoms.strip():
            return jsonify({'success': False, 'message': 'Please enter your symptoms.'})

        results = SymptomRemedy.query.filter(SymptomRemedy.symptom.ilike(f"%{symptoms}%")).all()

        if results:
            response = [{
                'symptom': r.symptom,
                'remedy': r.remedy,
                'advice': r.advice,
                'severity': r.severity
            } for r in results]
            return jsonify({'success': True, 'results': response})
        else:
            return jsonify({'success': False, 'message': 'No matching symptoms found. Please consult a doctor.'})

    except Exception as e:
        logging.error(f"Error in get_advice: {e}")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'})

if __name__ == '__main__':
    app.run(debug=True)
