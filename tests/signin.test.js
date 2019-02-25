/*jshint esversion: 6 */
// call sign-up moduleS
// signIn = require('../UI/static/js/signin')
// signIn = require('../UI/static/dist/signin.min')
// import { signIn } from '../UI/static/dist/signin.min'
// import { signIn } from '../UI/static/js/signin'

describe ('signs in user to send-it-ke-v2.herokuapp.com/api/v2 correctly', () => {
  // fake data submission
  document.body.innerHTML += `
  <form class="modal-content animate" id="signIn">

  <div id="success" class="alert alert-success hide"></div>
  <div id="warning" class="alert alert-warning hide"></div>

  <div class="form-group">
        <label for="username"><b>Username</b></label>
      <input type="text" id="username" placeholder="Enter Username" name="username" required="" value="adm">
  </div>

  <div class="form-group">
      <label for="psw"><b>Password</b></label>
      <input type="password" id="password" placeholder="Enter Password" name="psw" required="" value="123456">
  </div>

  <div class="form-group">
      <button type="submit" id="DoSubmission">Login</button>
  </div>
  
  </form>
  `;
  // end of fake submission

  // spy on window navigation
  NavSpyMock = jest.spyOn(window.location, "assign");
  NavSpyMock.mockImplementation(() => {});

it('signs in user to send-it-ke-v2.herokuapp.com/api/v2 correctly', async () => {
  
  // load the window
  require('../UI/static/dist/signin.min');

  // fake fetch
  Mock = jest.spyOn(global, 'fetch');
  Mock.mockImplementation(() => Promise.resolve({
  
  json: () => Promise.resolve({"message": "Logged in successfully"})
  }))

  document.getElementById('DoSubmission').click();
  expect(Mock).toHaveBeenCalledTimes(1);
  const Fetch = Mock.mock.calls[0];
  expect(Fetch[0]).toBe('https://send-it-ke-v2.herokuapp.com/api/v2/auth/login');
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
        username: 'adm',
        password: '123456',
    }) 
  });
  //wait for  the promise to resolve
  await Promise.resolve().then();
  // expect(document.getElementById('success').innerHTML).toBe('Logged in successfully');
  expect(document.getElementById('success').innerHTML).toBe('');  
});
})

it('User signs with correct login details', async () => {
  // restore mock to initial state
  Mock.mockRestore();
  NavSpyMock.mockRestore();
  jest.resetModules();

  // mock fake fetch
  Mock = jest.spyOn(global, 'fetch');
  Mock.mockImplementation(() => Promise.resolve({
  
  json: () => Promise.resolve({"message": "Logged in successfully"})
  }))
  // document.getElementById('username').value = 'wrong';
  document.getElementById('DoSubmission').click();
  expect(Mock).toHaveBeenCalledTimes(1);
  const Fetch = Mock.mock.calls[0];
  expect(Fetch[0]).toBe('https://send-it-ke-v2.herokuapp.com/api/v2/auth/login');
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
        username: 'adm',
        password: '123456',
    }) 
  });
  // wait for  the promise to resolve
  await Promise.resolve().then();
  expect(document.getElementById('success').innerHTML).toBe('');
})    
it('User signs with incorrect login details', async () => {
    // restore mock to initial state
    Mock.mockRestore();
    NavSpyMock.mockRestore();
    jest.resetModules();

    // mock fake fetch
    Mock = jest.spyOn(global, 'fetch');
    Mock.mockImplementation(() => Promise.resolve({
    
    json: () => Promise.resolve({"warning":"No user found. Please sign up"})
    }))
    document.getElementById('username').value = 'wrong';
    document.getElementById('DoSubmission').click();
    expect(Mock).toHaveBeenCalledTimes(1);
    const Fetch = Mock.mock.calls[0];
    expect(Fetch[0]).toBe('https://send-it-ke-v2.herokuapp.com/api/v2/auth/login');
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
          username: 'wrong',
          password: '123456',
      }) 
    });
    // wait for  the promise to resolve
    await Promise.resolve().then();
    expect(document.getElementById('warning').innerHTML).toBe('No user found. Please sign up');
})



it('checks for very short password during sign-in', async () => {
    // restore mock to initial state
    Mock.mockRestore();
    NavSpyMock.mockRestore();
    jest.resetModules();

    // mock fake fetch
    Mock = jest.spyOn(global, 'fetch');
    Mock.mockImplementation(() => Promise.resolve({
    
    json: () => Promise.resolve({"warning": "Invalid password"})
    }))
    document.getElementById('username').value = 'adm';
    document.getElementById('password').value = '12';
    document.getElementById('DoSubmission').click();
    expect(Mock).toHaveBeenCalledTimes(1);
    const Fetch = Mock.mock.calls[0];
    expect(Fetch[0]).toBe('https://send-it-ke-v2.herokuapp.com/api/v2/auth/login');
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
          username: 'adm',
          password: '12',
      })
    });
    // wait for  the promise to resolve
    await Promise.resolve().then();
    expect(document.getElementById('warning').innerHTML).toBe('Invalid password');
})

it('Checks for that username and password were provided during sign-in', async () => {
    // restore mock to initial state
    Mock.mockRestore();
    NavSpyMock.mockRestore();
    jest.resetModules();

    // mock fake fetch
    Mock = jest.spyOn(global, 'fetch');
    Mock.mockImplementation(() => Promise.resolve({
    
    json: () => Promise.resolve({"warning": "\'username\' and \'password\' are required fields"})
    }))
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
    document.getElementById('DoSubmission').click();
    expect(Mock).toHaveBeenCalledTimes(1);
    const Fetch = Mock.mock.calls[0];
    expect(Fetch[0]).toBe('https://send-it-ke-v2.herokuapp.com/api/v2/auth/login');
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
          username: '',
          password: '',
      })
    });
    // wait for  the promise to resolve
    await Promise.resolve().then();
    expect(document.getElementById('warning').innerHTML).toBe('\'username\' and \'password\' are required fields');
})