
# Sign Language Search
Sign language is a powerful tool for communication and connection. With this project, we aim to bridge the gap between the hearing and non-hearing communities, empowering individuals to easily access information and communicate with one another. <br>
A python application that allows users to perform a Google search using sign language. The application uses a combination of computer vision and machine learning to recognize and interpret the user's hand gestures, and then sends a request to the Google Search API with the corresponding text. The results of the search are displayed on the screen for the user to browse.
<br>
<br>
## How to Use
To use the Sign Language Search application, follow these steps:

- Open the repo in any python IDE.
- Run test.py
- Position yourself in front of the camera so that your hands are clearly visible.
- Make a hand gesture corresponding to the letter or word you want to search for. For example, to search for the word "cat", you might make a "C" hand gesture , then "A" hand gesture and "T" with an time period of 2 seconds per gesture.
- Press 'S' once the desired word is visible on the screen ,the application will recognize your hand gestures and send a search request to the Google Search API.
- The search results will be displayed on the screen for you to browse.

<br>
<br>

## Technology Used
The Sign Language Search application is built using a combination of the following technologies:

- Computer vision: To recognize and interpret the user's hand gestures
- Machine learning: To classify the hand gestures and convert them to text
- Google Search API: To send search requests and retrieve search results

<br>
<br>

## Future Work


- Creating a desktop/chrome extension via which the user would be able to not only search but type in the documents, mails, chat etc via sign language.
- A phone extension for better usability.
- 
- Adding support for more hand gestures: Currently, the application only supports a limited number of hand gestures. Adding support for more gestures would allow users to search for a wider range of words and phrases.
- Improving gesture recognition accuracy: The accuracy of the gesture recognition could be improved by training the machine learning model on a larger and more diverse dataset.
- Adding support for other languages: The application currently only supports English searches. Adding support for other languages would allow users to perform searches in their native language.
