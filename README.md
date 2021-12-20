<h3>The repository is to study how to use python for TAL Project. The book that our team chose is 'solving 150 problem'.
My son and I will try to finish them by the end of the year, 2021.</h3> 

>How to commit git-commits
>> git status<br>
>> git diff<br>
>> git add [file name]<br>
>> git commit -m "a brief description"<br>
>> git push

>When I need to sync the main branch into sub branch in repository.
>>git pull origin main<br>

* How to create the excutable file from python<br>
  * Find python install in your pc<br>
  * Put the directory path at environment variable of your PC<br>
    * my case : C:\Users\[user name]]\AppData\Local\Programs\Python\Python37<br> 
  * Enter "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py" in that path on command window
  * Enter "python get-pip.py"
  * Enter "pip install pyinstaller"
  * how to pyinstaller
    * pyinstaller a.py
    * pyinstaller --onefile a.py
    * pyinstaller --noconsole --onefile a.py