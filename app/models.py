from app import db

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    file_type = db.Column(db.String(50))
    upload_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"File('{self.name}', '{self.file_type}', '{self.upload_date}')"
