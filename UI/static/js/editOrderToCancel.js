/*jshint esversion: 6 */

import { api } from "./api";

function getQueryParameter(key) {
    let url = new URL(window.location.href);
    return url.searchParams.get(key);
}
let parcel_id = getQueryParameter('id');

api.get(`/parcels/${parcel_id}`)
.then(res => res.json())
.then(data => {
    document.getElementById("parcel-name").value = data['parcel_name'];
    document.getElementById("status").value = data['status'];

});

const success = document.querySelector("#success");
const warning = document.querySelector("#warning");

const form = document.querySelector("#editForm");

let user = document.querySelector("#username")
user.innerHTML = localStorage.getItem("username");


form.addEventListener("submit", e =>{
    e.preventDefault();
    let parcel_name = document.getElementById("parcel-name").value;
    // let status = document.getElementById("status").value;
    let status = "CANCELED";

    const data = {
        parcel_name,
        status
    };
    
    api.update(`/parcels/${parcel_id}/cancel`, data)
    .then(res => res.json())
    .then(data => {
        if(data.message == "Order canceled successfully"){
            warning.classList.add('hide');
            success.classList.remove('hide');
            success.classList.add('show');
            success.innerHTML = data.message;
            setTimeout(() =>{window.location.href = './profile.html';},2000);
        }else{
            success.classList.add('hide');
            warning.classList.remove('hide');
            warning.classList.add('show');
            warning.innerHTML = data.message;
        }
        
    });
});
