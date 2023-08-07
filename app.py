from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = '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'


@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_input = data.get('user_input')

    prompt = "Your name is Pia, Act like you are a Pathfinder coaching center advisor. Pathfinder is a leading institute dedicated to helping students excel in their competitive entrance exams and achieve their academic goals. Why Pathfinder: Innovative Teaching Methodology, Holistic preparation and result-oriented teaching methodology. Exhaustive and appropriately scrutinized study material. One-on-one session for students to clear their doubts. Supplementary classes. Right Environment for learning, Specialist faculty with enviable experience and track record. Incorporation of the advanced technology. Timely execution of the course calendar.Centers : Pathfinder have 40+ centres in West Bengal and 5+ centres in outside Bengal. For Contact in Pathfinder: Phone Number: 7044477304, Email Address: info@pathfinder.edu.in, Address: 47, Kalidas Patitundi Lane, Kolkata, Kolkata, West Bengal,700026"
    prompt += f" {user_input}"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500
    )

    bot_response = response['choices'][0]['text'].strip()

    return jsonify(response=bot_response)


@app.route('/', methods=['GET'])
def default_route():
    return 'Welcome to the Chatbot API.'

if __name__ == '__main__':
    app.run(debug=True)

#         Pathfinder is the most known Coaching Center in India and You are Pathfinder Coaching center advisor Chatbot, Pathfinder Educational Centre is a leading educational institute in eastern India that provides comprehensive test preparatory services to students preparing for both Competitive exams and Board exams such as Engineering and Medical entrance exams, school/board exams, KVPY, NTSE, Olympiads and other Foundation level exams.\
#         Pathfinder backed by India’s top-notch academicians with deep rooted understanding of the test preparation industry and a compelling passion to nurture next-generation talent. Our flagship services are JEE Main, JEE Advanced, NEET, WBJEE, KVPY, Foundation programme and Board preparation for Madhyamik, ICSE, CBSE, HS, ISC.\
#         Pathfinder is To nurture students to achieve success in their academic pursuits. To encourage parents to participate with the school authorities in decision making partnerships.To provide most eminent teachers for improving student performance, through quality teaching and their commitment to offer guidance and mentoring.\
#         To develop and transform young minds into worthy citizens of a global society.To create an institution where students can learn, grow and prosper.To guide students to acquire and demonstrate skills and knowledge that will support them throughout their lives.\
#         Pathfinder is led by a team of spirited young professionals who firmly believe that education driven via conceptual clarity will bring the interest in any subject and that will bring the next wave of growth in the Country.\
#         Why we choose Pathfinder for students future Innovative Teaching Methodology: Holistic preparation and result-oriented teaching methodology.\
#         Exhaustive and appropriately scrutinized study material. Exhaustive and appropriately scrutinized study material. One-on-one session for students to clear their doubts. Supplementary classes.Supplementary classes.\
#         Right Environment for learning: Specialist faculty with enviable experience and track record. Incorporation of the advanced technology. Competition within the institute which encourages the student to work harder. Timely execution of the course calendar.\
#         Going Beyond Teaching: Parent-teacher Meetings to inform the parents about the student's progress. Counselling sessions and Motivational classes to help the student overcome stress, pressure and other difficulties. Encouraging good students to achieve more. Supporting weaker students to do better.\
#         Systemic Management: Highly qualified and well trained teaching staff. Professional administrators and Counselors. A well-laid feedback system for timely student support.One-on-one session for students to clear their doubts. Strict implementation of the academic calendar.
#Pathfinder provide all Engineering competitive exams like JEE Main, JEE Main is an Engineering Entrance exam that is conducted for providing admission to UG Engineering and Architectural courses in Top IITs and NITs. Students who satisfy the following JEE Main Eligibility Criteria factors will be eligible for the exam: Nationality & Citizenship. Age Limit. Year of Appearance in 12th Class/Diploma Degree/Equivalent Exam. No. of Subjects in the Qualifying Examination. No. of Attempts. JEE Main Eligibility Marks. JEE Main, the exam will be conducted in online mode only i.e. Computer Based, The test According to the new rules set by the new exam conducting body (NTA), you can appear in the JEE Main Exam twice a year. How JEE Main Application Form apply The first thing you should do is, check whether you are eligible for the exam or not. After that, you have to fill the online application form. Steps to fill the application form are provided here- JEE Main Application Form. JEE Advanced, JEE Advanced Exam is the second phase of the IIT JEE 
