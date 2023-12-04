from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Приветствую тебя!"}
    
def test_read_predict():
    response = client.post("/predict/",
        json={"input": "Россия – великая страна и только ленивый не знает историю ее возникновения, развития и становления. Она занимает площадь около 17 миллионов километров. Расположилась страна в Северном полушарии и большая часть материка Евразии принадлежит именно ей. У России общие границы с восемнадцатью странами, в том числе и по морю. В море мы граничим с США и Японией."}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data[0] == 'Когда находится Россия?'
