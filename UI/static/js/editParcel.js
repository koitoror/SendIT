/*jshint esversion: 6 */

import { api } from "./api";

function getQueryParameter(key) {
    let url = new URL(window.location.href);
    return url.searchParams.get(key);
}
let parcelId = getQueryParameter(parcel_id);

api.get(`/parcels/${parcelId}`)
.then(res => res.json())
.then(data => {
    console.log(data);
    document.getElementById("parcel-name").value = data['parcel-name'];
    document.getElementById("status").value = data['status'];
});

const success = document.querySelector("#success");
const warning = document.querySelector("#warning");

const form = document.querySelector("#editForm");

form.addEventListener("submit", e =>{
    e.preventDefault();
    let parcel_name = document.getElementById("parcel-name").value;
    let status = document.getElementById("status").value;

    const data = {
        parcel_name,
        status
    };
    
    api.update(`/parcels/${parcelId}`, data)
    .then(res => res.json())
    .then(data => {
        if(data.message == "Updated successfully"){
            warning.classList.add('hide');
            success.classList.remove('hide');
            success.classList.add('show');
            success.innerHTML = data.message;
            setTimeout(() =>{window.location.href = './dashboard.html';},2000);
        }else{
            success.classList.add('hide');
            warning.classList.remove('hide');
            warning.classList.add('show');
            warning.innerHTML = data.warning;
        }
        
    });
});
