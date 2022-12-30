/* every button executes a function from below and calls the api on the back end app.py
*/

//gets a list of stores on the back end and displays them as a string
async function getStores(){
    console.log("get stores");
    var res = await fetch('http://127.0.0.1:5000/store');
    var res_json = await res.json();
    console.log(res_json.stores);
    console.log(res_json.stores.length);
    document.getElementById('storeList').innerHTML= JSON.stringify(res_json);
}

//adds a store calling the back end and displays a success message if it worked
async function addStore(url = 'http://127.0.0.1:5000/storePost', data = {"name":"placeholder"}) {
    var inputName = document.getElementById("storeName").value;
    data.name = document.getElementById("storeName").value;
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
       // 'Content-Type': 'text/plain'
        'Content-Type': 'application/json'
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    var resJson = await response.json();
    if(response.status == 200){
        document.getElementById('addStoreDiv').innerHTML= 'success' + JSON.stringify(resJson);
    }
    else{
        document.getElementById('addStoreDiv').innerHTML= 'error adding new store';
    }
    console.log(resJson);
  }

//adds an item with to an existing store calling the back end POST api. displays a success if it worked
async function addItem(){
    //I need to get the info from the input boxes before I send the url and data.
    var store = document.getElementById('existingStoreName').value;
    console.log("store");
    console.log(store);
    var url = "http://127.0.0.1:5000/store/" + store + "/items";
    console.log("url: " + url);
    var data = {
        "name": "placeholder",
        "price": "placeholder"
    };
    data.name = document.getElementById('addItemName').value;
    data.price = document.getElementById('addItemPrice').value;
    console.log(data)

    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
          'Content-Type': 'application/json'
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
      });
      if(response.status == 200){
        document.getElementById('addItemDiv').innerHTML = "successfully added " + data.name + " at a price of " 
        + data.price + " to store " + store;
      }
      else{
        document.getElementById('addItemDiv').innerHTML = "error processing request";
      }
      console.log(response);
}