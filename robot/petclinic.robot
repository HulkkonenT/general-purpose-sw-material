*** Settings ***
Documentation  Test cases for the PetClinic web application.

Test Timeout  2 minutes

Library  SeleniumLibrary
#Library  String
#Library  OperatingSystem
#Library  DateTime
#Library  Process
#Library  Dialogs
#Library  Remote
#Library  Telnet
#Library  Collections
#Library  Screenshot
#Library  XML

Variables  basic_variables.py
Resource  kw_resource.resource

Test Setup  Find PetClinic Home Page And All Owners Page
Test Teardown  Close Test Browser

*** Variables ***
${ADDRESS}
${CITY}
${TELEPHONE}
${NEWPETNAME}
${BIRTHDATE}
${EPTYPE}

*** Test Cases ***
Find All Owners
        [Documentation]  TC lists all the existing owners on that page.
	[Timeout]  ${FAO TIMEOUT} seconds
        List The Owners

Find A Specific Owner
        [Documentation]  TC fetches details of the given owner.
	[Timeout]  ${FASO TIMEOUT} seconds
        ${status}  Check If Only One Owner With This Lastname  ${speclastname}
        Run Keyword If  '${status}'=='False'  Find Owner  ${specfirstname}  ${speclastname}

Add Owner
        [Documentation]  TC adds an owner with the given details.
	[Timeout]  ${AO TIMEOUT} seconds
        Add A New Owner  ${firstname}  ${lastname}  ${aoaddress}  ${aocity}  ${aotelephone}

Add Pet
        [Documentation]  TC adds an owner with the given details.
	[Timeout]  ${AP TIMEOUT} seconds
	Add A New Pet   ${petfirstname}  ${petlastname}  ${adpetname}  ${adbirthdate}  ${type}

Add Visit
        [Documentation]  TC adds a new visting time for the pet.
        [Timeout]  ${AV TIMEOUT} seconds
        Add A Visit To Veterinarian  ${visfirstname}  ${vislastname}  ${vispetname}  ${date}  ${description}

Edit Owner
        [Documentation]  TC modifies owner data by taking positional arguments ${eofirstname} and
	...              ${eolastname}. Additionally, these optional parameters can be given:
	...              *${ADDRESS}  *${CITY}  *${TELEPHONE}.
        [Timeout]  ${EO TIMEOUT} seconds
	List The Owners
        Find Owner  ${eofirstname}  ${eolastname}
        Click Link  Xpath://*[contains(@href,'edit')]
	Details  Fill In Owner Data  ${ADDRESS}  ${CITY}  ${TELEPHONE}

Edit Pet
        [Documentation]  TC modifies pet data by taking positional arguments ${epfirstname},
	...              ${eplastname} and ${petname}. Additionally, these optional parameters
	...              can be given: *${NEWPETNAME}  *${BIRTHDATE}  *${EPTYPE}.
        [Timeout]  ${EP TIMEOUT} seconds
        List The Owners
        Find Owner  ${epfirstname}  ${eplastname}
	Details  Fill In Pet Data  ${petname}  ${NEWPETNAME}  ${BIRTHDATE}  ${EPTYPE}

*** Keywords ***
Find PetClinic Home Page And All Owners Page
        [Documentation]    Opens browser to PetClinic home page and finds owners page.
        Open Browser  ${LOGIN URL}  ${BROWSER}
        Title Should Be  PetClinic :: a Spring Framework demonstration
	Page should contain  Welcome
	Find The Owners Page

Find The Owners Page
        Click Link  Xpath://*[@href="/owners/find" and @title="find owners"]
	Page should contain  Find Owners
	Page should contain  Last name

Details
        [Arguments]    ${keyword}  @{keyargs}
	Run Keyword   ${keyword}  @{keyargs}

Fill In Owner Data
	[Documentation]    KW modifies owner data by taking up to three optional arguments:
	...                *${address}, *${city}, *${telephone}
        [Arguments]     ${address}=  ${city}=  ${telephone}=
	[Timeout]  25
        Run Keyword If  '${address}'!=''  Input Text  Xpath://input[@id="address"]  ${address}  clear=True
        Run Keyword If  '${city}'!=''  Input Text  Xpath://input[@id="city"]  ${city}  clear=True
	Run Keyword If  '${telephone}'!=''  Input Text  Xpath://input[@id="telephone"]  ${telephone}  clear=True
	Run Keyword If  '${address}'!='' or '${city}'!='' or '${telephone}'!=''  Click Button  Xpath://*[@type="submit"] 

Add A New Owner
        [Documentation]  KW adds owner with the specified arguments.
	[Arguments]    ${first name}  ${last name}  ${address}  ${city}  ${telephone}
	[Timeout]  25
	Click Link  Xpath://*[@href="/owners/new" and contains(text(), "Add Owner")]
        Input Text  Xpath://input[@id="firstName" and @value=""]  ${first name}  clear=True
	Input Text  Xpath://input[@id="lastName" and @value=""]  ${last name}  clear=True
	Input Text  Xpath://input[@id="address" and @value=""]  ${address}  clear=True
	Input Text  Xpath://input[@id="city" and @value=""]  ${city}  clear=True
	Input Text  Xpath://input[@id="telephone" and @value=""]  ${telephone}  clear=True
        Click Button  Xpath://*[@type="submit" and contains(text(), "Add Owner")]

Add A New Pet
        [Documentation]  KW adds pet for the given owner.
        [Arguments]     ${firstname}  ${lastname}  ${pet name}  ${birth date}  ${type}
	[Timeout]  20
	List The Owners
	Find Owner   ${firstname}  ${lastname}
	Page Should Contain  Owner Information
	Page Should Contain  Pets and Visits
	Click Link  Xpath://*[@class="btn btn-default" and contains(text(), "Add")]
        Input Text  Xpath://input[@id="name" and @type="text"]  ${pet name}  clear=True
        Input Text  Xpath://input[@placeholder="YYYY-MM-DD" and @type="text"]  ${birth date}  clear=True
        Select From List By Value  Xpath://select[@id="type"]  ${type}
        Click Button  Xpath://*[@type="submit" and contains(text(), "Add Pet")]

Add A Visit To Veterinarian
        [Documentation]  KW adds a new visting time for the pet.
        [Arguments]    ${firstname}  ${lastname}  ${petname}  ${date}  ${description}
        [Timeout]  20
	List The Owners
        Find Owner  ${firstname}  ${lastname}
	Page Should Contain  Visit Date
	Page Should Contain  Description
        ${status}  Set Variable  False
	${pet visit id}  Set Variable  ${0}
        FOR  ${index}  IN RANGE  1  ${PET MAX COUNT}  ${PET INCREMENT}    #1, 4, 7, 10,.....
            ${status}  Run Keyword And Return Status  SeleniumLibrary.Element Text Should Be  Xpath://*[@class="table table-striped"]//descendant::dd[${index}]  ${petname}
            ${pet visit id}  Set Variable  ${pet visit id + 2}
            Run Keyword If  '${status}'=='True'  Click Link  Xpath://*[@class="table table-striped"]//descendant::a[${pet visit id}]
            Exit For Loop If  '${status}'=='True'
	END
	Run Keyword If  '${status}'=='False'  Fail  msg=No pet found!!
        Page Should Contain  Visit
	Input Text  Xpath://input[@placeholder="YYYY-MM-DD" and @type="text"]  ${date}  clear=True
	Input Text  Xpath://input[@id="description" and @type="text"]  ${description}  clear=True
	Click Button  Xpath://*[@type="submit" and contains(text(), "Add Visit")]

Fill In Pet Data
        [Documentation]  KW modifies pet data by taking up to three optional arguments:
	...              *${NEWPETNAME}  *${BIRTHDATE}  *${EPTYPE}.
        [Arguments]    ${petname}  ${newpetname}=  ${birthdate}=  ${type}=
	[Timeout]  25
	Page Should Contain  Visit Date
	Page Should Contain  Description
        ${status}  Set Variable  False
	${pet visit id}  Set Variable  ${1}
        FOR  ${index}  IN RANGE  1  ${PET MAX COUNT}  ${PET INCREMENT}    #1, 4, 7, 10,..
            ${status}  Run Keyword And Return Status  SeleniumLibrary.Element Text Should Be  Xpath://*[@class="table table-striped"]//descendant::dd[${index}]  ${petname}
            Run Keyword If  '${status}'=='True'  Click Link  Xpath://*[@class="table table-striped"]//descendant::a[${pet visit id}]
	    ${pet visit id}  Set Variable  ${pet visit id + 2}
	    Exit For Loop If  '${status}'=='True'
	END
	Run Keyword If  '${status}'=='False'  Fail  msg=No pet found!!
        Page Should Contain  Pet
        Run Keyword If  '${newpetname}'!=''  Input Text  Xpath://input[@id="name" and @type="text"]  ${newpetname}  clear=True 
	Run Keyword If  '${birthdate}'!=''  Input Text  Xpath://input[@placeholder="YYYY-MM-DD" and @type="text"]  ${birthdate}  clear=True
	Run Keyword If  '${type}'!=''  Select From List By Value  Xpath://select[@id="type"]  ${type}
	Run Keyword If  '${newpetname}'!='' or '${birthdate}'!='' or '${type}'!=''  Click Button  Xpath://*[@type="submit"] 

Close Test Browser
	Close all browsers