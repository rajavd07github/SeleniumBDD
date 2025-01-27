Feature: User login

Scenario: Successful login
Given User is on the login page
When User enters valid credentials
Then User is redirected to the homepage