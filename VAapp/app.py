import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Grow an Inch Taller, Maggie!", layout="centered")

# --- CUSTOM CSS & JAVASCRIPT ---
# This includes the star background, the floating animation, and the "Runaway No" logic
custom_html = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');

    body {
        margin: 0;
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        overflow: hidden;
        height: 100vh;
        font-family: 'Dancing Script', cursive;
    }

    /* Star Background */
    .stars {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: -1;
    }

    /* Shooting Star Style */
    .shooting-star {
        position: absolute;
        height: 2px;
        background: linear-gradient(-45deg, #ff4b4b, rgba(0,0,0,0));
        filter: drop-shadow(0 0 6px #ff4b4b);
        animation: tail 3s ease-in-out infinite, shooting 3s ease-in-out infinite;
    }

    @keyframes shooting {
        0% { transform: translateX(0) translateY(0) rotate(45deg); }
        100% { transform: translateX(-1000px) translateY(1000px) rotate(45deg); }
    }

    .container {
        text-align: center;
        margin-top: 20vh;
        color: white;
    }

    .question {
        font-size: 3rem;
        color: #ff4b4b;
        text-shadow: 0 0 10px rgba(255, 75, 75, 0.8);
        padding: 20px;
    }

    .btn-container {
        display: flex;
        justify-content: center;
        gap: 50px;
        margin-top: 50px;
    }

    button {
        padding: 15px 30px;
        font-size: 1.5rem;
        border-radius: 20px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }

    #yes-btn {
        background-color: #ff4b4b;
        color: white;
        box-shadow: 0 0 15px #ff4b4b;
    }

    #no-btn {
        position: absolute;
        background-color: #555;
        color: white;
    }
</style>

<div class="stars" id="star-container"></div>

<div class="container" id="main-content">
    <h1 class="question">Will you please grow an inch taller, Maggie? 🦒📏</h1>
    <div class="btn-container">
        <button id="yes-btn" onclick="celebrate()">Yes!</button>
        <button id="no-btn" onmouseover="moveNo(event)" onclick="moveNo(event)" ontouchstart="moveNo(event)">No</button>
    </div>
</div>

<script>
    // Create stars
    const container = document.getElementById('star-container');
    for (let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.className = 'shooting-star';
        star.style.top = Math.random() * 100 + 'vh';
        star.style.left = Math.random() * 100 + 'vw';
        star.style.animationDelay = Math.random() * 5 + 's';
        container.appendChild(star);
    }

    // Runaway No Button Logic
    function moveNo(event) {
        if (event) {
            event.preventDefault();
        }
        const noBtn = document.getElementById('no-btn');
        const x = Math.random() * (window.innerWidth - 120);
        const y = Math.random() * (window.innerHeight - 80);
        noBtn.style.left = Math.max(10, x) + 'px';
        noBtn.style.top = Math.max(10, y) + 'px';
        
        if (!window.alertDone) {
            alert("You probably wish there was a 'Maybe' answer! 😂😆");
            window.alertDone = true;
        }
    }

    // Celebration Page Logic
    function celebrate() {
        document.getElementById('main-content').innerHTML = `
            <h1 class="question">YAY! Happy growing, Maggie! 🦒📏</h1>
            <p style="font-size: 1.5rem;">I knew you could reach new heights! ❤️</p>
            <div style="font-size: 5rem;">✨🌿🦒📏📈</div>
        `;
    }
</script>
"""

# Injecting the component
components.html(custom_html, height=800, scrolling=False)
