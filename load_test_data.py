from generic import db
from generic import User
joe = User('joe', 'joe@mejoe.com', 'admin')
guest = User('guest', 'guest@mejoe.com', 'guest')
cecilia = User('cecilia', 'cecilia@mejoe.com', 'user')

db.session.add(joe)
db.session.add(guest)
db.session.add(cecilia)
db.session.commit()