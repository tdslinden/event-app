
// gets all event objects from api
export async function getAllEventObjects() {
    const URL = 'http://127.0.0.1:8000/api/';
    return fetch(URL)
            .then(function(res){
                return res.json();
            })
            .catch(function(error) {
                console.log("error fetching all events: " + error.message);
                throw error;
            })
}