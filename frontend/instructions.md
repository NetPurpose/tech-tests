# Net Purpose frontend tech test

## What is the task?

Your task is to create a frontend "admin dashboard" for some fictional portfolio holdings. Portfolio details will be delivered via the API (see below)

We want to see three things: integration with APIs, display of data, and user interaction.

1. Integration with API

We'd like to see you fetch portfolio holdings data from the included API (see below for details), and ideally combine information from an external source like [AlphaVantage](https://www.alphavantage.co/).

2. Display data

Show the data retrieved from the APIs on the page. Bonus points for creative visualisations and ideas (we like charts)!

Some ideas (we're not expecting all of these!):

- List of holdings
- Aggregate statistics on holdings, e.g. total portfolio value
- Holdings performance over time - [link](https://www.alphavantage.co/documentation/#time-series-data)

3.  User interaction

An example of the user interacting with the page, e.g. using buttons, sliders, dropdowns etc.

Some ideas for this part (again not expecting all of them, and feel free to come up with something more interesting):

- Login flow
- Add / update / remove a holding
- Filter and sort the data that's displayed

## Judging criteria

We're going to look mostly at the structure and quality of your code, rather than how beautiful your solution looks. That being said, some appreciation of UX and interaction design principles are important.

We're also interested to hear your thoughts on, or see your implementation for, things like:

- State management
- Componentisation and project organisation
- Styling solutions
- Testing strategy

## The boilerplate

### Frontend

In the `frontend` directory, is an almost unmodified create-react-app project to help you get started quickly. If you prefer, please feel free to use your own boilerplate (and linting rules 😉).

If you like TypeScript, [go for it](https://create-react-app.dev/docs/adding-typescript/). We also accept solutions using Vue.

There is an example request to the API in `App.js`.

### API

Describe the existing API

- Docs at [http://localhost/docs](http://localhost/docs)

- If you want to inspect the database using pgAdmin - [http://localhost:5050](http://localhost:5050/)

## How to get it running

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Node](https://nodejs.org/en/)
- [Yarn](https://yarnpkg.com/getting-started/install)

### Start the app

```
# in the backend directory
docker-compose up -d

# in the frontend directory
yarn && yarn start
```

Now go to [http://localhost:3000](http://localhost:3000) and you should see the app!
