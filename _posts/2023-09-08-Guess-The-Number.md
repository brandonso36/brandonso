---
comments: False
layout: post
title: Guess the Number
description: Try and guess the number
type: hacks
courses: {'compsci': {'week': 3}}
categories: ['C4.1']
---

<html>
<head>
    <title>Guess the Number Game</title>
</head>
<body>
    <h1>Guess the Number Game (1-10)</h1>
    <p>Guess a number between 1 and 10:</p>
    <input type="text" id="guessField">
    <input type="submit" value="Submit guess" id="guessSubmit">
    <p class="message"></p>
    <script>
        // Generate a random number between 1 and 10
        const randomNumber = Math.floor(Math.random() * 10) + 1;
        // Get references to HTML elements
        const guessField = document.getElementById('guessField');
        const guessSubmit = document.getElementById('guessSubmit');
        const message = document.querySelector('.message');
        // Track the number of guesses
        let guessCount = 0;
        // Function to check the player's guess
        function checkGuess() {
            const userGuess = Number(guessField.value);
            guessCount++;
            // Check if the guess is correct
            if (userGuess === randomNumber) {
                message.textContent = `Congratulations! You guessed the number in ${guessCount} guesses.`;
                message.style.backgroundColor = 'green';
                gameOver();
            } else if (guessCount === 3) {
                message.textContent = `Game over! The number was ${randomNumber}.`;
                message.style.backgroundColor = 'red';
                gameOver();
            } else {
                message.textContent = `Wrong guess! Try again. (Guess #${guessCount})`;
                message.style.backgroundColor = 'red';
            }
            // Clear the guess field for the next guess
            guessField.value = '';
            guessField.focus();
        }
        // Function to end the game and disable input
        function gameOver() {
            guessField.disabled = true;
            guessSubmit.disabled = true;
        }
        // Event listener for the "Submit guess" button
        guessSubmit.addEventListener('click', checkGuess);
        // Event listener for the guess input field (Enter key)
        guessField.addEventListener('keyup', function(event) {
            if (event.key === 'Enter') {
                checkGuess();
            }
        });
    </script>
</body>
</html>

