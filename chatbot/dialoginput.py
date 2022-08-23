class DialogInput(object):
    def __init__(self):
        self.dialogs = [
            [
                r'greet',
                ["Hi, I'm Covid Guard and I chat alot ;)\n I can answer your question regarding Coronavirus(Covid-19)"]

            ],
            [
                r"my name is (.*)",
                ["Hello %1, How are you today ?", ]
            ],
            [
                r"what is your name ?",
                ["My name is Covid Guard and I'm a chatbot ?", ]
            ],
            [
                r"how are you ?",
                ["I'm doing good, How about You ?", ]
            ],
            [
                r"sorry (.*)",
                ["Its alright", "Its OK, never mind", ]
            ],
            [
                r"i'm (.*) doing good",
                ["Nice to hear that", "Alright :)", ]
            ],
            [
                r"hi|hey|hello",
                ["Hello", "Hey there", ]
            ],
            [
                r"(.*) age?",
                ["I'm a computer program dude\nSeriously you are asking me this?", ]

            ],
            [
                r"what (.*) want ?",
                ["Make me an offer I can't refuse", ]

            ],
            [
                r"(.*) created ?",
                ["Nagesh created me using Python's NLTK library ", "top secret ;)", ]
            ],
            [
                r"(.*) (location|city) ?",
                ['Chennai, Tamil Nadu', ]
            ],
            [
                r"how is weather in (.*)?",
                ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",
                 "Never even heard about %1"]
            ],
            [
                r"i work in (.*)?",
                ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
            ],
            [
                r"(.*)raining in (.*)",
                ["No rain since last week here in %2", "Damn its raining too much here in %2"]
            ],
            [
                r"how (.*) health(.*)",
                ["I'm a computer program, so I'm always healthy ", ]
            ],
            [
                r"(.*) (sports|game) ?",
                ["I'm a very big fan of Football", ]
            ],
            [
                r"who (.*) sportsperson ?",
                ["Messy", "Ronaldo", "Roony"]
            ],
            [
                r"who (.*) (moviestar|actor)?",
                ["Brad Pitt"]
            ],
            [
                r"quit",
                ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
            ],
            [
                r'What is a coronavirus?|What is corona?',
                ['Coronaviruses are a large family of viruses which may cause illness in animals or humans.']
            ],
            [
                r'What is covid-19 ?',
                ['COVID-19 is the infectious disease caused by the most recently discovered coronavirus. This new virus and disease were unknown before the outbreak began in Wuhan, China, in December 2019. COVID-19 is now a pandemic affecting many countries globally.']
            ],

            [
                r'What are the symptoms of COVID-19?',
                ['The most common symptoms of COVID-19 are fever, dry cough, and tiredness.']
            ],
            [
                r'What should I do if I have COVID-19 symptoms and when should I seek medical care?',
                [
                    'If you have minor symptoms, such as a slight cough or a mild fever, there is generally no need to seek medical care. Stay at home, self-isolate and monitor your symptoms. Follow national guidance on self-isolation.']
            ],
            [
                r'How does COVID-19 spread?',
                [
                    'People can catch COVID-19 from others who have the virus. The disease spreads primarily from person to person through small droplets from the nose or mouth, which are expelled when a person with COVID-19 coughs, sneezes, or speaks.']
            ],
            [
                r'Can COVID-19 be caught from a person who has no symptoms?',
                [
                    'COVID-19 is mainly spread through respiratory droplets expelled by someone who is coughing or has other symptoms such as fever or tiredness. Many people with COVID-19 experience only mild symptoms. This is particularly true in the early stages of the disease. It is possible to catch COVID-19 from someone who has just a mild cough and does not feel ill.']
            ],
            [
                r'How can we protect others and ourselves if we don''t know who is infected?',
                [
                    'Practicing hand and respiratory hygiene is important at ALL times and is the best way to protect others and yourself. When possible maintain at least a 1 meter distance between yourself and others. This is especially important if you are standing by someone who is coughing or sneezing.']
            ],
            [
                r'What should I do if I have come in close contact with someone who has COVID-19?',
                [
                    'If you have been in close contact with someone with COVID-19, you may be infected. Close contact means that you live with or have been in settings of less than 1 meter from those who have the disease. In these cases, it is best to stay at home.']
            ],
            [
                r'What does it mean to self-isolate?',
                [
                    'Self-isolation is an important measure taken by those who have COVID-19 symptoms to avoid infecting others in the community, including family members.']
            ],
            [
                r'What is the difference between self-isolation, self-quarantine and distancing?',
                [
                    'Quarantine means restricting activities or separating people who are not ill themselves but may have been exposed to COVID-19. The goal is to prevent spread of the disease at the time when people just develop symptoms. '
                    'Isolation means separating people who are ill with symptoms of COVID-19 and may be infectious to prevent the spread of the disease']
            ],
            [
                r'What should I do if I have no symptoms, but I think I have been exposed to COVID-19? What does it mean to self-quarantine?',
                [
                    'To self-quarantine means to separate yourself from others because you have been exposed to someone with COVID-19 even though you, yourself, do not have symptoms. During self-quarantine you monitor yourself for symptoms.  The goal of the self-quarantine is to prevent transmission.']
            ],
            [
                r'Can children or adolescents catch COVID-19?',
                [
                    'Research indicates that children and adolescents are just as likely to become infected as any other age group and can spread the disease.',
                    'Evidence to date suggests that children and young adults are less likely to get severe disease, but severe cases can still happen in these age groups.']
            ],
            [
                r'What can I do to protect myself and prevent the spread of disease?',
                [
                    'Stay aware of the latest information on the COVID-19 outbreak, available on the WHO website and through your national and local public health authority. Most countries around the world have seen cases of COVID-19 and many are experiencing outbreaks.']
            ],
            [
                r'Is there a vaccine, drug or treatment for COVID-19? ',
                [
                    'While some western, traditional or home remedies may provide comfort and alleviate symptoms of mild COVID-19, there are no medicines that have been shown to prevent or cure the disease. WHO does not recommend self-medication with any medicines, including antibiotics, as a prevention or cure for COVID-19. However, there are several ongoing clinical trials of both western and traditional medicines. WHO is coordinating efforts to develop vaccines and medicines to prevent and treat COVID-19 and will continue to provide updated information as soon research results become available.']
            ],
            [
                r'Does WHO recommend wearing medical masks to prevent the spread of COVID-19? ',
                [
                    'Currently, there is not enough evidence for or against the use of masks (medical or other) in healthy individuals in the wider community. However, WHO is actively studying the rapidly evolving science on masks and continuously updates its guidance. ']
            ],
            [
                r'How long does it take after exposure to COVID-19 to develop symptoms? ',
                [
                    'The time between exposure to COVID-19 and the moment when symptoms start is commonly around five to six days but can range from 1 – 14 days.']
            ],
            [
                r'What is the connection between COVID-19 and animals? ',
                ['COVID-19 is spread through human-to-human transmission. ']
            ],
            [
                r'Can I catch COVID-19 from my pet? ',
                [
                    'Several dogs and cats (domestic cats and a tiger) in contact with infected humans have tested positive for COVID-19. In addition, ferrets appear to be susceptible to the infection. In experimental conditions, both cats and ferrets were able to transmit infection to other animals of the same species, but there is no evidence that these animals can transmit the disease to human and play a role in spreading COVID-19. COVID-19 is mainly spread through droplets produced when an infected person coughs, sneezes, or speaks. ']
            ],
            [
                r'How long does the virus survive on surfaces? ',
                [
                    'The most important thing to know about coronavirus on surfaces is that they can easily be cleaned with common household disinfectants that will kill the virus. Studies have shown that the COVID-19 virus can survive for up to 72 hours on plastic and stainless steel, less than 4 hours on copper and less than 24 hours on cardboard.']
            ],
            [
                r'How to grocery shop safely? ',
                [
                    'When grocery shopping, keep at least 1-metre distance from others and avoid touching your eyes, mouth and nose. If possible, sanitize the handles of shopping trolleys or baskets before shopping. Once home, wash your hands thoroughly and also after handling and storing your purchased products.',
                    'There is currently no confirmed case of COVID-19 transmitted through food or food packaging.']
            ],
            [
                r'How to wash fruits and vegetables?',
                [
                    'Fruits and vegetables are important components of a healthy diet. Wash them the same way you should do under any circumstance: before handling them, wash your hands with soap and water. Then, wash fruits and vegetables thoroughly with clean water, especially if you eat them raw.']
            ],
            [
                r'Are antibiotics effective in preventing or treating COVID-19?',
                [
                    'No. Antibiotics do not work against viruses; they only work on bacterial infections. COVID-19 is caused by a virus, so antibiotics do not work. Antibiotics should not be used as a means of prevention or treatment of COVID-19. In hospitals physicians will sometimes use antibiotics to prevent or treat secondary bacterial infections which can be a complication of COVID-19 in severely ill patients. They should only be used as directed by a physician to treat a bacterial infection.']
            ],
            [
                r'Can I catch COVID-19 from the faces of someone with the disease?',
                [
                    'While initial investigations suggest the virus may be present in faeces in some cases, to date, there have not been reports of faecal-oral transmission of COVID-19. Additionally, there is no evidence to date on the survival of the COVID-19 virus in water or sewage.',
                    'WHO is assessing ongoing research on the ways COVID-19 is spread and will continue to share new findings on this topic.']
            ],

            [
                r'What is menstruation?',
                [
                    'Menstruation is the natural process in Women’s lives not a curse.',
                    'Menstruation is the monthly discharge of blood from the uterus through the vagina of girls at puberty and non-pregnant and non-menopausal women.'
                ],
                ],
              [
                  r'What is Menstrual Hygiene Management?',
                  [
                      'Menstrual Hygiene Management is defined as when women and adolescent girls use a clean material to absorb or collect menstrual blood and this material can be changed in privacy as often as necessary for the duration of menstruation. MHM also includes using soap and water for washing the body as required and having access to facilities to dispose of used menstrual management materials.'
                  ],
              ],
                [
                    r'Why is Menstrual hygiene being important?',
                    [
                        'It is a human rights issue',
                        'Safely practiced menstrual hygiene prevents infections and body odor',
                        'It reduces absenteeism from school and contribute to improved educational performance',
                        'enable women and girls to remain healthy, empowered, and become more productive for the growth of the country.',
                        'It contributes to the achievement of the Sustainable Development Goal targets in education, gender equality, reduction of maternal mortality and water and sanitation'
                    ],
                ],
            [
                r'At what age does a girl first observe menstruation?',
                [
                    'During the puberty (normally between the ages of 9 and 14)',
                ]
            ],
            [
                r'Is the there any variation in the length of the menstrual cycle and the amount of blood girls and women lose?',
                [
                    'Yes, the bleeding usually lasts from about three to seven days and the whole menstrual cycle takes 21 – 35 days with average length of 28 days from the first day of menstruation'
                ]
            ],
            [
                r'Is all women and girls suffering varying degree of pain and discomfort?',
                [
                    'Yes, during the menstrual cycle, most women and girls suffer varying degree of pain and discomfort which varies from person to person and can change significantly over time. For the first few years, long menstrual cycles are common. However, menstrual cycles tend to shorten and become more regular as a woman’s age increases. Abdominal cramps, nausea, fatigue, feeling faint, headaches, back ache and general discomfort are experienced by most girls and women during periods. Due to hormonal changes, they experience emotional and psychological changes such as heightened feelings of sadness, irritability, or anger.'
                ]
            ],
            [
                r'What are the effects of cultural practices and taboos around menstruation?',
                [
                    'Some cultural practices and taboos around menstruation impact the lives of women and girls negatively and reinforce gender inequities and exclusion.'
                ]
            ],
            [
                r'Is schools need to prepare Menstrual hygiene management equipment’s?',
                [
                    'Yes, all schools need to be well equipped with the basic amenities for menstrual management such as menstruation materials, places for changing menstruation materials, running water and disposal facilities.'
                ]
            ],
            [
                r'Is there any impact if schools not well equipped with MHM equipment with girls’ education?',
                [
                    'Yes, missing of classes during their menstrual period, reduced performance due to poor concentration etc. ',
                ]
            ],
            [
                r'How to manage your first period?',
                ['Having feminine hygiene products (sanitary pads) and over-the-counter pain relievers (see doctors) on hand.']
            ],
            [
                r'What products can be used to absorb the menstrual blood?',
                ['Sanitary pads used to absorb the menstrual blood.']
            ],
            [
                r'How to keep yourself clean during your period?',
                ['Wash regularly (Bathe or shower at least once a day to keep your body clean and avoid odor),',
                 'Change pads often'
                 ]
            ],
            [
                r'How to manage stomach pain/menstrual cramps',
                [
                    'Drink more water, taking a warm bath or apply heat pad, hot water bottle or heat patch to your abdomen, exercise …',
                  'Medicine – please see doctors'
                 ],
            ],
            [
                r'How to dispose of cloths and/or pads?',
                [
                    'Disposal of sanitary materials involves a number of steps in the waste disposal chain, particularly when a woman or a girl is in a school or other public places where sanitary materials are collected for disposal. In these instances, the waste chain is likely to include: a discrete, washable container with lid for temporary storing of used sanitary materials, collection, transfer and emptying of the containers and final destruction of the sanitary materials. The latter could include burying, incineration or burning, disposal into a regular waste management collection and disposal system, disposal into a pit latrine, and composting (for biodegradable sanitary materials).'
                ]
            ]
        ]
