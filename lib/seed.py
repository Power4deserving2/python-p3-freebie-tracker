from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Company, Freebie

engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()

# Drop and re-create all tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create Devs
ada = Dev(name="Ada Lovelace")
grace = Dev(name="Grace Hopper")

# Create Companies
google = Company(name="Google", founding_year=1998)
openai = Company(name="OpenAI", founding_year=2015)

# Create Freebies using give_freebie method
f1 = google.give_freebie(ada, "T-shirt", 25)
f2 = google.give_freebie(grace, "Sticker Pack", 5)
f3 = openai.give_freebie(ada, "Water Bottle", 15)

# Add all to session
session.add_all([ada, grace, google, openai, f1, f2, f3])
session.commit()

print("✅ Seeded!")