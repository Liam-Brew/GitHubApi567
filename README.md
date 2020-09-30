# Liam Brew : SSW567 Homework 04a

[![build status of master](https://travis-ci.org/Liam-Brew/GitHubApi567.svg?branch=master)](https://travis-ci.org/Liam-Brew/GitHubApi567)

## Design Strategy

When designing this code I thought it was very important for HTTP response codes to be maintained. I felt that this would give significant insight regarding the status of the program and assist in troubleshooting any errors. To manage this, I included the two global variables ```repo_status``` and ```commit_status``` and based my class's ```run()``` method on interpreting these statuses. An added benefit of monitoring these statuses in such a way was that it enabled early termination  in case of an API failure, increasing the efficiency of the program. For my unit testing, I tried to balance the testing of the API endpoints by looking at a mix of both status codes and the content returned.

## Challenges

The most difficult challenge I encountered was dealing with the API request cap. This impacted both the development and testing stages of writing this program. A major impact of this was constraining the possible test cases that I could implement, which decreased my testing coverage.
