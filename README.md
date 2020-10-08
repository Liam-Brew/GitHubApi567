# SSW567 Homework 05a

[![build status of HW05a_Mocking](https://travis-ci.org/Liam-Brew/GitHubApi567.svg?branch=HW05a_Mocking)](https://travis-ci.org/Liam-Brew/GitHubApi567)

**Author**: Liam Brew

**Date**: 30 September 2020

**Pledge**: I pledge my honor that I have abided by the Stevens Honor System

## Assignment Description

In last week's assignment HW 04a you may have encountered problems when testing your code in Travis-CI given that your tests were highly dependent on the GitHub APIs. Those APIs would start to return errors if you exceeded a threshold on use, or those APIs would return different results if you make a change to your repos. Remember that one of the key concepts behind unit-tests was that if you don't change your program then the unit-tests should behave consistently. Unfortunately that is not the case so far.

In this assignment you will use a mocking package to "mock" your program's external dependence on GitHub, so that you can guarantee that your unit tests will run consistently ever time you run them, no matter how many times you run them, and no matter what changes you make to your repos.

## Summary of Work

Luckily I had built my main github_api.py program to incorporate HTTP response codes, so this made my mocking progress somewhat easier. I was able to successful mock all API calls, whether they returned HTTP response codes or actual data.

## Challenges

I ran into some challenges when mocking tests that returned actual data (ex: the repo list). This is because I initially failed to account for my class-based structure. Once I revised my patch structure for the tests that referenced specific methods (ex: get_repos()) my tests seem to work ok without relying on the API.

## Reflection

I found this assignment interesting as the API call limit was a significant challenge for me to overcome in Homework 04. Using mock, this problem is completely circumnavigated.