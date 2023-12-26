<div id="top"></div>

# MEME_PAGE

<details>
<summary>Table of contents</summary>

-   [Overview](#overview)
-   [Technology Stack](#technology-stack)
-   [Getting Started](#getting-started)
-   [Features](#features)
-   [Screenshots](#screenshots)

</details>

## Overview

- This a meme page built using flask, it uses reddit-api to intreact with reddit and get the meme image
- And also added user authentication using MySQL database, where users can register, login and logout
- After every 25 seconds a new meme will be displayed

## Technology Stack

- Flask
- MySQL
- HTML
- CSS
- Js

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/hemanth110702/meme_page.git
   cd meme_page
   ```

2. Install Flask in that directory
   ```bash
   pip install flask
   ```

3. Install flask_mysqldb in that directory
   ```bash
   pip install flask_mysqldb
   ```

4. Install requests in that directory
   ```bash
   pip install requests
   ```

5. Update the config in app.py (you can find your details in MySQL workbench)

    ```python
    app.config['MYSQL_HOST'] = 'YOUR-HOST-NAME'
    app.config['MYSQL_USER'] = 'YOUR-USER-NAME'
    app.config['MYSQL_PASSWORD'] = 'YOUR-PASSWORD'
    app.config['MYSQL_DB'] = 'YOUR-DB-NAME'
    ```

6. Run XAMPP server
    - open XAMPP
    - Click on Apache - start

7. Run the flask file
    ```bash
    python app.py
    ```

## Features

- A new meme generates for every 25 seconds
- Users can register and login to their account

## Screenshots

<table>
    <tr>
        <th>Desktop View</th>
    </tr>
    <tr>
      <td style="text-align: left;font-weight: bold;">
      Home Page
      </td>
    </tr>
    <tr>
        <td>
            <img src="https://github.com/hemanth110702/meme_page/assets/89832451/d7f23e15-e911-40d7-8bdd-d71cea59303f" width="100%" title="Desktop view - Home"/>
        </td>
    </tr>
    <tr>
      <td style="text-align: left;font-weight: bold;">
      Login Page
      </td>
    </tr>
    <tr>
        <td>
            <img src="https://github.com/hemanth110702/meme_page/assets/89832451/a92cc6a3-b901-4694-ac10-8ea75e9d02f8" width="100%" title="Desktop view - login"/>
        </td>
    </tr>
    <tr>
      <td style="text-align: left;font-weight: bold;">
      Registration Page
      </td>
    </tr>
    <tr>
        <td>
            <img src="https://github.com/hemanth110702/meme_page/assets/89832451/1b617102-1ff2-486d-9944-e0be4c082b9a" width="100%" title="Desktop view - register"/>
        </td>
    </tr>
    <tr>
      <td style="text-align: left;font-weight: bold;">
      After Logged in
      </td>
    </tr>
    <tr>
        <td>
            <img src="https://github.com/hemanth110702/meme_page/assets/89832451/a7cae16d-2942-4024-8d57-82e9d710f6bc" width="100%" title="Desktop view - after logged in"/>
        </td>
    </tr>
</table>

<p align="right">(<a href="#top">back to top</a>)</p>