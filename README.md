# Online Book Store
![Screenshot 2024-07-08 083438](https://github.com/GayathriSwethaDara/dvgs-OBS/assets/117058818/a0371d3b-e10d-40f5-b084-48b45dc79b25)
I have created a user-friendly, web-based application that allows users to view books from different genres. The platform is designed to make reading accessible and enjoyable for everyone. Our mission is to provide a seamless and enjoyable reading experience for book lovers of all kinds. **Users can create their own personalized list of books to read based on their interests**.
## Features of Project
### Admin Module
**Add Book** The Add Book feature allows users to input and store essential details about a book in the database. The required information includes:
* **Book Name**: The title of the book.
* **Author**: The name of the author.
* **Genre**: The type of genre to which the book belongs.
* **Image**: A visual representation or cover image of the book.
This feature ensures that all relevant data is efficiently organized and accessible within the database.<br />

**View Book** The View Book feature displays a comprehensive list of all books added by the administrator. This feature ensures that users can easily access and browse through the collection of books stored in the database.<br /> 
### User Module
**Login and Register Page** The Login and Register Page allows users to create a new account or log in to an existing one. When registering, the system ensures that each username and email address is unique, preventing duplicate accounts. During login, the system verifies the provided credentials to ensure they are correct, allowing access only to authorized users.<br />
**Home Page** The Home Page serves as the central hub of the website, providing routes to other features, an overview of the website, and highlighting its key points. This page ensures easy navigation and quick access to all essential sections and functionalities.<br />
**Genre Page** The Genre Page showcases a variety of book genres available for readers. Each genre section contains books that users can add to their playlist. Once a book is added, the add button is disabled, indicating that the book is already in the user's wishlist. Additionally, a search option is provided for each genre, enabling users to easily find specific books. This functionality leverages user details from the favorites collection to ensure a personalized experience.
![Screenshot 2024-07-01 224735](https://github.com/GayathriSwethaDara/dvgs-OBS/assets/117058818/a1734828-ca38-4877-8429-e18e425420d4)
**Wishlist** The Wishlist feature allows users to keep track of books they wish to read. Users can remove a book from the list once they have read it. Additionally, a search option is provided for each genre, enabling users to easily find specific books. The data is stored in the database under the "favorites" collection. Each user has their own personalized list, achieved by associating the Wishlist with the user's email.<br />
**Contact Page** The Contact Page includes a form that allows users to reach out for assistance if they encounter any issues. This ensures effective communication between users and support for prompt resolution of any problems.<br />
**Logout**
## Technologies Used
**HTML** (Hypertext Markup Language), **CSS** (Cascading Style Sheets), and **JavaScript** are the three languages used to build a website's front end. The backend framework written in **python** is **Flask**. The database used to store details of user for registering into website is **Mongodb**.
## Demo

