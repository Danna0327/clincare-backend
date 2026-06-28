from app.main import app


def test_cita_controller_imports():
    assert app is not None
    assert app.openapi()["info"]["title"] == "ClinCare API"