import sys


sys.path.append('D:\\jib\\crud')
import pytest
import sys
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from src.entrypoint.database import Base, get_db
from src.entrypoint.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"

# Create an engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Create a sessionmaker
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

# Override get_db function in the app
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create a test client
client = TestClient(app)

# Fixture to drop the table after all tests have finished
@pytest.fixture(scope="session", autouse=True)
def drop_table():
  """
  Fixture that drops the database table after the test session is complete.
  """
  yield  
  Base.metadata.drop_all(bind=engine)

# Tests
def test_crud_post():
    data = {"username": "test_user"}
    response = client.post("/api/v1/crud/add", json=data)
    assert response.status_code == 200
    assert response.json() == "added successfully"

def test_crud_get():
    response = client.get("/api/v1/crud/get?index=1")
    assert response.status_code == 200
    assert response.json() is not None

def test_crud_getAll():
    response = client.get("/api/v1/crud/getAll")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_crud_put():
  """
  Test case for updating a resource using the PUT method.

  This test sends a PUT request to the '/api/v1/crud/update' endpoint with a JSON payload
  containing the updated username. It asserts that the response status code is 200 and
  the response JSON is equal to "updated successfully".
  """
  data = {"username": "updated_user"}
  response = client.put("/api/v1/crud/update?index=1", json=data)
  assert response.status_code == 200
  assert response.json() == "updated successfully"

def test_crud_delete():
    response = client.delete("/api/v1/crud/delete?index=1")
    assert response.status_code == 200
    assert response.json() == "deleted successfully"
