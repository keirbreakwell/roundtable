# Roundtable Project Notes

## Important Commands

### Virtual Environment
To activate the virtual environment (run this when starting work):
source roundtable_env/bin/activate

Save Changes:
git add .
git commit -m "Description of changes"
Check Status:git status
View history: git log
Undo changes: git restore filename

#### Project Structure

src/
main.py (main program file)
personal_assistant.py (PA class definition)

roundtable_env/ (virtual environment)
NOTES.md (this file)

##### How to Back Up and Retrieve Files
git status - check whats now saved
git add . - Adds all changed files in your current directory and below (this is what you'll use most often)
git add filename - Adds just one specific file
git add -A - Adds all changes across your entire repository, no matter which directory you're in

git commit -m "Your description of changes"

git push saves the changes
