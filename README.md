# 🎮 Tetris Game

A classic Tetris game built with Python and Pygame, with web deployment support via GitHub Pages.

## 🌐 Play Online

🎯 **[Play the game online here!](https://supremeashu.github.io/TetrisGame/)**

The game is deployed as a web app and can be played directly in your browser.

## 🚀 Features

- **Classic Tetris gameplay** with all standard pieces (T, O, J, L, I, S, Z)
- **Score tracking** and level progression
- **Preview** of upcoming pieces
- **Background music** and sound effects
- **Web compatible** - runs in any modern browser
- **Responsive design** - works on desktop and mobile

## 🎮 Controls

- **← → Arrow Keys**: Move pieces left/right
- **↑ Arrow Key**: Rotate piece  
- **↓ Arrow Key**: Drop faster
- **Space**: Hard drop

## 🛠️ Local Development

### Prerequisites
- Python 3.12+
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/supremeashu/TetrisGame.git
   cd TetrisGame
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install pygame-ce pygbag
   ```

4. **Run locally**
   ```bash
   # For desktop version
   cd "tetris game"
   python main.py
   
   # For web version
   python -m pygbag web_main.py
   ```

## 📁 Project Structure

```
TetrisGame/
├── tetris game/          # Desktop version source code
│   ├── main.py          # Entry point
│   ├── game.py          # Core game logic
│   ├── settings.py      # Game configuration
│   ├── score.py         # Score tracking
│   ├── preview.py       # Piece preview
│   └── timer.py         # Game timing
├── graphics/            # Game sprites and fonts
├── sound/              # Audio files
├── docs/               # Web deployment files
├── web_main.py         # Web-compatible entry point
└── .github/workflows/  # CI/CD for web deployment
```

## 🌐 Web Deployment

The game is automatically built and deployed to GitHub Pages using GitHub Actions. The deployment:

1. **Builds** the web version using `pygbag`
2. **Optimizes** for web compatibility
3. **Deploys** to GitHub Pages
4. **Serves** at: https://supremeashu.github.io/TetrisGame/

## 🔧 Technologies

- **Python 3.12** - Core language
- **Pygame** - Game framework
- **Pygbag** - Web deployment
- **GitHub Actions** - CI/CD
- **GitHub Pages** - Hosting

## 🎯 Game Rules

1. **Objective**: Clear horizontal lines by filling them completely
2. **Pieces**: Seven different tetromino shapes fall from the top
3. **Movement**: Use arrow keys to move and rotate pieces
4. **Scoring**: Points awarded for cleared lines, bonus for multiple lines
5. **Levels**: Game speed increases as you progress
6. **Game Over**: When pieces reach the top of the playing field

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Acknowledgments

- Original Tetris concept by Alexey Pajitnov
- Built with the amazing Pygame library
- Web deployment made possible by Pygame for Web (pygbag)

---

**Enjoy playing! 🎮✨**