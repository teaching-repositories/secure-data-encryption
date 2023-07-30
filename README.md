# Introduction to Data Encryption

## Purpose
This GitHub repository serves as a hands-on exercise for demonstrating version control, forking, branching, and submitting pull requests. The assignment focuses on data encryption using Python scripts, where students will encrypt their personal details using a provided public key.

## Repository Contents
1. `encrypt.py`: Python script for data encryption using the provided public key (`public_key.pem`).
2. `public_key.pem`: The public key file used for encryption. Students will have access to this file for encrypting their personal details.
3. `README.md`: This file contains instructions on how to complete the assignment and demonstrates the steps required to fork, branch, encrypt data, and submit a pull request.

## Assignment Steps
1. **Fork the Repository:**
   - Click the "Fork" button at the top right of the repository page to create your copy of the repository under your GitHub account.
   - These instructions your forked repository will be called `SecureDataEncryption`

2. **Clone the Forked Repository:**
   - On your local machine, navigate to the directory where you want to clone the repository.
   - Clone your forked repository using the following command (replace `<your-forked-repo-url>` with your forked repository URL):
     ```
     git clone <your-forked-repo-url>
     ```
   - Change to the repository directory:
     ```
     cd SecureDataEncryption
     ```

3. **Create a New Branch:**
   - Create a new branch named `personal-details` using the following command:
     ```
     git checkout -b personal-details
     ```

4. **Setup Python Environment:**
   - Create a new Python environment using `conda` by running the following command (for Windows users):
     ```
     conda create --name crypto python=3.9
     ```

5. **Install Required Packages:**
   - Activate the newly created environment (for Windows users):
     ```
     conda activate crypto
     ```
   - Install the required packages using `pip`:
     ```
     pip install -r requirements.txt
     ```

6. **Encrypt Personal Details:**
   - Run the `encrypt.py` script to encrypt your personal details (name, email, student ID) using the provided public key:
     ```
     python encrypt.py
     ```
   - The encrypted output will be displayed on the console.

7. **Save Output to a File:**
   - Save the output of the encryption process into a file named `<github-username>.txt`, where `<github-username>` is your GitHub username. Run the following command to save the file:
     ```
     python encrypt.py > <github-username>.txt
     ```

8. **Commit and Push:**
   - Commit your changes to the `personal-details` branch:
     ```
     git add <github-username>.txt
     git commit -m "Add encrypted personal details"
     ```
   - Push the branch to your forked repository on GitHub:
     ```
     git push origin personal-details
     ```

9. **Submit a Pull Request:**
   - Go to your forked repository on GitHub and switch to the `personal-details` branch.
   - Click on the "New pull request" button.
   - Submit the pull request to merge your changes into the main branch of the original repository.

**Note:**
- No one can decrypt your informaition without the private key.
- **The private key (`private_key.pem`).** is kept secure and is only used by the repository maintainer for verification.
- Your pull request will be reviewed, and any feedback or suggestions will be provided before merging it into the main branch.

**Helpful Resources:**
- [GitHub Forking Guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [GitHub Pull Requests Guide](https://docs.github.com/en/get-started/quickstart/opening-a-pull-request)
- [Conda Documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

By completing this assignment, you will demonstrate your proficiency in version control and your ability to work with Python scripts for data encryption. Remember to keep the private key secure and adhere to the given instructions to ensure a successful pull request submission. Good luck with the assignment!