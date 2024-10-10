

# 🎉 Welcome to "The Monty Hall Show!" 🎉

*Step right up, folks! You've seen it on TV, you've heard it in the legends, but now, you can experience the Monty Hall Problem like never before. It's the 1970s all over again—except this time, *you* are the contestant!*

🚪 **Three doors.**  
🚗 **One car.**  
🐐 **Two goats.**  
The question is, will you walk away with the shiny new car or get left with... the goat? But wait, there's more! Will you stick with your choice, or switch to increase your odds? 🎲

### But first! Here's how you can join the show:

## 🎬 Installation Instructions

Even if you've never been a contestant on a game show before, you can still participate in *The Monty Hall Show!* All you need is Python and a few simple steps to get started. Follow these instructions:

### Step 1: Get the Latest Python Version
- Make sure you have **Python 3.6 or higher** installed. Not sure? Run this in your terminal:
  ```bash
  python --version
  ```
  If Python isn’t installed, head over to [python.org](https://www.python.org/downloads/) and download the latest version.

### Step 2: Clone the Repository
- In your terminal (or command prompt), type the following to clone the game from GitHub:
  ```bash
  git clone https://github.com/your-username/monty-hall-show.git
  cd monty-hall-show
  ```

### Step 3: Install Required Libraries
- This show requires a couple of backstage helpers! Install them by running:
  ```bash
  pip install -r requirements.txt
  ```

  **Required Library**:  
  - `tabulate` (for making those stats tables look spiffy)
  
  If the file `requirements.txt` isn't available, you can install it manually with:
  ```bash
  pip install tabulate
  ```

## 🎮 How to Play the Game

Now that you’re set up, you’re just one step away from being the next contestant on *The Monty Hall Show!* 🎉 Follow these simple steps to play:

1. **Launch the game**: In your terminal, type:
   ```bash
   python monty_hall.py
   ```
   
2. **The Host will greet you** and show you **three mysterious doors**. Behind one is a brand-new car, and behind the other two... are goats! 🐐🐐🚗

3. **Round 1**: The Host will ask you to choose a door—**1, 2, or 3**. Don't worry, you don't need to open it just yet!

4. **Round 2**: The Host will open one of the doors that you didn’t choose—revealing a goat. Now the fun begins! Will you **stick** with your choice or **switch** to the other closed door? Decisions, decisions...

5. **Round 3**: The big reveal! The Host will open all the doors to reveal what’s behind each one. Did you win the car, or did you get the goat?

6. **Keep Playing!**: After each game, you can play again to test your luck—or view your stats to see how well you’re doing! 📊

## 🏆 Game Features

- **Interactive CLI Game**: Make your choices like a real contestant and enjoy the suspense.
- **Big ASCII Art**: The doors are bigger, better, and more nostalgic than ever before.
- **Live Stats**: Keep track of your wins, losses, and whether switching was the smarter choice.
- **Replayability**: Play as many rounds as you like, and test the famous theory!
  
## 🎲 Understanding the Monty Hall Problem

Ever wondered why switching doors gives you better odds? Here’s the lowdown:  
- When you first pick a door, you have a **1/3 chance** of picking the car.  
- After Monty opens a goat door, if you **switch**, you’ll have a **2/3 chance** of winning the car! That’s right—**switching is the winning strategy!**

**Will you stick to your guns or make the switch? The odds are in your hands!**

## 📊 Check Your Stats
At any point during your game journey, you can check your stats to see how well you're doing. How many times did switching win you the car? How many times did you get stuck with a goat?

Your results will look something like this:
```
+----------------+-------+
| Outcome        | Count |
+----------------+-------+
| Switch Wins    |   5   |
| Stick Wins     |   2   |
| Total Games    |   7   |
| Switch Win Rate| 71.43%|
| Stick Win Rate | 28.57%|
+----------------+-------+
```

## 🚀 Future Enhancements

- **Auto-Simulation Mode**: Coming soon! Run 1,000 games at once to watch the theory in action!
- **Difficulty Levels**: Want more than 3 doors? Get ready for more goats and more choices in a future update!
- **Sound Effects**: Experience the excitement of a real game show with sound effects (under development)!

## 🛠 Troubleshooting

If you encounter any issues, don’t panic! Here are some common problems and how to solve them:

- **Missing tabulate library?**  
  Run:
  ```bash
  pip install tabulate
  ```

- **Python version issues?**  
  Ensure you're running Python 3.6 or higher by checking:
  ```bash
  python --version
  ```

- **Something else?**  
  Feel free to open an issue on the GitHub repo, and we’ll help you out!

## 🤝 Contributing

If you want to make the Monty Hall Show even more exciting, feel free to contribute! Submit pull requests or open issues with suggestions. Let's make this game show bigger and better!

---

Get ready to dazzle the crowd, outwit the odds, and maybe—just maybe—win the car of your dreams. 🎉 **Good luck, contestants!**

---

### 📢 Disclaimer

*This game is for educational purposes and enjoyment only—no actual cars or goats will be won by playing!*

---
