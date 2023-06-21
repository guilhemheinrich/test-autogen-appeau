import requests

def api_parcellesdetails_listParcellesId_get_collection(
    host
    ,
    # Paths parameters
    listParcellesId

    , headers = None
):
    # build paramatered path
    final_path = "/api/parcelles/details/{listParcellesId}".format(
        listParcellesId = listParcellesId
        )


    response = requests.get(
        url = host + final_path,
        headers = headers
            )

    return response