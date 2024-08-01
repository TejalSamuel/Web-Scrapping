**Flask Books Application**

Welcome to the **Flask Books Application**! 📚 This is a simple Flask application designed to display and manage a collection of books. Built with **SQLAlchemy** for database interactions and styled with **Bootstrap**, this app provides a user-friendly interface to explore book information.

![Flask Books Application](https://via.placeholder.com/1200x400?text=Flask+Books+Application)

**Features**

- **📖 Book Display**: View a list of books with their title, price, and availability.
- **🔍 Modal View**: Click on a book to see detailed information in a stylish modal popup.
- **🌐 REST API**: Access book data in JSON format via a dedicated API endpoint.

**Getting Started**

Follow these instructions to set up and run the application locally.

**Prerequisites**

Make sure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package manager (usually comes with Python)

**Installation**

1. **Clone the repository:**

   ```
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Create a virtual environment:**

   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - **Windows:**

     ```
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```
   pip install -r requirements.txt
   ```

5. **Initialize the database:**

   ```
   flask db upgrade
   ```

6. **Run the application:**

   ```
   flask run
   ```

   Open your browser and navigate to `http://127.0.0.1:5000` to view the application.

**Usage**

**Home Page**

The home page displays a grid of books. Each card includes:

- **Book Title**: The name of the book.
- **Price**: The price of the book.
- **Availability**: Availability status.

![Home Page](https://via.placeholder.com/1200x600?text=Home+Page)

**Book Details Modal**

Click on any book card to view more details in a modal popup.

![Book Modal](https://via.placeholder.com/600x400?text=Book+Modal)

**REST API**

Fetch book data in JSON format by accessing the endpoint:

```
GET /api/books
```

**Contributing**

Feel free to fork the repository and submit pull requests. Please ensure that your contributions align with the project's coding standards.

**License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


**Happy Coding!** 😊
