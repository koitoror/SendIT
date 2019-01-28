/*jshint esversion: 6 */

import { api } from "./api";

function getQueryParameter(key) {
    let url = new URL(window.location.href);
    return url.searchParams.get(key);
}
let parcel_id = getQueryParameter('parcel_id');
let username = localStorage.getItem("username")


api.get(`/parcels/${parcel_id}`)
.then(res => res.json())
.then(data => {
    console.log(data)
    document.getElementById("parcel-name").innerHTML = data['parcel-name'];
    document.getElementById("user").innerHTML = username;
    document.getElementById("date").innerHTML = data['created_at'];
    document.getElementById("status").innerHTML = data['status'];
})