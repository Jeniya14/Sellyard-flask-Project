# Sellyard - Fruits, Vegetables, and Homemade Items Ordering and Selling Website

Welcome to Sellyard, a project created during my college studies in *2021*. Sellyard is a web application for ordering and selling fruits, vegetables, and homemade items. It features a frontend developed with HTML, CSS, and Flask framework for the backend, utilizing SQL for data storage.

## Introduction

Sellyard is a platform where users can log in, explore products in different categories. Sellers have a dedicated login to manage their products by adding new items, updating existing ones, and removing items. The admin has separate access to manage sellers and products on the platform.

## Screenshots

### Login Page
![Login Page](/screenshots/login.png)

### Home Page
![Home Page](/screenshots/home.png)
![Home Page](/screenshots/home2.png)

### Category Page
![Food Category Page](/screenshots/categories.png)

### Profile Page
![Profile Page](/screenshots/profile.png)

### Seller 

#### Product details
![seller Page](/screenshots/seller.png)

#### Add Product 
![seller Page](/screenshots/selller1.png)

### Admin Page
![admin Page](/screenshots/admin.png)

## Features

### User Features

- **User Authentication:** Users can log in, and their data is securely stored in an SQL database.

- **Product Categories:** Products are displayed in different categories, providing a user-friendly browsing experience.

### Seller Features

- **Seller Authentication:** Sellers can log in separately to view, add, update, and delete their products.

- **Product Management:** Sellers have the ability to add new products, update existing items, and remove products from the inventory.

### Admin Features

- **Admin Authentication:** Admins can log in separately to manage sellers and products.

- **User and Product Administration:** Admins can edit and delete seller accounts and products.

### Database Integration

- **SQL Database:** All data, including user information, product details, and seller information, is stored in an SQL database.

### Database Schema

1. **Users Table:**
   - `user_id` (Primary Key)
   - `username`
   - `password`
   - `Address`
   - `Email`

2. **Products Table:**
   - `product_id` (Primary Key)
   - `seller_id` (Foreign Key referencing Sellers Table)
   - `name`
   - `description`
   - `price`
   - `category`
   - `Quantity`
   - `Image`
   
3. **Sellers Table:**
   - `seller_id` (Primary Key)
   - `username`
   - `password`
   - `Address`
   - `Delivery-type`

4. **Admins Table:**
   - `admin_id` (Primary Key)
   - `username`
   - `password`


## Technologies Used

- Flask (Backend)
- HTML, CSS (Frontend)
- SQL (Database)

## Acknowledgements
This project was created by Me. Feel free to contribute, report issues, or provide feedback!


