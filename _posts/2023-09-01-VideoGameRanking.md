---
comments: false
layout: post
title: Video Game Table
description: Rable of video games and how many copies they sold
type: hacks
courses: { compsci: {week: 2} }
categories: [C4.1]
---

<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<body>
    <table id="demo" class="table">
      <thead>
            <tr>
                <th>Name</th>
                <th>Year</th>
                <th>Copies Sold</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <tr>
             <td>Minecraft</td>
                <td>2011</td>
                <td>238,000,000</td>
                <td>$29.99</td>
            </tr>
            <tr>
                <td>Grand Theft Auto V</td>
                <td>2013</td>
                <td>185,000,000</td>
                <td>$39.99</td>
            </tr>
            <tr>
                <td>Tetris (EA)</td>
                <td>2006</td>
                <td>100,000,000</td>
                <td>$9.99</td>
            </tr>
            <tr>
                <td>Wii Sports</td>
                <td>2006</td>
                <td>82,900,000</td>
                <td>$0.00</td>
            </tr>
            <tr>
                <td>PUBG: Battlegrounds</td>
                <td>2017</td>
                <td>75,000,000</td>
                <td>$0.00</td>
            </tr>
            <tr>
                <td>Mario Kart 8 / Deluxe</td>
                <td>2014</td>
                <td>63,920,000</td>
                <td>$59.99</td>
            </tr>
            <tr>
                <td>Super Mario Bros</td>
                <td>1985</td>
                <td>58,000,000</td>
                <td>$40.00</td>
            </tr>
            <tr>
                <td>Red Dead Redemption 2</td>
                <td>2018</td>
                <td>55,000,000</td>
                <td>$59.99</td>
            </tr>
            <tr>
                <td>Overwatch</td>
                <td>2016</td>
                <td>50,000,000</td>
                <td>$39.99</td>
            </tr>
            <tr>
                <td>The Witcher 3: Wild Hunt</td>
                <td>2015</td>
                <td>50,000,000</td>
                <td>$39.99</td>
            </tr>
        </tbody>
    </table>
</body>
    
<!-- Script is used to embed executable code -->
<script>
    $("#demo").DataTable();
</script>