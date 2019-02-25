/*jshint esversion: 6 */

import { api } from './api'

function loadParcels(){
    let table = document.querySelector("#table")
    table.classList.add("loading");
    let user_id = localStorage.getItem("user_id");
    api.get(`/users/${user_id}/parcels`)
    .then(res => res.json())
    .then(data => {
        let user = document.querySelector("#username")
        let noOfParcels = document.querySelector("#parcels");
        let view = document.querySelector("#view")
        user.innerHTML = localStorage.getItem("username");

        table.classList.remove("loading");

        let i = data.length

        if(data) {
            noOfParcels.innerHTML = i
            let rows = `<tr class="table">
                <th>#</th>
                <th>User ID</th>                
                <th>Order ID</th>
                <th>Parcel Name</th>         
                <th>Price</th>
                <th>Date Ordered</th>
                <th>Order Status</th>
                <th>PickUp Location</th>    
                <th>Present Location</th>
                <th>Destination</th>
             
                
                
                </tr>`
            table.innerHTML = rows
            for (let parcel of data){
            
                let tr = document.createElement('tr');
                tr.innerHTML = `<td><input type="checkbox"/></td>
                    <td>${parcel.user_id}</td>
                    <td>${parcel.parcel_id}</td>
                    <td>${parcel.parcel_name}</td>
                    <td>${parcel.price}</td>
                    <td>${parcel.date_ordered}</td>
                    <td>${parcel.status}
                        <button class="button button1 float-right"> 
                            <a href="editOrderToCancel.html?id=${parcel.parcel_id}">CANCEL <i class="fa fa-times-circle""></i></a>
                        </button>
                    </td>
                    <td>${parcel.pickup_location}</td>
                    <td>${parcel.present_location}</td>
                    <td>${parcel.destination_location}
                        <button class="button button2 float-right"> 
                            <a href="editOrderDestination.html?id=${parcel.parcel_id}">EDIT <i class="fa fa-edit"></i></a>
                        </button>
                    </td>
                    </tr>`
                rows += tr

                
                // let td = document.createElement('td');
                // let link = document.createElement('a');
                // link.innerHTML = "Edit";
                // link.classList.add('button');
                // link.classList.add("button2");
                // link.classList.add("float-right");
                
                // link.addEventListener("click", () => {
                //     let destination_location = document.getElementById("destination_location").value;
                //     let status = document.getElementById("status").value;

                //     const data = {
                //         destination_location,
                //         status
                //     };
                    
                //     editDestination(parcel.parcel_id, data);
                // });
                // td.appendChild(link);
                // tr.appendChild(td);

                
                // let td0 = document.createElement('td');
                // let link0 = document.createElement('a');
                // link0.innerHTML = "Cancel";
                // link0.classList.add('button');
                // link0.classList.add("button2");
                // link0.classList.add("float-right");
                
                // link0.addEventListener("click", () => {
                //     let destination_location = document.getElementById("destination_location").value;
                //     let status = "CANCELED";

                //     const data = {
                //         destination_location,
                //         status
                //     };
                    
                //     cancelOrder(parcel.parcel_id, data);
                // });
                // td0.appendChild(link0);
                // tr.appendChild(td0);


                let td1 = document.createElement('td');
                let link1 = document.createElement('a');
                link1.innerHTML = "Delete";
                link1.classList.add('button');
                link1.classList.add("button1");
                link1.classList.add("float-right");
                
                link1.addEventListener("click", () => {

                    deleteParcel(parcel.parcel_id);
                });
                td1.appendChild(link1);
                tr.appendChild(td1);

                table.appendChild(tr);            
        }

        }else{
            table.innerHTML = "";
            noOfParcels.innerHTML = 0;
            view.classList.add("alert", "alert-warning")
            view.innerHTML = "No parcels found"

        }
    })

}

window.addEventListener("load", ()=> {
   loadParcels()
})


// function cancelOrder(parcel_id, data){
//     if ( confirm("Do you want to edit this parcel?")){
//         api.update(`/parcels/${parcel_id}/cancel`, data)
//         .then(res => res.json())
//         .then(data => {
//             let info1 = document.getElementById("info1")
//             info1.classList.add("alert", "alert-success")
//             info1.innerHTML = data.message
//             info1.style.display = "block"

//             setTimeout(() =>{
//                 info1.style.display = ""
//                 loadParcels()
//             }, 2000)

//             setTimeout(() =>{window.location.href = './profile.html'},4000)

//         })
//     }
// }

// function editDestination(parcel_id, data){
//     if ( confirm("Do you want to edit this parcel?")){
//         api.update(`/parcels/${parcel_id}/destination`, data)
//         .then(res => res.json())
//         .then(data => {
//             let info = document.getElementById("info")
//             info.classList.add("alert", "alert-success")
//             info.innerHTML = data.message
//             info.style.display = "block"

//             setTimeout(()=> {
//                 info.style.display = ""
//                 loadParcels()
//             }, 4000)

//             setTimeout(() =>{window.location.href = './profile.html'},6000)

//         })
//     }
// }

function deleteParcel(parcel_id){
    if ( confirm("Do you want to delete this parcel?")){
        api.delete(`/parcels/${parcel_id}`)
        .then(res => res.json())
        .then(data => {
            let info = document.getElementById("info")
            info.classList.add("alert", "alert-success")
            info.innerHTML = data.message
            info.style.display = "block"

            setTimeout(() => {
                info.style.display = ""
                loadParcels()
            }, 1000)
        })
    }
}


