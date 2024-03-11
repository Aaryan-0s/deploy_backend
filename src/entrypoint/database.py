

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker
SQLALCHEMY_URL = "mysql+pymysql://user:password@localhost/neuralevo"
user=[]
blog=[]
intents={
  "conversations": [
    {
      "input": "How are you?",
      "response": "Hello, thanks for asking"
    },
    {
      "input": "What can you do?",
      "response": "I can guide you through Adverse drug reaction list, Blood pressure tracking, Hospitals and Pharmacies"
    },
    {
      "input": "Find me a pharmacy",
      "response": "Please provide pharmacy name"
    },
    {
      "input": "Thanks for helping me",
      "response": "Happy to help!"
    },
    {
      "input": "Open blood pressure module",
      "response": "Navigating to Blood Pressure module"
    },
    {
      "input": "Bye",
      "response": "See you! Have a nice day"
    },
    {
      "input": "How you could help me?",
      "response": "I can guide you through Adverse drug reaction list, Blood pressure tracking, Hospitals and Pharmacies"
    },
    {
      "input": "I want to log blood pressure results",
      "response": "Navigating to Blood Pressure module"
    },
    {
      "input": "Search pharmacy",
      "response": "Please provide pharmacy name"
    },
    {
      "input": "Lookup for hospital",
      "response": "Please provide hospital name or location"
    },
    {
      "input": "Not sure I understand",
      "response": "Sorry, can't understand you"
    },
    {
      "input": "What support is offered?",
      "response": "Offering support for Adverse drug reaction, Blood pressure, Hospitals and Pharmacies"
    },
    {
      "input": "Show blood pressure results for patient",
      "response": "Please provide Patient ID"
    },
    {
      "input": "Is anyone there?",
      "response": "Hello, how can I help?"
    },
    {
      "input": "List of pharmacies nearby",
      "response": "Please provide pharmacy name"
    },
    {
      "input": "Nice chatting to you, bye",
      "response": "See you! Come back again soon."
    }
  ]
}

engine = sa.create_engine(SQLALCHEMY_URL)
Base = declarative_base()
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionFactory()

    try:
        return db
    except:
        db.rollback()

    finally:
        db.close()


# db = get_db()
# res = db.execute(sa.text("SELECT 1"))
# for i in res:
#     print(i)


