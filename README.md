Framework : pytest
Programming Language : python

Feature: Login

  @valid
  Scenario: Login in Github successfully
    Given User have already access Login Page and already have account in Github
    When User input username or email "testingkaryasa21@gmail.com"
    And User input password "carrot2348."
    Then The user should login successfully and should see her name when he clicks on the avatar icon
    
  @invalid
  Scenario Outline: Login in Github failed
    Given User have already access Login Page and already have account in Github
    When User input username or email with invalid data <email>
    And User input password with invalid data <password>
    Then The user should login is failed and shoul see error message "Incorrect username or password."
    
    |email                      |password      |
    |testingkaryasa21@gmail.com |carrot2348    |
    |testingsaja@gmail.com      |carrot2348.   |
    |testingkaryasa21           |rambutan123@  |
    |                           |carrot2348.   |
    |testingkaryasa21@gmail.com |              |
    
    
name file : test_tugas05.py

Step write code:
1. User imports library 
![image](https://user-images.githubusercontent.com/49749221/136488888-e13bab59-eb39-4a0b-aad0-619ddec0420b.png)
2. User create a list to accommodate invalid user data named "Account"
3. User write @pytest.fixture to group steps / code that is run repeatedly and create function setup()
4. User create function test_login_success() for login successfully
5. User write @pytest.mark.parametrize to call list Account
6. User create function test_login_unsuccess() for login failed

How to Run? 
1. Open terminal
2. Make sure the file path location is correct
3. Type 'pytest -v test_tugas05.py'
4. if you want get the report, type 'pytest -v test_tugas05.py --html=LoginReport.html'
5. Then press enter

The Result : 
You will see the result in Terminal
If Success, you will see green text with information 'PASSED'
If Fail, you will see red text with text with information 'FAILED'



