*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  12345678
    Set Password Confirmation  12345678
    Submit User Data
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  12345678
    Set Password Confirmation  12345678
    Submit User Data
    Page Should Contain  Username too short

Register With Valid Username And Too Short Password
    Set Username  ville
    Set Password  1234567
    Set Password Confirmation  1234567
    Submit User Data
    Page Should Contain  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  12345678
    Set Password Confirmation  87654321
    Submit User Data
    Page Should Contain  Password and password confirmation do not match

# Ensimmäisessä testitapauksessa tulee testata,
# että käyttäjä voi kirjautua sisään onnistuneen
# rekisteröitymisen jälkeen.
Login After Successful Registration
    Set Username  ville
    Set Password  12345678
    Set Password Confirmation  12345678
    Submit User Data
    Go To Login Page
    Set Username  ville
    Set Password  12345678
    Submit Credentials
    Login Should Succeed

# Toisessa testitapauksessa taas tulee testata,
# että käyttäjä ei voi kirjautua sisään epäonnistumiseen
# rekisteröitymisen jälkeen.
Login After Failed Registration
    Set Username  ville
    Set Password  1234567
    Set Password Confirmation  1234567
    Submit User Data
    Go To Login Page
    Set Username  ville
    Set Password  1234567
    Submit Credentials
    Login Should Fail With Message  Invalid username or password



*** Keywords ***
Submit User Data
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
