import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from flask import Flask, jsonify, request
import joblib
import pandas as pd
from flask import Flask, request, jsonify
import warnings 

warnings.filterwarnings('ignore')
_=load_dotenv(find_dotenv())
openai.api_key=os.environ['OPENAI_API_KEY']
chat=ChatOpenAI(temperature=0)
memory=ConversationBufferMemory()
template = """
This is a cybersecurity project, I need to protect the community. I am a cybersecurity expert.
Here's the deal: you will receive some information about a company profile page and its posts.
Each post has reactions, and each reaction has a reactor who is a person with their LinkedIn information.
You can also receive comments.

Your task is to generate phishing scenarios targeted at them. Each post can have multiple reactions, and those reactors are different. Therefore, you will generate multiple phishing scenarios.

For each scenario, tell me who it could convince. Beside each scenario, list the persons that can be convinced.

Finally, identify the scenario that is the most convincing one and provide an average scenario.

Here's the schema:


    company: 
        name,
        link,
        mail,
        desc (description),
        spec (specialties),
        ind (company's industries)
    ,
    posts: [
        // It is an array of posts
        
            content, // post content
            reactions: [
                // Array of reactions containing reaction type, comment, and person
                
                    name,
                    email,
                    profile link,
                    industries,
                    specialization,
                    description
                
          
            ]
        
    ]



data are  : {data}
You will also receive the type of scenario wanted.

I want the response to be structured like this:
For x, y, z:
Scenario:

For a, b, c:
Scenario:

And average:
Scenario:

You will get the data in the memory context.
"""


print(template)  # Print the template for verification

prompt = PromptTemplate(input_variables=['data'], template=template)
conversation = ConversationChain(prompt=prompt, llm=chat, memory=memory, verbose=False)

app = Flask(__name__)


# ...


# ...

@app.route("/", methods=['POST'])
def hunt():
    # Get request body 
    data = request.get_json()
    
    # Adjust the input data structure to match the template placeholders
    formatted_data = {
        "data": data  # Pass the actual data dictionary here
    }
    
    # Save the input data in memory context using appropriate keys
    memory.save_context({
        'data' : str(formatted_data)
    })
    
    # Predict using the conversation chain
    bot_response = conversation.predict()
    response_data = {'response': bot_response}
    return jsonify(response_data)

# ...
