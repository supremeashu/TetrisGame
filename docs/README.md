# Tetris Web Game with Authentication

This directory contains the web version of the Tetris game built with Pygame and JavaScript, featuring a complete authentication system.

## 🔐 Authentication Features

### User Registration & Login
- **Secure user accounts** with username and password
- **Guest play option** for quick games without registration
- **Session management** to keep users logged in
- **Input validation** for secure account creation

### Progress Tracking
- **Best Score** tracking for each user
- **Highest Level** reached
- **Total Lines** cleared across all games
- **Games Played** counter
- **Last Played** timestamp

### Leaderboard System
- **Top Scores** leaderboard showing best performers
- **Highest Levels** leaderboard for level progression
- **Global Statistics** showing total players, games, and lines
- **Ranking system** with gold, silver, bronze medals

## 📁 Files

- `index.html` - Landing page with game options
- `auth.html` - User authentication (login/register)
- `tetris-web.html` - Main Tetris game with auth integration
- `leaderboard.html` - Community leaderboards and stats
- `tetris.html` - Python-based web version 
- `.nojekyll` - GitHub Pages configuration

## 🎮 How to Play

1. **Visit the landing page** and choose your play style
2. **Create an account** or login to track your progress
3. **Play Tetris** with the classic controls:
   - Arrow keys for movement and rotation
   - Down arrow to drop faster
   - Space bar for hard drop
   - P to pause/unpause
4. **View leaderboards** to see how you rank against others
5. **Track your progress** across multiple gaming sessions

## 🌐 Web Features

- **Local Storage** for user data persistence
- **Session Management** for seamless user experience
- **Real-time Statistics** updating during gameplay
- **Responsive Design** working on desktop and mobile
- **Animated UI** with falling Tetris blocks
- **Original Game Colors** and authentic design

## 🚀 Deployment

Ready for GitHub Pages deployment:
1. Push to GitHub repository
2. Enable GitHub Pages from Settings
3. Select "main" branch and "/docs" folder
4. Game will be available at your GitHub Pages URL

## 🔒 Security Notes

- User passwords are stored in browser localStorage
- No server-side authentication (client-side only)
- Suitable for casual gaming and progress tracking
- For production use, implement server-side authentication

## 🎯 Game Rules

1. **Objective**: Clear horizontal lines by filling them completely
2. **Pieces**: Seven different tetromino shapes fall from the top
3. **Scoring**: Points awarded for cleared lines, bonus for multiple lines
4. **Levels**: Game speed increases as you progress
5. **Progress Saving**: Best scores and stats saved automatically for logged-in users

The authentication system adds a competitive and social element to the classic Tetris experience while maintaining the original game mechanics and visual design.
