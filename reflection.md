# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It worked but some behaviors were incorrect. I noticed the hints were not displayed accurately where the game told me go higher when i am supposed to go lower and lower when I am supposed to go higher. I also noticed how the difficulty level is to guess between 1-50 but the game tells me to guess from 1-100. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Secret = 50,Guess = 60| Hint should say "GO LOWER"| Hint says "GO HIGHER" | No Error|
|Secret = 50,Guess = 40| Hint should say "GO HIGHER" | Hint says "GO LOWER"| No Error|
|Game on Hard Difficulty|Instructions should show 1-50|Instructions show 1-100 | No Error|
|First Page load| Full number of attempts available| Attempts displayed are lower than expected| No Error|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
My check_guess() function was returning a tuple with a message and emoji instead of returning a simple string. I verified with oytest and after changing the function to return only the outcome string is when the tests passed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
With Claude's suggested check_guess() function , the tests were still failing and when i examined the code, it had inconsistent return types and missing equality check in except block. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
When all tests have passed and manual testing in the Streamlit app by playing the game again. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested with numbers higher than the secret number and lowerr than the secret number making sure the hints were accurate. For example my secret number was 47 so i tried 48, 50 , 30 and 20 until I used all attempts.
- Did AI help you design or understand any tests? How?
Yes. AI made me understand the tests with normal gameplay and edge cases like it helped create tests for winning guesses, guesses that were too high or too low, and comparisons between integers and strings such as check_guess(50, "50")
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire script every time a user interacts with a widget and because of it, session state is used to store information that should persist between reruns. 

A memorybox would a good example to explain session state to a friend. Without it, variables would reset every time teh page is refrshed or a button is clicked. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Reproducing bugs with specific test cases before making changes. Having a clear example of the problem made it much easier to verify that my fixes actually worked.
- What is one thing you would do differently next time you work with AI on a coding task?
I will verify the suggestions more carefully instead of assuming it is correct.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It showed me that code can appear correct but it can contian subtle logic errors. AI may produce instant results but it is our responsibilty to test and validate the final result.
