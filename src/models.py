from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.database import Base


class UrlModel(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    short_url: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    long_url: Mapped[str] = mapped_column(nullable=False)