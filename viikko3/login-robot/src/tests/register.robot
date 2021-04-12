*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  abc  12345678
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  abc  12345678
    Input Credentials  abc  12345678
    Output Should Contain  User with username abc already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  12345678
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  abc  1234567
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  abc  abcdefgh
    Output Should Contain  Password contains only letters
