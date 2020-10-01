# SSW567 Homework 04a

[![build status of master](https://travis-ci.org/Liam-Brew/GitHubApi567.svg?branch=master)](https://travis-ci.org/Liam-Brew/GitHubApi567)

**Author**: Liam Brew

**Date**: 30 September 2020

**Pledge**: I pledge my honor that I have abided by the Stevens Honor System

## Assignment Description

This assignment will require that you write code to interface with an external REST-based APIs.   We could have used almost any external APIs, but for this assignment we chose GitHub because many of its APIs are public and do not require any authorization or API Keys.   This simplifies both the use and setup.


For this assignment imagine that you have been asked to develop a function that will interface with GitHub in order to extract and present useful information to your user. The function will communicate using the RESTful services APIs provided by GitHub. The GitHub APIs will allow you to query for information about users, repositories, etc... which can be retrieved using the function, and then be displayed in the application.

What should make this assignment different from other programming assignments is in how you will approach it.  You should approach this assignment as a developer who more than anything else has the perspective of the tester in the front of your mind. 

The developer looks at the requirements and asks how should I design and implement this function, but the tester will ask questions such as what will I need to test for in this function?  And how will I test this function?   As you design and write the function as a developer, you should consider the perspective of the tester in any of your design and implementation decisions.   One deliverable of this assignment will be to reflect and comment on this.

## Summary of Work/Design Strategy

When designing this code I thought it was very important for HTTP response codes to be maintained. I felt that this would give significant insight regarding the status of the program and assist in troubleshooting any errors. To manage this, I included the two global variables ```repo_status``` and ```commit_status``` and based my class's ```run()``` method on interpreting these statuses. An added benefit of monitoring these statuses in such a way was that it enabled early termination  in case of an API failure, increasing the efficiency of the program. For my unit testing, I tried to balance the testing of the API endpoints by looking at a mix of both status codes and the content returned.

## Challenges

The most difficult challenge I encountered was dealing with the API request cap. This impacted both the development and testing stages of writing this program. A major impact of this was constraining the possible test cases that I could implement, which decreased my testing coverage.

## Reflection

I found this assignment to be very useful and the premise to be interesting. Often times when I am writing code, I do not really consider the testing implications of certain design decisions and instead seek to focus on the immediate efficiency of the development process. When I was working on this assignment, I tried my best to make the code as portable and specific as possible. This explains my object-oriented approach wherein I grouped related functions, each with a specific task to play a role in the larger system. I found this especially useful when working with the HTTP return calls, which was a specific goal of mine when considering the tester. The management of these calls enabled me to see exactly where the program failed and due to what reasons, which definitely helped the testing phase of development.

