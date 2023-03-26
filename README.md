# Flask File Reader (Vetty Backend Assignment)

This is a simple Flask application that reads the contents of a file and displays it on a webpage.

## Installation

1. Clone this repository: `git clone https://github.com/prateekb1912/vetty-backend-assignment.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Flask app: `python app.py`

## Usage

The app has a single GET endpoint, which accepts an optional filename parameter in the URL. If no filename is specified, it defaults to **file1.txt**.

You can also specify start and end line numbers as query parameters to only display a portion of the file.

For example:

- To display the entire contents of file1.txt: http://localhost:5000/
- To display lines 2-4 of file2.txt: http://localhost:5000/file2.txt?start=2&end=4

## Supported Encodings

Currently the app supports both UTF-8 and UTF-16 encoded files.
It automatically detects the encoding of the file and reads it accordingly.
