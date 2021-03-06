Framework : pytest

Programming Language : python

File Name : test_tugas05.py

**Scenario Test**

![image](https://user-images.githubusercontent.com/49749221/136492025-b306f9ca-97f3-4e9f-b072-49e49c72ddf3.png)



**Step write code:**
1. User imports library
2. User create a list to accommodate invalid user data named "Account"
3. User write @pytest.fixture to group steps / code that is run repeatedly and create function setup()
4. User create function test_login_success() for login successfully
5. User write @pytest.mark.parametrize to call list Account
6. User create function test_login_unsuccess() for login failed

**How to Run?**
1. Open terminal
2. Make sure the file path location is correct
3. Type 'pytest -v test_tugas05.py'
4. if you want get the report, type 'pytest -v test_tugas05.py --html=LoginReport.html'
5. Then press enter

**The Result:**

You will see the result in Terminal: If **Success**, you will see green text with information 'PASSED'. If **Fail**, you will see red text with text with information 'FAILED'



