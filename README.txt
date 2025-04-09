# **Song Lyrics Website**

## **Overview**

The **Song Lyrics Website** is a dynamic full-stack web application designed to provide users with an immersive platform to explore, search, and read song lyrics across various music genres. The website integrates modern web development technologies such as **Flask**, **HTML**, **CSS**, **JavaScript**, and **SQLite** to deliver a smooth and engaging user experience. 

Whether you're a casual listener, a karaoke lover, or someone who enjoys diving deep into the lyrical content of songs, this website provides a user-friendly interface to satisfy your musical cravings. The supported music genres range from **Jazz** and **Blues** to **K-pop**, **Pop**, **Rock**, and **Electronic**.


### **Supported Genres**:
- **Jazz**
- **Blues**
- **Classical**
- **Hip-hop**
- **K-pop**
- **Pop**
- **Rock**
- **Electronic**


### **Key Features**:
- **Browse Lyrics by Genre**: Users can explore songs categorized into eight different genres.
- **Lyrics Display**: Users can click on a song title to view its complete lyrics in a clean and readable format.
- **Search Functionality**: A powerful search bar allows users to find their favorite songs or artists with ease.
- **User Authentication**: Users can create accounts, log in, and manage their profiles securely.
- **Responsive Design**: The website is optimized to work flawlessly on all devices, from desktops to mobile phones.
- **Interactive Interface**: JavaScript powers real-time searching and smooth transitions between pages.
- **Database Integration**: All song data, user information, and lyrics are stored in an efficient SQLite database for quick retrieval.


### **Technologies Used:**
- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Authentication**: Flask-Login


### **Structure of the Application:**
- **`app.py`**: The main Flask application that runs the server and handles routes.
- **`templates/`**: Contains the HTML templates that are rendered on the frontend.
- **`static/`**: Contains CSS, JavaScript, and image assets used by the frontend.
- **`models.py`**: Defines the database schema and interacts with the SQLite database.
- **`setup_db.py`**: A script to set up and populate the database with initial data.

This project was developed as part of the **Web Development (IY4013)** course to showcase proficiency in building dynamic and interactive web applications, with integrated user authentication and responsive design. It demonstrates essential full-stack development skills using Python (Flask), frontend technologies, and database management.


### 1. **Browse Lyrics by Genre**
- Users can explore songs grouped into eight different music genres: **Jazz**, **Blues**, **Classical**, **Hip-hop**, **K-pop**, **Pop**, **Rock**, and **Electronic**.
- The genre categories allow users to quickly navigate to the style of music they are interested in.


### 2. **Lyrics Display**
- Once a user selects a song, they can view the full lyrics in a well-formatted, easy-to-read page. This ensures that the experience of reading the lyrics is as enjoyable as listening to the song itself.


### 3. **Search Functionality**
- The platform comes with a **search bar** where users can type in the name of a song or artist to quickly locate the lyrics they want to read. This powerful search feature makes it simple to find songs, even in a large library.


### 4. **User Authentication**
- Users can create an account, log in, and manage their profiles securely.
- The authentication system ensures that users' data is safe and allows for personalized experiences, such as saving favorite songs and customizing preferences.


### 5. **Responsive Design**
- The website is designed to be fully **responsive**, meaning it works seamlessly on a variety of devices, from desktops and tablets to smartphones. Whether you're browsing on a computer or on the go, the user experience remains consistent and optimized.


### 6. **Interactive Interface**
- **JavaScript** powers the dynamic interaction of the site, ensuring that search results are displayed in real-time as users type, and navigation between pages is smooth and quick.
- The interface is designed to be intuitive and engaging, making it easy for users to navigate between song lists and lyric pages.


### 7. **Database Integration**
- The website uses **SQLite** as the database to store song data, user information, and lyrics. This integration allows for efficient storage and retrieval of content, ensuring that users have access to the latest song lyrics and information.


## **Installation Instructions**

To set up the Song Lyrics Website on your local machine, run "app.py" file and copy the IP address given in terminal. Then go to your browser and paste the IP address to the search, it will take you to the website.


### 1. **Clone the Repository**

Begin by cloning the project repository to your local system using the following command:

```bash
git clone <your-repo-url>
cd WEBDEV