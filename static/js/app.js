"use strict";
const menuBtn = document.getElementById("menu");
const orderBtn = document.getElementById("my-order");
const menuContainer = document.getElementById("menu-list");

//Generates CSRFToken required for sending form data in django
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

//Fetches and sends menu items to render function when button is clicked
menuBtn.addEventListener("click", function (e) {
  fetch("api/menu/")
    .then((res) => {
      return res.json();
    })
    .then((menu) => {
      showMenu(menu);
      console.log(menu);
    })
    .catch((error) => {
      console.log(error);
    });
});

//Renders menu items to html template
function showMenu(menu) {
  menuContainer.innerHTML = "";
  menu.forEach((el, i) => {
    menuContainer.innerHTML += `
    <tr >
            
            <th scope="row">${i + 1} </th>
            <td>${el.food_type}</td>
            <td>Ksh ${el.price} </td>
            <td><button class="btn btn-warning" id="place-order">Order</button></td>
            
            </tr>`;
  });

  const orderFoodBtn = document.querySelectorAll("#place-order");
  orderFoodBtn.forEach((el, i) => {
    //Gets all order btns dynamically generated above and adds an eventlistener to them
    console.log(el, i);
    el.addEventListener("click", () => {
      // alert(`Button clicked for ${i}`);
      makeOrder(menu[i]);
    });
  });
}

//Sends menu item to database when button is clicked!
function makeOrder(menu) {
  const url = "api/make-order/";
  let tableNum = Math.floor(Math.random() * 5 + 1);
  let quanity = Math.floor(Math.random() * 5 + 1);
  fetch(url, {
    method: "POST",
    headers: {
      "Content-type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      "food_type": menu.food_type,
      "table_number": tableNum,
      "quantity": quanity,
      "total": quanity * menu.price,
    }),
  }).then((res) => {
    alert("Order sent!");
  });
}

//Fetches menu items from order table in database and sends them to render function
orderBtn.addEventListener("click", renderOrders);

function renderOrders() {
  const url = "api/orders/";
  fetch(url)
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      showOrders(data);
    });
}

//Renders order items to html template
function showOrders(data) {
  menuContainer.innerHTML = "";
  data.forEach((el, i) => {
    menuContainer.innerHTML += `
            <tr>
            <th scope="row">${i + 1} </th>
            <td>${el.quantity}x ${el.food_type} for table ${
      el.table_number
    } </td>
            <td>Ksh ${el.total} </td>
            <td><button class="btn btn-danger" id="delete-order">Delete</button></td>
            </tr>
            `;
  });

  const deleteBtn = document.querySelectorAll("#delete-order");
  deleteBtn.forEach((el, i) => {
    //Gets all delete btns dynamically generated above and adds an eventlistener to them
    console.log(el, i);
    el.addEventListener("click", () => {
      //alert(`Button clicked for ${data[i].id}`);
      deleteOrder(data[i].id);
    });
  });
}

function deleteOrder(id) {
  fetch(`api/order-delete/${id}`, {
    method: "DELETE",
    headers: {
      "Content-type": "application/json",
      "X-CSRFToken": csrftoken,
    },
  }).then((res) => {
    renderOrders();
  });
}
