# Table of Contents



# Testing
The testing approach(described in detail in this testing readme) is as follows:
1. Manual testing using emulators and real devices
2. Automated testing using the Django unit test framework

## Unit testing information
- I wrote a number of unit tests using the Django unit test framework
- I used coverage(coverage.py) for code coverage and to ensure a high code coverage was met on all python files in the project


## Automated testing information
- I wrote a simple automated e2e testing on UILIcious(www.uilicious.com)
- The test accesses all pages and ensures the simple e2e flow of accessing all pages is successful
- Below are screenshots of the tests(steps and results) running on UILicious(Desktop, Chrome and Mozilla Firefox)
![Chrome](football_memories/static/images/testing/chrome_automation.PNG)
![Firefox](football_memories/static/images/testing/mozilla_automation.PNG)

## Manual testing information
Testing was completed on the following browsers and device types

Device Number | Physical/Emulator | Device Name | Device Type | Browser | Version
------------ | ------------ | ------------- | ------------- | ------------- | -------------
1 | Physical | iPad | Tablet |  Safari | 14.4 |
2 | Physical | iPhone | Mobile |Safari | 14.4 |
3 | Physical | One Plus 5 | Mobile | Chrome | 91.0 |
4 | Physical | Windows Desktop| Desktop | IE Edge | 42.0 |
5 | Physical | Windows Desktop| Desktop | Mozilla Firefox | 85.0 |
6 | Physical | Windows Desktop| Desktop | Chrome | 91.0 |
7 | Emulator | Galaxy S5 | Mobile | Chrome Emulator | 91.0 |
8 | Emulator | iPad | Tablet | Chrome Emulator | 91.0 |
9 | Emulator | iPhone X | Mobile | Chrome Emulator | 91.0 |
10 | Emulator | iPhone 5/SE | Mobile | Chrome Emulator | 91.0 |

- Below are the test results for testing the website requirements against a range of browsers and devices
- For the purpose of the screenshots I used a Chrome emulator for desktop, tablet and mobile (Device numbers 6(Desktop), 8(Tablet), 9(Mobile))

## Feature 1 Navigation Bar
### User Story 1-1

### Test case steps 1-1

### Expected Result 1-1
1. The home/index page will be displayed with logo and navigation bar, with a burger menu on mobile devices

### Actual Result 1-1
Step Number | Desktop | Tablet | Mobile | Result 
------------ | ------------ | ------------- | ------------- | ------------- |
Step 1 | [Desktop Result](football_memories/static/images/testing/index_desktop.png)  | [Tablet Result](football_memories/static/images/testing/index_tablet.png) |[Mobile Result](football_memories/static/images/testing/index_mobile.png) | Passed |

## Feature 2 Footer

## Feature 3 Landing Home page


# Bugs found during the testing phase

Bug no. | Bug description |  Bug fix |
------------ | ------------- | ------------- | 
1 | When adding a memory, the memory_name was being stored as null in the memory collection| The "name" field was missing from the form field for the input type memory_name


# Code Validators and Website Analysis
The website's pages was tested against the following validators:

## HTML Markup Validation Service
I used https://validator.w3.org/ to validate the html files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
administration/dashboard.html | Passed, No errors found | [Results](football_memories/static/images/html_validation/dashboard_html_validation.PNG)

<br>

## CSS Validation Service
I used https://jigsaw.w3.org/css-validator/ to validate the css(style.css)
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
style.css | Passed, No errors found | [Results](football_memories/static/images/css_validation/css_validation.PNG)

<br>

## Chrome Dev tools Lighthouse 

- I used Lighthouse (https://developers.google.com/web/tools/lighthouse) to test the performance, seo, best practices and accessibility of the site
- Overall the results are very good. The memory pages performance is affected by the Google map load times and making this load more efficient was out of my control from a code perspective 

### Desktop
Page | Result 
------------ | ------------- 
administration/dashboard.html |  ![Results](football_memories/static/images/lighthouse_validation/dashboard_desktop.PNG)

### Mobile
Page | Result
------------ | ------------- 
administration/dashboard.html |  ![Results](football_memories/static/images/lighthouse_validation/dashboard_mobile.PNG)

<br>

## Wave Accessibility
- Wave accessibility(https://wave.webaim.org/) was used to test the websites accessibility

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
bag/templates/bag/bag.html  |  |
checkout/templates/checkout/checkout.html | |
checkout/templates/checkout/checkout_success.html | |
favourites/templates/favourites/favourites.html | |
home/templates/home/index.html | 0 errors and 0 contrast errors| [Results](readme/wave_validation/wave_index.PNG)
news/templates/news/add_news_item.html | | 
news/templates/news/edit_news_item.html | | 
news/templates/news/manage_news_items.html | 0 errors and 0 contrast errors| [Results](readme/wave_validation/wave_news_item_management.PNG) 
news/templates/news/news.html | 0 errors and 0 contrast errors| [Results](readme/wave_validation/wave_news.PNG)  
products/templates/products/add_product.html | 0 errors and 0 contrast errors| [Results](readme/wave_validation/wave_add_product.PNG)
products/templates/products/edit_product.html | | 
products/templates/products/product_detail.html | | 
products/templates/products/products.html | | 
profile/templates/profile/profile.html | |
templates/allauth/account/login.html | 0 errors and 0 contrast errors| [Results](readme/wave_validation/wave_login.PNG)
templates/allauth/account/logout.html | 0 errors and 0 contrast errors| [Results](readme/wave_validation/wave_logout.PNG)
templates/allauth/account/register.html | 0 errors and 0 contrast errors| [Results](readme/wave_validation/wave_register.PNG) 
templates/allauth/account/password_change.html | |
templates/allauth/account/password_reset.html | 0 errors and 0 contrast errors| [Results](readme/wave_validation/wave_password_reset.PNG)
templates/allauth/account/password_reset_done.html | |
templates/allauth/account/password_set.html | |
templates/allauth/account/verification_sent.html | |
templates/allauth/account/verification_email_required.html | |


## JSHint
- JSHint(https://jshint.com/) was used to analyse the Javascript files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
bag/static/bag/js/bag.js | 0 errors and 0 warnings | [Results](readme/jshint/jshint_bag.PNG)
checkout/static/checkout/carousel.js | 0 errors and 0 warnings | [Results](readme/jshint/jshint_stripe_elements.PNG) 
home/static/home/carousel.js | 0 errors and 0 warnings | [Results](readme/jshint/jshint_carousel.PNG) 
news/static/news/carousel.js | 0 errors and 0 warnings | [Results](readme/jshint/jshint_news.PNG) 
favourites/static/favourites/favourites.js | 0 errors and 0 warnings | [Results](readme/jshint/jshint_favourites.PNG) 
products/static/products/products.js | 0 errors and 0 warnings | [Results](readme/jshint/jshint_products.PNG)

<br>

## PEP8online
- PEP8online was used to analyse the Python files (https://pep8online.com/)
- I used the pep8 checker in my IDE Pycharm, and created a scope and included the following files
- ![PEP8 scope](readme/pep8/pep8_scope.PNG)
- The report shows no errors/warnings for the files listed below
- ![PEP8 report](readme/pep8/pep8_report.PNG)
- One of the main errors on several files was to ensure the character count was less than 80 characters

Page | Result 
------------ | ------------- 
bag/admin.py | No errors/warnings 
bag/apps.py | No errors/warnings 
bag/contexts.py | No errors/warnings 
bag/models.py | No errors/warnings 
bag/test_views.py | No errors/warnings 
bag/urls.py | No errors/warnings 
bag/views.py | No errors/warnings 
checkout/admin.py | No errors/warnings 
checkout/apps.py | No errors/warnings 
checkout/forms.py | No errors/warnings 
checkout/models.py | No errors/warnings 
checkout/signals.py | No errors/warnings 
checkout/test_forms.py | No errors/warnings 
checkout/test_models.py | No errors/warnings 
checkout/test_views.py | No errors/warnings 
checkout/urls.py | No errors/warnings 
checkout/views.py | No errors/warnings 
checkout/webhook_handler.py | No errors/warnings 
checkout/webhooks.py | No errors/warnings 
favourites/admin.py | No errors/warnings 
favourites/apps.py | No errors/warnings 
favourites/contexts.py | No errors/warnings 
favourites/models.py | No errors/warnings 
favourites/test_models.py | No errors/warnings 
favourites/test_views.py | No errors/warnings 
favourites/urls.py | No errors/warnings 
favourites/views.py | No errors/warnings 
home/admin.py | No errors/warnings 
home/apps.py | No errors/warnings 
home/models.py | No errors/warnings 
home/test_views.py | No errors/warnings 
home/urls.py | No errors/warnings 
home/views.py | No errors/warnings 
news/admin.py | No errors/warnings 
news/apps.py | No errors/warnings 
news/forms.py | No errors/warnings 
news/models.py | No errors/warnings 
news/test_models.py | No errors/warnings 
news/test_views.py | No errors/warnings 
news/urls.py | No errors/warnings 
news/views.py | No errors/warnings 
products/admin.py | No errors/warnings 
products/apps.py | No errors/warnings 
products/forms.py | No errors/warnings 
products/models.py | No errors/warnings 
products/test_forms.py | No errors/warnings 
products/test_models.py | No errors/warnings 
products/test_views.py | No errors/warnings 
products/urls.py | No errors/warnings 
products/views.py | No errors/warnings 
products/widgets.py | No errors/warnings 
profiles/admin.py | No errors/warnings 
profiles/apps.py | No errors/warnings 
profiles/forms.py | No errors/warnings 
profiles/models.py | No errors/warnings 
profiles/test_models.py | No errors/warnings 
profiles/test_views.py | No errors/warnings 
profiles/urls.py | No errors/warnings 
profiles/views.py | No errors/warnings 
custom_storages.py | No errors/warnings
env.py | No errors/warnings
manage.py | No errors/warnings
unit/unit.py | No errors/warnings
