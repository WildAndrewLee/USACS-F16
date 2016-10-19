from flask import Flask, render_template
from sqlalchemy import create_engine, _or
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, String, Boolean
from contextlib import contextmanager

eng = 'mysql://usacs:usacs@reticent.io:3306/usacs?charset=utf8'
engine = create_engine(eng)

results = engine.execute('my sql')

results[0]

app = Flask(__name__)

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
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    age = Column(Integer)
    gender = Column(Integer)
    right_handed = Column(Boolean)
    skill_level = Column(String)
    wins = Column(Integer)
    loses = Column(Integer)
    tournament = Column(Integer)

@app.route('/<var>')
def index(var):
    with session_factory() as sess:
        x = sess.query(Player).fetchall()

        sess.query(Player).filter(
            age>18,
            wins>5,
            tournament==5,
            or_(name='hi', name='there')
        ).join().


        sess.__engine__.exec('my sql')

        return render_template('index.html', my_variable=5, players=x)

    from flask import redirect, abort

    abort(404)

    dict(key=val)
    {
        'key': 'val'
    }

    return jsonify({
        
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242, debug=True)
