Demo: https://youtu.be/OB0jeGnNiqw

## Inspiration

With the internet’s increasing influence on people’s lives, the internet has changed the fundamental nature in which we communicate and consume information. 

Although there is a vast amount of information available with just an internet connection, there are many problems we face when interacting with news online. Some of these include too much information, irresponsible headlines/reporting, and a lack of ways to act on the information you read. **This is a particularly big issue when it comes to reporting on mental health and suicide.** Studies have shown that the way we talk about suicide publicly can have astounding consequences.

## What it does

takeAction! is a google chrome extension that analyzes a webpage the user is currently on. Machine learning is then used to analyze the content of the webpage and detect if there is unethical or misleading reporting regarding mental health or suicide. If it is detected, articles are provided to the user to explain the misunderstood aspects of mental illness that are often exacerbated by the media.

The extension also offers trusted organizations that the user can truly take action by donating to. Thus, our solution works in two ways: spreading awareness for mental health and the truth about suicide, and then bringing real change.

## How I built it

Our datasets were created through web scraping relevant articles. We then used state of the art NLP models developed in Tensorflow to categorize articles. A high validation accuracy was achieved by using a large dataset and extensive data preprocessing. 

In addition, Our system architecture was developed with scalability and ease of use in mind. Technologies such as kubernetes, docker, Google cloud were used to ensure that we can scale to thousands of users at a time.

## Accomplishments that I'm proud of

After hours of hard work, we were extremely proud to see our program respond to the ML training via the data sets. We were also happy with our frontend Chrome Extension functionality, as it is the fastest way that the widest group of users would conveniently be able to use our powerful tool.

## What I learned

Prior to this project, our team members had little to no experience with ML, but as we dived into this project we learned valuable skills. The project was also a unique opportunity for us to brush up on our Python, React, and JavaScript skills.

## What's next for takeAction!

In the future, we hope to hone our project further by improving the accuracy of the ML model and have it return links to resources that are both, directly and indirectly, related to the article's core issue. Celebrity suicide reporting is just one consequence of mass media that poses a threat to mental health. We would like to broaden our product's use cases as there are many different issues that our quick and accessible extension can be used to solve.  
