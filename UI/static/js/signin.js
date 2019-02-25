/*jshint esversion: 6 */

import { api } from './api'

// export const signI = () => {
const signin = document.querySelector("#signIn")
const success = document.querySelector("#success")
const warning = document.querySelector("#warning")
signin.addEventListener('submit', e =>  {
    e.preventDefault()
    signin.classList.add("loading");
    const username = document.querySelector("#username").value
    const password = document.querySelector("#password").value

    const data = {
        username,  
        password, 
    }

    api.post('/auth/login', data)
    .then(res => res.json())
    .then(data => {
        signin.classList.remove("loading");
        if (data.admin == true){
            localStorage.setItem("token", data.token)
            localStorage.setItem("username", username)
            localStorage.setItem("user_id", data.user_id)
            warning.classList.add('hide')
            success.classList.remove('hide')
            success.classList.add('show')
            success.innerHTML = data.message
            // setTimeout(() =>{window.location.href = './dashboard.html'}, 2000)
            setTimeout(() => window.location.assign('./dashboard.html'), 2000)

        }
        else if (data.admin == false){
            localStorage.setItem("token", data.token)
            localStorage.setItem("username", username)
            localStorage.setItem("user_id", data.user_id)
            warning.classList.add('hide')
            success.classList.remove('hide')
            success.classList.add('show')
            success.innerHTML = data.message
            // setTimeout(() =>{window.location.href = './profile.html'}, 2000)
            setTimeout(() => window.location.assign('./profile.html'), 2000)

        }
        else{
            success.classList.add('hide')
            warning.classList.remove('hide')
            warning.classList.add('show')
            warning.innerHTML = data.warning
        }
    } )
})
// }

// module.exports = signIn