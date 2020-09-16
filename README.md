# NetPurpose tech test

## Objectives:

In the data folder is a `.csv` file containing information on the counts of various phytoplankton samples found in monitoring stations throughout the UK. The data is taken from the UK government website [here](https://data.gov.uk/dataset/9a86b044-58a3-46d0-8455-5046f5769627/phytoplankton-results-for-england-and-wales). The names of the different phytoplankton species have been changed to make them slightly less confusing (columns K-T).

Your goal is to:
1. Design a datamodel to store this data.
2. Create a flow to take the data from the csv and load it into that data model
3. Write an interface for two kinds of queries:
	* Get phytoplankton counts by year as a function of local authority. i.e. We would like to be able to answer the question: `What was the total count of Dino as a function of year in Weymouth PHA`
	* The 10 slowest samples to be processed (i.e. longest time from collection to analysis), for each collection method.

## What we're looking for

When completing the project try and complete it as if this is an MVP product for a larger phytoplankton data store, e.g. other potential queries may be added at a later stage.

Overall we are looking for:
* Code quality and style
* Ability to work with data
* Data design and wider thinking

Ultimately, this is an exercise for us to see how you think, and whilst there may be some wrong answers, there isn't a specific right answer either. We want to see you make technical decisions which are well informed, and can be justified within the context of the problem given.

## Getting started
There is some boilerplate code provided, but it has a strong opinion on the technology choices you would make (most notably using PostgreSQL and SQLAlchemy for the database). You are free to use as much of that boilerplate as you wish, and if you feel more comfortable with a different set of tools, then please go ahead - just be prepared to justify your choices! We do ask, however, that you stick to Python as the main language for the code, as this is currently the main language of our stack.

The project was setup with python3.7, and requirements for the basics are in requirements.txt.

If you install these:

   - [virtualenv](https://virtualenv.pypa.io/en/stable/installation.html)
   - [Docker](https://docs.docker.com/engine/install/)
   - [docker-compose](https://docs.docker.com/compose/install/)
   - [gnu-make](https://www.gnu.org/software/make/)

the provided `Makefile` will give you three commands:

* `install`: use virtualenv to create a local virtual environment and install all requirements into it. Then start docker containers and run the `phyto.database.py` file.

* `start`: spin up the docker containers using docker-compose, then run the `phyto.database.py` file

* `stop`: stop the local containers

