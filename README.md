# Mail Merge Script with Python


**Generate personalized letters with ease using this Python mail merge script!**

## How it works

1. The script reads a list of names from the file `invited_names.txt` located in the `./Input/Names/` directory.
2. It then loads the content of the letter template from `starting_letter.txt` in the `./Input/Letters/` directory.
3. For each name in the list, it replaces the placeholder `[name]` in the letter template with the current name.
4. The personalized letter is saved in the `./Output/ReadyToSend/` directory with the filename `letter_for_[name].txt`.

## 🌟 Learning

This project is an excellent learning exercise for beginners to Python programming. By working on this script, you can gain experience in the following areas:

- **File Handling:** You'll learn how to read from and write to files using Python, which is a fundamental skill for working with various data formats.

- **String Manipulation:** The script utilizes string manipulation techniques to replace the placeholder in the letter template with each name from the list.

- **Loops and Iteration:** You'll understand the concept of loops and iteration by processing each name in the list and creating a personalized letter for each recipient.

- **Python Libraries:** The script demonstrates how to use standard Python libraries for file handling and string operations.

- **Project Organization:** You'll learn how to structure a small project with different directories to keep the code organized and maintainable.

## 🤝 Collaboration

We welcome contributions from the open-source community to improve this mail merge script further. If you have any ideas for enhancements, bug fixes, or additional features, feel free to collaborate with us.

### How to contribute

1. Fork the project repository on GitHub.
2. Create a new branch for your contributions.
3. Make your changes and improvements.
4. Test your changes thoroughly.
5. Commit your changes and push them to your forked repository.
6. Create a pull request detailing the changes you made and the problem it solves.
7. We will review your pull request, provide feedback, and merge it into the main project if everything looks good.

By contributing to this project, you'll not only learn more about Python and software development but also become part of a community that encourages learning and sharing knowledge.

## Usage

1. Prepare the list of names in the file `invited_names.txt`, with one name per line.
2. Customize the letter template in `starting_letter.txt`, adding the placeholder `[name]` where you want the recipient's name to appear.
3. Run the script using Python:

```bash
python mail_merge.py
