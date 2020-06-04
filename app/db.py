from sqlalchemy import create_engine, Column, String, Integer, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import hashlib

engine = create_engine('sqlite:///shimerundesu.db', connect_args={"check_same_thread": False}) #違うスレッドからもアクセスできるようにする
Base = declarative_base()

#与えられた文字列をハッシュ化
def hash(password): return str(hashlib.sha256(password.strip().encode("utf-8")).digest())

#データの構造
class User(Base):
    __tablename__ = 'users'
    name = Column(String, primary_key=True, unique=True)
    password = Column(String)
    email = Column(String)

    def __repr__(self):
        return "User<{}, {}, {}>".format(self.name, self.password)


Base.metadata.create_all(engine)
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()


if __name__ == "__main__":
    #データベース作成処理。このファイルを直接実行すればデータベースを作成可能
    user1 = User(name="AAA", password=hash("AAA"), email="AAA@gmail.com")
    user2 = User(name="BBB", password=hash("BBB"), email="BBB@gmail.com")
    user3 = User(name="CCC", password=hash("CCC"), email="CCC@gmail.com")
    user4 = User(name="DDD", password=hash("DDD"), email="DDD@gmail.com")
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)
    session.commit()