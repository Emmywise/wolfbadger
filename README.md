
# wolf $ badgar



# User account/profile app Introduction

The User Profile Management App is a Django application that allows users to create, view, edit, and delete their user profiles. It provides a user-friendly interface for managing personal profile information, such as name, address, phone number, and more.

## Features

- User registration and login functionality using OAuth with GitHub as the provider.
- Secure storage of user credentials and profile information.
- Display of user profile information and management
- Edit and update user profile details.
- Deletion of user profile.

## Prerequisites

- Python 3.x
- Django 3.x
- GitHub OAuth App credentials (Client ID and Client Secret)

## Installation

1. Clone the repository: git clone <https://github.com/Emmywise/wolfbadger.git
2. Change into the project directory:cd user-profile-management-app
3. Create a virtual environment:python3 -m venv venv
4. Activate the virtual environment:source venv/bin/activate
5. Install the dependencies: pip install -r requirements.txt


## Configuration

1. Set up OAuth with GitHub:
   - Register a new OAuth application on GitHub (https://github.com/settings/applications/new).
   - Set the authorization callback URL to `http://localhost:8000/accounts/complete/github/`.
   - Obtain the Client ID and Client Secret provided by GitHub.
   - In the Django project settings file (`settings.py`), update the `SOCIALACCOUNT_PROVIDERS` configuration with your GitHub OAuth credentials.

2. Run database migrations: python manage.py migrate


## Usage

1. Start the development server: python manage.py runserver
2. Open your web browser and access the app at `http://localhost:8000`.
3. Register a new user or log in with your GitHub account.
4. Once logged in, you will be redirected to your user profile page.
5. On the user profile page, you can view your profile information and edit it by clicking the "Edit Profile" button.
6. Update your profile details and click "Save Changes" to save the changes to the database.
7. To delete your user profile, click the "Delete Profile" button.

## Testing

To run the automated tests for the app, use the following command: python manage.py test

The test suite includes test cases for user profile creation, retrieval, update, and deletion.