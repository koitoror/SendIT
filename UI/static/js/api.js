/*jshint esversion: 6 */

const uri = 'https://send-it-ke-v2.herokuapp.com/api/v2'
// const uri = 'http://127.0.0.1:5000/api/v2'

export const api = {
    post(endpoint, data) {
        return fetch(`${uri}${endpoint}`, {
            method: 'POST',
            body: JSON.stringify(data),
            mode: 'cors',
            headers: {
                "x-access-token": localStorage.getItem("token"),
                "content-type": "application/json",
                'Access-Control-Allow-Origin': '<origin> | *',
                'Access-Control-Allow-Credentials': 'true'
            }
        })
    },

    update(endpoint, data = null) {
        return fetch(`${uri}${endpoint}`, {
            method: 'PUT',
            body: JSON.stringify(data),
            mode: 'cors',
            headers: {
                "x-access-token": localStorage.getItem("token"),
                "content-type": "application/json",
                'Access-Control-Allow-Origin': '<origin> | *',
                'Access-Control-Allow-Credentials': 'true'
            }
        })
    },

    get(endpoint) {
        return fetch(`${uri}${endpoint}`, {
            method: 'GET',
            mode: 'cors',
            headers: {
                "x-access-token": localStorage.getItem("token"),
                "content-type": "application/json",
                'Access-Control-Allow-Origin': '<origin> | *',
                'Access-Control-Allow-Credentials': 'true'
            }
        })
    },

    delete(endpoint) {
        return fetch(`${uri}${endpoint}`, {
            method: 'DELETE',
            mode: 'cors',
            headers: {
                "x-access-token": localStorage.getItem("token"),
                "content-type": "application/json",
                'Access-Control-Allow-Origin': '<origin> | *',
                'Access-Control-Allow-Credentials': 'true'
            }
        })
    }
}