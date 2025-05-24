from flask import Flask, render_template, request, make_response
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import fitz
app = Flask(__name__, template_folder='templates')
model = SentenceTransformer("all-MiniLM-L6-v2")

# @app.route('/')
@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('home.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    job_desc = request.form.get('job_description')
    resume = request.files['resume']
    file = fitz.open(stream=resume.stream.read(), filetype="pdf")
    resume_text=""
    for page in file:
        resume_text += page.get_text()
    embeddingsjd = model.encode(job_desc)
    embeddingsresume = model.encode(resume_text)
    similarities = cos_sim(embeddingsjd, embeddingsresume) *100
    score = f"{float(similarities):.2f}"
    print(score)
    if similarities < 40:
        feedback = '''
        There’s a low similarity between your resume and the job description. <br>
        You should review the job requirements and revise your resume to highlight relevant skills, tools, and experience.
        '''
    elif similarities < 60:
        feedback = '''Your resume has some overlap with the job description, but important skills or experiences might be missing. <br>
        Consider tailoring your resume more closely to the job.'''
    elif similarities < 80:
        feedback = '''Your resume is a strong match. <br>
        However, you may want to include more keywords or experiences that reflect the job requirements more clearly.'''
    else:
        feedback = '''Your resume aligns very well with the job description. Great job! <br>
        You can still consider fine-tuning some phrases or keywords for even more precision'''
    return render_template('result.html', score=score, feedback=feedback)

    



#how to handle url paramters
# @app.route('/handle_url_params', methods=['POST', 'GET'])
# def handle_params():
#     # greeting = request.args.get('greeting') #this is how to get the value for greeting in the url parameter
#     # name = request.args.get('name') #this is how to get the value for name in the url parameter
#     # return f"{greeting}, {name}"

#     if 'greeting' in request.args.keys() and 'name' in request.args.keys():
#         greeting = request.args.get('greeting')
#         name = request.args.get('name')
#         return f"{greeting}, {name}"
#     else:
#         return 'Some parameters are missing'
    

@app.route('/hello')
def hello(): 
    return "Hello, World!"



if __name__ in "__main__":
    app.run()