import requests

def api_parcelles_parcelleIdresultat_dateDebut_dateFin_get_collection(
    host
    ,
    # Paths parameters
    parcelleId, 
    dateDebut, 
    dateFin

    , headers = None
):
    # build paramatered path
    final_path = "/api/parcelles/{parcelleId}/resultat/{dateDebut}/{dateFin}".format(
        parcelleId = parcelleId, 
        dateDebut = dateDebut, 
        dateFin = dateFin
        )


    response = requests.get(
        url = host + final_path,
        headers = headers
            )

    return response