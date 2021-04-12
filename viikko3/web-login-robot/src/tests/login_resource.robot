*** Variables ***
${SERVER}  localhost:5000
${LOGIN URL}  http://${SERVER}/login

*** Keywords ***

Go To Login Page
    Go To  ${LOGIN URL}

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
