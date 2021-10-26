# Table of Contents



# Testing
The testing approach(described in detail in this testing readme) is as follows:
1. Manual testing using emulators and real devices
2. Automated testing using the Django unit test framework

## Unit testing information
Note: 
- 
![pytest](football_memories/static/images/testing/pytest.PNG)
- Code coverage details of running the two tests is as follows, first install coverage(pip install coverage)
- Then run "coverage run -m pytest" to run coverage against the codebase
- -To generate a report run "coverage report -m"
![coverage](football_memories/static/images/testing/coverage_report.PNG)

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
football_memories/templates/administration/dashboard.html | 0 errors and 0 contrast errors| [Results](football_memories/static/images/wave_validation/wave_dashboard.PNG)

## JSHint
- JSHint(https://jshint.com/) was used to analyse the Javascript files

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
authentication.js | 0 errors and 0 warnings | [Results](football_memories/static/images/jshint/authentication.PNG)

<br>

## PEP8online
- PEP8online was used to analyse the Python files (https://pep8online.com/)

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
app.py | No errors/warnings | [Results](football_memories/static/images/pep8/app.PNG)
