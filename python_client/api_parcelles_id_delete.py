import requests

def api_parcelles_id_delete(
    host
    ,
    # Paths parameters
    id

    , headers = None
):
    # build paramatered path
    final_path = "/api/parcelles/{id}".format(
        id = id
        )


    response = requests.delete(
        url = host + final_path,
        headers = headers
            )

    return response