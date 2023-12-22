# Dcomforters' Kitchen 

![Dcomforters' Kitchen Logo](secondproject/newapp/static/img/DK_logo.png)

Dcomforters' Kitchen is a dynamic web application built with Django, offering a platform for managing, exploring, and reserving a table at an African Restaurant serving a variety of delightful menus. Whether you are a Full Stack, BackEnd or FrontEnd developer, this project provides an opportunity to see how all these are put together to design this dynamic application.

## Features

- **Menu Management:** Create, edit, and delete your menus with ease.
- **User Management:** Create, edit, delete and add users to groups.
- **User Authentication:** Securely sign up, log in, and manage your account.
- **Recipe Exploration:** Discover a variety of recipes shared by the community.
- **Ingredient Tracking:** Keep track of ingredients needed for your recipes.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd DcomfortersKitchen
    ```

3. Install dependencies using [Pipenv](https://pipenv.pypa.io/):

    ```bash
    pipenv install
    ```

4. Apply database migrations:

    ```bash
    pipenv run python manage.py migrate
    ```

5. Start the development server:

    ```bash
    pipenv run python manage.py runserver
    ```

6. Visit `http://127.0.0.1:8000/` in your browser to access Dcomforters' Kitchen.

## Usage

- **Create an Account:** Sign up to start creating and managing your recipes.
- **Explore Recipes:** Discover a variety of recipes shared by the community.
- **Add a Recipe:** Share your favorite recipes with others.
- **Manage Your Profile:** Edit your profile details and preferences.

## Technologies Used

- **Django:** A high-level web framework for Python.
- **SQLite:** Lightweight and easy-to-use database for development.
- **Bootstrap:** Front-end framework for responsive and modern design.
- **Pipenv:** Dependency management tool for Python projects.

## Contributing

If you would like to contribute to Dcomforters' Kitchen, please follow our [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc.

---

**Note:** This README template is a starting point. Customize it according to the specific details of your project.

Happy cooking!
