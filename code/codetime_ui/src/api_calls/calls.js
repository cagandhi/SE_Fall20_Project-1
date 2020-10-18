const server_endpoint = "http://localhost:8000/"


export async function signup(user_cred) {


    const response = await fetch(server_endpoint + "/codetime/user/?type=signup", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            "Content-Type": "application/json"
        },
        body: JSON.stringify(user_cred)
    });

    return await response.json();

}


export async function login(user_cred) {


    const response = await fetch(server_endpoint + "/codetime/user/?type=login", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            "Content-Type": "application/json"
        },
        body: JSON.stringify(user_cred)
    });

    return await response.json();

}

export async function get_account_info(api_token) {


    const response = await fetch(server_endpoint + "/codetime/user/?api_token="+api_token, {
        method: "GET",
        headers: {
            'Accept': 'application/json',
            "Content-Type": "application/json"
        }
    });

    return await response.json();

}