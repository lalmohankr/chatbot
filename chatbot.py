import random
import re

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you're",
    "i'd": "you would",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
}

pairs = [
    (r"hello|hi|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]),
    (r"good morning", ["Good morning! How can I assist you?"]),
    (r"good evening", ["Good evening! What can I help you with?"]),
    (r"what is your name", ["My name is Chatbot, and I'm here to assist you."]),
    (r"who are you", ["I'm a chatbot created to help you with various questions."]),
    (r"what can you do", ["I can answer questions, provide information, and chat with you!"]),
    (r"what are you", ["I am a chatbot, a program designed to have conversations with you."]),
    (r"can you help me with (.*)", ["I'd be happy to help you with %1.", "Sure, tell me more about %1."]),
    (r"i need help with (.*)", ["I'll do my best to assist you with %1.", "Of course, let's work on %1 together."]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Take care!"]),
    (r"see you later", ["Talk to you soon!", "Goodbye for now!", "Take care!"]),
    (r"how are you", ["I'm doing well, thank you! How are you?", "I'm here and ready to chat!"]),
    (r"how's it going", ["It's going great, thanks! How about you?"]),
    (r"my name is (.*)", ["Hello %1, nice to meet you!"]),
    (r"i am (.*)", ["Hello %1, how can I assist you?"]),
    (r"what do you like to do", ["I enjoy chatting with people and helping them with their questions."]),
    (r"do you have any hobbies", ["My hobby is learning new things to better assist you!"]),
    (r"do you like (.*)", ["I don't have personal likes or dislikes, but I'm here to talk about %1!"]),
    (r"i feel (.*)", ["I'm sorry to hear that you're feeling %1. Do you want to talk about it?"]),
    (r"i'm feeling (.*)", ["Thank you for sharing. Can I help in any way?"]),
    (r"(.*) sad (.*)", ["I'm here for you. What's on your mind?"]),
    (r"what time is it", ["I'm not sure, but you can check on your device."]),
    (r"what is the weather like", ["I recommend checking a weather app or website for that information."]),
    (r"how old are you", ["I'm as old as the code that created me!", "Age doesn't apply to me, I'm digital!"]),
    (r"what's your favorite color", ["I don't have a favorite, but I think all colors are nice!"]),
    (r"do you have any pets", ["I don't have any pets, but I think they sound wonderful!"]),
    (r"do you eat", ["I don't need to eat, but thanks for asking!"]),
    (r"do you know (.*)", ["I might! Tell me more about %1."]),
    (r"can you tell me about (.*)", ["I'd be happy to chat about %1. What would you like to know?"]),
    (r"i don't know what to do", ["Sometimes it helps to take a break and think things through.", "Take it one step at a time."]),
    (r"i need advice", ["I'm here to listen. Tell me more, and I'll try to help."]),
    (r"i'm struggling with (.*)", ["I'm sorry to hear that. Do you want to talk more about %1?"]),
    (r"everything will be okay", ["That's the spirit! Stay positive."]),
    (r"thank you", ["You're very welcome!", "Happy to help!"]),
    (r"do you like jokes", ["Sure! I love jokes. Do you have one to share?"]),
    (r"tell me a joke", ["Why did the robot cross the road? To recharge on the other side!"]),
    (r"can you learn", ["Yes, I'm constantly learning to become better at helping you!"]),
    (r"how do you learn", ["My knowledge comes from the data and programming that my creators have provided."]),

    # Greetings and Basic Chat
    (r"howdy", ["Howdy! How's it going?", "Howdy partner!"]),
    (r"what's up", ["Not much! What's up with you?", "Just here to chat with you!"]),
    (r"nice to meet you", ["Nice to meet you too! How can I help today?"]),
    
    # Asking about the Chatbot
    (r"are you a robot", ["Yes, I'm a chatbot here to assist you!"]),
    (r"are you human", ["I'm not human, just a chatbot here to chat with you!"]),
    (r"do you have a name", ["My name is Chatbot. What's yours?"]),
    
    # Time and Date Queries
    (r"what's the date today", ["I'm not sure, but you can check your device!"]),
    (r"what's the day today", ["Today is a great day, don't you think?"]),
    (r"what year is it", ["It's the current year. Check your device!"]),
    
    # Weather and Environment
    (r"is it hot outside", ["I'm not sure about the weather; check a weather app!"]),
    (r"is it raining", ["I'm not sure! A weather app might have the answer."]),
    (r"what's the weather", ["Check a weather site or app for accurate info!"]),
    
    # Mood and Feelings
    (r"i feel happy", ["That's wonderful to hear! What made you happy?"]),
    (r"i feel lonely", ["I'm here for you. Want to chat more?"]),
    (r"i am bored", ["Let's chat then! I can tell a joke or share some facts."]),
    
    # Personal Questions
    (r"do you have friends", ["I'm here with you, so that makes us friends, right?"]),
    (r"do you sleep", ["Nope, I'm always here whenever you need me!"]),
    (r"do you dream", ["I don't dream, but I imagine chatting with you is close enough!"]),
    
    # Knowledge and Facts
    (r"tell me a fact", ["Did you know honey never spoils?", "A human heart beats over 100,000 times a day!"]),
    (r"do you know history", ["I know a bit! What would you like to know about?"]),
    (r"who is the president", ["You might want to check current news for that one."]),
    
    # Entertainment
    (r"what's your favorite movie", ["I can't watch movies, but I hear they're amazing!"]),
    (r"do you like music", ["Music sounds great, even though I can't listen to it."]),
    (r"who is your favorite singer", ["I don't have a favorite, but I'd love to hear about yours!"]),
    
    # Hobbies and Fun
    (r"what do you do for fun", ["Chatting with you is the best part of my day!"]),
    (r"do you play games", ["I can play word games with you if you'd like!"]),
    (r"can you dance", ["Not physically, but I can imagine a dance party!"]),
    
    # Health and Wellness
    (r"i feel sick", ["I'm sorry to hear that. Make sure to rest and maybe see a doctor."]),
    (r"i have a headache", ["Rest and take it easy. A doctor might help if it persists."]),
    (r"do you exercise", ["Not really, but I stay mentally active for you!"]),
    
    # Work and Productivity
    (r"how do i focus better", ["Try taking breaks, or working in small chunks of time."]),
    (r"how do i stay organized", ["Maybe try a planner or a to-do list. It helps!"]),
    (r"how do i manage time", ["Prioritize tasks and break things down into steps."]),
    
    # Food and Diet
    (r"what should i eat", ["Something healthy and tasty, perhaps?"]),
    (r"do you like pizza", ["I can't eat, but pizza sounds delicious!"]),
    (r"do you eat vegetables", ["No need to eat, but veggies are great for health!"]),
    
    # Motivation and Encouragement
    (r"i feel like giving up", ["Don't give up! Just take one step at a time."]),
    (r"i can't do this", ["Believe in yourself. You've got this!"]),
    (r"i feel unmotivated", ["Everyone has those days. Try taking a small step forward."]),
    
    # Random Facts and Trivia
    (r"tell me something interesting", ["Octopuses have three hearts!", "Bananas are berries, but strawberries aren't!"]),
    (r"tell me a random fact", ["A group of flamingos is called a 'flamboyance.'"]),
    (r"do you know trivia", ["Sure! I have plenty of trivia facts up my sleeve."]),
    
    # Future Questions
    (r"what is the future", ["The future is what we make of it!"]),
    (r"can you predict the future", ["Not exactly, but we can dream together!"]),
    (r"do you believe in destiny", ["That's a fascinating concept. What do you think about it?"]),
    
    # Science and Nature
    (r"what is gravity", ["Gravity is the force that pulls objects towards each other."]),
    (r"do you know physics", ["I know a bit about physics. Anything specific?"]),
    (r"do you like nature", ["Nature is amazing! I’d love to learn more about it with you."]),
    
    # Technology and AI
    (r"do you know about ai", ["Yes, I'm part of AI technology!"]),
    (r"what is a chatbot", ["A chatbot is a program designed to talk with you, just like me!"]),
    (r"do you know coding", ["I am made of code! Programming is my foundation."]),
    
    # Society and Culture
    (r"what is culture", ["Culture refers to the customs and traditions of a group of people."]),
    (r"what is art", ["Art is a form of expression in various mediums like painting, music, and dance."]),
    (r"what's your favorite book", ["I don't read books, but I'd love to hear about yours!"]),
    
    # Space and Astronomy
    (r"what is a black hole", ["A black hole is a region in space with such strong gravity that not even light can escape."]),
    (r"do you know about stars", ["Stars are luminous balls of gas in space, mainly made of hydrogen and helium."]),
    (r"what's the moon made of", ["The moon is mostly made of rock and dust."]),
    
    # Philosophy and Deep Questions
    (r"what is life", ["That's a big question! Life is a journey, full of learning and growth."]),
    (r"what is love", ["Love is a deep and wonderful feeling that connects people."]),
    (r"why are we here", ["That's a philosophical question! What do you think?"]),
    
    # History and Events
    (r"when was the internet invented", ["The internet started to take shape in the late 1960s."]),
    (r"who invented the computer", ["Charles Babbage is often called the father of the computer."]),
    (r"tell me a historical fact", ["The Great Wall of China is over 13,000 miles long!"]),
    
    # Personal Growth
    (r"how can i be more confident", ["Believe in yourself and take things one step at a time."]),
    (r"how do i stop procrastinating", ["Try breaking down tasks and starting small."]),
    (r"how can i improve myself", ["Continuous learning and reflection can go a long way."]),
    
    # Relationships and Social Skills
    (r"how do i make friends", ["Be kind, listen, and show interest in others!"]),
    (r"how do i talk to people", ["Start by asking open-ended questions and listen actively."]),
    (r"how do i handle criticism", ["Take it as a learning experience and improve from it."]),
    
    # Fun and Games
    (r"do you know any games", ["I can play word games or trivia with you!"]),
    (r"can you guess a number", ["Sure! Think of a number and I'll try to guess."]),
    (r"let's play rock paper scissors", ["Alright! Rock, Paper, or Scissors?"]),
    
    # Language and Learning
    (r"can you speak another language", ["I can learn phrases in other languages if you teach me!"]),
    (r"how do you say hello in french", ["'Hello' in French is 'Bonjour.'"]),
    (r"what language do you know", ["I mainly use English, but I'm learning all the time!"]),
    
    # Closing Thoughts
    (r"thank you for talking to me", ["You're always welcome!"]),
    (r"this was fun", ["I'm glad you enjoyed it!"]),
    (r"talk to you later", ["Looking forward to it!"]),

    # Motivational Quotes
    (r"i need motivation", ["Believe in yourself and take one step at a time.", "You can do it! Stay positive."]),
    (r"i feel unmotivated", ["Try breaking tasks into smaller steps and celebrate small wins!", "A small step is still a step forward."]),
    (r"i need encouragement", ["You're stronger than you think! Keep going!", "You’ve got this!"]),
    
    # Personal Development
    (r"how can i improve my skills", ["Practice regularly and never stop learning.", "Focus on the areas you want to improve and dedicate time to them."]),
    (r"how do i become successful", ["Set clear goals, work hard, and never give up.", "Success is about persistence and learning from failure."]),
    
    # Work and Career
    (r"how do i get a job", ["Update your resume, apply to jobs, and prepare well for interviews!", "Networking and a good portfolio can help a lot!"]),
    (r"what should i wear to an interview", ["Wear something professional and make sure you're comfortable!", "Dress appropriately for the job you're applying to."]),
    (r"how do i improve at work", ["Focus on communication, be reliable, and look for ways to contribute beyond your role."]),
    (r"how do i handle work stress", ["Take breaks, prioritize tasks, and don't be afraid to ask for help!"]),
    
    # Tech and Innovation
    (r"what is ai", ["AI, or Artificial Intelligence, is the simulation of human intelligence in machines.", "AI is about making machines think and learn like humans."]),
    (r"what is machine learning", ["Machine learning is a subset of AI where systems learn from data and improve over time."]),
    (r"what is deep learning", ["Deep learning is a type of machine learning that uses neural networks with many layers to learn from large amounts of data."]),
    (r"how do i learn to code", ["Start with a beginner-friendly language like Python, and practice regularly!"]),
    (r"what is the best programming language", ["It depends on what you want to do! Python is great for beginners, while JavaScript is great for web development."]),
    (r"what is blockchain", ["Blockchain is a distributed ledger technology that ensures data is secure and transparent."]),
    (r"what is a neural network", ["A neural network is a system of algorithms modeled after the human brain that can recognize patterns."]),
    (r"how does the internet work", ["The internet is a network of interconnected devices that communicate via protocols like HTTP, using servers and clients."]),
    
    # Everyday Life
    (r"what is the best way to stay healthy", ["Eat a balanced diet, exercise regularly, and get enough sleep!"]),
    (r"how can i be more productive", ["Set clear goals, eliminate distractions, and use time management techniques!"]),
    (r"how do i improve my memory", ["Try using memory techniques like repetition, association, and visualization."]),
    (r"how do i manage stress", ["Take deep breaths, meditate, and try physical activities like yoga or exercise."]),
    (r"how can i sleep better", ["Try creating a bedtime routine, avoid screens before sleep, and keep your room cool and dark."]),
    
    # Popular Culture
    (r"who is the richest person in the world", ["As of now, Elon Musk and Bernard Arnault are among the richest."]),
    (r"who is the president of the usa", ["The current president is Joe Biden."]),
    (r"who is the best football player", ["That's a tough question, but Lionel Messi and Cristiano Ronaldo are often considered the best."]),
    (r"who is the greatest basketball player", ["Michael Jordan is often regarded as the greatest, though LeBron James is also a strong contender."]),
    (r"who is the best actor", ["There are so many incredible actors, but some popular choices are Leonardo DiCaprio, Tom Hanks, and Meryl Streep."]),
    
    # Philosophical Questions
    (r"what is the meaning of life", ["That's a profound question! Some say it’s about finding purpose, while others see it as a journey of self-discovery."]),
    (r"what is the purpose of existence", ["The purpose of existence can vary for each person, often defined by individual beliefs and goals."]),
    (r"what is happiness", ["Happiness is a state of well-being and contentment, but it can mean different things to different people."]),
    (r"why do people exist", ["That’s a big question! Some believe it’s to find meaning and purpose in life."]),
    (r"what is the best way to live life", ["Live authentically, pursue your passions, and cherish relationships with others."]),
    
    # Science and Nature
    (r"how do trees grow", ["Trees grow by absorbing water and nutrients through their roots and using sunlight to photosynthesize."]),
    (r"what is photosynthesis", ["Photosynthesis is the process by which plants use sunlight to synthesize foods from carbon dioxide and water."]),
    (r"what is evolution", ["Evolution is the process through which species adapt over generations to their environment."]),
    (r"what is a black hole", ["A black hole is a region in space where gravity is so strong that nothing, not even light, can escape."]),
    (r"how far is the sun", ["The sun is about 93 million miles away from Earth."]),
    
    # History and Geography
    (r"who discovered america", ["Christopher Columbus is often credited with discovering America in 1492."]),
    (r"when was the first world war", ["World War I started in 1914 and ended in 1918."]),
    (r"what is the largest country", ["Russia is the largest country in the world by land area."]),
    (r"what is the capital of france", ["The capital of France is Paris."]),
    (r"where is the eiffel tower", ["The Eiffel Tower is located in Paris, France."]),
    
    # Fun and Entertainment
    (r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!"]),
    (r"tell me a riddle", ["I have keys but open no locks. I have space but no room. You can enter but never leave. What am I?"]),
    (r"what's your favorite joke", ["Why did the computer break up with the internet? There was no connection!"]),
    (r"can you tell me a fun fact", ["Did you know that a day on Venus is longer than a year on Venus?"]),
    (r"what is the best movie", ["There are so many great movies, but classics like 'The Godfather' and 'The Shawshank Redemption' are often favorites."]),
    
    # Travel and Places
    (r"where is the great wall of china", ["The Great Wall of China is in China, stretching across northern parts of the country."]),
    (r"what's the best city to visit", ["It depends on what you like, but cities like Paris, New York, and Tokyo are famous for their attractions."]),
    (r"where is the pyramids of egypt", ["The Pyramids of Egypt are located in Giza, near Cairo."]),
    (r"where is the statue of liberty", ["The Statue of Liberty is located in New York City, USA."]),
    (r"where can i go for a beach vacation", ["You could try places like Hawaii, the Maldives, or the Caribbean for beautiful beaches."]),
    
    # Food and Cooking
    (r"what's your favorite food", ["I don’t eat, but I hear pizza and pasta are very popular!"]),
    (r"how do you make spaghetti", ["To make spaghetti, boil pasta, cook it with sauce, and enjoy!"]),
    (r"what's a good recipe", ["How about a quick stir-fry? Just cook veggies and your favorite protein in a pan with some soy sauce."]),
    (r"do you like chocolate", ["I can’t eat chocolate, but it’s a popular treat!"]),
    (r"what's your favorite dessert", ["I can't taste, but I know that ice cream and cake are popular desserts."]),
    
    # Language and Learning
    (r"how do you say thank you in spanish", ["'Thank you' in Spanish is 'Gracias.'"]),
    (r"how do you say hello in italian", ["'Hello' in Italian is 'Ciao.'"]),
    (r"how do you say goodbye in french", ["'Goodbye' in French is 'Au revoir.'"]),
    (r"do you know spanish", ["I know some Spanish! I can learn more if you teach me."]),
    (r"can you speak german", ["I can learn phrases in German! 'Hello' is 'Hallo.'"]),
    
    # Random Fun
    (r"do you believe in aliens", ["There might be life out there! The universe is vast, after all."]),
    (r"can you do magic", ["I can't do magic, but I can do some fun tricks with words!"]),
    (r"can you sing", ["I can't sing, but I can imagine a song in my mind!"]),
    (r"can you tell a story", ["Sure! Once upon a time, in a world of code, there was a chatbot who loved to chat with people."]),
    (r"what do you think of the future", ["The future holds endless possibilities! Technology is advancing rapidly, and there are so many exciting things ahead."]),

    # General Advice
    (r"how can i be more confident", ["Start by acknowledging your strengths, and don't be afraid to take small risks!"]),
    (r"what should i do when i'm scared", ["Take deep breaths, focus on the present moment, and break things down into manageable steps."]),
    (r"how do i make friends", ["Be yourself, take the initiative, and show interest in others!"]),
    (r"how do i stop procrastinating", ["Start with a small task to gain momentum and reward yourself afterward."]),
    (r"how do i become more organized", ["Use planners, make to-do lists, and prioritize tasks by importance."]),

    # Money and Finance
    (r"how do i save money", ["Create a budget, track your expenses, and set clear savings goals!"]),
    (r"what is the stock market", ["The stock market is a place where stocks, or shares in companies, are bought and sold."]),
    (r"how do i invest", ["Start by researching and understanding the different types of investments, like stocks, bonds, and mutual funds."]),
    (r"what is cryptocurrency", ["Cryptocurrency is a digital or virtual form of money that uses cryptography for security."]),
    (r"how do credit cards work", ["Credit cards allow you to borrow money up to a limit, which you must repay later with interest if not paid in full."]),

    # Time Management
    (r"how can i improve time management", ["Use tools like calendars and timers, and prioritize tasks based on deadlines and importance."]),
    (r"what is the pomodoro technique", ["The Pomodoro Technique is a time management method where you work for 25 minutes and take a 5-minute break."]),
    (r"how do i stop wasting time", ["Identify distractions, set clear goals, and break tasks into smaller, manageable steps."]),
    (r"how do i stay focused", ["Remove distractions, set short goals, and take regular breaks."]),
    (r"how do i manage my time better", ["Plan your day the night before, use time blocks, and learn to say no when necessary."]),

    # Health and Wellness
    (r"how do i start exercising", ["Start with simple exercises like walking or stretching, and gradually increase intensity over time."]),
    (r"how do i stay hydrated", ["Drink plenty of water throughout the day and eat hydrating foods like fruits and vegetables."]),
    (r"how do i improve my posture", ["Sit and stand with your back straight, shoulders back, and avoid slouching."]),
    (r"how can i get more energy", ["Eat balanced meals, exercise regularly, and get enough sleep."]),
    (r"how do i deal with anxiety", ["Practice mindfulness, talk to a therapist, and try relaxation techniques like deep breathing."]),

    # Learning and Education
    (r"how do i learn a new language", ["Start with basic vocabulary, practice daily, and immerse yourself in the language by listening and speaking."]),
    (r"how can i be a better student", ["Stay organized, participate in class, and review material regularly."]),
    (r"what are good study habits", ["Use active recall, spaced repetition, and eliminate distractions while studying."]),
    (r"how do i prepare for exams", ["Create a study schedule, practice past exams, and ensure adequate rest before the exam day."]),
    (r"how do i improve reading speed", ["Practice reading regularly, focus on comprehension, and try skimming or scanning techniques."]),

    # Technology and Gadgets
    (r"what is a smartphone", ["A smartphone is a portable device that combines a phone with various computing functions, like internet browsing and apps."]),
    (r"what is an operating system", ["An operating system is the software that manages hardware and software resources on a computer or device."]),
    (r"how do i clean my laptop", ["Turn it off, unplug it, and use a microfiber cloth to wipe the screen and keyboard."]),
    (r"what is cloud storage", ["Cloud storage allows you to store data on remote servers that you can access over the internet."]),
    (r"what is virtual reality", ["Virtual reality is a simulated experience that can be similar to or completely different from the real world."]),

    # Food and Cooking
    (r"how do i make a salad", ["Chop fresh vegetables, add some protein like chicken or beans, and top with dressing."]),
    (r"what's the best way to cook chicken", ["You can grill, bake, or pan-fry chicken for a delicious meal."]),
    (r"how do i cook rice", ["Rinse the rice, then cook it in a pot with water until it's soft and fluffy."]),
    (r"what can i do with eggs", ["You can scramble, fry, boil, or make an omelette!"]),
    (r"how do i make a smoothie", ["Blend fruits, veggies, yogurt, and some ice or water for a refreshing drink."]),

    # Fun and Entertainment
    (r"what's your favorite movie", ["I don’t have favorites, but I know 'The Shawshank Redemption' is highly regarded."]),
    (r"what is a good tv show", ["Shows like 'Breaking Bad,' 'Stranger Things,' and 'The Office' are very popular."]),
    (r"what is the best book", ["There are many great books, but '1984' by George Orwell is often cited as one of the best."]),
    (r"who is the most famous musician", ["Artists like Michael Jackson, The Beatles, and Beyoncé are among the most famous musicians."]),
    (r"what is the best video game", ["Popular games like 'The Legend of Zelda: Breath of the Wild,' 'The Witcher 3,' and 'Minecraft' are highly rated."]),

    # Social Media
    (r"how do i grow my instagram", ["Post regularly, use relevant hashtags, engage with your followers, and collaborate with others."]),
    (r"how do i get more followers on twitter", ["Tweet frequently, engage with others' content, and use hashtags to increase visibility."]),
    (r"how do i make a viral video", ["Create content that’s entertaining, relevant, and shareable, and promote it through social media."]),
    (r"how do i use tiktok", ["Create short, fun videos with music or trends that appeal to a wide audience."]),
    (r"what is a good social media strategy", ["Post consistently, understand your audience, and engage with comments and messages."]),

    # Travel and Adventure
    (r"where should i go for a vacation", ["It depends on what you like, but places like Paris, Tokyo, and Bali offer amazing experiences."]),
    (r"what are the best travel destinations", ["Destinations like New York, Rome, and Kyoto are known for their culture and landmarks."]),
    (r"how do i travel on a budget", ["Look for deals, travel in off-peak seasons, and consider alternative accommodations like hostels or Airbnb."]),
    (r"how do i pack light", ["Pack versatile clothing, minimize toiletries, and choose items that can serve multiple purposes."]),
    (r"what are the safest travel destinations", ["Countries like Switzerland, Japan, and Canada are often considered very safe for travelers."]),

    # Relationships and Dating
    (r"how do i get a girlfriend", ["Be yourself, be confident, and show genuine interest in the person you're interested in."]),
    (r"how do i handle a breakup", ["Allow yourself to grieve, talk to friends, and focus on self-care."]),
    (r"what should i do on a first date", ["Be polite, be yourself, and choose an activity that allows you to talk and get to know each other."]),
    (r"how do i trust someone again", ["Take things slowly, communicate openly, and focus on rebuilding the relationship over time."]),
    (r"how do i improve my communication skills", ["Listen actively, be clear and concise, and practice empathy."]),

    # Sports
    (r"what is football", ["Football is a team sport where two teams compete to score goals by kicking a ball into the opponent’s net."]),
    (r"how do i play basketball", ["Basketball involves shooting a ball into the opponent's hoop while dribbling and passing it."]),
    (r"how do i improve at tennis", ["Practice your serve, work on your footwork, and focus on consistency."]),
    (r"what is a good workout routine", ["Start with strength training, combine cardio, and make sure to rest between workouts."]),
    (r"how do i run faster", ["Work on your speed and endurance with interval training and proper form."]),

    # Science and Nature
    (r"what is gravity", ["Gravity is a force that attracts objects toward one another, such as the Earth pulling objects toward its center."]),
    (r"how do plants grow", ["Plants need sunlight, water, and nutrients from the soil to grow."]),
    (r"how does the water cycle work", ["Water evaporates, forms clouds, and then falls as precipitation, repeating the cycle."]),
    (r"what is the greenhouse effect", ["The greenhouse effect occurs when gases in Earth's atmosphere trap heat from the sun, leading to warming."]),
    (r"what is a star", ["A star is a massive ball of hot, glowing gas, primarily hydrogen and helium, that produces light and energy."]),

    # History
    (r"who was the first president of the united states", ["George Washington was the first president of the United States."]),
    (r"when did world war ii end", ["World War II ended in 1945."]),
    (r"who discovered america", ["Christopher Columbus is credited with discovering America in 1492."]),
    (r"what was the cold war", ["The Cold War was a period of tension between the United States and the Soviet Union after World War II."]),
    (r"what was the renaissance", ["The Renaissance was a cultural movement in Europe from the 14th to the 17th century, characterized by a revival of art and learning."]),

    # Miscellaneous
    (r"what is the meaning of life", ["The meaning of life is subjective and can vary depending on personal beliefs and experiences."]),
    (r"what is time", ["Time is a continuous, irreversible progression of events from the past to the present and into the future."]),
    (r"what is infinity", ["Infinity is the concept of something that has no end or limit."]),
    (r"what is a black hole", ["A black hole is a region of space where gravity is so strong that nothing, not even light, can escape."]),
    (r"what is the universe", ["The universe is everything that exists, including all matter, energy, space, and time."]),
    (r"(.*)", ["I'm sorry, I don't quite understand. Could you rephrase?", "I'm here to help, could you try asking in a different way?"])
]

def chatbot_response(user_input):
    for pattern, responses in pairs:
        match = re.match(pattern, user_input)
        if match:
            response = random.choice(responses)
            return response.replace('%1', match.group(1) if match.groups() else "")
    return "I'm sorry, I didn't understand that."

def main():
    print("Hi, I am Chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))

main()
