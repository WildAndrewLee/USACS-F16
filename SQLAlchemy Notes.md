When using SQLAlchemy, you should be utilizing sessions and transactions. The following is some example code for doing that:
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

# secrets is not included with Python and is my own creation. All you need to do is know that it's used
# to fill in the blanks when initializing __eng__.
from secrets import secrets

# Creating the engine performs the actual database connection.
eng = 'mysql://{username}:{password}@{host}:3307/{name}?charset=utf8'.format(**secrets.db.__dict__)
engine = create_engine(
	eng, pool_recycle=600 # pool_recycle is the delay before throwing away old connections and making new ones. Avoids "mysql has gone away"
)

factory = sessionmaker(bind=engine)
Session = scoped_session(factory)
BaseModel = declarative_base()

# Context manager allows for "with". Check out: http://preshing.com/20110920/the-python-with-statement-by-example/
@contextmanager
def session_factory():
	s = Session()

	try:
		yield s
		s.commit()
	except:
		s.rollback()
		raise
	finally:
		s.close()
        
class Player(BaseModel):
    ...

with session_factory() as sess:
    x = sess.query(Player).one()
    x.name = 'abc'
    sess.merge(x)
    sess.execute('SELECT * FROM players WHERE name="abc"')
```
When you use sessions like this, any errors that occur will cause a transaction to abort and be rollbacked. Sessions are useful because you can make sure everything is ok before actually saving your changes to the database.