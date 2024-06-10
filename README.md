# NovelMaker
Use the OpenAI API to write a novel or a story

Novel Generation using OpenAI GPT

This project uses OpenAI's GPT model to generate a novel based on user inputs. The user provides details such as the length of the novel, language, style, character descriptions, and chapter prompts. The project then uses these inputs to generate the novel's content, including chapter summaries.

Features

Generates a novel based on user-defined inputs.
Supports character and chapter prompt inputs.
Uses OpenAI GPT models to generate chapter content and summaries.
Combines all chapters into a final book file.
Requirements

Python 3.7 or higher
OpenAI Python client library
Gradio library for user interface
Installation

Clone the repository:

bash
Copy code
git clone https://github.com/thatlawyerfellow/NovelMaker.git
cd NovelMaker
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required libraries:

bash
Copy code
pip install -r requirements.txt
Running the Application

Make sure you have your OpenAI API key ready.
Run the application:
bash
Copy code
python novel_generator.py
Usage

Open the application in your web browser. You will see the Gradio interface.
Enter the OpenAI API key.
Select the model (e.g., gpt-3.5-turbo).
Provide the following inputs:
Novel Length (in words)
Language
Style
Total Number of Characters
Total Number of Chapters
Character Descriptions (one per line)
Chapter Prompts (one per line)
Click the "Submit" button.
After processing, you will be able to download the generated novel.
File Structure

novel_generator.py: Main script containing the novel generation logic and Gradio interface.
requirements.txt: List of required Python libraries.
README.md: Project documentation.
License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

Acknowledgements

OpenAI for providing the GPT models.
Gradio for the easy-to-use web interface.
