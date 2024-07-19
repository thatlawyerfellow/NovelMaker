import openai
import gradio as gr

# Function to get user input for novel details
def get_novel_details(novel_length, language, style, total_characters, total_chapters):
    return {
        "novel_length": int(novel_length),
        "language": language,
        "style": style,
        "total_characters": int(total_characters),
        "total_chapters": int(total_chapters)
    }

# Function to get character details
def get_character_details(character_descriptions):
    character_files = []
    for i, description in enumerate(character_descriptions.split("\n")):
        filename = f"character_{i+1}.txt"
        with open(filename, 'w') as file:
            file.write(description)
        character_files.append(filename)
    return character_files

# Function to save all character descriptions into one file
def combine_character_files(total_characters):
    with open("characters.txt", 'w') as outfile:
        for i in range(1, total_characters + 1):
            with open(f"character_{i}.txt") as infile:
                outfile.write(infile.read() + "\n")

# Function to get chapter prompts from the user
def get_chapter_prompts(chapter_prompts):
    chapter_files = []
    for i, prompt in enumerate(chapter_prompts.split("\n")):
        filename = f"chapter_{i+1}_prompt.txt"
        with open(filename, 'w') as file:
            file.write(prompt)
        chapter_files.append(filename)
    return chapter_files

# Function to save all chapter prompts into one file
def combine_chapter_prompts(total_chapters):
    with open("chapter_prompts.txt", 'w') as outfile:
        for i in range(1, total_chapters + 1):
            with open(f"chapter_{i}_prompt.txt") as infile:
                outfile.write(infile.read() + "\n")

# Function to generate chapter content and summary using the selected model
def generate_chapter_content(client, chapter_number, prompt, character_details, chapter_length, previous_summaries, model):
    prompt_with_summaries = f"{prompt}\n\nCharacter Details: {character_details}\n\nPrevious Summaries: {previous_summaries}"
    
    # Generate chapter content
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate chapter {chapter_number} based on the following details: {prompt_with_summaries}"}
        ],
        max_tokens=chapter_length
    )
    content = response.choices[0].message.content
    
    with open(f"Chapter_{chapter_number}.txt", 'w') as file:
        file.write(content)
    
    # Generate chapter summary
    summary_response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Provide a 300-word summary for the following chapter content:\n\n{content}"}
        ],
        max_tokens=600
    )
    summary = summary_response.choices[0].message.content
    
    with open(f"chapter_summary_{chapter_number}.txt", 'w') as file:
        file.write(summary)
    
    return content, summary

# Function to combine all chapters into one book file
def combine_chapters(total_chapters):
    with open("book.txt", 'w') as outfile:
        for i in range(1, total_chapters + 1):
            with open(f"Chapter_{i}.txt") as infile:
                outfile.write(infile.read() + "\n")
    return "book.txt"

# Main function to orchestrate the novel generation process
def generate_novel(api_key, model, novel_length, language, style, total_characters, total_chapters, character_descriptions, chapter_prompts):
    client = openai.OpenAI(api_key=api_key)
    novel_details = get_novel_details(novel_length, language, style, total_characters, total_chapters)
    character_files = get_character_details(character_descriptions)
    combine_character_files(novel_details["total_characters"])
    chapter_files = get_chapter_prompts(chapter_prompts)
    combine_chapter_prompts(novel_details["total_chapters"])
    
    with open("characters.txt", 'r') as file:
        character_details = file.read()
    
    chapter_length = novel_details["novel_length"] // novel_details["total_chapters"]
    previous_summaries = ""
    for i in range(1, novel_details["total_chapters"] + 1):
        with open(f"chapter_{i}_prompt.txt", 'r') as file:
            prompt = file.read()
        content, summary = generate_chapter_content(client, i, prompt, character_details, chapter_length, previous_summaries, model)
        previous_summaries += summary + "\n"
    
    book_file = combine_chapters(novel_details["total_chapters"])
    return book_file

# Gradio interface
interface = gr.Interface(
    fn=generate_novel,
    inputs=[
        gr.Textbox(label="OpenAI API Key", type="password"),
        gr.Dropdown(label="Model", choices=["gpt-3.5-turbo", "gpt-4"]),
        gr.Textbox(label="Novel Length (in words)"),
        gr.Textbox(label="Language"),
        gr.Textbox(label="Style"),
        gr.Number(label="Total Number of Characters"),
        gr.Number(label="Total Number of Chapters"),
        gr.Textbox(label="Character Descriptions (one per line)", lines=10, placeholder="Enter each character description on a new line."),
        gr.Textbox(label="Chapter Prompts (one per line)", lines=10, placeholder="Enter each chapter prompt on a new line.")
    ],
    outputs=gr.File(label="Download the generated novel")
)

# Launch the interface
interface.launch()
