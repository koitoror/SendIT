/*jshint esversion: 6 */

import { api } from './api'

function loadParcels(){
    let table = document.querySelector("#table")
    table.classList.add("loading");
    api.get("/parcels")
    .then(res => res.json())
    .then(data => {
        let user = document.querySelector("#username")
        let noOfParcels = document.querySelector("#parcels");
        let view = document.querySelector("#view")
        user.innerHTML = localStorage.getItem("username");

        table.classList.remove("loading");

        let i = data.length
        if(i > 0) {
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
                        <button class="button button2 float-right"> 
                            <a href="editOrderStatus.html?id=${parcel.parcel_id}" onclick="document.getElementById('id03').style.display='block'" style="width:auto;">EDIT <i class="fa fa-edit"></i></a>
                        </button>
                        
                    </td>
                    <td>${parcel.pickup_location}</td>
                    <td>${parcel.present_location}
                        <button class="button button2 float-right"> 
                            <a href="editOrderPresentLocation.html?id=${parcel.parcel_id}" onclick="document.getElementById('id04').style.display='block'" style="width:auto;">EDIT <i class="fa fa-edit"></i></a>
                        </button>
                    </td>
                        
                    <td id="destination_location">${parcel.destination_location}</td>        
                    </tr>`
                rows += tr
            

                // let td = document.createElement('td');
                // let link = document.createElement('a');
                // link.innerHTML = "Present";
                // link.classList.add('button');
                // link.classList.add("button2");
                // link.classList.add("float-right");
                
                // link.addEventListener("click", () => {
                //     let present_location = document.getElementById("present_location").value;
                //     let status = document.getElementById("status").value;

                //     const data = {
                //         present_location,
                //         status
                //     };

                //     editPresent(parcel.parcel_id, data);
                // });
                // td.appendChild(link);
                // tr.appendChild(td);

                                
                // let td0 = document.createElement('td');
                // let link0 = document.createElement('a');
                // link0.innerHTML = "Status";
                // link0.classList.add('button');
                // link0.classList.add("button2");
                // link0.classList.add("float-right");
                
                // link0.addEventListener("click", () => {
                //     let present_location = document.getElementById("present_location").value;
                //     let status = document.getElementById("status").value;

                //     const data = {
                //         present_location,
                //         status
                //     };
                    
                //     changeStatus(parcel.parcel_id, data);
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

        }else if (i = 0) {
            console.log(i)
            table.innerHTML = "";
            noOfParcels.innerHTML = 0;
            view.classList.add("alert", "alert-warning")
            view.innerHTML = "No parcels found"

        }
    })

}

window.addEventListener("load", ()=>{
   loadParcels()
})


// function editPresent(parcel_id, data){
//     if ( confirm("Do you want to edit this parcel?")){
//         api.update(`/parcels/${parcel_id}/presentLocation`, data)
//         .then(res => res.json())
//         .then(data => {
//             let info = document.getElementById("info")
//             info.classList.add("alert", "alert-success")
//             info.innerHTML = data.message
//             info.style.display = "block"

//             setTimeout(() => {
//                 info.style.display = ""
//                 loadParcels()
//             }, 2000)

//             setTimeout(() =>{window.location.href = './dashboard.html'},4000)

//         })
//     }
// }

// function changeStatus(parcel_id, data){
//     if ( confirm("Do you want to edit this parcel?")){
//         api.update(`/parcels/${parcel_id}/status`, data)
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

//             setTimeout(() =>{window.location.href = './dashboard.html'},4000)

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
            }, 2000)

            setTimeout(() =>{window.location.href = './dashboard.html'},4000)

        })
    }
}


