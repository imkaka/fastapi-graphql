import graphene
import pytest
from app.schema import Mutation, Query
from graphene.test import Client
from orator import DatabaseManager, Model, Schema
from orator.migrations import DatabaseMigrationRepository, Migrator

from .fixtures import *  # noqa


@pytest.fixture(autouse=True)
def setup_database():
    DATABASES = {"sqlite": {"driver": "sqlite", "database": "test.db"}}

    db = DatabaseManager(DATABASES)
    Schema(db)

    Model.set_connection_resolver(db)

    repository = DatabaseMigrationRepository(db, "migrations")
    migrator = Migrator(repository, db)

    if not repository.repository_exists():
        repository.create_repository()

    migrator.reset("app/migrations")
    migrator.run("app/migrations")


@pytest.fixture(scope="module")
def client():
    client = Client(schema=graphene.Schema(query=Query, mutation=Mutation))
    return client
