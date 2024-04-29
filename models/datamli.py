class Datamli(db.Model):
    _tablename_='tbdata'

    id = db.Column(db.Integer, primary_key = True) 
    cigaretteday = db.Column(db.Integer)
    habitduration = db.Column(db.Integer)
    lungcancer=db.Column(db.Integer)

    def __init__(self, cigaretteday, habitduration,lungcancer):
        self.cigaretteday = cigaretteday
        self.habitduration = habitduration
        self.lungcancer=lungcancer
    
with app.app_context():
    db.create_all()
    
class DatamliSchema(ma.Schema):
    class Meta:
        fields = ('id','cigaretteday','habitduration','lungcancer')