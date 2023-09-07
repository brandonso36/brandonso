---
comments: False
layout: post
title: Calculator 
description: A simple calcualtor with addition, subtraction, division, and multiplication
type: hacks
courses: {'compsci': {'week': 3}}
categories: ['C4.1']
---


<html>
<head>
    <title>Simple Calculator</title>
    <style>
        input[type="text"] {
            width: 100%;
            padding: 10px;
            font-size: 18px;
        }
        button {
            width: 48px;
            height: 48px;
            font-size: 18px;
            margin: 5px;
        }
    </style>
</head>
<body>
    <h1>Simple Calculator</h1>
    <input type="text" id="display" readonly>
    <br>
    <button onclick="appendToDisplay('9')">9</button>
    <button onclick="appendToDisplay('7')">7</button>
    <button onclick="appendToDisplay('8')">8</button>
    <button onclick="clearDisplay()">C</button>
    <button onclick="appendToDisplay('+')">+</button>
    <br>
    <button onclick="appendToDisplay('4')">4</button>
    <button onclick="appendToDisplay('5')">5</button>
    <button onclick="appendToDisplay('6')">6</button>
    <button onclick="appendToDisplay('-')">-</button>
    <br>
    <button onclick="appendToDisplay('1')">1</button>
    <button onclick="appendToDisplay('2')">2</button>
    <button onclick="appendToDisplay('3')">3</button>
    <button onclick="appendToDisplay('*')">*</button>
    <br>
    <button onclick="appendToDisplay('0')">0</button>
    <button onclick="calculate()">=</button>
    <button onclick="appendToDisplay('/')">/</button>
</body>
<script>
    function appendToDisplay(value) {
        const display = document.getElementById("display");
        display.value += value;
    }

    function clearDisplay() {
        const display = document.getElementById("display");
        display.value = "";
    }

    function calculate() {
        const display = document.getElementById("display");
        try {
            display.value = eval(display.value);
        } catch (error) {
            display.value = "Error";
        }
    }
</script>
</html>
