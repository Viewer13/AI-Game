# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked normal when I first ran it, only took two attempts to guess the right answer. On the second attempt, I used the hint available and the number was correct. The third attempt was when I noticed something off, with the level difficulties not being fair/even between easy, medium, and hard. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
I checked the hint, expecting it to be in the bounds of the level difficulty parameters, instead it was lower/higher than the level difficulty allowed and yet it worked. The input bar accepts negative numbers even though the full set of acceptable numbers are between the positive numbers of 1 and 100. When I guess a number and I'm givin an message that told me to go higher/lower, I check the hint expecting it to be in the bounds and the final number is higher/lower than the message. When I type a number out of bounds of the level difficulty set I expected an message telling me it's out of bounds, instead it's accepted.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot on this project. It's the best geared for the coding challenges. I attempted the same thing with other AI's, they didn't have the same help as Copilot.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When I asked about adjusting the level difficulty boundaries, it gave a very logical and correct change in the code. From there, I double checked the logic and ensured it was sound and correct.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). When I asked about the logic change, it gave me an error at first. I had to do some research to fix the mistake.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
After checking for any errors in the game, I changed the code and then refreshed the game page to confirm it worked.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran a pytest to see if the code was correct and it gave me an error. I had to make changes and saw that it was working in the game page itself.
- Did AI help you design or understand any tests? How?
AI was essentially a guide/tutor throughout the entire adjustment of the code.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because of it being a random variable to keep the game interesting.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Imagine your Streamlit app is like a simple Python script that runs from top to bottom every single time something changes. That complete re-execution of the script is called a rerun. If every rerun starts fresh, how do you keep track of things that should last longer, like a user's progress through a form or items in a shopping cart? This is where session state comes in. Session state is a special, built-in dictionary in your app (st.session_state) where you can store variables and data that need to stick around across different reruns for a specific user.
- What change did you make that finally gave the game a stable secret number? I asked AI to help me readjust the code to not make it random.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Reusing the pytesting made by Copilot to test the code and understanding the logic behind the bad code.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I would properly test the code for errors using a pre-test case. Along with more outside research.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I found that AI generated code was both effective and teachable. Especially when I want to understand how certain lines of code work.