# **Software Requirements** 

## Vision
What is the vision of this product?  
This product creates a seamless way to track attendance in Zoom meetings.  
What pain point does this project solve?  
Hosts often take a valuable minute or two in every meeting counting little black boxes to check who is in attendance at the meeting.  
Why should we care about your product?  
This app removes this awkward pause at the beginning of a meeting, or a host forgetting to take the time to record attendance by automating this reporting.  

## Scope (In/Out)
### IN
What will your product do  
This web app will utilize Zoom API endpoints to find which users logged in to an individual meeting  
The web app will use AuthO for secure login and data access  
Reports will be generated containing user attendance data   
Reporting will be automated in some way to be sent to the host  

### OUT
What will your product not do.  
This product will not be integrated with the Canvas API  

## Minimum Viable Product 
What will your MVP functionality be?  
MVP functionality will allow a user to login to their zoom account, gather API data from a specific meeting, and return that data in the simplest automated way possible to the user.   
What are your stretch goals?  

## Stretch
What stretch goals are you going to aim for?    
Have multiple options for report generation (Slackbot/G-sheet)   
Use data visualization libraries for additional zoom data   

## Functional Requirements
List the functionality of your product. This will consist of tasks such as the following:  
This web app will utilize Zoom API endpoints to find which users logged in to an individual meeting  
The web app will use AuthO for secure login and data access  
Reports will be generated containing user attendance data   
Reporting will be automated to be sent to the host  

## Data Flow
Describe the flow of data in your application. Write out what happens from the time the user begins using the app to the time the user is done with the app. Think about the “Happy Path” of the application. Describe through visuals and text what requests are made, and what data is processed, in addition to any other details about how the user moves through the site.  

## Non-Functional Requirements (301 & 401 only)
Non-functional requirements are requirements that are not directly related to the functionality of the application but still important to the app.  

1. Security - We have a couple of options to use when connecting to the API app securely. We can use AuthO to log in, but Zoom recommends the using of a JSON Web Token (JWT). We will explore both routes.  

2. Testability - We will be writing unit tests for each method we use on our app along with unit tests to test out functionality of the app. We hope to write at least 2 tests for each method or function. Along with achieving 80% testing coverage using pytest as our testing option.    

