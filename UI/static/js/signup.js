/*jshint esversion: 6 */

import { api } from './api';
const signup = document.querySelector("#myForm")
const success = document.querySelector('#success')
const warning = document.querySelector('#warning')

signup.addEventListener('submit', e =>  {
    e.preventDefault()
    const username = document.querySelector("#username").value
    const email = document.querySelector("#email").value
    const password = document.querySelector("#password").value
    const confirm = document.querySelector("#password_confirm").value

    const data = {
        username, 
        email, 
        password, 
        confirm
    }

    api.post('/auth/signup', data)
    .then(res => res.json())
    .then(data => {
        if (data.message === 'User registered successfully'){
            warning.classList.add('hide')
            success.classList.remove('hide')
            success.classList.add('show')
            success.innerHTML = data.message
            setTimeout(() =>{window.location.href = './index.html'},2000)
        }
        else{
            success.classList.add('hide')
            warning.classList.remove('hide')
            warning.classList.add('show')
            warning.innerHTML = data.warning
        }
    }) 
})
