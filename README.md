# Love Rugby shop
Love Rugby is an ecommerce rugby website allowing users to purchase rugby boots, jerseys and accessories developed for Milestone 4 as milestone project 4 as part of the Code Institute - Diploma in Software Development (Full stack) course.

- There are two types of users, and I have set up accounts for both
    - An admin(administrator) user account has been set up with username/password of administrator/66Nov2009
    - A regular(shopper) user account has been set up with username/password of johnnysexton/Password456!
    - When making a payment as a regular user, a test credit card of 4242424242424242 has been set up for the card number
    - For the expiry date, cvc and postal code any series number(s) can be used(once they meet the mimimum values)
<br>

**View the live site [here](https://ci-ms4-loverugby.herokuapp.com/)**
<br><br>
![Responsive site example](readme/responsive/responsive.PNG)

# Table of Contents
- [Love Rugby shop](#love-rugby-shop)
- [Project Overview](#project-overview)
- [UX](#ux)
  * [Strategy](#strategy)
    + [Primary Goal](#primary-goal)
  * [Structure](#structure)
    + [Website pages](#website-pages)
    + [Code Structure](#code-structure)
    + [Database](#database)
      - [Physical database model](#physical-database-model)
      - [Models](#models)
        * [User Model](#user-model)
        * [UserProfile Model](#userprofile-model)
        * [Order Model](#order-model)
        * [OrderLineItem Model](#orderlineitem-model)
        * [Favourites Model](#favourites-model)
        * [Product Model](#product-model)
        * [Category Model](#category-model)
        * [News Model](#news-model)
        * [Comment Model](#comment-model)
        * [Review Model](#review-model)
  * [Scope](#scope)
    + [User Stories Potential or Existing Customer](#user-stories-potential-or-existing-customer)
    + [User Stories Website Owner](#user-stories-website-owner)
  * [Skeleton](#skeleton)
    + [Wireframes](#wireframes)
  * [Surface](#surface)
    + [Color Palette](#color-palette)
    + [Typography](#typography)
- [Features](#features)
  * [Existing Features](#existing-features)
    + [Feature 1 Navigation Bar and Homepage](#feature-1-navigation-bar-and-homepage)
      - [Description feature 1](#description-feature-1)
      - [User Stories feature 1](#user-stories-feature-1)
    + [Feature 2 Footer](#feature-2-footer)
      - [Description feature 2](#description-feature-2)
      - [User Stories feature 2](#user-stories-feature-2)
    + [Feature 3 Register](#feature-3-register)
      - [Description feature 3](#description-feature-3)
      - [User Stories feature 3](#user-stories-feature-3)
    + [Feature 4 Login](#feature-4-login)
      - [Description feature 4](#description-feature-4)
      - [User Stories feature 4](#user-stories-feature-4)
    + [Feature 5 Products and Product Detail Pages](#feature-5-products-and-product-detail-pages)
      - [Description feature 5](#description-feature-5)
      - [User Stories feature 5](#user-stories-feature-5)
    + [Feature 6 Sale items page](#feature-6-sale-items-page)
      - [Description feature 6](#description-feature-6)
      - [User Stories feature 6](#user-stories-feature-6)
    + [Feature 7 Favourites page](#feature-7-favourites-page)
      - [Description feature 7](#description-feature-7)
      - [User Stories feature 7](#user-stories-feature-7)
    + [Feature 8 News Page](#feature-8-news-page)
      - [Description feature 8](#description-feature-8)
      - [User Stories feature 8](#user-stories-feature-8)
    + [Feature 9 Profile Page](#feature-9-profile-page)
      - [Description feature 9](#description-feature-9)
      - [User Stories feature 9](#user-stories-feature-9)
    + [Feature 10 Product Management](#feature-10-product-management)
      - [Description feature 10](#description-feature-10)
      - [User Stories feature 10](#user-stories-feature-10)
    + [Feature 11 News item Management](#feature-11-news-item-management)
      - [Description feature 11](#description-feature-11)
      - [User Stories feature 11](#user-stories-feature-11)
    + [Feature 12 Bag and Checkout](#feature-12-bag-and-checkout)
      - [Description feature 12](#description-feature-12)
      - [User Stories feature 12](#user-stories-feature-12)
    + [Feature 13 Admin](#feature-13-admin)
      - [Description feature 13](#description-feature-13)
      - [User Stories feature 13](#user-stories-feature-13)
  * [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Libraries and other resources](#libraries-and-other-resources)
- [Testing](#testing)
- [APIs and configuration](#apis-and-configuration)
  * [Email JS](#email-js)
  * [Google emails](#google-emails)
  * [Stripe](#stripe)
- [Deployment](#deployment)
  * [Amazon WebServices](#amazon-webservices)
  * [Local Deployment](#local-deployment)
  * [Heroku and Postgres Database](#heroku-and-postgres-database)
- [Credits](#credits)
- [Content](#content)
- [Media](#media)
- [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Project Overview
- This project is a website is for submission as milestone project 4 as part of the Code Institute - Diploma in Software Development (Full stack) course.
- The website is deployed using Heroku pages at the following url: [Love Rugby](https://ci-ms4-loverugby.herokuapp.com/)
- The repository on GitHub that contains the website source code and assets is available at the following url: [Code Repository](https://github.com/pmeeny/CI-MS4-LoveRugby)
- The website was built with a responsive look and feel for desktop, tablet and mobile devices

# UX
## Strategy
### Primary Goal
The primary goal of the website from the site 
owners perspective is as follows:
- To add, edit and delete products with the relevant information (price, description, rating, comments, image, sizes and category) on the website 
- To allow a user make a purchase of the products on the website
- To categorise sale items on the website
- To add, edit and delete website news for publication to website users

The primary goal of the website from a site users perspective is as follows:
- To register for an account on the website and receive an email after successful registration
- To login or logout from the website
- To easily recover my password in case I forget it
- Have a personalised user profile with my delivery, payment information and order history
- View a list of products on the website
- View an individual product detail(price, description, rating, comments, image, sizes and category)
- To add an item to a shopping bag, and select the quantity and size if applicable
- Complete a purchase of items in a shopping bag
- To post a review(rating and comment) on a product
- To sort the list of available products by rating, price and category
- Search for a product by name or description and view the search results
- To view website news, and comment on a news item
- To have a list of product favourites and to add/delete items from the list

## Structure
### Website pages
- I have structured the website into over 20 pages, each with clear, concise structure, information and purpose. I use the Bootstrap grid system throughout, which gave a consistent structure and responsive design "out of the box"
- Below are the main page's/features functionality wise, there are some others for password reset/verification etc. that are described in the user story section 
- All pages have a common look and feel and a common header/footer. On a tablet/mobile the look and feel is slightly different with a burger menu
- These pages are described in more detail in the user stories section

Page            |Description
:-------------         |:------------- 
Home     |The homepage consists of a carousel of three images     
Products           | The products page displays 4 products(image, price, rating) in a paginated way      
Product Detail           | The product detail page displays the product image, description, price, reviews, add to bag buttons    
Products Detail (Review)          | A review(rating(1-5) and comment) can be added to a product. A review can be deleted  
Product Management(Add Product)     | A product can be added to the website    
Product Management(Edit Product)     | A product can be edited to the website     
Product Management(Delete Product)     | A product can be deleted from the website. This is a modal triggered by a delete button
Favourites     | A user can have their own favourites list   
Add to Favourites     |Products can be added or removed to/from a users favourite list by clicking on the heart icon on the product detail page      
My Profile             |The users profile(delivery information) and previous orders is displayed       
Order History         | A order history page per order details the order information and price
Log out               | A logout button is provided under the My Account link to logout
Register               | A user can register an account on the site with a valid email address
Log in               | A user can login with a valid username and password     
News                | News items can be viewed by all users
News Item             | A new item contains an image and text and can be added by an admin user      
News Item (comment) | A user can comment on a news item. They can delete comments(an admin can also delete a users comment)    
Bag | A user can add products to a shopping bag which contains each item in the order and an overall price/delivery if applicable   
Checkout | A user can enter their delivery details and credit card information to checkout an order   
Checkout success | Once an order is successful, the user can view the checkout success

### Code Structure
The project is divided into a number of apps, as is built using the Django Framework
The project was built on the Boutique Ado project, that was part of the project content
The apps are described as follows
- bag (part of the original Boutique Ado project): This app contains functionality regarding a users shopping bag
- checkout (part of the original Boutique Ado project): This app contains functionality regarding a users checking out and payment of an order
- favourites: A newly written app, that allows the user to add and remove items from a favourites list. This list is unique to the user.
- home (part of the original Boutique Ado project): This app contains functionality regarding the users home page
- news: A newly written app, that allows admin users to publish news items, and allows regular users to view and comment on the news items
- products (part of the original Boutique Ado project): This app contains functionality regarding a product. I added functionality for adding/removing a rating/comment to a product
- profiles (part of the original Boutique Ado project): This app contains functionality regarding a users profile and order history

To complement the apps there are
- rugby_shop: Containing settings.py(Settings) and urls.py(Website urls) for example
- templates: Containing the base.html, allauth(django authentication) and includes html files
- util: Utility for generic pagination reusable code
- static: Base css and Javascript files(toast and send_email) There is some javascript in some html files, but I have tried to minimise that
- manage.py: Main python file for starting the website
- README.md: Readme documentation
- TESTING.md: Testing documentation
- custom_storage.py: AWS Boto3 configuration
- Procfile: To run the application
- Requirements.txt: Containing the python libraries installed
Note: Environment variable values are not exposed in the source code, they are stored locally in env.py that is not checked in(and listed in .gitignore, and on Heroku in app settings

### Database
- The website is a data-centric one with html, javascript, css used with the bootstrap(version 5) framework as a frontend
- The backend consists of Python built with the Django framework with a database of a Postgres for the deployed Heroku version(production)
- Postgres is a powerful, open source object-relational database system (https://www.postgresql.org/)
- A SQLLite database was used for local development (https://www.sqlite.org/index.html)

#### Physical database model
This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database
<br>![Database model](readme/misc/database_schema.png)


#### Models
- The following models were created to represent the database model structure for the website
##### User Model
- The User model contains information about the user. It is part of the Django allauth library
- The model contains the following fields: username, password, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, date_joined

##### UserProfile Model
- The UserProfile model has a one-to-one relationship with User
- The model contains the following fields: default_phone_number, default_street_address1, default_street_address2
default_town_or_city, default_county, default_postcode and default_country

##### Order Model
- The Order model contains information about orders made on the website.
- It contains UserProfile as a foreign-key.
- The model contains the following fields: order_number, user_profile, full_name, email, phone_number, country, postcode, town_or_city, street_address1
, street_address2, county, date, delivery_cost, order_total, grand_total, original_bag, stripe_pid

##### OrderLineItem Model
- The OrderLineItem model contains information about an entry in an order, for orders made on the website.
- It contains Order and Product as foreign-keys.
- The model contains the following fields: order, product, product_size, quantity, lineitem_total

##### Favourites Model
- The Favourites model contains a users favourite products
- It contains Products as many-to-many field, and User as a one-to-one relationship
- The model contains the following fields: products, username

##### Product Model
- The Product Model represents a product and its details
- It contains Category as a foreign-key
- The model contains the following fields: name, category, price, colour, code, description, feature1, feature2, feature3, feature4, has_sizes, rating, pre_sale_price, image_url, image
- The image field contains the product image
- The image_url field contains the url to where the image file is physically stored, for example AWS S3 bucket

##### Category Model
- The Category model contains a product category
- The model contains the following fields: name, friendly_name

##### News Model
- The News model contains a new item and its details
- It contains User as a foreign-key
- The model contains the following fields: title, user, news_item_text, update_date, create_date, status

##### Comment Model
- The News model contains a comment on a new story
- It contains News as a foreign-key
- The model contains the following fields: user, new_story, comment_text, create_date

##### Review Model
- The Review model contains a review of a product by a user
- It contains User and Product as foreign-keys.
- The model contains the following fields: user, product, product_rating, review_text, create_date


## Scope
There is overlap in terms of user stories for the two types of users, and they are described below
### User Stories Potential or Existing Customer
The user stories for the regular user eg: "shopper user" (a potential or existing customer) are described as follows: 
- User Story 1.1: As an admin/regular user the navigation bar is displayed with a logo on all pages with a search box, My account, Favourites and shopping bag icons on a desktop device
- User Story 1.2: As an admin/regular user the navigation bar is displayed on all pages with a search box, My account, Favourites and shopping bag icons on a mobile/tablet device
- User Story 1.3: As a regular user not logged in, I see a Register/Login link under the My Account dropdown
- User Story 1.4: As a regular user not logged in, I am brought to the Login link if I click on the Favourites icon
- User Story 1.5: As a regular logged in, I am brought to the Favourites page if I click on the Favourites icon
- User Story 1.6: As a regular user logged in/not logged in, I am brought to my shopping bag if I click on the Bag icon
- User Story 1.7: As a regular/admin user logged in, I see a "My Profile"/Logout under the My Account dropdown
- User Story 1.9: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the My Profile page
- User Story 1.10: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the Logout page. If I click Logout I am Logged out. If I click cancel I am brought back to the homepage
- User Story 1.13: As a regular/admin user I can view the Home link in the header, and clicking it will bring the user to the homepage
- User Story 1.15: As a regular/admin user I can click on the "All Products" filter, click By Price, and will be brought to the Products page, with products price low to high displayed
- User Story 1.16: As a regular/admin user I can click on the "All Products" filter, click By Rating, and will be brought to the Products page, with products rating high to low displayed
- User Story 1.17: As a regular/admin user I can click on the "All Products" filter, click By Category, and will be brought to the Products page, with products category a-z displayed
- User Story 1.18: As a regular/admin user I can click on the "Rugby Boots" filter, and filter by Adidas Kakari, Adidas Malice or All Rugby Boots
- User Story 1.19: As a regular/admin user I can click on the "Jerseys" filter, and filter by Leinster, Munster, Ulster or All Jerseys
- User Story 1.20: As a regular/admin user I can click on the "Accessories" filter, and filter by Balls, Gum shields, Protection or All Accessories
- User Story 1.21: As a regular/admin user if I encounter an error on the site, I will be navigated to the applicable 400, 403, 404 or 500 error page
- User Story 2.1: As an admin/regular user four text messages are displayed with icons regarding delivery, packaging, dispatch and knowledge
- User Story 2.2: As a regular user the footer is displayed with a logo, product links(Rugby Boots, Jerseys, Accessories), website links(Profile/News/Sale)
- User Story 2.4: As a regular user I can sign up for a newsletter by entering my email address and clicking Signup. I will receive an email after signing up
- User Story 3.1: As a regular user I can register on the website by providing an email address, email address(confirmation), username, password, password confirmation
- User Story 3.1: As a regular user I will receive an email to verify my account after registering
- User Story 3.1: As a regular user I can log in to my account once I click on the verification link in the email I receive regarding my registration
- User Story 4.1: As an admin/regular user I can log in to the website using my username or email address and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed
- User Story 4.2: As an admin/regular user I can request a new password if I forget my current password. I will receive an email to reset my password. Once I reset I can log in
- User Story 5.1: As a regular user I can view the products page with product count and with each product image, title, category, price and presale price(if applicable)
- User Story 5.2: As a regular user I can sort the products by Price(high to low, low to high), Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)
- User Story 5.3: As a regular user if there are more than four products on the page, the page is paginated with four products per page
- User Story 5.4: As a regular user if I click on a product I will be navigated to the product detail page
- User Story 5.5: As a regular user I can view the product image, description, colour, code, rating, category, description, features and reviews(the latest first)
- User Story 5.6: As a regular user if the product is in my favourites list, the heart colour is red in the product detail page. If not the heart colour is white
- User Story 5.7: As a regular user I can add a review, by selecting a rating and entering a comment(both fields are mandatory), the review is displayed and a message is displayed
- User Story 5.8: As a regular user I can delete a review I have added(the comment and rating is removed from the product detail), but I cannot delete other users review
- User Story 5.9: As a regular user if there are more than four reviews for a product, the reviews are paginated
- User Story 5.10: As a regular user I can click on the Keep Shopping button on the product detail page, and it will navigate the user to the products page
- User Story 5.11: As a regular user I can set the product size(if applicable for the product) and quantity for a product (one plus)
- User Story 5.14: As a regular user who has not registered or logged into the website, I cannot add a review to a product
- User Story 6.1: As a regular user I can view the products with sale prices, the product image, category, presale price and price is displayed
- User Story 6.2: As a regular user if I click on a product in the sale items, I am navigated to the product detail page for that product
- User Story 6.3: As a regular user if there are more than four products on the sale items page, the page is paginated with four products per page
- User Story 7.1: As a regular user I can click on the heart icon on a product in the product details page, a message is displayed, and the product is added to my favourites list
- User Story 7.2: As a regular user I can click on the heart icon on a product that is already in my favourites list, a message is displayed, and the product is removed to my favourites list
- User Story 7.3: As a regular user I can view my favourites list, the product image, category, presale price and price is displayed
- User Story 7.4: As a regular user I remove a product from my favorites list by clicking on the Delete button on the product. A confirmation modal and message is displayed
- User Story 7.5: As a regular user if there are more than four products in my favourites page, the page is paginated with four products per page
- User Story 7.6: As a regular user who has not registered or logged into the website, I cannot add an item to the favourites and will be brought to the login page
- User Story 8.1: As a regular user I can view 4 news items on a page with a news image, and 150 characters of the news item text and a read more button
- User Story 8.2: As a regular user I can click on the read more button on the News page, I will be navigated to the news item with a news item image, news item text and any comments will be displayed
- User Story 8.3: As a regular user I can add a comment to a news item
- User Story 8.4: As a regular user I can add a delete a comment that I had originally added on a news item
- User Story 8.6: As a regular user who has not registered or logged into the website, I cannot add a comment to a news item
- User Story 9.1: As a regular user I can view my Default delivery information: Phone Number, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country
- User Story 9.2: As a regular user I can update my Default delivery information: Phone Number, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country
- User Story 9.3: As a regular user I can view my order history(Order Number, Date, Items and Order Total)
- User Story 9.4: As a regular user I can click on an order number to view the order information (Order number, Order date/time, Full Name, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total)
- User Story 12.1: As a regular user I can click on a product, set the size(if applicable) and quantity, click Add to Bag and the product will be added to my bag, a message displayed, and a toast will be displayed with the bag contents
- User Story 12.2: As a regular user I can click on the bag icon, I will be brought to my bag. If there are no items in the bag, a message will be displayed
- User Story 12.3: As a regular user I can click on the bag icon, I will be brought to my bag. If there are items, the product image, detail, price, quantity, subtotal will be displayed for the item. The bag total, delivery(if applicable), grand total would be displayed
- User Story 12.4: As a regular user I can update the quantity or remove an item from my shopping bag
- User Story 12.5: As a regular user I can click on the Secure Checkout button on the bag page or toast message, and I will be brought to the Checkout page
- User Story 12.6: As a regular user on the checkout page I can set my details(Full Name, email address, both mandatory) and Delivery Information(Phone Number(mandatory), Street Address 1(mandatory), Street Address 2, Town or City(mandatory, County, State or Locality, Postal Code and Country(mandatory), which is populated from my profile if filled in
- User Story 12.7: As a regular user on the checkout page I can view the order summary(item image, title, size, quantity, subtotal, order total, delivery, grand total)
- User Story 12.8: As a regular user on the checkout page if the order total is greater than 99 euros, there is no delivery charge
- User Story 12.9: As a regular user on the checkout page if the order total is less than 99 euros, there is delivery charge(10% of the order total) A message is displayed to the user on the toast message of what they need to add to the bag to avail of no delivery charge
- User Story 12.10: As a regular user on the checkout page if I click "Save this delivery information to my profile", the details entered will be saved on the users profile
- User Story 12.11: As a regular user on the checkout page I can enter a credit card number(16 digits), expiry date(2 digits/2digits) and a postal code(up to 5 digits), these fields are mandatory
- User Story 12.12: As a regular user on the checkout page if I click the Keep Shopping button I will be navigated to the products page
- User Story 12.13: As a regular user on the checkout page if I click the Complete Order button, and the transaction is not successful, a message will be displayed
- User Story 12.14: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the user will be navigated to a checkout success page, and an email is sent to the user
- User Story 12.15: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the order is saved to my order history in My profile page
- User Story 12.16: As a regular user on the checkout success page, the Order details will be displayed (Order number, Order date/time, Full NameStreet Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total) and a link to the sales item page is displayed
- User Story 12.17: As a regular user not logged in, I can add items to my bag and make a purchase

### User Stories Website Owner
The user stories for the website owner(admin/administrator user) are described as follows: 
There is a lot of overlap between the two user types, the admin user however has more administrative rights throughout but their roles and responsibilities
are defined
- User Story 1.1: As an admin/regular user the navigation bar is displayed with a logo on all pages with a search box, My account, Favourites and shopping bag icons on a desktop device
- User Story 1.2: As an admin/regular user the navigation bar is displayed on all pages with a search box, My account, Favourites and shopping bag icons on a mobile/tablet device
- User Story 1.8: As an admin user logged in, I see a Product Management/News Item Management/My Profile/Logout under the My Account dropdown
- User Story 1.9: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the My Profile page
- User Story 1.10: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the Logout page. If I click Logout I am Logged out. If I click cancel I am brought back to the homepage
- User Story 1.11: As an admin user logged in, if I click on Product Management under My Account I am brought to the Product Management(Add Product) page
- User Story 1.12: As an admin user logged in, if I click on News Item Management under My Account I am brought to the News Item Management page
- User Story 1.13: As a regular/admin user I can view the Home link in the header, and clicking it will bring the user to the homepage
- User Story 1.15: As a regular/admin user I can click on the "All Products" filter, click By Price, and will be brought to the Products page, with products price low to high displayed
- User Story 1.16: As a regular/admin user I can click on the "All Products" filter, click By Rating, and will be brought to the Products page, with products rating high to low displayed
- User Story 1.17: As a regular/admin user I can click on the "All Products" filter, click By Category, and will be brought to the Products page, with products category a-z displayed
- User Story 1.18: As a regular/admin user I can click on the "Rugby Boots" filter, and filter by Adidas Kakari, Adidas Malice or All Rugby Boots
- User Story 1.19: As a regular/admin user I can click on the "Jerseys" filter, and filter by Leinster, Munster, Ulster or All Jerseys
- User Story 1.20: As a regular/admin user I can click on the "Accessories" filter, and filter by Balls, Gum shields, Protection or All Accessories
- User Story 1.21: As a regular/admin user if I encounter an error on the site, I will be navigated to the applicable 400, 403, 404 or 500 error page
- User Story 2.1: As an admin/regular user four text messages are displayed with icons regarding delivery, packaging, dispatch and knowledge
- User Story 2.3: As an admin user logged in the footer is displayed with a logo, product links(Rugby Boots, Jerseys, Accessories), website links(Product Management/News Item Management)
- User Story 4.1: As an admin/regular user I can log in to the website using my username or email address and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed
- User Story 4.2: As an admin/regular user I can request a new password if I forget my current password. I will receive an email to reset my password. Once I reset I can log in
- User Story 5.10: As an admin user I can view the Add product page by clicking on the Product Management link.
- User Story 5.11: As an admin user I can view the Edit product page by clicking on the Edit button on the product. 
- User Story 5.12: As an admin user I can click on a product, and I am navigated to the product detail page. I can edit or delete the product by clicking on the Edit or Delete links on the page
- User Story 5.13: As an admin user I can delete a review a regular user has added
- User Story 6.4: As an admin user I can delete a comment on a news item, even if I did not add the comment
- User Story 10.1: As an admin user I can add a product by clicking on the Product Management link in My Account. I must enter a name, category, price, colour, code, description and can optionally add a feature (1-4), has Sizes(Unknown, Yes, No), Rating, Pre-sale price, Image url, upload an image and click the 
Add Product button. Clicking cancel navigates the user to the product page.
- User Story 10.2: As an admin user I can edit a product by clicking on the Edit button on the Products page for the product. I can update thea name, category, price, colour, code, description, feature (1-4), has Sizes(Unknown, Yes, No), Rating, Pre-sale price, Image url, update an image and click the 
Edit Product button. Clicking cancel navigates the user to the product page
- User Story 10.3: As an admin user I can delete a product by clicking on the Delete button on the product. A modal will appearing asking to confirm, and a message displayed once I confirm.
- User Story 11.1: As an admin user I can view News items by clicking on the News Item Management link under My account. The news item count and title, create date, status(Published or Draft), and Edit and Delete buttons is displayed
- User Story 11.2: As an admin user if there are more than four news items added, the page is paginated
- User Story 11.3: As an admin user I can add a news item, by clicking on the Add button. I can enter a Title and news item text, add an image and set the item to Published or Draft
- User Story 11.4: As an admin user I can edit a news item, by clicking on the Edit button for the news item. I can update a Title and news item text, update an image and update the item to Published or Draft
- User Story 11.5: As an admin user if a news item is set to Draft, admin and regular users will NOT see this item on the News Page.
- User Story 11.6: As an admin user if a news item is set to Published, admin regular users will see this item on the News Page.
- User Story 11.7: As an admin user I can delete a news item, and I will be asked to confirm the deletion
- User Story 13.1: As an admin user I can view users orders in the django admin page and can view order number, date, full name, order total, delivery cost, grand total
- User Story 13.2: As an admin user I can view users orders in the django admin page and can search by order number, full name and filter by order number, full name and order date
- User Story 13.3: As an admin user I can view users favourites in the django admin page and can view all favourites
- User Story 13.4: As an admin user I can view users favourites in the django admin page and can search and filter by username
- User Story 13.5: As an admin user I can view news items in the django admin page and can view a news item title, user, news item text and image
- User Story 13.6: As an admin user I can view news items in the django admin page and can search and search by title, user, news item text and image, create date, update date status and filter by title, user, create date
- User Story 13.7: As an admin user I can view products in the django admin page and can view a products code, name, category, has sizes, price, presale price, rating, image, image url
- User Story 13.8: As an admin user I can view products in the django admin page and can view search and filter by code, category, name and price
- User Story 13.9: As an admin user I can view users in the django admin page and can view their username, email address, first name, last name, staff status
- User Story 13.10: As an admin user I can view users in the django admin page and can search by username and email address and  filter by staff status, superuser status and active status
- User Story 13.11: As an admin user I can view news items comments in the django admin page and can view a comment user, title, text and create date
- User Story 13.12: As an admin user I can view news items comments in the django admin page and can filter by user, title, create date and search by user, title, text and create date
- User Story 13.13: As an admin user I can view reviews in the django admin page and can view a review user, product, rating, text and create date
- User Story 13.14: As an admin user I can view reviews in the django admin page and can filter by user, product rating, create date and search by user, product, rating, text
- User Story 13.15: As an admin user I can view categories in the django admin page and can view a category name and friendly name

## Skeleton
### Wireframes
Each wireframe image below contains three sub images, one for desktop, tablet and mobile
Balsamiq was used to create the wireframes

Page | Wireframe | 
------------ | ------------- 
bag/templates/bag/bag.html | [Desktop/Tablet/Mobile](readme/wireframes/bag.png)
checkout/templates/checkout/checkout.html | [Desktop/Tablet/Mobile](readme/wireframes/checkout.png)
checkout/templates/checkout/checkout_success.html | [Desktop/Tablet/Mobile](readme/wireframes/checkout_success.png)
favourites/templates/favourites/favourites.html | [Desktop/Tablet/Mobile](readme/wireframes/favourites.png)
home/templates/home/index.html | [Desktop/Tablet/Mobile](readme/wireframes/index.png)
news/templates/news/add_news_item.html | [Desktop/Tablet/Mobile](readme/wireframes/add_news_item.png)
news/templates/news/edit_news_item.html | [Desktop/Tablet/Mobile](readme/wireframes/edit_news_item.png)
news/templates/news/manage_news_items.html  | [Desktop/Tablet/Mobile](readme/wireframes/manage_news_items.png)
news/templates/news/news.html | [Desktop/Tablet/Mobile](readme/wireframes/news.png)
news/templates/news/news_item.html | [Desktop/Tablet/Mobile](readme/wireframes/news_item.png)
products/templates/products/add_product.html | [Desktop/Tablet/Mobile](readme/wireframes/add_product.png)
products/templates/products/edit_product.html | [Desktop/Tablet/Mobile](readme/wireframes/edit_product.png)
products/templates/products/product_detail.html | [Desktop/Tablet/Mobile](readme/wireframes/product_detail.png)
products/templates/products/products.html  | [Desktop/Tablet/Mobile](readme/wireframes/products.png)
products/templates/products/sale_items.html | [Desktop/Tablet/Mobile](readme/wireframes/sale_items.png)
profile/templates/profile/profile.html | [Desktop/Tablet/Mobile](readme/wireframes/profile.png)
profile/templates/profile/order_history.html | [Desktop/Tablet/Mobile](readme/wireframes/order_history.png)
templates/allauth/account/login.html | [Desktop/Tablet/Mobile](readme/wireframes/login.png)
templates/allauth/account/logout.html | [Desktop/Tablet/Mobile](readme/wireframes/logout.png)
templates/allauth/account/register.html| [Desktop/Tablet/Mobile](readme/wireframes/register.png)

## Surface
### Color Palette
I have gone for a simple and minimal design for the website, with predominately green, grey and whitesmoke font colours
There are five colours in the color palette
- 000000/555555 - Black and grey colours for the majority ot text on the website
- 1E5128 - Dark green for background and buttons
- DB4437 - Warning and sale item buttons and text
- 0B51C1 - Blue for links
- F5F5F5/FFFFFF - Whitesmoke and white for background colours

I feel the colours complement each other very well, and I choose those colours after testing a number of palettes while making sure the colour palette met accessibility standards.
![Colour Palette](readme/misc/color_palette.png)

### Typography
The Poppins font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the Poppins font cannot be imported into the website correctly. This font is from the Google fonts library.
![Font](readme/misc/font.PNG)

# Features
The website has twenty distinct features, and they are described below
What is important to detail is what pages are accessible by the three types of users
1. A user not logged into the site
2. A regular(shopper) user logged into the site
3. An admin(administrator) user
The navigation buttons update depending on whether a user is logged in or not, and whether that user is the admin:

 Nav Link              |Not logged in  |Logged in as regular user|Logged in as admin
:-------------         |:------------- |:----------------|:------------- |
Home     |&#9989;        |&#9989;          |&#9989; |
Products           |&#9989;        |&#9989;          |&#9989; |
Product Detail           |&#9989;        |&#9989;          |&#9989; |
Products Detail (Review)          |&#10060;        |&#9989;          |&#9989; |
Product Management(Add Product)     |&#10060;       |&#10060;         |&#9989; |
Product Management(Edit Product)     |&#10060;       |&#10060;         |&#9989; |
Product Management(Delete Product)     |&#10060;       |&#10060;         |&#9989; |
Favourites     |&#10060;       |&#9989;         |&#9989; |
Add to Favourites     |&#10060;       |&#9989;        |&#9989; |
My Profile             |&#10060;       |&#9989;          |&#9989; |
Order History         |&#10060;       |&#9989;          |&#9989; |
Log out               |&#10060;       |&#9989;          |&#9989; |
Register               |&#9989;        |&#10060;         |&#10060; |
Log in               |&#9989;        |&#10060;         |&#10060; |
News                |&#9989;        |&#9989;         |&#9989; |
News Item             |&#9989;        |&#9989;        |&#9989; |
News Item (comment) |&#10060;        |&#9989;          |&#9989; |
Bag |&#9989;        |&#9989;          |&#9989; |
Checkout |&#9989;        |&#9989;          |&#9989; |
Checkout success |&#9989;        |&#9989;          |&#9989; |

## Existing Features
The screenshots below show mainly desktop images, the tablet and mobile images are displayed in the TESTING.MD file for each feature/user story
### Feature 1 Navigation Bar and Homepage
#### Description feature 1
- The homepage consists of a carousel of three images, a header/nav bar and footer
- The header and footer is consistent across all pages
- The navigation bar is displayed with a logo on all pages with a search box, My account, Favourites and shopping bag icons on a desktop device
<br>![Homepage desktop](readme/testing/homepage_loggedin_regular_desktop.PNG)
The website links in the footer differ between a regular user and an admin user
<br>![Homepage footer admin](readme/testing/footer_desktop_admin.PNG)
<br>![Homepage footer regular](readme/testing/footer_desktop_regular.PNG)
- The navigation bar is displayed on all pages with a search box, My account, Favourites and shopping bag icons on a mobile/tablet device
<br>![Homepage tablet](readme/testing/homepage_loggedin_regular_tablet.PNG)
<br>![Homepage mobile](readme/testing/homepage_loggedin_regular_mobile.PNG)
- A regular user logged in, I see a "My Profile"/Logout under the My Account dropdown
- An admin user logged in, I see a Product Management/News Item Management/My Profile/Logout under the My Account dropdown
<br>![Homepage admin desktop](readme/testing/homepage_admin_desktop.PNG)
- On a desktop device there is a number of filters described below: All Products, Rugby Boots, Jerseys and Accessories
<br>![Homepage desktop filter price](readme/testing/filter_price_desktop.PNG)
- If a user encounters an error, the relevant error page is displayed (400, 403, 404 or 500)
<br>![404](readme/testing/404_desktop.PNG)

#### User Stories feature 1
- User Story 1.1: As an admin/regular user the navigation bar is displayed with a logo on all pages with a search box, My account, Favourites and shopping bag icons on a desktop device
- User Story 1.2: As an admin/regular user the navigation bar is displayed on all pages with a search box, My account, Favourites and shopping bag icons on a mobile/tablet device
- User Story 1.3: As a regular user not logged in, I see a Register/Login link under the My Account dropdown
- User Story 1.4: As a regular user not logged in, I am brought to the Login link if I click on the Favourites icon
- User Story 1.5: As a regular  logged in, I am brought to the Favourites page if I click on the Favourites icon
- User Story 1.6: As a regular user logged in/not logged in, I am brought to my shopping bag if I click on the Bag icon
- User Story 1.7: As a regular user logged in, I see a "My Profile"/Logout under the My Account dropdown
- User Story 1.8: As an admin user logged in, I see a Product Management/News Item Management/My Profile/Logout under the My Account dropdown
- User Story 1.9: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the My Profile page
- User Story 1.10: As a regular/admin user logged in, if I click on the My Profile under My Account I am brought to the Logout page. If I click Logout I am Logged out. If I click cancel I am brought back to the homepage
- User Story 1.11: As an admin user logged in, if I click on Product Management under My Account I am brought to the Product Management(Add Product) page
- User Story 1.12: As an admin user logged in, if I click on News Item Management under My Account I am brought to the News Item Management page
- User Story 1.13: As a regular/admin user I can view the Home link in the header, and clicking it will bring the user to the homepage
- User Story 1.15: As a regular/admin user I can click on the "All Products" filter, click By Price, and will be brought to the Products page, with products price low to high displayed
- User Story 1.16: As a regular/admin user I can click on the "All Products" filter, click By Rating, and will be brought to the Products page, with products rating high to low displayed
- User Story 1.17: As a regular/admin user I can click on the "All Products" filter, click By Category, and will be brought to the Products page, with products category a-z displayed
- User Story 1.18: As a regular/admin user I can click on the "Rugby Boots" filter, and filter by Adidas Kakari, Adidas Malice or All Rugby Boots
- User Story 1.19: As a regular/admin user I can click on the "Jerseys" filter, and filter by Leinster, Munster, Ulster or All Jerseys
- User Story 1.20: As a regular/admin user I can click on the "Accessories" filter, and filter by Balls, Gum shields, Protection or All Accessories
- User Story 1.21: As a regular/admin user if I encounter an error on the site, I will be navigated to the applicable 400, 403, 404 or 500 error page 

### Feature 2 Footer
#### Description feature 2
- A footer is displayed at the bottom of the page
- The product links change dependent on whether the user is logged in/regular user/admin user as per the below user stories
<br>![Footer admin](readme/testing/footer_desktop_admin.PNG)
<br>![Footer regular](readme/testing/footer_desktop_regular.PNG)
- The footer also contains a logo, some text, social media icons(that open in a new tab) and product links for Rugby Boots, Jerseys and Accessories
- A user can sign up for the mailing list by entering their email and clicking the "Signup" button
<br>![Mailing list](readme/testing/mailing_list_email.PNG)
#### User Stories feature 2
- User Story 2.1: As an admin/regular user logged in four text messages are displayed with icons regarding delivery, packaging, dispatch and knowledge
- User Story 2.2: As a regular user the footer is displayed with a logo, product links(Rugby Boots, Jerseys, Accessories), website links(Profile/News/Sale)
- User Story 2.3: As an admin user logged in the footer is displayed with a logo, product links(Rugby Boots, Jerseys, Accessories), website links(Product Management/News Item Management)
- User Story 2.4: As a regular user I can sign up for a newsletter by entering my email address and clicking Signup. I will receive an email after signing up

### Feature 3 Register
#### Description feature 3
- A regular user can register for an account.
- The user must provide a valid email address, email address(confirmation), username, password, password confirmation
<br>![Register](readme/testing/register_desktop.PNG)
- These 5 fields are  mandatory and a user cannot register the same details twice for an account
<br>![Register error](readme/testing/registration_fields.PNG)
- A confirmation link is sent to the users email address, they must click on the verification link to verify the account.
<br>![Email content](readme/testing/verification_email_content.jpg)
- The user must confirm their email address
<br>![Confirm email](readme/testing/confirm_email.jpg)
<br>![Email confirmed](readme/testing/email_confirmed.jpg)
- Once that is done they can sign in to the website with their username/email address and password
#### User Stories feature 3
- User Story 3.1: As a regular user I can register on the website by providing an email address, email address(confirmation), username, password, password confirmation
- User Story 3.1: As a regular user I will receive an email to verify my account after registering
- User Story 3.1: As a regular user I can log in to my account once I click on the verification link in the email I receive regarding my registration

### Feature 4 Login
#### Description feature 4
- An admin/regular user can log in to the website using their username or email address and password
- Both fields are mandatory
- Once logged in the user will be navigated to the homepage
<br>![Email confirmed](readme/testing/login_fails_desktop.PNG)
- The user must have an account in the system, and they must enter the correct  username or email address and password
- If the user needs to request a password, they can click on the Forgot Password link
<br>![Forgot Password](readme/testing/password_reset_email.PNG)
- They enter their email address, and they are emailed reset their password. Once they do this they can log in
<br>![Password updated](readme/testing/password_updated_desktop.PNG)
#### User Stories feature 4
- User Story 4.1: As an admin/regular user I can log in to the website using my username or email address and password. Both fields are mandatory. Once correct, I will be navigated to the homepage and a message displayed
- User Story 4.2: As an admin/regular user I can request a new password if I forget my current password. I will receive an email to reset my password. Once I reset I can log in

### Feature 5 Products and Product Detail Pages
#### Description feature 5
- A user view the products page with product count and with each product image, title, category, price and presale price
<br>![Products Desktop](readme/testing/products_desktop.PNG)
<br>![Products Tablet](readme/testing/products_tablet.PNG)
- The user can sort the products by Price(high to low, low to high), Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)
- If there are more than four products on a page, the page is paginated
- A product detail page displays all the product information (image, description, colour, code, rating, category, description, features and reviews(the latest first))
<br>![Products Detail 1](readme/testing/product_detail_desktop.PNG)
- If the product has a size(boots have size 8-13, jerseys have a size XS-XXL) this information is displayed
<br>![Products Detail 2](readme/testing/product_detail2_desktop.PNG)
- A review can be added to a product, only one review per user. 
<br>![Products Add Review repeat](readme/testing/add_review_repeat_desktop.PNG)
- A review consists of a rating(1-5) and a comment
<br>![Products Add Review Tablet](readme/testing/add_review2_tablet.PNG)
<br>![Products Add Review Mobile](readme/testing/add_review2_mobile.PNG)
- A user can delete a review they wrote, but not another users review
- If a product does not have a review, a message is displayed on the products page and product detail page
<br>![Products No Review](readme/testing/products_price_desktop.PNG)
- A user must have an account and be logged in to review a product, otherwise they will see a link to login or create an account
<br>![Review Not logged in](readme/testing/add_review_notloggedin_desktop.PNG)

#### User Stories feature 5
- User Story 5.1: As a regular user I can view the products page with product count and with each product image, title, category, price and presale price(if applicable)
- User Story 5.2: As a regular user I can sort the products by Price(high to low, low to high), Rating(high to low, low to high), Name(A-Z, Z-A), Category(A-Z, Z-A)
- User Story 5.3: As a regular user if there are more than four products on the page, the page is paginated with four products per page
- User Story 5.4: As a regular user if I click on a product I will be navigated to the product detail page
- User Story 5.5: As a regular user I can view the product image, description, colour, code, rating, category, description, features and reviews(the latest first)
- User Story 5.6: As a regular user if the product is in my favourites list, the heart colour is red in the product detail page. If not the heart colour is white
- User Story 5.7: As a regular user I can add a review, by selecting a rating and entering a comment(both fields are mandatory), the review is displayed and a message is displayed
- User Story 5.8: As a regular user I can delete a review I have added(the comment and rating is removed from the product detail), but I cannot delete other users review
- User Story 5.9: As a regular user if there are more than four reviews for a product, the reviews are paginated
- User Story 5.9: As a regular user I can click on the Keep Shopping button on the product detail page, and it will navigate the user to the products page
- User Story 5.9: As a regular user I can set the product size(if applicable for the product) and quantity for a product (one plus)
- User Story 5.10: As an admin user I can view the Add product page by clicking on the Product Management link.
- User Story 5.11: As an admin user I can view the Edit product page by clicking on the Edit button on the product. 
- User Story 5.12: As an admin user I can click on a product, and I am navigated to the product detail page. I can edit or delete the product by clicking on the Edit or Delete links on the page
- User Story 5.13: As an admin user I can delete a review a regular user has added
- User Story 5.14: As a regular user who has not registered or logged into the website, I cannot add a review to a product

### Feature 6 Sale items page
#### Description feature 6
- The app "products" contains the admin, forms, views, models and templates(sale_items) for this functionality
- A regular user can view products with sale prices
- A product that is categories as a sale item is a product that has a price and a presale price
- The sale items page is paginated if there are more than four sale items
- If a user clicks on a sale item, they are brought to its relevant product detail page
<br>![Sale items Desktop](readme/testing/sale_items_desktop.PNG)
- All users see the same sale items and any product can be a sale item
<br>![Sale items Tablet](readme/testing/sale_items_tablet.PNG)
#### User Stories feature 6
- User Story 6.1: As a regular user I can view the products with sale prices, the product image, category, presale price and price is displayed
- User Story 6.2: As a regular user if I click on a product in the sale items, I am navigated to the product detail page for that product
- User Story 6.3: As a regular user if there are more than four products on the sale items page, the page is paginated with four products per page

### Feature 7 Favourites page
#### Description feature 7
- The app "favourites" contains the admin, forms, views, models and templates for this functionality
- A user has their own favourites list and that is unique to them
- A user must have an account and be logged in to add products to the favourites list, otherwise they will be navigated to the login page
<br>![Favourites 2](readme/testing/favourites2_desktop.PNG)
<br>![Favourites](readme/testing/favourites_desktop.PNG)
- There is no limit to how many products can be in a users favourites list and if there are more than four the paginated is paginated
- A user can add a product to their favourites list by clicking on the heart icon on the product detail page, the colour will change to red with a red border
<br>![Add Favourite](readme/testing/favourites_add_desktop.PNG)
- A user can remove a product from their favourites list by clicking on the heart icon on the product detail page, the colour will change to white with a red border
- Alternatively the user can click on the Delete button on the favourites page and confirm the removal from their favourites
<br>![Delete Favourite](readme/testing/favourites_delete_desktop.PNG)
#### User Stories feature 7
- User Story 7.1: As a regular user I can click on the heart icon on a product in the product details page, a message is displayed, and the product is added to my favourites list
- User Story 7.2: As a regular user I can click on the heart icon on a product that is already in my favourites list, a message is displayed, and the product is removed to my favourites list
- User Story 7.3: As a regular user I can view my favourites list, the product image, category, presale price and price is displayed
- User Story 7.4: As a regular user I remove a product from my favorites list by clicking on the Delete button on the product. A confirmation modal and message is displayed
- User Story 7.5: As a regular user if there are more than four products in my favourites page, the page is paginated with four products per page
- User Story 7.6: As a regular user who has not registered or logged into the website, I cannot add an item to the favourites and will be brought to the login page

### Feature 8 News Page
#### Description feature 8
- The app "news" contains the admin, forms, views, models and templates for this functionality
- A regular user can view news items, and add a comment to a news item.
- A user must have an account and be logged in to comment on a news item, otherwise they will see a link to login or create an account
- Four news items are displayed and the page is paginated if there are more than four news entries
<br>![News desktop](readme/testing/news_desktop.PNG)
<br>![News tablet](readme/testing/news_tablet.PNG)
<br>![News mobile](readme/testing/news_mobile.PNG)
- They can click on the read more button to open up the news item and from there can add a comment
- Comments are paginated if there are more than 2 comments on a news item
<br>![News item](readme/testing/news_item_desktop.PNG)
<br>![News Delete Comment](readme/testing/news_delete_comment_desktop.PNG)
- They can also delete a comment on a news item, they can do so by clicking on the delete button and confirming.
<br>![News Delete Comment Admin](readme/testing/news_delete_comment_admin_desktop.PNG)
- An admin user can delete a comment added by a regular user, they can do so by clicking on the delete button and confirming.
#### User Stories feature 8
- User Story 8.1: As a regular user I can view 4 news items on a page with a news image, and 150 characters of the news item text and a read more button
- User Story 8.2: As a regular user I can click on the read more button on the News page, I will be navigated to the news item with a news item image, news item text and any comments will be displayed
- User Story 8.3: As a regular user I can add a comment to a news item
- User Story 8.4: As a regular user I can delete a comment that I had originally added on a news item
- User Story 8.5: As an admin user I can delete a comment on a news item, even if I did not add the comment
- User Story 8.6: As a regular user who has not registered or logged into the website, I cannot add a comment to a news item

### Feature 9 Profile Page
#### Description feature 9
- A regular user can update their default delivery information as per the user stories below
- A use must be logged in to see their profile page
- This is the information that is displayed when the user is checking out an order
- A user can view and update their Default delivery information
<br>![Default delivery information](readme/testing/myprofile_desktop.PNG)
- The user can also view their past orders and click on an order to view the order details
<br>![Order History](readme/testing/order_history_desktop.PNG)
- This data is consistent with the information they supplied when they made the order
#### User Stories feature 9
- User Story 9.1: As a regular user I can view my Default delivery information: Phone Number, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country
- User Story 9.2: As a regular user I can update my Default delivery information: Phone Number, Street Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country
- User Story 9.3: As a regular user I can view my order history(Order Number, Date, Items and Order Total)
- User Story 9.4: As a regular user I can click on an order number to view the order information (Order number, Order date/time, Full NameStreet Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total)

### Feature 10 Product Management
#### Description feature 10
- An admin user can add, edit and delete products
- To add a product the user can click on the Product Management link in My Account
- They must enter a name, category, price, colour, code, description and can optionally add a feature (1-4), has Sizes(Unknown, Yes, No), Rating, Pre-sale price, Image url, upload an image
<br>![Add Product](readme/testing/10_1_1_desktop.PNG)
- The product is then added and visible on the products page, and by clicking on the product itself
- The image is stored in the AWS S3 bucket
<br>![Product Detail](readme/testing/product_detail_desktop.PNG)
- An admin user can edit a product, by updating the relevant field(s)
<br>![Edit Product](readme/testing/10_2_1_desktop.PNG)
- An admin user can delete a product, by clicking on the delete link on the product detail page or the delete button on the products page
- A confirmation modal is displayed asking the user to confirm the deletion
- All reviews on the product are subsequently deleted
<br>![Delete Product](readme/testing/10_3_1_desktop.PNG)
#### User Stories feature 10
- User Story 10.1: As an admin user I can add a product by clicking on the Product Management link in My Account. I must enter a name, category, price, colour, code, description and can optionally add a feature (1-4), has Sizes(Unknown, Yes, No), Rating, Pre-sale price, Image url, upload an image and click the 
Add Product button. Clicking cancel navigates the user to the product page.
- User Story 10.2: As an admin user I can edit a product by clicking on the Edit button on the Products page for the product. I can update thea name, category, price, colour, code, description, feature (1-4), has Sizes(Unknown, Yes, No), Rating, Pre-sale price, Image url, update an image and click the 
Edit Product button. Clicking cancel navigates the user to the product page
- User Story 10.3: As an admin user I can delete a product by clicking on the Delete button on the product. A modal will appearing asking to confirm, and a message displayed once I confirm. 

### Feature 11 News item Management
#### Description feature 11
- The app "news" contains the admin, forms, views, models and templates for this functionality
- An admin user can add/edit or delete a news item, a regular user can only view published news items
- They can also set the status of a news item to Published or Draft
- If a news item is set to Draft, admin and regular users will NOT see this item on the News Page
- If a news item is set to Published, admin and regular users will see this item on the News Page
- To add a news item the user can enter a title, text and image
<br>![Add News Item](readme/testing/add_news_item_desktop.PNG)
- The news item is displayed in the Manage News Item page, this is a table with 5 columns, 2 containing Edit and Delete buttons
<br>![Manage news items](readme/testing/manage_news_items_desktop.PNG)
- To edit a news item the user can enter a title, text and image after clicking on the Edit button in the Manage News Item page 
<br>![Edit News Item desktop](readme/testing/edit_news_item_desktop.PNG)
<br>![Edit News Item tablet](readme/testing/edit_news_item_tablet.PNG)
- To delete a news item, click on the delete button and confirm, this will also delete all comments on the news item
<br>![Delete News Item](readme/testing/delete_news_item_desktop.PNG)
#### User Stories feature 11
- User Story 11.1: As an admin user I can view News items by clicking on the News Item Management link under My account. The news item count and title, create date, status(Published or Draft), and Edit and Delete buttons is displayed
- User Story 11.2: As an admin user if there are more than four news items added, the page is paginated
- User Story 11.3: As an admin user I can add a news item, by clicking on the Add button. I can enter a Title and news item text, add an image and set the item to Published or Draft
- User Story 11.4: As an admin user I can edit a news item, by clicking on the Edit button for the news item. I can update a Title and news item text, update an image and update the item to Published or Draft
- User Story 11.5: As an admin user if a news item is set to Draft, admin and regular users will NOT see this item on the News Page.
- User Story 11.6: As an admin user if a news item is set to Published, admin regular users will see this item on the News Page.
- User Story 11.7: As an admin user I can delete a news item, and I will be asked to confirm the deletion

### Feature 12 Bag and Checkout
#### Description feature 12
Note: Some screenshots show dollars, I have since changed all instances in the project to euros
- A user can add items to a bag, if the bag is empty a message is displayed
- A user can update the quantity or remove an item from their shopping bag
<br>![Bag Empty](readme/testing/12_2_desktop.PNG)
- An order over 99 euros means free delivery. An order less than 99 incurs a 10% delivery charge
<br>![Bag 1](readme/testing/12_1_desktop.PNG)
<br>![Bag 1](readme/testing/12_1_tablet.PNG)
<br>![Bag 2](readme/testing/12_4_desktop.PNG)
- The user can "checkout" and their details will be displayed.
- The fields are: (Full Name, email address, both mandatory) and Delivery Information: Phone Number(mandatory), Street Address 1(mandatory), Street Address 2, Town or City(mandatory, County, State or Locality, Postal Code and Country(mandatory)), which is populated from my profile if filled in
<br>![Order](readme/testing/12_5_desktop.PNG)
<br>![Order mobile](readme/testing/12_5_mobile.PNG)
- The user receives a confirmation email to their email address supplied
<br>![Email](readme/testing/email_confirmation_over99.PNG) 
- The order is available on the user profile page,a nd they can click on the order itself
<br>![User profile](readme/testing/12_6_desktop.PNG)
- A regular user not logged in, I can add items to my bag and make a purchase
<br>![Not logged in 1](readme/testing/not_logged_in_checkout_desktop.PNG) 
<br>![Not logged in 2](readme/testing/not_logged_in_checkout_success_desktop.PNG) 
<br>![Not logged in 2](readme/testing/not_logged_in_checkout_success_desktop.PNG) 

#### User Stories feature 12
- User Story 12.1: As a regular user I can click on a product, set the size(if applicable) and quantity, click Add to Bag and the product will be added to my bag, a message displayed, and a toast will be displayed with the bag contents
- User Story 12.2: As a regular user I can click on the bag icon, I will be brought to my bag. If there are no items in the bag, a message will be displayed
- User Story 12.3: As a regular user I can click on the bag icon, I will be brought to my bag. If there are items, the product image, detail, price, quantity, subtotal will be displayed for the item. The bag total, delivery(if applicable), grand total would be displayed
- User Story 12.4: As a regular user I can update the quantity or remove an item from my shopping bag
- User Story 12.5: As a regular user I can click on the Secure Checkout button on the bag page or toast message, and I will be brought to the Checkout page
- User Story 12.6: As a regular user on the checkout page I can set my details(Full Name, email address, both mandatory) and Delivery Information(Phone Number(mandatory), Street Address 1(mandatory), Street Address 2, Town or City(mandatory, County, State or Locality, Postal Code and Country(mandatory), which is populated from my profile if filled in
- User Story 12.7: As a regular user on the checkout page I can view the order summary(item image, title, size, quantity, subtotal, order total, delivery, grand total)
- User Story 12.8: As a regular user on the checkout page if the order total is greater than 99 euros, there is no delivery charge
- User Story 12.9: As a regular user on the checkout page if the order total is less than 99 euros, there is delivery charge(10% of the order total) A message is displayed to the user on the toast message of what they need to add to the bag to avail of no delivery charge
- User Story 12.10: As a regular user on the checkout page if I click "Save this delivery information to my profile", the details entered will be saved on the users profile
- User Story 12.11: As a regular user on the checkout page I can enter a credit card number(16 digits), expiry date(2 digits/2digits), cvc(3 digits) and a postal code(up to 5 digits), these fields are mandatory
- User Story 12.12: As a regular user on the checkout page if I click the Keep Shopping button I will be navigated to the products page
- User Story 12.13: As a regular user on the checkout page if I click the Complete Order button, and the transaction is not successful, a message will be displayed
- User Story 12.14: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the user will be navigated to a checkout success page, and an email is sent to the user
- User Story 12.15: As a regular user on the checkout page if I click the Complete Order button, and the transaction is successful, the order is saved to my order history in My profile page
- User Story 12.16: As a regular user on the checkout success page, the Order details will be displayed (Order number, Order date/time, Full NameStreet Address 1, Street Address 2, Town or City, County, State or Locality, Postal Code and Country, Phone Number, Order Total, Deliver, Grand Total) and a link to the sales item page is displayed
- User Story 12.17: As a regular user not logged in, I can add items to my bag and make a purchase

### Feature 13 Admin
#### Description feature 13
- As per the user stories below there are a number of admin views that have been configured at https://ci-ms4-loverugby.herokuapp.com/admin
- They give excellent CRUD operations to the data in the Postgres database as well as search and filter options
- They are as follows:
- Order
<br>![Order](readme/testing/13_1_order.PNG)
- Favourites
<br>![Favourites](readme/testing/13_3_favourites.PNG)
- News
<br>![News](readme/testing/13_5_news.PNG)
- Products
<br>![Products](readme/testing/13_7_products.PNG)
- Users
<br>![Users](readme/testing/13_9_users.PNG)
- Comments 
<br>![Comments](readme/testing/13_11_comments.PNG)
- Reviews
<br>![Reviews](readme/testing/13_14_reviews.PNG)
- Categories
<br>![Categories](readme/testing/13_15_categories.PNG)

#### User Stories feature 13
- User Story 13.1: As an admin user I can view users orders in the django admin page and can view order number, date, full name, order total, delivery cost, grand total
- User Story 13.2: As an admin user I can view users orders in the django admin page and can search by order number, full name and filter by order number, full name and order date
- User Story 13.3: As an admin user I can view users favourites in the django admin page and can view all favourites
- User Story 13.4: As an admin user I can view users favourites in the django admin page and can search and filter by username
- User Story 13.5: As an admin user I can view news items in the django admin page and can view a news item title, user, news item text and image
- User Story 13.6: As an admin user I can view news items in the django admin page and can search and search by title, user, news item text and image, create date, update date status and filter by title, user, create date
- User Story 13.7: As an admin user I can view products in the django admin page and can view a products code, name, category, has sizes, price, presale price, rating, image, image url
- User Story 13.8: As an admin user I can view products in the django admin page and can view search and filter by code, category, name and price
- User Story 13.9: As an admin user I can view users in the django admin page and can view their username, email address, first name, last name, staff status
- User Story 13.10: As an admin user I can view users in the django admin page and can search by username and email address and  filter by staff status, superuser status and active status
- User Story 13.11: As an admin user I can view news items comments in the django admin page and can view a comment user, title, text and create date
- User Story 13.12: As an admin user I can view news items comments in the django admin page and can filter by user, title, create date and search by user, title, text and create date
- User Story 13.13: As an admin user I can view reviews in the django admin page and can view a review user, product, rating, text and create date
- User Story 13.14: As an admin user I can view reviews in the django admin page and can filter by user, product rating, create date and search by user, product, rating, text
- User Story 13.15: As an admin user I can view categories in the django admin page and can view a category name and friendly name

##  Features Left to Implement
- I am content with what was implemented. The site is a feature rich site
- However, here are some additional "nice to have" features and updates that could be added to the project

Number | Update  
 ------------ | ------- |
1 | Increased code coverage and unit tests in the checkout view.py for stripe payments |
2 | A new release section displaying new release products |
3 | Improved searching and filtering on the products page, a side panel filter |
4 | Integration with a Continuous Integration application, for example: Travis CI or Semaphore CI |
5 | Improved pagination look/feel on products page |
6 | I could have made some part of the code more generic and moved it to the util.py package(that currently contains pagination code only) |
7 | The functionality to add and display multiple images per product |

# Technologies Used
## Languages 
- HTML (https://en.wikipedia.org/wiki/HTML)
    - The project uses html to build the relevant pages
- CSS (https://en.wikipedia.org/wiki/CSS)
    - The project uses CSS to style the relevant pages
- Javascript (https://www.javascript.com/)
    - Javascript was used for all scripting on the site 
- Django (https://www.djangoproject.com/)
    - Django is the framework used in this project
    - The Django templating language was used to render pages
    - The Django unit test library was used for unit tests (https://docs.djangoproject.com/en/3.2/topics/testing/overview/)
- Python v3.9 (https://www.python.org/)
    - Python was used for server side coding on the project, a number of libraries were also used(The requirements.txt file 
  contains this list):
      - asgiref==3.4.1 (Support for Python asynchronous web apps and servers to communicate with each other) 
      - boto3==1.18.47 (Python SDK for AWS)
      - botocore==1.21.47 (Python SDK for AWS) 
      - dj-database-url==0.5.0 (Support for DATABASE_URL environment variable)
      - Django==3.2.7 (Web framework)
      - django-allauth==0.41.0 (Web framework authentication)
      - django-countries==7.2.1 (ISO 3166 countries list)
      - django-crispy-forms==1.12.0 (Django rendering of forms)
      - django-storages==1.11.1 (Django storage backend for AWS S3)
      - gunicorn==20.1.0 (Python WSGI Http server)
      - jmespath==0.10.0 (Full suite of data driven testcase)
      - oauthlib==3.1.1 (Framework for oauth1 and oauth2)
      - Pillow==8.3.2 (Imaging library)
      - psycopg2-binary==2.9.1 (Postgres adapter)
      - python3-openid==3.2.0 (Support for the OpenID decentralized identity system)
      - pytz==2021.1 (Interface to the IANA database, which uses ASCII name)
      - requests-oauthlib==1.3.0 (Authentication support for Requests)
      - s3transfer==0.5.0 (Python library for managing Amazon S3 transfers)
      - sqlparse==0.4.1 (Non-validating SQL parser for Python)
      - stripe==2.60.0 (SDK for processing payments)

    
## Libraries and other resources
- Bootstrap 5.0 (https://getbootstrap.com/docs/5.0)
    - The project uses the bootstrap library for some UI components in the website (Buttons, Card, Carousel, Modal, Pagination, Navbar)
- Postgres (https://www.postgresql.org/)
  - The deployed project on Heroku uses a Postgres database
- SQLLite (https://www.sqlite.org/index.html)
  - The database uses in local development was a SQLLite database
- Gitpod (https://gitpod.io/)
    - Gitpod was used as an IDE for the project initially, then I switched to Pycharm
- Pycharm (https://www.jetbrains.com/pycharm/)
    - Pycharm was the main IDE used on the project
- Github (https://github.com/)
    - GitHub was used to store the project code in a repository
- Google Fonts (https://fonts.google.com/)
    - Google font Poppins was used as the website font
- Balsamiq (https://balsamiq.com/)
    - Balsamiq was used to create the website wireframes
- Font Awesome (https://fontawesome.com/)
    - Font awesome was used to provide the relevant fonts/icons for the website
- JQuery (https://jquery.com)
    - JQuery was used in some javascript files for DOM manipulation
- TinyPNG (https://tinypng.com/)
    - TinyPNG was used to compress images to improve performance and reduce space
- CSS Validation Service (https://jigsaw.w3.org/css-validator/)
   - CSS validation service for validation the css in the project  
- HTML Markup Validation Service (https://validator.w3.org/)   
    - HTML validation service for validation the css in the project  
- Chrome dev tools (https://developers.google.com/web/tools/chrome-devtools)
    - For troubleshooting and debugging of the project code
- Chrome Lighthouse (https://developers.google.com/web/tools/lighthouse)
    - For performance, accessibility, progressive web apps, SEO analysis of the project code
- Responsive Design (http://ami.responsivedesign.is/)
    - Website for generating the responsive image in this README
- JS Fiddle (https://jsfiddle.net/)
    - Used for testing html and css concepts
- GitHub Wiki TOC generator (https://ecotrust-canada.github.io/markdown-toc/)
    - Used for generating a table of contents for this README
- Gofullpage chrome plugin  (https://chrome.google.com/webstore/detail/gofullpage-full-page-scre)
    - This plugin was used to take full page screenshots for testing images
- Python online interpreter (https://www.programiz.com/python-programming/online-compiler/)
    - For testing python code snippets
- Unittest (https://docs.djangoproject.com/en/3.2/topics/testing/overview/)
    - For Python unit testing
- JSHint (https://jshint.com/)
  - For javascript code quality
- PEP8 (https://www.python.org/dev/peps/pep-0008/)
  - I used the pep8 code analysis plugin in Pycharm to check for pep8 errors
- Stripe (https://www.stripe.com)
  - For processing a test credit card to test a payment as part of an order
- Coverage (https://coverage.readthedocs.io/en/6.1.2/)
  - For unit test code coverage reports
- Quick Database diagrams (https://www.quickdatabasediagrams.com)
  - For the database schema diagram
- Temp mail (http://temp-mail.org/en/)
  - For a temporary email account for test registrations

# Testing
The testing information and results for this project are documented in [TESTING.md](TESTING.md)

# APIs and configuration
The project also uses a number of API's and configuration, below are the steps to configure the API in your environment

## Email JS
1. Create an account at emailjs.com 
2. In the integration screen in the emailjs dashboard, note your userid, this is a unique string for your users
3. Create an email service in the Email Services section and note the id, for example "gmail"
4. Create an email template in the Email templates section and note the id, for example "love_rugby"
5. Update the script /static/js/sendEmail.js, the method sendMail with your user id, email service id and email template id

## Google emails
To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required
1. Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings
2. Turn on 2-step verification and follow the steps to enable
3. Click on app passwords, select Other as the app and give the password a name, for example Django
<br>![App password](readme/misc/gmail_app_password.png)
4. Click create and a 16 digit password will be generated, note the password down
5. In the env.py file, create an environment variable called EMAIL_HOST_PASS with the 16 digit password
6. In the env.py file, create an environment variable called EMAIL_HOST_USER with the email address of the gmail account
7. Set and confirm the following values in the settings.py file to successfully send emails
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_USE_TLS = True</code>
<br><code>EMAIL_PORT = 587</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')</code>
<br><code>DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')</code>
8. You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in your production instance, for example Heroku

## Stripe
1. Register for an account at stripe.com
2. Click on the Developers section of your account once logged in
3. Under Developers, click on the API keys section
<br>![API keys](readme/misc/stripe_keys1.png)
4. Note the values for the publishable and secret keys
5. In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</code>
6. Back in the Developers section of your stripe account click on Webhooks
7. Create a webhook with the url of your website <url>/checkout/wh/, for example: https://ci-ms4-loverugby.herokuapp.com/checkout/wh/
8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
<br>![Webhook](readme/misc/stripe_keys2.png)
9. Note the key created for this webhook
10. In your local environment(env.py) and heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</code>
11. Feel free to test out the webhook and note the success/fail attempts for troubleshooting

# Deployment
There are a number of applications that need to be configured to run this application locally or on a cloud based service, for example Heroku

## Amazon WebServices
1. Create an account at aws.amazon.com
2. Open the S3 application and create an S3 bucket named "ci-ms4-rugby-shop"
3. Uncheck the "Block All Public access setting"
4. In the Properties section, navigate to the "Static Website Hosting" section and click edit
5. Enable the setting, and set the index.html and the error.html values
<br>![AWS Static](readme/misc/aws_static.png)
6. In the Permissions section, click edit on the CORS configuration and set the below configuration
<br>![AWS CORS](readme/misc/aws_cors.png)
7. In the permissions section, click edit on the bucket policy and generate and set the below configuration(or similar to your settings)
<br>![AWS Bucket Policy](readme/misc/aws_bucket_policy.png)
8. In the permissions section, click edit on the Access control list(ACL)
9. Set Read access for the Bucket ACL for Everyone(Public Access)
10. The bucket is created, the next step is to open the IAM application to set up access
11. Create a new user group named "ci-ms4-rugby-shop"
12. Add the "AmazonS3FullAccess" policy permission for the user group
<br>![AWS Bucket Policy](readme/misc/aws_user_group.png)
13. Go to "Policies" and click "Create New Policy"
14. Click "Import Managed Policy" and select "AmazonS3FullAccess" > Click 'Import'.
15. In the JSON editor, update the policy "Resource" to the following
<br><code>"Resource": [</code>
<br><code>"arn:aws:s3:::ci-ms4-rugby-shop",</code>
<br><code>"arn:aws:s3:::ci-ms4-rugby-shop/*"</code>
<br><code>]</code>
16. Give the policy a name and click "Create Policy"
17. Add the newly created policy to the user group
<br>![AWS Bucket Policy](readme/misc/aws_policy.png)
18. Go to Users and create a new user
19. Add the user to the user group ci-ms4-rugby-shop
20. Select "Programmatic access" for the access type
21. Note the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID variables, they are used in other parts of this README for local deployment and Heroku setup
22. The user is now created with the correct user group and policy
<br>![AWS Bucket Policy](readme/misc/aws_user.png)
23. Note the AWS code in settings.py. Note an environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage
<br>![AWS Settings](readme/misc/aws_settings.PNG)
24. These settings set up a cache policy, set the bucket name, and the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY that you set in your aws account
25. The configuration also requires the media/static folders that must be setup in the AWS S3 bucket to store the media and static files 

## Local Deployment
To run this project locally, you will need to clone the repository
1. Login to GitHub (https://wwww.github.com)
2. Select the repository pmeeny/CI-MS4-LoveRugby
3. Click the Code button and copy the HTTPS url, for example: https://github.com/pmeeny/CI-MS4-LoveRugby.git
4. In your IDE, open a terminal and run the git clone command, for example 

    ```git clone https://github.com/pmeeny/CI-MS4-LoveRugby.git```

5. The repository will now be cloned in your workspace
6. Create an env.py file(do not commit this file to source control) in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<br><code>import os</code>
<br><code>os.environ.setdefault("SECRET_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("STRIPE_PUBLIC_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("STRIPE_SECRET_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("STRIPE_WH_SECRET", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("AWS_ACCESS_KEY_ID", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("AWS_SECRET_ACCESS_KEY", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("EMAIL_HOST_USER", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("EMAIL_HOST_PASS", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("USE_AWS", TO BE ADDED BY USER)</code>
<br><code>os.environ.setdefault("DATABASE_URL", TO BE ADDED BY USER)</code>
7. Some values for the environment variables above are described in different sections of this readme
8. Install the relevant packages as per the requirements.txt file
9. In the settings.py ensure the connection is set to either the Heroku postgres database or the local sqllite database
10. Ensure debug is set to true in the settings.py file for local development
11. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in settings.py
12. Run "python3 manage.py showmigrations" to check the status of the migrations
13. Run "python3 manage.py migrate" to migrate the database
14. Run "python3 manage.py createsuperuser" to create a super/admin user
15. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories
16. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products
17. Run "python3 manage.py loaddata news.json" on the news file in news/fixtures to create the news items(optional)
18. Start the application by running <code>python3 manage.py runserver</code>
19. Open the application in a web browser, for example: http://127.0.0.1:8000/

## Heroku and Postgres Database
To deploy this application to Heroku, run the following steps.
1. Create an account at heroku.com
2. Create an app, give it a name for example ci-ms4-loverugby, and select a region
3. Under resources search for postgres, and add a Postgres database to the app

![Heroku Postgres](readme/misc/heroku_postgres.png)
    
4. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
5. Install the plugins dj-database-url and psycopg2-binary.
6. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
7. Create a Procfile with the text: web: gunicorn rugby_shop.wsgi:application for example
8. In the settings.py ensure the connection is to the Heroku postgres database
9. Ensure debug is set to false in the settings.py file
10. Add localhost/127.0.0.1, and ci-ms4-loverugby.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
11. Run "python3 manage.py showmigrations" to check the status of the migrations
12. Run "python3 manage.py migrate" to migrate the database
13. Run "python3 manage.py createsuperuser" to create a super/admin user
14. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories
15. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products
16. Install gunicorn and add it to the requirements.tx file using the command pip3 freeze > requirements.txt
17. From the CLI login to Heroku using the command heroku git:remote -a ci-ms4-loverugby
18. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a ci-ms4-loverugby
19. Push the code to Heroku using the command git push heroku master
20. Ensure the following environment variables are set in Heroku
<br>![Heroku Env variables](readme/misc/heroku_env_variables.png)
21. Connect the app to GitHub, and enable automatic deploys from main
<br>![Heroku Postgres](readme/misc/heroku_deployment.png)
    
22. Click deploy to deploy your application to Heroku for the first time
23. Click on the link provided to access the application
24. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

# Credits
- The project is based on the Boutique Ado project by the Code Institute and was used as a basic for my project (https://github.com/Code-Institute-Solutions/boutique_ado_v1/)
- For the product, favourites and sale items pages, I used some html and css code from https://bootstrapious.com/p/bootstrap-photo-gallery as a basis
for the memories gallery
- I used html/css code, then tweaked it accordingly for the site footer: https://jsfiddle.net/bootstrapious/c7ash30w/
- For the send-email functionality I used some code from the code institute module from the course
- For pagination, I found this tutorial invaluable https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
- For Div alignment I used code from here: https://www.freecodecamp.org/news/how-to-center-anything-with-css-align-a-div-text-and-more/ 
and https://blog.hubspot.com/website/center-div-css
- For Django Comments, I found this link useful: https://djangocentral.com/creating-comments-system-with-django/
- For unit testing, I found the unit test code in the Code Institute chapter Hello Django very useful and this link also: 
https://www.section.io/engineering-education/django-unit-testing/#testing-views where it gave me a good idea on the type of unit tests
to write
- Bootstrap 5.0, I used some sample code from https://getbootstrap.com/docs/5.0/customize/components/ for a number of 
  component's(Buttons, Card, Carousel, Modal, Pagination, Navbar)
- For combining filtering and pagination, I used code from https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/
- For mobile flexbox updates, I used code examples from https://www.digitalocean.com/community/tutorials/css-improve-responsiveness-flex-wrap
- I used some code and found the examples useful in https://www.youtube.com/watch?v=OvTs8BMLb7o and https://www.youtube.com/watch?v=H4QPHLmsZMU for the favourites and reviews functionality
in the relevant applications
- I used stackoverflow.com a lot for programming issues, for example: https://stackoverflow.com/questions/56332524/how-to-update-queryset-value-in-django

# Content
- Font Awesome (http://fontawesome.com)    
    - The icons used on the site from font awesome
- Fonts (https://fonts.google.com/)    
    - The text font(Poppins) is from Google fonts
- Product information, news (text) was taken from https://www.lifestylesports.com/ie/rugby/

<br>

# Media
- Product information, news (images) was taken from https://www.lifestylesports.com/ie/rugby/
- News stories and images was taken from https://www.theguardian.com/ and https://www.lifestylesports.com/ie/rugby/
 <br>

# Acknowledgements
- I would like to thank my fiancée Mary for her help, constant support and ideas for the website, my son Liam, and also to my dog Lily for her company during development of the website.
- I would like to thank my mentor Mo Shami for his input, help and feedback.
