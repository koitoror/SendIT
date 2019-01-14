/*jshint esversion: 6 */

import { api } from './api';

function loadParcels(){
    let table = document.querySelector("#table");
    table.classList.add("loading");
    api.get("/parcels")
    // api.get("/users/<int:id>/parcels")
    .then(res => res.json()
    .then(data => {
        let user = document.querySelector("#username");
        let admin = document.querySelector("#admin");
        let noOfParcels = document.querySelector("#parcels");
        let view = document.querySelector("#view");
        user.innerHTML = localStorage.getItem("username");
        admin.innerHTML = localStorage.getItem("admin");

        table.classList.remove("loading");
        table.classList.add("dashboard")
        if(data.parcels){
            noOfParcels.innerHTML = data.parcels.length;
            let rows = `<tr>
                <th>Checkbox</th>
                <th>User ID</th>                
                <th>Order ID</th>
                <th>Parcel Name</th>         
                <th>Price</th>
                <th>Date Ordered</th>
                <th>Order Status</th>
                <th>Cancel Order</th>
                <th>PickUp Location</th>    
                <th>Present Location</th>
                <th>Destination</th>
                <th>Date Modified</th>
                <th></th>

                </tr>`;
            table.innerHTML = rows;
            for (let parcel of data.parcels){

                let tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><input type="checkbox"/></td>
                    <td>${parcel.user_id}</td>
                    <td>${parcel.parcel_id}</td>
                    <td>${parcel.parcel_name}</td>
                    <td>${parcel.price}</td>
                    <td>${parcel.date_ordered}</td>
                    <td>${parcel.status}</td>
                    <td>${parcel.cancel_order}</td>
                    <td>${parcel.pickup_location}</td>
                    <td>${parcel.present_location}</td>
                    <td>${parcel.destination_location}</td>
                    <td>${parcel.date_modified}</td>

                    </tr>`;
                rows += tr;
            

                let td = document.createElement('td');
                let link = document.createElement('a');
                link.innerHTML = "Delete";
                link.classList.add('button');
                link.classList.add("button1");
                link.classList.add("float-right");
                
                link.addEventListener("click", ()=>{
                    deleteParcel(parcel.parcel_id);
                });
                td.appendChild(link);
                tr.appendChild(td);

                table.appendChild(tr);
        }

        }else{
            table.innerHTML = "";
            noOfParcels.innerHTML = 0;
            view.classList.add("alert", "alert-warning");
            view.innerHTML = "No parcels found";

        }
    })

}
window.addEventListener("load", ()=>{
   loadParcels();
});
function deleteParcel(parcel_id){
    if ( confirm("Do you want to delete this parcel?")){
        api.delete(`/parcels/${parcel_id}`)
        .then(res => res.json())
        .then(data => {
            let info = document.getElementById("info");
            info.classList.add("alert", "alert-success");
            info.innerHTML = data.message;
            info.style.display = "block";

            setTimeout(function(){
                info.style.display = "";
                loadParcels();
            }, 1000);
        });
    }
}


