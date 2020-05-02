from app import db
from app import Event

event=Event.query.get_or_404(11)
db.session.delete(event)
db.session.commit()

print (Event.query.all())