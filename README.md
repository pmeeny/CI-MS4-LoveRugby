# Love Rugby shop
Love Rugby is a website that allows users

- There are two types of users, and I have set up accounts for both
    - An admin user account has been set up with username/password of administrator/Password123
    - A regular user account has been set up with username/password of mikemurphy/Password123
<br>

**View the live site [here](https://ci-ms4-loverugby.herokuapp.com/)**
<br><br>
![Responsive site example](readme/responsive/responsive.PNG)

# Table of Contents

# Project Overview
- This project is a website that allows users to add/edit/delete football memories for given tournament for submission as milestone project 3 as part of the Code Institute - Diploma in Software Development (Full stack) course.
- The website is deployed using Heroku pages at the following url: [Football Memories](https://ci-ms3-footballmemories.herokuapp.com/)
- The repository on GitHub that contains the website source code and assets is available at the following url: [Code Repository](https://github.com/pmeeny/CI-MS3-FootballMemories)
- The website was built with a responsive look and feel for desktop, tablet and mobile devices

# UX
## Strategy
### Primary Goal
The primary goal of the website from the site 
owners perspective is as follows:
- To 

The primary goal of the website from a site users perspective is as follows:
- To 

## Structure
### Website pages
I have structured the website into 19 pages, each with clear, concise structure, information and purpose. I use the Bootstrap grid system throughout, which gave a consistent structure and responsive design "out of the box"

### Code Structure.

    
### Database
- The website is a data-centric one with html, javascript, css used with the bootstrap framework as a frontend
- The backend consists of Python, flask and jinja templates with a database of a mongodb open-source document-oriented database


#### Conceptual database model
The first step in the database design was to create a conceptual data model. The helped me understand the design at a conceptual level while enabling me to understand the required collections in the database
![conceptual](football_memories/static/images/database_design/conceptual_design_model.png)

#### Physical database model
From the conceptual database model I created the physical database model. This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the mongo database(mongodb)
<br>
Note: The lines/links in the diagram denote the relationship in the python code between the different collection fields and not foreign keys, for example 
when a memory is created in the memories' collection, it also stores the tournament name from the tournament's collection.
![conceptual](football_memories/static/images/database_design/physical_design_model.png)

#### Postgres DB database information
- One production database(football_memories_prod) was created to store site information, it contains five collections described below


#### Model
- The model

### Amazon Web Services S3 bucket
While mongodb stores the majority of the users' data in the database, any images added
by a regular user or admin user when adding a new tournament or memory is stored in an 
Amazon Web services(AWS) S3(storage) bucket. I made this choice for performance reasons(https://aws.amazon.com/s3/faqs/)
and to challenge myself to learn how to integrate the site with AWS.
Here are the steps I took for the integration
1. I created an account with AWS, and created an S3 bucket named "ci-ms3-football-memories"
![s3 bucket](football_memories/static/images/readme/aws_s3_bucket.PNG)
2. I created a user in AWS IAM, and gave the user the AmazonS3FullAccess permission   
3. I then gave the bucket policy the necessary permissions to allow my application to access 
the S3 bucket
![s3 bucket policy](football_memories/static/images/readme/aws_s3_policy.PNG)
4. I imported the Boto3 python library (https://boto3.amazonaws.com/) in the util.py file
I made a design decision to have an util.py in an util flask route python file that would be used to store common code
that could be used by multiple routes
5. The relevant s3 variables for the bucket name, url and access/secret keys are defined at the top of the util.py file
   <code>
   s3_bucket_name = "ci-ms3-football-memories"
s3_bucket_url = "https://ci-ms3-football-memories.s3.eu-west-1.amazonaws.com/"
client = boto3.client('s3', 
                aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"))
   </code>
6. A single function was written named storeImageAWSS3Bucket that takes one parameter, the filename to store
7. This single function is used by the tournament and memories routes to store the images in the S3 bucket
8. This function stores a file in an AWS S3 bucket using boto3. The filename is in the form timestamp + name of file added by the user. The timestamp ensures uniqueness for every file added to the s3 bucket allowing users to use the same filename if desired.<code>
   image_file = secure_filename(image.filename)
    image_to_upload = timestamp + image_file</code>
9. The boto3 put_object method is used to store the image taking two parameters, the file name and actual file
<code>s3.Bucket(s3_bucket_name).put_object(Key=image_to_upload, Body=image)</code>
10. An image url is returned, and it is the image url that is stored in the mongodb for the relevant tournament or memory, described below in the two screenshots, field 
names memory_image and tournament_image in the memory and tournament collections
<code>image_url = s3_bucket_url + image_to_upload</code>
![tournaments](football_memories/static/images/database_design/tournaments.PNG)
![memories](football_memories/static/images/database_design/memories.PNG)
   

## Scope
There is overlap in terms of user stories for the two types of users, and they are described below
### User Stories Potential or Existing Customer
The user stories for the website user "regular user" (a potential or existing customer) are described as follows: 
- User Story 1.1: As a regular user the navigation bar is displayed with a logo on all pages for easy navigation, with a burger menu on mobile devices

### User Stories Website Owner
The user stories for the website owner(admin user) are described as follows: 
There is a lot of overlap between the two user types, the admin user however has more administrative rights throughout
- User Story 1.1: As an admin user the navigation bar is displayed with a logo on all pages for easy navigation, with a burger menu on mobile devices

## Skeleton
### Wireframes
Each wireframe image below contains three sub images, one for desktop, tablet and mobile

Page | Wireframe | 
------------ | ------------- 
index | [Desktop/Tablet/Mobile](football_memories/static/images/wireframes/index.png)


## Surface
### Color Palette
I have gone for a simple and minimal design for the website, with predominately green, black and white font colours over a large hero image on all pages
There are five colours in the color palette

- 000000 - Black color for some text


I feel the colours complement each other very well, and I choose those colours after testing a number of palettes while making sure the colour palette met accessibility standards.
![Palette](football_memories/static/images/readme/color_palette.PNG)

### Typography
The Poppins font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the Poppins font cannot be imported into the website correctly. This font is from the Google fonts library.
![Font](football_memories/static/images/readme/font.PNG)

# Features
The website has seven distinct features, and they are described below
## Existing Features
### Feature 1 Navigation Bar
#### Description feature 1

#### User Stories feature 1
- User Story 1.1: As an admin/regular user the navigation bar is displayed with a logo on all pages for easy navigation, with a burger menu on mobile devices

##  Features Left to Implement
- I am content with what was implemented. The site is a feature rich site using a number of linked namespaces in a mongodb collection.
- However, here are some additional "nice to have" features that could be added to the site

Number | Feature  
 ------------ | ------- |
1 | Social sharing of a memory on facebook, twitter  |

# Technologies Used
## Languages 
- HTML (https://en.wikipedia.org/wiki/HTML)
    - The project uses html to build the relevant pages
- CSS (https://en.wikipedia.org/wiki/CSS)
    - The project uses CSS to style the relevant pages
- Javascript (https://www.javascript.com/)
    - Javascript was used for all scripting on the site
- Python v3.9 (https://www.python.org/)
    - Python was used for server side coding on the project, a number of libraries were also used: 
        - boto, boto3, botocore, click, dnspython, Flask, flask-paginate, 
        Flask-PyMongo, itsdangerous, Jinja2, jmespath, MarkupSafe, pymongo, s3transfer,Werkzeug
- Jinja (https://jinja.palletsprojects.com/en/3.0.x/)
    - Jinja is a templating engine for Python that is used throughout the project

## Libraries and other resources
- Bootstrap 5.0 (https://getbootstrap.com/docs/5.0)
    - The project uses the bootstrap library for some UI components in the website
- Gitpod (https://gitpod.io/)
    - Gitpod was used as an IDE for the project
- Github (https://github.com/)
    - GitHub was used to store the project code in a repository
- Google Fonts (https://fonts.google.com/)
    - Google font Roboto was used as the website font
- Balsamiq (https://balsamiq.com/)
    - Balsamiq was used to create the website wireframes
- Font Awesome (https://fontawesome.com/)
    - Font awesome was used to provide the relevant fonts/icons for the website
- Lucidchart (http://lucidchart.com)    
    - Lucidchart was used to create the database design diagrams
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
- Google Maps api (https://developers.google.com/maps)
    - The Google Maps api is used to display the stadium information on the memory page
- Google maps geocode API (https://developers.google.com/maps/documentation/geocoding/start)
    - The Google Maps geocode api is used to translate the event name returned from the memory stadium name value and translate to a Google Maps location on the memory page
- Gofullpage chrome plugin  (https://chrome.google.com/webstore/detail/gofullpage-full-page-scre)
    - This plugin was used to take full page screenshots for testing images
- Python online interpreter (https://www.programiz.com/python-programming/online-compiler/)
    - For testing python code snippets
- Pytest (https://docs.pytest.org/en/6.2.x/)
    - For Python unit testing
- UILicious (www.uilicious.com)
    - For automated testing

# Testing
The testing information and results for this project are documented in [TESTING.md](TESTING.md)

# APIs
The project also uses a number of API's, below are the steps to configure the API in your environment

## Email JS
1. Create an account at emailjs.com 
2. In the integration screen in the emailjs dashboard, note your userid
3. Create an email service in the Email Services section and note the id
4. Create an email template in the Email templates section and note the id
5. Update the script sendEmail.js, method sendMail with your user id, email service id and email template id

# Deployment
There are a number of applications that need to be configured to run this application locally or on a cloud based service, for example Heroku

## Amazon WebServices
1. Create an account at aws.amazon.com
2. Open the IAM application and create a new user
3. Set the AmazonS3FullAccess for the user and note the users AWS ACCESS and SECRET keys
![Iam](football_memories/static/images/readme/iam.PNG)
4. Open the S3 application and create a new bucket. For the purpose of this application the bucket name is ci-ms3-football-memories but this can be updated in the util.py route
5. With security best practices update the public access and policy bucket to enable the user created and the application access to read/write to the S3 bucket. Consult the AWS documentation if required: https://aws.amazon.com/s3/
![policy](football_memories/static/images/readme/policy.PNG)
6. The s3 bucket is now updated to be accessed by your application
7. In the util.py route update the variables s3_bucket_name and s3_bucket_url with the correct information that you have set up, for example:
<br>
<code>s3_bucket_name = "ci-ms3-football-memories"</code><br>
<code>s3_bucket_url = "https://ci-ms3-football-memories.s3.eu-west-1.amazonaws.com/" </code>


## Postgres Database
Postgres is the database used in the application

## Local Deployment
To run this project locally, you will need to clone the repository
1. Login to GitHub (https://wwww.github.com)
2. Select the repository pmeeny/CI-MS3-FootballMemories
3. Click the Code button and copy the HTTPS url, for example: https://github.com/pmeeny/CI-MS3-FootballMemories.git
4. In your IDE, open a terminal and run the git clone command, for example 

    ```git clone https://github.com/pmeeny/CI-MS3-FootballMemories.git```

5. The repository will now be cloned in your workspace
6. Create an env.py file in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<code>import os</code><br>
<code>os.environ.setdefault("IP", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("PORT", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("SECRET_KEY", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("MONGO_URI", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("MONGO_DBNAME", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("AWS_ACCESS_KEY_ID", TO BE ADDED BY USER)</code><br>
<code>os.environ.setdefault("AWS_SECRET_ACCESS_KEY", TO BE ADDED BY USER)</code>
7. Install the relevant packages as per the requirements.txt file
8. Start the application by running <code>python3 app.py</code>

## Heroku
To deploy this application to Heroku, run the following steps.
1. In the app.py file, ensure that debug is not enabled, i.e. set to True
2. Create a file called ProcFile in the root directory, and add the line <code>web: python app.py</code> if the file does not already exist
3. Create a requirements.txt file by running the command <code>pip freeze > requirements.txt</code> in your terminal if the file doesn't already exist
5. Both the ProcFile and requirements.txt files should be added to your git repo in the root directory
6. Create an account on heroku.com
7. Create a new application and give it a unique name
8. In the application dashboard, navigate to the deploy section and connect your application to your git repo, by selecting your repo
![Heroku dashboard](football_memories/static/images/readme/heroku_dashboard.PNG)
9. Select the branch for example master and enable automatic deploys if desired. Otherwise, a deployment will be manual
10. The next step is to set the config variables in the Settings section
![Config vars](football_memories/static/images/readme/config_vars.PNG)
11. Set key/value pairs for the following keys: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, IP, MONGO_DBNAME, MONGO_URI, PORT, SECRET_KEY
12. Go to the dashboard and trigger a deployment
![Deploy](football_memories/static/images/readme/deploy.PNG)
13. This will trigger a deployment, once the deployment has been successful click on the "Open App" link to open the app
14. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

# Credits
- For the memories page, I used some html and css code from https://bootstrapious.com/p/bootstrap-photo-gallery as a basis
for the memories gallery

- For storing images in an AWS S3 bucket, I found the following links very useful
    - https://www.youtube.com/watch?v=s1Tu0yKmDKU
    - https://stackoverflow.com/questions/44228422/s3-bucket-action-doesnt-apply-to-any-resources
    - https://www.youtube.com/watch?v=7gqvV4tUxmY 


- I used html/css code, then tweaked it accordingly for the site footer: https://jsfiddle.net/bootstrapious/c7ash30w/

- For the send-email functionality I used some code from the code institute module from the course

- Pagination- https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
- Div alignment: https://www.freecodecamp.org/news/how-to-center-anything-with-css-align-a-div-text-and-more/ 

- Django Comments: https://djangocentral.com/creating-comments-system-with-django/

# Content
- Font Awesome (http://fontawesome.com)    
    - The icons used on the site from font awesome

- Fonts (https://fonts.google.com/)    
    - The text font(Poppins) is from Google fonts
    
- The terms and conditions and privacy policy page content was copied from https://www.privacypolicies.com/blog/privacy-policy-template/

<br>

# Media

 <br>

# Acknowledgements
- I would like to thank my fiancée Mary for her help, constant support and ideas for the website, my son Liam, and also to my dog Lily for her company during development of the website.
- I would like to thank my mentor Mo Shami for his input, help and feedback.