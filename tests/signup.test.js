// call sign-up module
// signUp = require('./UI/static/js/sign-up')
// signUp = require('../UI/static/dist/signup.min.js')

describe ('signs up user to send-it-ke-v2.herokuapp.com correctly', () => {
    // fake data submission
    document.body.innerHTML += `
    <form class="modal-content" id="signUp">
    
    <div id="success1" class="alert alert-success hide"></div>
    <div id="warning1" class="alert alert-warning hide"></div>
        
    <div class="form-group">
        <input type="text" id="username1" placeholder="username" value="kamar">
    </div>
    <div class="form-group">
        <input type="email" id="email" placeholder="Email" value="kamar@gmail.com">
    </div>
    <div class="form-group">
        <input type="password" id="password1" placeholder="Password" value="1234">
    </div>
    <div class="form-group">
        <input type="password" id="password_confirm" placeholder="Password" value="1234">
    </div>
    <div class="form-group">
        <button id="DoSubmission">Register</button>
    </div>
    </form>
    `;
    // end of fake submission

    // spy on window navigation
    NavSpyMock = jest.spyOn(window.location, "assign");
    NavSpyMock.mockImplementation(() => {});

it('signs up user to send-it-ke-v2.herokuapp.com correctly', async () => {
    
    // load the window
    require('../UI/static/dist/signup.min')

    // fake fetch
    Mock = jest.spyOn(global, 'fetch');
    Mock.mockImplementation(() => Promise.resolve({
    
    json: () => Promise.resolve({"message": "User registered successfully"})
    }))
  
    document.getElementById('DoSubmission').click();
    expect(Mock).toHaveBeenCalledTimes(1);
    const Fetch = Mock.mock.calls[0];
    expect(Fetch[0]).toBe('https://send-it-ke-v2.herokuapp.com/api/v2/auth/signup');
    expect(Fetch[1]).toEqual({
      method: "POST",
      mode: "cors",
      headers: {
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Origin": "<origin> | *",
        "content-type": "application/json",
        "x-access-token": null,
      },
      body: JSON.stringify({
          username: 'kamar',
          email: 'kamar@gmail.com',
          password: '1234',
          confirm: '1234'
      })
    });
    // wait for  the promise to resolve
    await Promise.resolve().then();
    expect(document.getElementById('success1').innerHTML).toBe('User registered successfully');
  });
});

it('Prevents duplicate registration', async () => {

    // restore mock to initial state
    Mock.mockRestore();
    NavSpyMock.mockRestore();
    jest.resetModules();

    // mock fake fetch
    Mock = jest.spyOn(global, 'fetch');
    Mock.mockImplementation(() => Promise.resolve({
    
    json: () => Promise.resolve({"warning" : "Email exists, please login or register with another email"})
    }))
    document.getElementById('username1').value = '@@#BadVeryB@d';
    document.getElementById('DoSubmission').click();
    expect(Mock).toHaveBeenCalledTimes(1);
    const Fetch = Mock.mock.calls[0];
    expect(Fetch[0]).toBe('https://send-it-ke-v2.herokuapp.com/api/v2/auth/signup');
    expect(Fetch[1]).toEqual({
      method: "POST",
      mode: "cors",
      headers: {
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Origin": "<origin> | *",
        "content-type": "application/json",
        "x-access-token": null,
      },
      body: JSON.stringify({
          username: '@@#BadVeryB@d',
          email: 'kamar@gmail.com',
          password: '1234',
          confirm: '1234'
          
          
      })
    });
    // wait for  the promise to resolve
    await Promise.resolve().then();
    expect(document.getElementById('warning1').innerHTML).toBe('Email exists, please login or register with another email');

})
    
it('User signs up with incorrect email', async () => {
    // restore mock to initial state
    Mock.mockRestore();
    NavSpyMock.mockRestore();
    jest.resetModules();

    // mock fake fetch
    Mock = jest.spyOn(global, 'fetch');
    Mock.mockImplementation(() => Promise.resolve({
    
    json: () => Promise.resolve({"warning": "Enter a valid email address"})
    }))
    document.getElementById('email').value = 'thisIsnotanEmail';
    document.getElementById('DoSubmission').click();
    expect(Mock).toHaveBeenCalledTimes(1);
    const Fetch = Mock.mock.calls[0];
    expect(Fetch[0]).toBe('https://send-it-ke-v2.herokuapp.com/api/v2/auth/signup');
    expect(Fetch[1]).toEqual({
      method: "POST",
      mode: "cors",
      headers: {
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Origin": "<origin> | *",
        "content-type": "application/json",
        "x-access-token": null,
      },
      body: JSON.stringify({
          username: '@@#BadVeryB@d',
          email: 'thisIsnotanEmail',
          password: '1234',
          confirm: '1234'
      })
    });
    // wait for  the promise to resolve
    await Promise.resolve().then();
    expect(document.getElementById('warning1').innerHTML).toBe('Enter a valid email address');

})

it('Notify user for any reason they are not able to sign-up like invalid email', async () => {
    // restore mock to initial state
    Mock.mockRestore();
    NavSpyMock.mockRestore();
    jest.resetModules();

    // mock fake fetch
    Mock = jest.spyOn(global, 'fetch');
    Mock.mockImplementation(() => Promise.resolve({
    
    json: () => Promise.resolve({"warning": "email is a required field"})
    }))
    document.getElementById('email').value = '';
    document.getElementById('DoSubmission').click();
    expect(Mock).toHaveBeenCalledTimes(1);
    const Fetch = Mock.mock.calls[0];
    expect(Fetch[0]).toBe('https://send-it-ke-v2.herokuapp.com/api/v2/auth/signup');
    expect(Fetch[1]).toEqual({
      method: "POST",
      mode: "cors",
      headers: {
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Origin": "<origin> | *",
        "content-type": "application/json",
        "x-access-token": null,
      },
      body: JSON.stringify({
          username: '@@#BadVeryB@d',
          email: '',
          password: '1234',
          confirm: '1234'
      })
    });
    // wait for  the promise to resolve
    await Promise.resolve().then();
    expect(document.getElementById('warning1').innerHTML).toBe('email is a required field');

})

it('User signs with incorrect username', async () => {
    // restore mock to initial state
    Mock.mockRestore();
    NavSpyMock.mockRestore();
    jest.resetModules();

    // mock fake fetch
    Mock = jest.spyOn(global, 'fetch');
    Mock.mockImplementation(() => Promise.resolve({
    
    json: () => Promise.resolve({"warning": "Enter a valid username"})
    }))
    document.getElementById('username1').value = '$$bad';
    document.getElementById('email').value = 'kamar@gmail.com';
    document.getElementById('DoSubmission').click();
    expect(Mock).toHaveBeenCalledTimes(1);
    const Fetch = Mock.mock.calls[0];
    expect(Fetch[0]).toBe('https://send-it-ke-v2.herokuapp.com/api/v2/auth/signup');
    expect(Fetch[1]).toEqual({
      method: "POST",
      mode: "cors",
      headers: {
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Origin": "<origin> | *",
        "content-type": "application/json",
        "x-access-token": null,
      },
      body: JSON.stringify({
          username: '$$bad',
          email: 'kamar@gmail.com',
          password: '1234',
          confirm: '1234'
      })
    });
    // wait for  the promise to resolve
    await Promise.resolve().then();
    expect(document.getElementById('warning1').innerHTML).toBe('Enter a valid username');

})
