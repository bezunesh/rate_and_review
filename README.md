# Rate and Review

A web application tool which allows customers to rate and review local businesses. The main goal of the project is to help users make informed purchase decisions while encouraging businesses to provide quality services.

## Prerequisites

- Python 3.9
- django 3.1.7
- [django-rated-reviews](https://django-rated-reviews.readthedocs.io/en/latest/index.html)

### Local environment setup

1. clone the repo

   ```bash
   git clone https://github.com/bezunesh/rate_and_review.git
   ```

2. Create a virtual environment and activate it

   ```bash
    cd rate_and_review
    make setup
    ```

3. Install dependecies

    ```bash
    make install
    ```

4. Run database migrations

    ```bash
    make migrate
    ```

5. Run linting (optional)

    ```bash
    make lint
    ```
