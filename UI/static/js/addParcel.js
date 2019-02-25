/*jshint esversion: 6 */

import { api } from './api';

const user = document.querySelector("#username")
user.innerHTML = localStorage.getItem("username")

const addParcel = document.querySelector(".myForm")
// const addParcel = document.querySelector("#myForm")
const success = document.querySelector("#success")
const warning = document.querySelector("#warning")



addParcel.addEventListener("submit", e => {
    e.preventDefault();
    const parcel_name = document.querySelector("#parcel-name").value
    const price = document.querySelector("#price").value
    const pickup_location = document.querySelector("#pickup").value
    const destination_location = document.querySelector("#destination").value
    const status = document.querySelector("#status").value

    const data = {
        parcel_name,
        price,
        pickup_location,
        destination_location,
        status
    }

    console.log(data)

    api.post("/parcels", data)
    .then(res => res.json())
    .then(data => {
        if(data.message === "Parcel added successfully"){
            warning.classList.add('hide')
            success.classList.remove('hide')
            success.classList.add('show')
            success.innerHTML = data.message
            // setTimeout(() =>{window.location.href = './profile.html'},2000)
            setTimeout(() => window.location.assign('./profile.html'), 2000)


        }else{
            success.classList.add('hide')
            warning.classList.remove('hide')
            warning.classList.add('show')
            warning.innerHTML = data.warning
        }

    })
})