from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Studies(DB.Model): 
    """Table containing records for active studies"""
    nct_id = DB.Column(DB.BigInteger, primary_key=True)
    start_date = DB.Column(DB.String(20), nullable=True)
    completion_date = DB.Column(DB.String(20), nullable=True)
    study_type = DB.Column(DB.String(20), nullable=True)
    overall_status = DB.Column(DB.String(20), nullable=True)
    brief_title = DB.Column(DB.String(1000), nullable=True)
    phase = DB.Column(DB.String(20), nullable=True)

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
           'phase': self.phase
       }

