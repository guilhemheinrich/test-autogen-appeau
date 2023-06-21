import requests

def api_parcelles_id_patch(
    host
    ,
    # Paths parameters
    id

    ,
    # Optional body content
    optional_json_content = {}
    , headers = None
):
    # build paramatered path
    final_path = "/api/parcelles/{id}".format(
        id = id
        )



    json_content = {
            **optional_json_content
        }

    response = requests.patch(
        url = host + final_path,
        headers = headers
                ,
        json = json_content
    )

    return response