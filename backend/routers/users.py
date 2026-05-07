from fastapi import APIRouter
import requests


router = APIRouter(prefix="/api/users", tags=["Users"])


USERS_URL = "https://dummyjson.com/users"

@router.get("/")
def get_users_data():
    response = requests.get(USERS_URL).json()
    
    users = response.get("users", [])
    
    table_data = []           
    distribution_state = {}   
    distribution_university = {} 

    for u in users:
        
        table_data.append({
            "name": f"{u['firstName']} {u['lastName']}", 
            "age": u['age'],
            "gender": u['gender'],
            "image": u['image'],
            "role": u['role'],
            "state": u['address']['state'], 
            "university": u['university']
        })

        state = u['address']['state']
        
        distribution_state[state] = distribution_state.get(state, 0) + 1

        uni = u['university']
        distribution_university[uni] = distribution_university.get(uni, 0) + 1

    return {
        "users": table_data,
        "analytics": {
            "by_state": distribution_state,
            "by_university": distribution_university
        }
    }
