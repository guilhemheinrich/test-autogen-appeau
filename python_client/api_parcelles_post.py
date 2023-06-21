import requests

def api_parcelles_post(
    host

    ,
    # Body parameters
    id, 
    nom, 
    latitude, 
    longitude, 
    parametres
    ,
    # Optional body content
    optional_json_content = {}
    , headers = None
):
    final_path = "/api/parcelles"


    # Body parameters (required)
    required_body_content = {
        "id": id, 
        "nom": nom, 
        "latitude": latitude, 
        "longitude": longitude, 
        "parametres": parametres
    }

    json_content = {
            **optional_json_content
            ,
            **required_body_content
        }

    response = requests.post(
        url = host + final_path,
        headers = headers
                ,
        json = json_content
    )

    return response