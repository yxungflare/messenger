import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import JSON, TIMESTAMP, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(
        Integer, unique=True, primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String(length=150), nullable=False
    )
    permission: Mapped[TIMESTAMP] = mapped_column(
        JSON, nullable=False
    )


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(
        Integer, unique=True, primary_key=True
    )
    username: Mapped[str] = mapped_column(
        String(length=150), unique=True, nullable=False
    )
    registreted_date: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, default=datetime.datetime.utcnow
    )
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('role.id')
    )
    email: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=False
        )
    hashed_password: Mapped[str] = mapped_column(
            String(length=1024), nullable=False
        )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
    is_verified: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )