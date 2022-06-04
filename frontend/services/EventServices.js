
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

// gets event by id
export async function getEventById(id) {
    const URL = 'http://127.0.0.1:8000/api/get/' + id.toString() + '/';
    return fetch(URL)
            .then(function(res){
                return res.json();
            })
            .catch(function(error) {
                console.log("error fetching event with id=" + id.toString() + ":" + error.message);
                throw error;
            })
}

// deletes event by id
export async function deleteEventByID(id) {
    const URL = 'http://127.0.0.1:8000/api/delete/' + id.toString() + '/';
    return fetch(URL)
            .then(function(res){
                return res.json();
            })
            .catch(function(error) {
                console.log("error deleting event with id=" + id.toString() + ":" + error.message);
                throw error;
            })
}

