import requests

def login_check_post(
    host

    ,
    # Body parameters
    username, 
    password
    ,
    # Optional body content
    optional_json_content = {}
    , headers = None
):
    final_path = "/auth"


    # Body parameters (required)
    required_body_content = {
        "username": username, 
        "password": password
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