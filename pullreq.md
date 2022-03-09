Because of the fact that this is our first experience with using GitHub and working on a large nonacademic project, this markdown file is used to facilitate how to make
a pull request.

# What is a Pull Request?

A pull request – also referred to as a merge request – is an event that takes place in software development when a contributor/developer is ready to begin the process 
of merging new code changes with the main project repository.

The idea of a pull request is that it acts as a buffer to stop accidentally breaking the whole system. In a repo that contains all the project's code, metadata, etc.
A maintainer (Matthew Dharmawan) is responsible for maintianing the repository. This means the maintainer is in charge of which updates can be merged with the final 
project and made available for the other users (Oscar Tapia and Joseph Selfani). 

To make a pull request, the repo maintainer reviews new code updates from a developer (Matthew, Oscar, Joseph) and determines if it is ready to be released. Pull requests
encourage collaboration and open communication when working on new product updates. They also keep teams motivated by notifying the team when someone completes a new feature.

# How to Make a Pull Request?

## 1. Fork Main Repository and Create Local Clone
The developer creates a fork of the main repository, and clones this onto their local machine

## 2. Local Changes
That developer then is able to make their needed changes or additions to the code

## 3. Push Local Changes to Forked Repository
Once developer completed and tested the new code changes, they push these changes back to the forked repository they created in step one

## 4. Make a Pull Request
Make a pull request on the repo. Please add in a message describing what files are updated/added, and a brief description of what it does.

## 5. Maintainer Looks at the Code
The maintainer will look at the work done in the developer's forked repository, and then make comments or requests on any edits that need to be made for approval.
Any edits are sent back to the developer for additional commits that may be needed. Once no more edits are needed, the Maintainer will approve the pull request

## 6. Merging with Master
Once the repo maintainer approves, the developer's updates in the forked repository are merged with the main project repository. The product is updated with the new
feature/bug fix, and now can be viewed by other end users.


# Try it Out to Test
Make a pull request that creates a new python folder with any function inside. Call it pullreqtest.py
Or, make an edit to pullreqtest.py by deleting code, adding more, or editing the existing code.

Sources:
https://www.pagerduty.com/resources/learn/what-is-a-pull-request/#:~:text=A%20pull%20request%20%E2%80%93%20also%20referred,with%20the%20main%20project%20repository.
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
