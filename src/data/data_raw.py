import pandas as pd
def data_raw():

    data = {
        'question': [
            "What is Lionel Messi's full name?",
            "Which club did Messi start his professional career with?",
            "How many Ballon d'Or awards has Messi won?",
            "In which year did Messi join Paris Saint-Germain (PSG)?",
            "How many goals did Messi score for Barcelona?",
            "Which country does Messi represent in international football?",
            "How many FIFA World Cups has Messi won with Argentina?",
            "What is Messi's nickname?",
            "Which team did Messi join after leaving Barcelona?",
            "How many times has Messi been named the European Golden Shoe winner?",
            "What is Virat Kohli's full name?",
            "Which Indian Premier League (IPL) team does Kohli play for?",
            "How many centuries has Kohli scored in One Day Internationals (ODIs)?",
            "What is Kohli's highest score in Test cricket?",
            "Which year did Kohli become the captain of the Indian cricket team?",
            "How many runs has Kohli scored in T20 Internationals?",
            "What is Kohli's nickname?",
            "Which award has Kohli won the most in his career?",
            "How many times has Kohli been named the ICC ODI Player of the Year?",
            "What is Kohli's highest score in T20 Internationals?",
            "What is Shah Rukh Khan's full name?",
            "In which year did Shah Rukh Khan make his Bollywood debut?",
            "Which production company did Shah Rukh Khan found?",
            "How many Filmfare Awards has Shah Rukh Khan won?",
            "Which iconic character did Shah Rukh Khan portray in the film 'Dilwale Dulhania Le Jayenge'?",
            "What is Shah Rukh Khan's nickname?",
            "Which film marked Shah Rukh Khan's 100th movie?",
            "Which sport does Shah Rukh Khan own a franchise in?",
            "What is Shah Rukh Khan's alma mater?",
            "Which award did Shah Rukh Khan receive from the Government of France?"
        ],
        'answer': [
            "Lionel Andrés Messi Cuccittini",
            "FC Barcelona",
            "Seven",
            "2021",
            "672 goals",
            "Argentina",
            "One, in 2022",
            "\"La Pulga\" (The Flea)",
            "Inter Miami CF",
            "Six times",
            "Virat Kohli",
            "Royal Challengers Bangalore",
            "43",
            "254 against South Africa in 2013",
            "2017",
            "2,928 runs",
            "\"King Kohli\"",
            "ICC Cricketer of the Year",
            "Four times",
            "94 against Australia in 2016",
            "Shah Rukh Khan",
            "1992 with the film \"Deewana\"",
            "Red Chillies Entertainment",
            "14",
            "Raj Malhotra",
            "\"King Khan\"",
            "\"Zero\" (2018)",
            "Cricket, Kolkata Knight Riders in the IPL",
            "Hansraj College, Delhi University",
            "Legion of Honour"
        ]
    }

    # Create DataFrame
    df = pd.DataFrame(data)
    return df

