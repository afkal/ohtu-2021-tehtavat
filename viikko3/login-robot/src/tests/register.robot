*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  Abc  12345678
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  Abc  12345678
    Input Credentials  Abc  12345678
    Output Should Contain  User with username Abc already exists

Register With Too Short Username And Valid Password
    Input Credentials  Ab  12345678
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  Abc  1234567
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  Abc  abcdefgh
    Output Should Contain  Password contains only letters
