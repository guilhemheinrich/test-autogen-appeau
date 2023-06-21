import requests

def api_parcellesmulti_listParcellesIdresultat_dateDebut_dateFin_get_collection(
    host
    ,
    # Paths parameters
    listParcellesId, 
    dateDebut, 
    dateFin

    , headers = None
):
    # build paramatered path
    final_path = "/api/parcelles/multi/{listParcellesId}/resultat/{dateDebut}/{dateFin}".format(
        listParcellesId = listParcellesId, 
        dateDebut = dateDebut, 
        dateFin = dateFin
        )


    response = requests.get(
        url = host + final_path,
        headers = headers
            )

    return response