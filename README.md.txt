# Movie Recommendation System

A simple **Movie Recommendation System** built using Python and Pandas.  
It suggests movies similar to the one you like based on cosine similarity of movie genres and features.


## Features

- Recommends movies similar to the input movie  
- Uses TF-IDF Vectorization and Cosine Similarity  
- Works with a small sample dataset (movies.csv)  
- Clean and beginner-friendly code  



## Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, Scikit-learn, Numpy  
- **Algorithm:** Cosine Similarity  



## Folder Structure

Movie_Recommendation_System/
│
├── movie.py # Main Python script
├── movies.csv # Dataset file
└── README.md # Project documentation





## How to Run

1. **Clone the Repository**
  
   git clone https://github.com/<your-username>/Movie_Recommendation_System.git
Navigate to the Folder


cd Movie_Recommendation_System
Install Dependencies

pip install pandas scikit-learn numpy
Run the Project


python movie.py
Example Output


Enter your favorite movie: Avatar
Movies similar to Avatar:
- Guardians of the Galaxy
- Star Trek
- The Fifth Element
- Independence Day
- Star Wars
Dataset Information
The dataset contains basic information about movies such as:

Movie Title

Genre

Director

Cast

Future Improvements
Add TMDB/IMDB API integration

Improve recommendation accuracy with NLP models

Build a web-based frontend using Flask or Streamlit
Harshal Nimse
BTech CSE Student | Java | Python | Web Development | AI Enthusiast
Connect with me on LinkedIn
https://www.linkedin.com/in/harshal-nimase-73b496326/