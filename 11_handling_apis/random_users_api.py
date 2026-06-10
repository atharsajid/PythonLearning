import requests

def fetch_random_users(page_no, limit = 10):
    url = f"https://api.freeapi.app/api/v1/public/randomusers?page={page_no}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        return data["data"]["data"], data["data"]["nextPage"]
    else:
        raise Exception("Failed to fetch random users at page", page_no)
    

def main():
    page_no = 1
    while True:
        index_page = (page_no - 1) * 10 
        users, next_page = fetch_random_users(page_no)
        for index, user in enumerate(users, start = 1):
            user_name = user["login"]['username']
            country = user['location']['country']
            print("-*-"*5, "\n")
            print(f"{index_page+index}. UserName: {user_name}, Country: {country}")

        if next_page:
            page_no += 1
        else:
            break


if __name__ == "__main__":
    main()    
    

