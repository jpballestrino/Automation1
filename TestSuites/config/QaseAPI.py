import requests


# API token: "154f61512d2aff33141c7ca96aea23bf2623b3cb"

def delete_test_run(project,id):
    url = "https://api.qase.io/v1/run/"+project+"/"+str(id)

    headers = {
        "Accept": "application/json",
        "Token": "154f61512d2aff33141c7ca96aea23bf2623b3cb"
    }

    response = requests.delete(url, headers=headers)

    print(response.text)

def create_test_run(title,
                    description,
                    project_code,lista_test_cases,environment_id) -> None:
    url = "https://api.qase.io/v1/run/"+project_code
    print(url)

    payload = {
        "cases": lista_test_cases,
        "title": title,
        "description": description,
        "include_all_cases": False,
        "tags": ["Prueba_Automatizada"],
        "environment_id": environment_id,
        "is_autotest": True
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Token": "154f61512d2aff33141c7ca96aea23bf2623b3cb"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)


def actualizar_state(project_code,status_test,case_id,run_id):
    url = "https://api.qase.io/v1/result/"+project_code+"/"+run_id

    payload = {
        "status": status_test,
        "case_id": case_id,
        "comment": "Este test case fallo"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Token": "154f61512d2aff33141c7ca96aea23bf2623b3cb"
    }

    response = requests.post(url, json=payload, headers=headers)


def get_id_of_active_run(project_code):
    url = "https://api.qase.io/v1/run/"+project_code+"?status=active&limit=10&offset=0"

    headers = {
        "Accept": "application/json",
        "Token": "154f61512d2aff33141c7ca96aea23bf2623b3cb"
    }

    response = requests.request("GET",url, headers=headers)

    return str(response.json()["result"]["entities"][0]["id"])