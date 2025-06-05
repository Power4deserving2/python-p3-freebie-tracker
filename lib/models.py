from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Naming convention for Alembic
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    freebies = relationship("Freebie", back_populates="company", cascade="all, delete-orphan")
    devs = relationship(
        "Dev",
        secondary="freebies",
        back_populates="companies",
        viewonly=True
    )

    def give_freebie(self, dev, item_name, value):
        return Freebie(item_name=item_name, value=value, dev=dev, company=self)

    def __repr__(self):
        return f"<Company {self.name}>"

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    freebies = relationship("Freebie", back_populates="dev", cascade="all, delete-orphan")
    companies = relationship(
        "Company",
        secondary="freebies",
        back_populates="devs",
        viewonly=True
    )

    def __repr__(self):
        return f'<Dev {self.name}>'


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)

    dev_id = Column(Integer, ForeignKey("devs.id"), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)

    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

    def __repr__(self):
        return f"<Freebie {self.item_name} (${self.value})>"