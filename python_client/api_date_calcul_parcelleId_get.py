import requests

def api_date_calcul_parcelleId_get(
    host
    ,
    # Paths parameters
    parcelleId

    , headers = None
):
    # build paramatered path
    final_path = "/api/date_calcul/{parcelleId}".format(
        parcelleId = parcelleId
        )


    response = requests.get(
        url = host + final_path,
        headers = headers
            )

    return response