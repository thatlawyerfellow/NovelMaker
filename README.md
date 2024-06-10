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

This code is designed to generate a novel using the OpenAI GPT model based on user inputs provided through a Gradio interface. Below is a detailed summary of how each part of the code works:

Import Libraries
openai: To interact with the OpenAI API.
gradio: To create a web-based user interface for collecting user inputs.
Function Definitions
get_novel_details:

This function collects and stores details about the novel such as its length, language, style, total number of characters, and total chapters.
It returns these details as a dictionary.
get_character_details:

This function accepts a string of character descriptions, with each description on a new line.
It saves each character description to a separate text file (character_1.txt, character_2.txt, etc.).
It returns a list of these file names.
combine_character_files:

This function reads the individual character files created in the previous function and combines them into a single file (characters.txt).
get_chapter_prompts:

This function accepts a string of chapter prompts, with each prompt on a new line.
It saves each chapter prompt to a separate text file (chapter_1_prompt.txt, chapter_2_prompt.txt, etc.).
It returns a list of these file names.
combine_chapter_prompts:

This function reads the individual chapter prompt files and combines them into a single file (chapter_prompts.txt).
generate_chapter_content:

This function generates the content and summary for a single chapter.
It combines the chapter prompt with character details and previous summaries to form the input prompt for the OpenAI API.
It calls the OpenAI API to generate the chapter content and saves it to a file (Chapter_1.txt, Chapter_2.txt, etc.).
It also calls the OpenAI API to generate a summary of the chapter and saves it to a file (chapter_summary_1.txt, chapter_summary_2.txt, etc.).
It returns the generated content and summary.
combine_chapters:

This function reads the individual chapter files and combines them into a single book file (book.txt).
It returns the name of the combined book file.
generate_novel:

This is the main function that orchestrates the novel generation process.
It initializes the OpenAI API key and collects novel details from the user.
It generates character details and combines them into a single file.
It generates chapter prompts and combines them into a single file.
It iteratively generates the content and summary for each chapter and combines the chapters into a final book file.
It returns the name of the final book file.
Gradio Interface
The Gradio interface collects inputs from the user, including:

OpenAI API Key
Model (e.g., gpt-3.5-turbo)
Novel Length (in words)
Language
Style
Total Number of Characters
Total Number of Chapters
Character Descriptions (one per line)
Chapter Prompts (one per line)
The interface calls the generate_novel function with these inputs and provides the generated novel file for download.

Launch the Interface
The Gradio interface is launched, allowing users to interact with the application through a web browser.

License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

Acknowledgements

OpenAI for providing the GPT models.
Gradio for the easy-to-use web interface.
