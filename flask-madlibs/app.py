from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def home():
    # Get the prompts for the story
    prompts = story.prompts
    # Render the template for the homepage, passing in the prompts
    return render_template('home.html', prompts=prompts)

@app.route('/story')
def generate_story():
    # Get the answers from the form
    answers = {}
    for prompt in story.prompts:
        answer[prompt] = request.args.get(prompt)
        generated_story = story.generate(answer)
        # Render the Template for the story, passing in the generated story
        return render_template('story.html', story=generated_story)