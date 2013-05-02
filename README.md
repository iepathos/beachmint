Dear Beachmint,

I didn't know very much PHP when I received the test on Wednesday night and I was under the impression that I was expected to do the exam in PHP.  So, I spent the first 5 days I had with this test watching PHP training videos through USC and lynda.com.  I received the ok to do the app in Python on Monday.  So, I've done my best with the past 3 nights of coding.

I solved the [jewelry app](https://github.com/iepathos/beachmint/tree/master/jewelry) section of the test.  Please view my code within the jewelry app and [template](https://github.com/iepathos/beachmint/tree/master/templates/jewelry) folders.  You may view a live demo of the jewelry application at:
https://whois-iepathos.rhcloud.com/jewelry/

For the first part of the test, in what I called the [directory app](https://github.com/iepathos/beachmint/tree/master/directory), I decided to [hook up the built-in file system](https://github.com/iepathos/beachmint/blob/master/directory/models.py#L62) to database references to those files and folders.  In the end, I was able to get a functional model and [crud](https://github.com/iepathos/beachmint/blob/master/directory/models.py#L144), but still needed to work out several kinks in the program.  What I did was add file and folder create/delete hooks into the objects.  I think having database objects that reference actual file paths on the system like this will be much more adaptable.  What I need to finish the program is time to fix my [function](https://github.com/iepathos/beachmint/blob/master/directory/views.py#L89) for generating file/folder database objects based on the user's home directory path.  

My code for the directory portion of the exam and the partial tests are in the directory app and template folders.  My tests aren't in a ready-to-ship state.  I often test my code by running through the Django shell.  [directory/test_file](https://github.com/iepathos/beachmint/blob/master/directory/test_file.py), [directory/test_folder](https://github.com/iepathos/beachmint/blob/master/directory/test_folder.py), and [directory/test_reference](https://github.com/iepathos/beachmint/blob/master/directory/test_references.py) are a collection of shell scripts I cut/paste to the shell to make sure everything is working right.  Once the app is functional, I would go back and turn the scripts into an executable testing function.

Thank you for your time, consideration and opportunity to interview.  I hope my code here is enough to give you a good idea of how I think and how I approach coding problems.

Sincerely,

Glen Baker
