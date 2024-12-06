# Magazine Domain Project
This project models a system of authors, articles, and magazines. It demonstrates basic object-oriented principles and relationships between these entities.

# Features
Author: Authors can write articles and contribute to magazines.
Article: Articles have a title, and each is written by an author and published in a magazine.
Magazine: Magazines hold articles and track the authors contributing to them.
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/magazine-domain.git
Navigate to the project folder:

bash
Copy code
cd magazine-domain
Install dependencies:

bash
Copy code
pipenv install
Activate the virtual environment:

bash
Copy code
pipenv shell
Usage
Here is an example of how to use the classes:

# python
Copy code
# Create Author and Magazine instances
author = Author("John Doe")
magazine = Magazine("TechMag", "Technology")

# Author adds an article
article = author.add_article(magazine, "Understanding Python")

# Access article details
print(article.title)  # Output: "Understanding Python"
print(author.articles())  # List of articles by John Doe
print(magazine.article_titles())  # List of article titles in TechMag
Error Handling
Instead of raising errors, invalid inputs will print messages. For example:

# python
Copy code
print("Error: Title must be a string between 5 and 50 characters.")
License
This project is licensed under the MIT License.

