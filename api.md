# flask-shop API

## **Show Product**

取得特定商品資料

- **URL**

  /api/product/:id

- **Method:**

  `GET`

- **URL Params**

  **Required:**

  `id=[integer]`

- **Data Params**

  None

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    {
        id: 1,
        name: 'apple',
        price: '8787',
        image: 'https://as-images.apple.com/is/og-default?wid=1200&hei=630&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1525370171638',
        url: 'www.apple.com',
        description: 'this is an apple',
        category_id: 1
    }
    ```

- **Error Response:**

  - **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Product doesn't exist" }`

  OR

  - **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

- **Sample Call:**

  ```javascript
  $.ajax({
    url: '/api/product/1',
    dataType: 'json',
    type: 'GET',
    success: function(r) {
      console.log(r)
    }
  })
  ```

## **Show Products**

取得一堆商品

- **URL**

  /api/products

- **Method:**

  `GET`

- **URL Params**

  None

- **Data Params**

  None

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```
    [
        {
        id: 1,
        name: 'apple',
        price: '8787',
        image: 'https://as-images.apple.com/is/og-default?wid=1200&hei=630&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1525370171638',
        url: 'www.apple.com',
        description: 'this is an apple',
        category_id: 1
    },{
        id: 2,
        name: 'banana',
        price: '8787',
        image: 'https://as-images.apple.com/is/og-default?wid=1200&hei=630&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1525370171638',
        url: 'www.banana.com',
        description: 'this is an banana',
        category_id: 1
    },{
        id: 3,
        name: 'cat',
        price: '8787',
        image: 'https://as-images.apple.com/is/og-default?wid=1200&hei=630&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1525370171638',
        url: 'www.cat.com',
        description: 'this is an cat',
        category_id: 1
    }
    ]
    ```

- **Error Response:**

  - **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Products doesn't exist" }`

  OR

  - **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

- **Sample Call:**

  ```javascript
  $.ajax({
    url: '/api/products',
    dataType: 'json',
    type: 'GET',
    success: function(r) {
      console.log(r)
    }
  })
  ```
