# Chatbots

## **Define scope of business case:**
* Open Domain or Closed Domain? - Closed
* B2C Services or B2B Operations? - B2B
* B2C improvement by Auto Query Handling (Trains on H2H conv history) or Information Retrieval (Trains on Info Map)? - NA
* B2B improvement by Knowledge Retrieval or AI Generation ? - Knowledge Retrieval
* Retrieval (Q&A Capability) or Generative (Dialectic Capability - AI)? - Retrieval
* Knowledge Retrival on Concepts or Metrics ? - 

## **Prediction problems:**
* define Regression problem:
* demonstrate capability of Machine Learning to solve regression:
* define Classification problem:
* demonstrate capability of Machine Learning to solve classification:
* define Clustering problem:
* demonstrate capability of Machine Learning to solve Clustering:
* define NLP problem: 
* demonstrate capability of deep learning to solve NLP:


### Glossary
* **Retrieval-Based vs. Generative Models:**
Retrieval-based models (easier) use a repository of predefined responses and some kind of heuristic to pick an appropriate response based on the input and context. The heuristic could be as simple as a rule-based expression match, or as complex as an ensemble of Machine Learning classifiers. These systems don’t generate any new text, they just pick a response from a fixed set.
Generative models (harder) don’t rely on pre-defined responses. They generate new responses from scratch. Generative models are typically based on Machine Translation techniques, but instead of translating from one language to another, we “translate” from an input to an output (response).
But why would you want to build a retrieval-based model if you can build a generative model? Generative models seem more flexible because they don’t need this repository of predefined responses, right?
The problem is that generative models don’t work well in practice. At least not yet. Because they have so much freedom in how they can respond, generative models tend to make grammatical mistakes and produce irrelevant, generic or inconsistent responses. They also need huge amounts of training data and are hard to optimize. The vast majority of production systems today are retrieval-based, or a combination of retrieval-based and generative. Google’s Smart Reply is a good example. Generative models are an active area of research, but we’re not quite there yet. If you want to build a conversational agent today your best bet is most likely a retrieval-based model.

* **Open Domain vs. Closed Domain:**
In an open domain (harder) setting the user can take the conversation anywhere. There isn’t necessarily have a well-defined goal or intention. Conversations on social media sites like Twitter and Reddit are typically open domain – they can go into all kinds of directions. The infinite number of topics and the fact that a certain amount of world knowledge is required to create reasonable responses makes this a hard problem.
In a closed domain (easier) setting the space of possible inputs and outputs is somewhat limited because the system is trying to achieve a very specific goal. Technical Customer Support or Shopping Assistants are examples of closed domain problems. These systems don’t need to be able to talk about politics, they just need to fulfill their specific task as efficiently as possible. Sure, users can still take the conversation anywhere they want, but the system isn’t required to handle all these cases – and the users don’t expect it to.

* **Long vs. Short Conversations:**
The longer the conversation the more difficult to automate it. On one side of the spectrum are Short-Text Conversations (easier) where the goal is to create a single response to a single input. For example, you may receive a specific question from a user and reply with an appropriate answer. Then there are long conversations (harder) where you go through multiple turns and need to keep track of what has been said. Customer support conversations are typically long conversational threads with multiple questions.

### Scaling up to a Generative system or Dialogue Agent or Conversation System 
* **Incorporating Context:**
To produce sensible responses systems may need to incorporate both linguistic context and physical context. 
In long dialogs people keep track of what has been said and what information has been exchanged which is the linguistic context.
One may also need to incorporate other kinds of contextual data such as date/time, location, or information about a user which the physical context.
In machine translation and Jeopardy-playing Q/A systems, the context is limited to the current question. In an extended dialog-based conversational system, the context needs to be maintained across multiple Q/A sequences. Maintaining context over a period of time is a key requirement for dialog systems

* **Incorporating Coherent Personality:**
When generating responses the agent should ideally produce consistent answers to semantically identical inputs. For example, you want to get the same reply to “How old are you?” and “What is your age?”. 

* **Incorporating Intention and Diversity:**
A common problem with generative systems is that they tend to produce generic responses like “That’s great!” or “I don’t know” that work for a lot of input cases. Early versions of Google’s Smart Reply tended to respond with “I love you” to almost anything. That’s partly a result of how these systems are trained, both in terms of data and in terms of actual training objective/algorithm. Some researchers have tried to artificially promote diversity through various objective functions. However, humans typically produce responses that are specific to the input and carry an intention. Because generative systems (and particularly open-domain systems) aren’t trained to have specific intentions they lack this kind of diversity

* **Incorporating Attention and Memory:**



**References :**
http://www.wildml.com/2016/04/deep-learning-for-chatbots-part-1-introduction/
http://www.wildml.com/2016/07/deep-learning-for-chatbots-2-retrieval-based-model-tensorflow/
http://www.wildml.com/2016/01/attention-and-memory-in-deep-learning-and-nlp/
https://www.tensorflow.org/tutorials/seq2seq
