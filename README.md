# YouTube Manager App (Python)

## Overview

The **YouTube Manager App** is a beginner-friendly **command-line application built with Python** that helps users manage a collection of YouTube videos efficiently. This project demonstrates the practical use of **Python programming concepts**, including file handling, JSON data storage, functions, lists, dictionaries, loops, conditional statements, and exception handling.

The application allows users to **store, view, update, and delete YouTube video details** such as the **video title** and **duration**. Instead of losing data every time the program closes, the app uses a local file (`youtube.txt`) with **JSON storage**, making the data persistent even after restarting the application.

This project was created to strengthen my understanding of **Python fundamentals** and apply programming concepts to a real-world mini project.

## Features

### 📋 List All Videos

Users can view all saved YouTube videos in a clean and organized numbered format.

### ➕ Add New Videos

Easily add a new YouTube video by entering:

* Video Title
* Video Duration

The information is automatically saved to the file.

### ✏️ Update Existing Videos

Users can modify video details by selecting the index number of the video and updating the title or duration.

### ❌ Delete Videos

Remove any saved video from the list using its corresponding index number.

### 💾 Data Persistence

All video details are stored using **JSON file handling**, ensuring data remains saved even after the program is closed.

## Python Concepts Used

This project helped in understanding and implementing:

* **Functions** for modular programming
* **File Handling** to read and write data
* **JSON Module** for storing structured data
* **Lists & Dictionaries** for data management
* **Loops** for continuous program execution
* **Conditional Statements** for decision-making
* **Exception Handling (`try-except`)** to avoid errors when files are missing
* **Match-Case Statement** for menu-based navigation

## Project Structure

```bash
youtube_manager_app.py   # Main application file
youtube.txt              # Stores video data in JSON format
```

## How It Works

1. Run the Python script.
2. Choose an option from the menu.
3. Add, update, view, or delete YouTube videos.
4. The data gets saved automatically into `youtube.txt`.

## Purpose of This Project

This project was built as a practice project to improve my problem-solving skills and gain hands-on experience with Python development. It helped me understand how real-world applications can store and manage data while improving my coding structure and logic-building skills.

## Future Improvements

* Add search functionality 🔍
* Add categories for videos 📂
* Improve UI for better user experience 🎨
* Add timestamps or upload date support 📅

## Tech Stack

**Language:** Python
**Storage:** JSON File (`youtube.txt`)
**IDE Used:** VS Code
