## FastAPI GraphQL API

Developed a GraphQL API powering Blogging Application Backend using FastAPI, Graphene
and Orator ORM.

Wanna Try?

- Fork/Clone the Repo
  ```sh
  git clone https://github.com/imkaka/fastapi-graphql.git
  ```
- Initialize the Dev Environment
  ```sh
  poetry install && poetry shell
  ```
- Copy and populate DB creds in `.env`, or chnage `db.py` to use your favourite other DB.

  ```sh
  cp .env.sample .env

  ```

- Run the server and visit `localhost:500/graphql`

  ```sh
  python run.py

  ```

Credits - [TestDriven.io](https://testdriven.io/)
