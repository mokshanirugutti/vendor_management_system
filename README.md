# Vendor management system

## Setup and Installation 
### cloning repo

- Clone repo into to local space
    ```
    git clone https://github.com/mokshanirugutti/vendor_management_system
    ```
    
- Create virutal environment
    - ``` virutalenv {environment name}```
- Once virutal environment is created activate it with command
    - ``` env\Scripts\activate ```

Now navigate into cloned repo 

``` cd Vendor_management_system ```

- install requirements 

```bash
pip install requirements.txt
 ```

 - starting server 
 ```
 python manage.py runserver
 ```

 Now server will be running on localhost:8000 
 
 check out end point documentaion to understand usage

# API Reference


## User authentication 

### Singup

End point 

``` 
POST /api/signup/
```

Data sending Format

```
{
    "username":"testabc",
    "password":"passabc"
}
```

**Respone**

code : `201 CREATED`
```
[
    "Success : User created "
]
```


### login

End point 

``` 
POST /api/login/
```

Data sending Format

```
{
    "username":"testabc",
    "password":"passabc"
}
```

**Respone**

code : `200 OK`
```
{
    "token": "7461adcc6b916f42ae297128e25096253f43877e"
}
```

> [!IMPORTANT]
> Don't forget to send the token in header while sending request to **Vendor/purchase_orders endpoints**  




## Below endpoints need auntetication 
## Vendor endpoints 

###  Create a new vendor

```http
   POST /api/vendors/
```

To create new Vendor send the data in the following format
```http 
    {
    "name": "DXG Prints",
    "contact_details": "+1234567890",
    "address": "22 Main Street, City, Country"
    }
```


#### Response
code : `201 created`
```
[
    "Success: Vendor created "
]
```
### Get all vendors

```http
  GET /api/vendors/
```

#### Response 

code : `200 OK`
```
[
    {
        "id": 4,
        "name": "Vendor XYZ",
        "contact_details": "Contact details of Vendor XYZ",
        "address": "123 Main Street, City, Country",
        "vendor_code": "3a2c5b81-dc7e-4ddb-8023-7338622948cc",
        "on_time_delivery_rate": 0.0,
        "quality_rating_avg": 4.5,
        "average_response_time": 0.0,
        "fulfillment_rate": 0.7
    },
    {
        "id": 5,
        "name": "ABC Tech",
        "contact_details": "+1234567890",
        "address": "456 Main Street, City, Country",
        "vendor_code": "9947f335-7b00-42b2-8215-829751d24733",
        "on_time_delivery_rate": 0.0,
        "quality_rating_avg": 3.8,
        "average_response_time": 2.5,
        "fulfillment_rate": 1.0
    },
    {
        "id": 8,
        "name": "DXG Prints",
        "contact_details": "+1234567890",
        "address": "22 Main Street, City, Country",
        "vendor_code": "06dfcc45-4957-4da6-9c0e-33825525bfe9",
        "on_time_delivery_rate": 0.0,
        "quality_rating_avg": 0.0,
        "average_response_time": 0.0,
        "fulfillment_rate": 0.0
    }
]
```

### Retrieve a specific vendor's details.

```http
  GET /api/vendors/{vendor_id}/
```
for example vendor id = 4 
#### Response
```
[
    {
        "id": 4,
        "name": "Vendor XYZ",
        "contact_details": "Contact details of Vendor XYZ",
        "address": "123 Main Street, City, Country",
        "vendor_code": "3a2c5b81-dc7e-4ddb-8023-7338622948cc",
        "on_time_delivery_rate": 0.0,
        "quality_rating_avg": 4.5,
        "average_response_time": 0.0,
        "fulfillment_rate": 0.7
    }
]

```

###  Update a vendor's details.

```http
  PUT /api/vendors/{vendor_id}/
```
for example vendor id = 8

To update vendor send the data in the following format
```http 
    {
    "name": "DXG Prints and more",
    "contact_details": "+1234567890",
    "address": "22 Main Street, City, Country"
    }
```
#### Response
code : `200 OK`
```
{
    "id": 8,
    "name": "DXG Prints and more",
    "contact_details": "+1234567890",
    "address": "22 Main Street, City, Country",
    "vendor_code": "06dfcc45-4957-4da6-9c0e-33825525bfe9",
    "on_time_delivery_rate": 0.0,
    "quality_rating_avg": 0.0,
    "average_response_time": 0.0,
    "fulfillment_rate": 0.0
}

```


###  Delete a vendor

```http
  DELETE /api/vendors/{vendor_id}/
```
Example vendor id = 8

#### Response
code : `204 No Content`
```
{
    "message": "Vendor deleted successfully"
}
```

## Purchase Orders

###   Create a purchase order

```http
  POST /api/purchase_orders/
```
To create a new purchase send the purchase details like this 
```json
{
    "po_number": "PO04",
    "order_date": "2024-05-10T08:30:00Z",
    "delivery_date": "2024-05-17T09:00:00Z",
    "items": {
        "item1":{
            "name" : "laptop",
            "price" : "100k",
            "company":"hp"
        },
        "item2":{
            "name" : "Phone",
            "price" : "10k",
            "company":"xyz"
        }
    },
    "quantity": 1,
    "status": "completed",
    "quality_rating": 3.5,
    "issue_date": "2024-05-12T08:00:00Z",
    "acknowledgment_date": "2024-05-12T08:00:00Z",
    "vendor": 5
}
```

#### Response
code : `201  created`
```
{
    "id": 18,
    "po_number": "PO04",
    "order_date": "2024-05-10T08:30:00Z",
    "delivery_date": "2024-05-17T09:00:00Z",
    "items": {
        "item1": {
            "name": "laptop",
            "price": "100k",
            "company": "hp"
        },
        "item2": {
            "name": "Phone",
            "price": "10k",
            "company": "xyz"
        }
    },
    "quantity": 1,
    "status": "completed",
    "quality_rating": 3.5,
    "issue_date": "2024-05-12T08:00:00Z",
    "acknowledgment_date": "2024-05-12T08:00:00Z",
    "vendor": 5
}
```

###  List all purchase orders

```http
  GET /api/purchase_orders/
```

#### Response
code : `200 OK`
```
[
    {
        "id": 15,
        "po_number": "P1",
        "order_date": "2024-05-10T08:30:00Z",
        "delivery_date": "2024-05-10T09:00:00Z",
        "items": {
            "item7": 20,
            "item8": 1
        },
        "quantity": 3,
        "status": "completed",
        "quality_rating": 3.5,
        "issue_date": "2024-05-15T08:00:00Z",
        "acknowledgment_date": "2024-05-17T08:00:00Z",
        "vendor": 5
    },
    {
        "id": 17,
        "po_number": "P3",
        "order_date": "2024-05-10T08:30:00Z",
        "delivery_date": "2024-05-15T09:30:00Z",
        "items": {
            "item7": 20,
            "item8": 1
        },
        "quantity": 3,
        "status": "completed",
        "quality_rating": 4.5,
        "issue_date": "2024-05-15T08:00:00Z",
        "acknowledgment_date": "2024-05-17T08:00:00Z",
        "vendor": 5
    },
    {
        "id": 18,
        "po_number": "PO04",
        "order_date": "2024-05-10T08:30:00Z",
        "delivery_date": "2024-05-17T09:00:00Z",
        "items": {
            "item1": {
                "name": "laptop",
                "price": "100k",
                "company": "hp"
            },
            "item2": {
                "name": "Phone",
                "price": "10k",
                "company": "xyz"
            }
        },
        "quantity": 1,
        "status": "completed",
        "quality_rating": 3.5,
        "issue_date": "2024-05-12T08:00:00Z",
        "acknowledgment_date": "2024-05-12T08:00:00Z",
        "vendor": 5
    }
]
```
####  To filter by vendor
```http
GET /api/purchase_orders?vendor=4/
```
#### Response 
```
[
    {
        "id": 17,
        "po_number": "P3",
        "order_date": "2024-05-10T08:30:00Z",
        "delivery_date": "2024-05-15T09:30:00Z",
        "items": {
            "item7": 20,
            "item8": 1
        },
        "quantity": 3,
        "status": "completed",
        "quality_rating": 4.5,
        "issue_date": "2024-05-15T08:00:00Z",
        "acknowledgment_date": "2024-05-17T08:00:00Z",
        "vendor": 4
    }
]
```

###  Retrieve details of a specific purchase order.


```http
  GET /api/purchase_orders/{po_id}/
```
Example purchase_order id : 17

#### Response
code : `200 OK`

```
{
    "id": 17,
    "po_number": "P3",
    "order_date": "2024-05-10T08:30:00Z",
    "delivery_date": "2024-05-15T09:30:00Z",
    "items": {
        "item7": 20,
        "item8": 1
    },
    "quantity": 3,
    "status": "completed",
    "quality_rating": 4.5,
    "issue_date": "2024-05-15T08:00:00Z",
    "acknowledgment_date": "2024-05-17T08:00:00Z",
    "vendor": 4
}

```

###   Update a purchase order


```http
  PUT /api/purchase_orders/{po_id}/
```
Example purchase_order id : 17

sending format 

```
{
    "po_number": "P3",
    "order_date": "2024-05-10T08:30:00Z",
    "delivery_date": "2024-05-15T09:30:00Z",
    "items": {
        "item7": 20,
        "item8": 1
    },
    "quantity": 3,
    "status": "completed",
    "quality_rating": 4.5,
    "issue_date": "2024-05-15T08:00:00Z",
    "acknowledgment_date": "2024-05-17T08:00:00Z",
    "vendor": 4
}

```

#### Response

code : `200 OK`

```
{
    "id": 17,
    "po_number": "P3",
    "order_date": "2024-05-10T08:30:00Z",
    "delivery_date": "2024-05-15T09:30:00Z",
    "items": {
        "item7": 20,
        "item8": 1
    },
    "quantity": 3,
    "status": "completed",
    "quality_rating": 4.5,
    "issue_date": "2024-05-15T08:00:00Z",
    "acknowledgment_date": "2024-05-17T08:00:00Z",
    "vendor": 4
}

```
###   Delete a purchase order.


```http
  DELETE /api/purchase_orders/{po_id}/
```
Example purchase_order id : 17

#### Response

code : `204 No Content`

```
{
    purchase deleted
}

```


###  Vendor Performance Evaluation

#### Retrieve a vendor's performance metrics

```
 GET /api/vendors/{vendor_id}/performance/
```

Example vendor id : 4

```
{
    "on_time_delivery_rate": 0.0,
    "quality_rating_avg": 4.5,
    "average_response_time": 2.2,
    "fulfillment_rate": 0.7
}

```