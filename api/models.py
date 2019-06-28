from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Studies(DB.Model): 
    """Table containing records for active studies"""
    nct_id = DB.Column(DB.String(15), primary_key=True)
    start_date = DB.Column(DB.String(15), nullable=True)
    completion_date = DB.Column(DB.String(15), nullable=True)
    study_type = DB.Column(DB.String(40), nullable=True)
    overall_status = DB.Column(DB.String(30), nullable=True)
    brief_title = DB.Column(DB.String(350), nullable=True)
    phase = DB.Column(DB.String(20), nullable=True)
    condition_name = DB.Column(DB.String(200), nullable=True)
    description = DB.Column(DB.String(6000), nullable=True)
    gender = DB.Column(DB.String(10), nullable=True)
    minimum_age = DB.Column(DB.String(15), nullable=True)
    maximum_age = DB.Column(DB.String(15), nullable=True)
    healthy_volunteers = DB.Column(DB.String(5), nullable=True)
    sponsor_name = DB.Column(DB.String(150), nullable=True)
    name = DB.Column(DB.String(150), nullable=True)
    phone = DB.Column(DB.String(50), nullable=True)
    email = DB.Column(DB.String(80), nullable=True)
    completion_prob = DB.Column(DB.BigInteger, nullable=True)
    minimum_age_val = DB.Column(DB.Integer, nullable=True)
    maximum_age_val = DB.Column(DB.Integer, nullable=True)


    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'nct_id': self.nct_id,
            'start_date': self.start_date,
            'completion_date': self.completion_date,
            'study_type': self.study_type,
            'overall_status': self.overall_status,
            'brief_title': self.brief_title,
            'phase': self.phase,
            'condition_name': self.condition_name,
            'description': self.description,
            'gender': self.gender,
            'minimum_age': self.minimum_age,
            'maximum_age': self.maximum_age,
            'healthy_volunteers': self.healthy_volunteers,
            'sponsor_name': self.sponsor_name,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'completion_prob': self.completion_prob,
            'minimum_age_val': self.minimum_age_val,
            'maximum_age_val': self.maximum_age_val
        }

