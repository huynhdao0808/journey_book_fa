from app import db
from app import Event
import datetime

db.create_all()

event_1 = Event(image='CHIANGMAI.jpg', city='CHIANGMAI', country='THAILAND', description="Chiang Mai is a city in mountainous northern Thailand. Founded in 1296, it was capital of the independent Lanna Kingdom until 1558. Its Old City area still retains vestiges of walls and moats from its history as a cultural and religious center. It’s also home to hundreds of elaborate Buddhist temples, including 14th-century Wat Phra Singh and 15th-century Wat Chedi Luang, adorned with carved serpents.",date=datetime.datetime(2020,1,1))
event_2 = Event(image='PARIS.jpg', city='PARIS', country='FRANCE', description="Paris, France's capital, is a major European city and a global center for art, fashion, gastronomy and culture. Its 19th-century cityscape is crisscrossed by wide boulevards and the River Seine. Beyond such landmarks as the Eiffel Tower and the 12th-century, Gothic Notre-Dame cathedral, the city is known for its cafe culture and designer boutiques along the Rue du Faubourg Saint-Honoré.",date=datetime.datetime(2020,1,1))
event_3 = Event(image='MUNICH.jpg', city='MUNICH', country='GERMANY', description="Munich, Bavaria’s capital, is home to centuries-old buildings and numerous museums. The city is known for its annual Oktoberfest celebration and its beer halls, including the famed Hofbräuhaus, founded in 1589. In the Altstadt (Old Town), central Marienplatz square contains landmarks such as Neo-Gothic Neues Rathaus (town hall), with a popular glockenspiel show that chimes and reenacts stories from the 16th century.",date=datetime.datetime(2020,1,1))
event_4 = Event(image='ROME.jpg', city='ROME', country='ITALY', description="Rome, is the capital city and a special comune of Italy. Rome also serves as the capital of the Lazio region. With 2,879,728 residents in 1,285 km², it is also the country's most populated comune. It is the third most populous city in the European Union by population within city limits.",date=datetime.datetime(2020,1,1))

db.session.add(event_1)
db.session.add(event_2)
db.session.add(event_3)
db.session.add(event_4)

db.session.commit()