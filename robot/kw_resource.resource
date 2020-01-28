*** Settings ***
Documentation  Resource file for keywords.

*** Variables ***
${FO TIMEOUT}  25

*** Keywords ***
Find Owner
	[Documentation]    KW takes two positional arguments: firstname, lastname to
	...                find the owner from the list.
        [Arguments]    ${firstname}  ${lastname}  
        [Timeout]  ${FO TIMEOUT}
        ${name str}  Catenate  ${firstname}  ${lastname}
        FOR  ${index}  IN RANGE  1  ${OWNER MAX COUNT}
            ${status}  Run Keyword And Return Status  SeleniumLibrary.Element Text Should Be
	    ...  Xpath://*[@id="owners" and @class="table table-striped"]//descendant::a[${index}]  ${name str}
            Run Keyword If  '${status}'=='True'  Click Link  Xpath://*[@id="owners" and @class="table table-striped"]//descendant::a[${index}]
            Exit For Loop If  '${status}'=='True'
        END
	Run Keyword If  '${status}'=='False'  Fail  msg=No owner found!!

List The Owners
        [Documentation]    KW clicks on the 'Find Owner' button.
	Click Button  Xpath://*[@type="submit" and @class="btn btn-default"]

Check If Only One Owner With This Lastname
        [Documentation]    KW finds owner data according to given lastname.
	...                'True' status is returned if the name is found.
        [Arguments]    ${lastname}
	Input Text  Xpath://input[@id="lastName"]  ${lastname}  clear=True
	List The Owners
        ${status}  Run Keyword And Return Status  Page Should Contain  Pets and Visits
	Return From Keyword  ${status}

