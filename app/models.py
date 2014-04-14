from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, desc
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from db import Base, session


class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    comments = relationship("Comment", backref="topic", order_by="desc(Comment.created_at)")

    @classmethod
    def create_topic(cls, title, description):
        topic = cls()
        topic.title = title
        topic.description = description
        session.add(topic)
        session.commit()
        return topic

    @classmethod
    def find_by_id(cls, topic_id):
        return session.query(cls).filter(cls.id==topic_id).first()

    @classmethod
    def recent(cls, n=10, page=0):
        return session.query(cls).order_by(desc(cls.created_at)).limit(20)

    def append_comment(self, comment):
        new_comment = Comment()
        new_comment.topic_id = self.id
        new_comment.description = comment
        session.add(new_comment)
        session.commit()
        return new_comment


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    topic_id = Column(Integer, ForeignKey('topics.id'))
