# random-password-generator

Project Name: Random Password Generator

Description:
This project is a Python script that generates a random and unique password based on user-defined length requirements. It utilizes Python's string and random modules to create passwords with a combination of lowercase letters, uppercase letters, digits, and special punctuation characters.

Key Components:

generate_password Function: This function takes an input argument plen (password length) and generates a random password based on the specified length. It combines lowercase letters, uppercase letters, digits, and special characters, shuffles them to make the password unique, and then selects the first plen characters as the password.

User Input: The script prompts the user to enter the desired password length (plen).

Password Generation: The script calls the generate_password function with the user-defined password length and retrieves the generated password.

Display: The generated password is displayed to the user.

Summary:
This project provides a simple and useful utility for generating secure and random passwords of varying lengths. Users can specify the desired length, and the script ensures that the generated password contains a mix of characters, making it difficult to guess. Random passwords like these are valuable for enhancing security in various contexts, such as online accounts, applications, or systems where strong authentication is required.
