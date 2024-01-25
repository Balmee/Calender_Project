# Computer-Projects-two

## Introduction
This project was to see us create our own interactive calender up to our own intuition by using the python turtle to complete this task

## What Have I Produced?
- **Description of the Project:** my calender makes use of the entire 12 month annual calender format with a dinosaur theme. this is shown with the background image and emoji interactivity placing dinosaurs in the back, with the case of the emoji placing the dragon emoji instead to convey a similar theme. my calender also plays music akin to more jungle like themes via its assortment of instruments to convey more to the theme of dinosaurs

- **Key Features:** 

## My Coding Experience

- **Thinking:** the start of this project saw me drawing out the 12 boxes, inititially going to be the 12 months. this then followed me mindmapping themes i could use to have the most interactivity with the resources I already had in my possesion, changing the themes I started my calender on twice, from Roman Gladiators, to Coral reefs, to what it became now in Dinosaurs specifically from the triassic period. when touching up my finished calender with colours I spent a long time editing the calenders shape and colours to try to make it pop off from its background, aswell as make sure the emojis stood out too, that would go other top of the calenders dates.
- **Reading:** when it came to coding I needed to use new methods to which at that point I had not used before in python. this lead to me using methods such as ondrag and onscreenclick for user interactivity. through my reading, I came across dificulties in understanding how these new methods and some lines of code would work, howver through going line by line as I incorporated it into my own practise code I slowly understood, until I got it and altered it so it could fit my main body of code.
- **Copying and Modifying:** When it came to making the body of the calender and incorporating its dates and month names, I originally didnt have this. when I recieved feedback on refining my code I was given the use of the import calender which is built in to python turtle alongside how to much each month as it is shown now. with this code now including the dates, which I wanted I could move on with my own input to define my calender
- **Writing Code:** through writing my own code I learnt the importance of placing all import commands at the top of the code, as before I used import calender further down alongside used of tkinter, which kept giving me errors, preventing completion of code, or when it was complete, the interactivity would not work. I also stumbled up multiple times in writing code as I would misspell words or miss quatations for colours causing errors in my work, however after looking over these mistakes were quickly rectified.
- **Challenges and Learnings:** as mentioned above the use of tkinter and calender elsewhere but the top caused my problems with the code, except when I moved them at the top, however tkinter still caused my problems as it wouldnt let me run the code most the times, especially on mac. to rectify this I found out that tkinter was no longer needed with this newere code I made that still made use of ondrag and onclick, with the only downside being the dragging function was not as smooth as before when it is pulled across the canvas. I also wanted to make music play when the canvas would open, howver as I run on windows, the use of winsound did not work on Mac. this lead to me learning how to use pygame, howver I had issues pulling from the library as pip doesnt work on my system, this lead to me using -3 -m pip install pygame which was a success, as now to use music all I had to do was copy relative path like I did with the background and use pygame.mixer to load and play music. I also faced trouble with useing a background initially to as vscode wounldnt recognise it as a readable object despite being saved to the folder of use. To rectify this I had to convert the image into a .gif file as I found out online as only then was it readable. 

## Technologies Used
used python turtle functionality to create my calender with use of the calendar and pygame imports to work code from their librarys. 

## How to install and/or run the Project

- **Installation:** Download the entire folder of files associated with the project. make sure you have used pip install or equivalent of the other libraries of python being turtle, calender and pygame to make sure code will work when ran.

- **Running the Project:** highlight all code with mouse on the Triassic_Calender file and press "shift + Return" executing the code.

## Contributing
Go to the GitHub repository of calender_project.
Click on the "Fork" button in the upper right corner of the repository page. This creates a copy of the repository to your GitHub account.
Clone Your Fork to Your Local Machine:
On your forked repository page, click the "Code" button and copy the URL provided.

Open vscode on your local machine.
Navigate to the gear in the bottom left and click on it, then command palette.
Then type GIT clone: and press enter.
Paste the URL copied
You now has access to this repository
Make the necessary changes to the code you want.
Then you open terminal in vscode and type
Add changes:
git add .
Commit Changes:
git commit -m “and type what you want to call it”
Push the changes:
git push origin  // or another branch if wanted

Create a Pull Request:
Visit your forked repository on GitHub.
Switch to the branch you just created by clicking the branch dropdown and selecting your branch.
Click the "New Pull Request" button.
Ensure the changes you made are listed in the pull request.
Write a title and description for your pull request, explaining the changes you made.
Click the "Create Pull Request" button.

Others may review your changes and provide feedback.
Here you can make additional changes if necessary.
Then merge the Pull Request:

Once your pull request is approved and the continuous integration checks pass, it can be merged into the main repository.


## License
Choose an open source license
[MIT lisence](https://choosealicense.com/licenses/mit/).

## Contact
b.hunumunt0820231@arts.ac.uk