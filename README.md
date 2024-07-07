# CodeInspires
Code Inspirations and References

## Ubuntu
sudo apt update
<br> sudo apt install <package name>
<br> sudo apt list | grep <package name>
<br> sudo apt install --only-upgrade <package name>
<br> sudo apt install --only-upgrade <package-name1> <package-name2> <package-name3>

#### Force Delete
sudo rm -rf /path/to/directory

#### Create a Virtual environment
python -m venv .venv
<br> source .venv/bin/activate
<br> source <virtual environment name>/bin/activate
<br> activate
<br> deactivate

#### Install dependencies using pip
pip install -r requirements.txt
<br> pip freeze > requirements.txt (system packages are not included here)
<br> pip --version
<br> pip list
<br> pip list packageName
<br> pip install packageName
<br> pip uninstall packageName
<br> pip install -r requirements.txt
<br> pip freeze (to see all the packages installed)
<br> pip freeze > requirements.txt
<br> pip install --upgrade package-name  (This command tells pip to install the latest version of the package and uninstall the old version.)
<br> pip install --upgrade pip   (to upgrade pip itself)
<br> The -U option in pip install -U langchain stands for --upgrade. It means that pip will upgrade the package langchain-community to the latest version if it’s already installed. If the package is not installed, pip will install the latest version.

## Poetry
poetry init -To initialize pyproject.toml file
<br> poetry -V -Finding poetry version
<br> poetry show -To see all the packages
<br> poetry show <package name> -To see all the dependencies of the package
<br> poetry  shell -Activate the Python environment in the Folder that you are in
<br> poetry add <package name> -Create virtual environment (.venv) and install the package
<br> poetry add <package name>@version -To install exact version
<br> poetry add <package name>^2.12.1 -To install 2.Latest version.Latest version
<br> poetry add <package name>~2.12.1 -To install 2.12.Latest version
<br> poetry remove <package name> -To uninstall / remove the package
<br> poetry config --list -To see all the poetry configuration parameters
<br> poetry config virtualenvs.in-project true -To store the .venv folder in the project directory
<br> poetry config virtualenvs.prompt "{project_name}" -To change the virtual environment name
<br> poetry env info -To see the environment information
<br> poetry version minor -To update poetry to minor version
<br> poetry install -To install the dependencies and packages from the lock file
<br> poetry install --no-root -To install the dependencies and packages from the lock file
<br> poetry publish -To publish the package

## pyenv
pyenv for listing all the subcommands
<br> pyenv version
<br> pyenv versions
<br> pyenv update (to update pyenv)
<br> pyenv install --list
<br> pyenv install 3.11 (installs latest version)

pyenv shell command only activates a particular python version for the shell that you ran that command line. And so when I opened up a new shell or a new terminal session, we can see that the PI shell command was no longer in effect. If we want to change to a version of Python system wide, we can use pyenv global and then a python version.
<br> pyenv global 3.11.9
<br> pyenv uninstall 3.11.7

## Helpful
export PATH=/usr/local/cuda-12.1/bin${PATH:+:${PATH}}
<br> sudo apt-get install python3-pip
<br> sudo apt-get update
#### Symbolic Link (symlink) Linux / Mac
ln -s /path/to/original /path/to/symlink

## Directories
root, bin, tmp, lib, dev, usr
<br> __Different types of Shells Bourne Shell(sh), Bash Shell (bsh), C shell (csh), Korn shell(ksh)__
### Frequently Used Commands
logname		# Display's logged in user name		
<br> pwd			# Present working directory / To display relative path
<br> clear			# Clear the screen
<br> exit			# Exit and Close the window
<br> which <command name>	# Returns path names of the files
su <username> 		# To switch from one user account to given user account
<br> whoami
<br> useradd		# Adding user
<br> passwd			# Changing password
<br> man <command name>	# manual for the given command
file <file name>	# To know the type of the file
<br> touch f1 f2 f3		# Create an empty file/files
<br> tee			# It is used to write the given data to the file as well as to print on the screen
<br> date			# Present date
<br> cal <year>		# Present year
<br> cal <month> <year>	# Present month and year
<br> tty			# It displays the name of the user terminal

### cat
cat f1 f2 f3
<br> cat f1 f2>f3 (or) cat f1 f2>>f3	# Concatenate f1 and f2 and put it in f3
<br> cat<f1 or cat f1	# To open file and display contents
<br> cat>>f3 or cat>f3	# Append the content to existing f3
<br> cat .f1			# To display content in hidden file
<br> cat>.f1			# To append hidden file
<br> cat f1 f2>>.f3
<br> Ctrl+d			# To abort the cat command

### mkdir
mkdir dir1		# To create dir1
<br> mkdir -m  754 dir5	# To create a directory with given file permission
<br> mkdir -p dir1/dir2/dir3	# To create sub-directories within a directory (p - parent)
<br> rmdir dir1		# Remove empty directory, 'rmdir' can remove only empty directories
<br> rmdir -p dir1/dir2/dir3	# To remove directory along parent directory
<br> rmdir -p sdir1
<br> rm -r directoryname	# It removes all files and sub directories, sub directory files

### cd
cd dir1			# Navigate/change directories
<br> cd <relative path/absolute path> # You can give relative path or absolute path
<br> cd dir1/dir2		# relative path is given as argument
<br> cd			# Takes to the home directory
<br> cd ..			# Go back to the previous directory
<br> cd /			# Takes to the root directory
<br> cd ../..		# To change two root directory level back

### cp
<br> cp  <source file name>  <target file name>
<br> cp f1 f2
<br> cp /usr1/file1 /usr2/file1	# Can copy files across directories  by providing absolute or relative  path
<br> cp /dir1/f1 /usr/home/
<br> cp  file1 file2 dirname     # To copy files f1 and f2 to directory

### rm
<br> rm f1			# To remove the file
<br> rm *			# It removes all files in current directory
<br> rm -i f1		# Removes file interactively. Removes after confirmation
<br> rm -i dir1
<br> rm f1 f2 f3		# It removes all the three files
<br> rm -r  dir1		# Removes files from dir1 recursively
<br> rm -ir dir1		# Removes file from dir1 recursively  and interactively
<br> rm -rf  dir1		# Forced delete,even though you don't have a right permission

### mv
<br> mv oldfilename newfilename
<br> mv old-dir new-dir
<br> mv f1 f3		# To rename the file from f1 to f3
<br> mv emp .emp		# To hide file
<br> mv .emp emp		# To unhide file

### cmp
cmp <file1> <file2>	# It compares file1 and file2
if both file contents are same no output is displayed
if both files are different then it displays line number and character location 

### comm
<br> comm <file1> <file2>	# It will display the files having common content.Output contains 3 columns
    	First Column Contains lines unique to file1
	Second Column contains lines unique to file2
	Third column contains lines common to both the files file1 and file2
<br> comm f1 f2                                                        
<br> comm -1 f1 f2		# Removes lines belonging to file1 and displays only file2
<br> comm -2 f1 f2		# Removes lines belonging to file2 and displays only file1
<br> comm -3 f1 f2		# Removes lines that are common to both file1 and file2

### diff
<br> diff f1 f2		# It shows different lines or difference lines between two files
<br> grep unix students | cut -f 2 3 | sort | tee file1
<br> <br> head -10 sample|tail +5|tee file1
<br> -----------------------------------------------------------------------------------------
<br> Display owner name, file size, file name
<br> ls -l | tr -s " " | cut -d " " -f 3,5,9  # Here tr -s squeezes the space to one space
<br> -----------------------------------------------------------------------------------------
<br> wc <filename> 		# It counts number of lines, words and characters
<br> wc f1
<br> wc -l f1
<br> wc -w f1
<br> wc -c f1
<br> wc -lwc f1
<br> wc -lw f1
<br> ls | wc -l		# Total number of files and directories in a given directory
<br> ls | wc -l > outfile
<br> who | tee file1 | sort	# Total number of users logged into the server

### I/O Redirection & Piping
<br> 	UNIX has keyboard as Standard Input device denoted by 0
<br> 	Display unit is the Standard Output device denoted by 1
<br> 	Display unit is the Standard Error device denoted by 2
<br> I/O can be redirected using ‘<‘ &  ‘>’  
<br> 	'<' symbol implies # take the input from a file instead of keyboard
<br> 	'>' symbol implies # write the output in the file instead of display unit
<br> 	'2>'symbols implies # write the error in a file rather than display unit
<br> < -Redirect Input
<br> > -Redirect Output

<br> e.g.:
<br> abc<in-file>out-file
<br> 2>err-file

<br> A '>>' indicates the appending of data to a file if it exists, instead of  over-writing
<br> 1>&2  indicates # redirect Standard Output to Standard Error

### Piping(|) or Pipe(|) # It is used to combine 2 or more commands. Any concept can be achieved using piping command. You can combine any number of commands, This is the best advantage of piping command 
<br> ^			# Starts with
<br> $			# Ends with
<br> ls -l | grep ^d		# List out total number of directories
<br> ls -l | grep ^d| wc -l	# Count total number of directories
<br> grep unix stud | cut -f 2,3 | sort
<br> ls |more		# It displays list of files and directories page wise
<br> ls -x			# list entries by lines instead of by columns
<br> ls  dir1
<br> ls -a			# do not ignore entries starting with .
<br> ls -R			# list subdirectories
<br> ls -t			# sort by modification time, newest first
<br> ls -i			# print the index number of each file
<br> ls -r 			# It display all files and subdirectories in reverse(descending order)

### There are three types of permissions like
<br> r - read permission
<br> w - write permission
<br> x - execution permission

<br> rwxr-x--x  means
<br> Owner of this file has read, write  and execute permissions
<br> Group has read and execute  permissions
<br> Others has only execution  permissions

<br> Permissions can be encoded  numerically
<br> 	Read ( r ) - Weight 4  (2^2)
<br> 	Write ( w ) - Weight 2  (2^1)
<br> 	Execute ( x ) - Weight 1 (2^0)
<br> The weight of  Read+Write+Execution (rwx) is  4 + 2 + 1 = 7
<br> The weight of Read+Execution (r- x) is 4 + 1 = 5

### RegEx
<br> Wild card Characters or Meta characters
<br> * , ? , - , []   : These are called wild card characters or meta characters
<br> * -> It matches 0 or more characters(i.e., all)
<br> ? -> It mathches a single character
<br> - -> It matches a character in the given range
<br> [] ->It mathches a single character in the give list 
<br> .  ->It mathches any single character except new line character
<br> Derrivations of above wild characters are
<br> [! ]-> It matches characters other than the character in list
<br> [^ ]-> It matches characters that starts with either of alphabets mentioned in the list

<br> ls a* 
<br> ls b*K 
<br> ls b??k 
<br> ls b?k
<br> ls [aeiou]* 
<br> ls [!aeiou]* 
<br> ls [k-v]* 
<br> ls [0-9]* 
<br> ls [d-m][p-s][b-g]*
<br> ls [dhpt]?

<br> cp dir1/sdir1/sdir2/*  dir2/sdir2
<br> head -15 file1
<br> tail -15 file1
<br> head -10 sa|tail -5|tee sand

<br> cut -f 5,10 file1
<br> cut -f 1,3 emp			# It displays the 1st and 3rd field's data from emp
<br> cut -c 1,3 emp			# It displays the 1st and 3rd character data from emp
<br> cut -c 2-6 emp			# It treats delimeter (ie., Tab-space is considered as one character) and one character and displays  2nd,3rd ,4th(delimeter),5th ,6th  character
<br> cut -f 1,2 -d ':' f9 			# -f is field and -d is delimiter
<br> cut -f 1,2 -d ':' f9>f11

<br> paste emp f9				# It will join two or more files by keeping tab space between them
<br> paste emp f9 f11

<br> tr aeiou AEIOU<f1			# It is used to translate the characters from one form to another form
<br> tr '\t' ':'<emp			# tab space(\t) is replaced with column(:)
<br> tr '\t' ',' <emp>temp
<br> tr [a-z] [A-Z]<f3

<br> tr -s ' ' <sample			# To squeeze the space to one space

<br> sort file1				# Sorts file1 and displays the sorted  file on terminal. It will sort data in a file based on ASCII values. By default it sorts in ascending order
<br> sort -o file2 file1			# Instead of displaying the sorted file on terminal, can be written in to a file
<br> sort temp temp1 temp2 temp3		# The Sort command can be used for sorting the contents of a file. Apart from sorting file, the SORT  can merge multiple sorted files and store the result in the specified output file. While sorting the SORT command bases it comparisions on the first character in each line in the file. If the first character of two line  is same then the second character in each line is compared and so on i.e, The sorting done according to the ASCII collating sequence.

<br> -n – sort based on numeric values
<br> -r – descending order
<br> -u – ignore duplicates
<br> -nu or nr – you can use any combination

<br> sort -o result temp temp1 temp2 temp3 – Instead of displaying the  sorted output on the screen we can store it in a file.In this command it sorts the three files temp temp1 temp2 temp3 and saves the result in a file 'result' file
<br> sort -m f1 f2				# If the files have already been sorted and we just want to merge them, then we can use this command
<br> sort - temp				# Sometimes we may want to combine the contents of a file with the input from the keyboard and then carry out the sorting.This can be achieved by using above command .Where '-' stands for the standard input i.e., the keyboard.

<br> sort -r temp
<br> sort -u dupli 
<br> sort numfile
<br> sort -n numfile
<br> sort -rn numfile 
<br> sort -u -o num numfile
<br> sort -n -u -o num numfile
<br> sort -nuo num1 numfile
<br> sort -f +position1 -position2 filename  # sort data Field Wise.-f – Stands for sort based on 'field'
<br> sort +0 students
<br> sort +1 students
<br> sort -t ',' -f +1 -2 emp 		– In sort command -t(tab key) is used as default delimiter

### head and tail
head -15 file1
<br> tail -15 file1

### Uniq Command -It will display unique lines from the sorted file. It never sorts the unsorted file
uniq dup1
<br> uniq -u dup1				# It displays lines which are not duplicates in file dup1
<br> uniq -d dup1				# It displays lines which are duplicates in file dup1
<br> uniq -c dup1				# It will count the lines in the file dup1
<br> sort dupli | uniq -d			# Displays lines which are duplicates in file
<br> uniq -u sample>temp			# Writes all the uniq records in temp
<br> mv temp sample

### grep
grep tecno stu			# G lobally search a R egular E xpression and P rint it
<br> grep "of the" f1			# To search more than a word the string should be in double quotes
<br> grep "technologies" stu
<br> grep "tecnosoft" stu;
<br> grep tec stu 
<br> grep "C++" stu 
<br> grep "105" stu 
<br> grep 10 stu
<br> grep Unix *				# Using grep to locate files
<br> grep Unix sam sample students students2
<br> grep unix *
<br> grep -i unix *				# -i ignore case sensitive 
<br> grep -v Unix students			# It deletes lines containing pattern from output
<br> grep -n Unix students 		# Display lines with line numbers that containing the pattern
<br> grep -c Unix students			# It will count the lines
<br> grep -c Unix *			# It will count the lines in present directory
<br> grep -e sandeep -e Unix students	# used to search for multiple patterns in a single command
<br> grep -e sandeep -e Unix *
<br> grep -vn Unix students
<br> grep -vi Unix students
<br> grep -vc Unix students
<br> grep -vci Unix students

### Compressing and Uncompressing files (compress,gzip,pack - uncompress,gunzip,unpack)
<br> compress -v file1	# The Optional -v(for verbose) option files compress to report how much space it saved.
<br> zcat filename.Z	# It displays the zipped file contents in readable format
<br> compress filename
<br> uncompress dupli.z
<br> uncompress dupli.Z 
<br> gzip dupli
<br> gunzip dupli
<br> pack sample
<br> pcat filename 
<br> unpack sample.z
<br> unpack filename

### Regular Expressions
<br> If any string contains wild card characters then it is known as Regular Expressions or Patterns.
<br> Patterns are classified into 3 types
<br> 1)Character Pattern(Default)
<br> 2)Word Pattern
<br> 3)Line Pattern

#### 1)Character Pattern(Default)
<br> grep "s*" students
<br> grep "sa*" students
<br> grep "sandeep*" students
<br> grep "sand*" students
<br> grep "te*" f1
<br> grep "t[aeiou]" f1

#### 2)Word Pattern
<br> grep \<wordpattern\> filename
<br> grep "\<the\>" f1
<br> grep "\<file\>" f1
<br> grep "\<[0-9][0-9][0-9][0-9]\>" students -It searches 4 digit numbers in a given file 
<br> grep "\<[0-9][0-9][0-9]\>" students 
<br> grep "\<...\>" students -It searches for any 3 character or numberic or alpha-numeric characters 
<br> grep "\<.\>" students # It searches for any single character word, '+' will not be treated as a character or numeric or alpha-numeric

#### 3) Line Pattern 
<br> ^ - Start of the Line
<br> $ - End of the Line
<br> grep "^t" f1
<br> grep '^t' f1
<br> grep "^1" emp
<br> grep '^all' f1
<br> grep "0$" temp  
<br> grep "[0-9]$" temp	# Line not ending with a digit 
<br> grep "[0-9][0-9][0-9][0-9]$" temp
<br> grep "^[423]" temp	# Line Starting with 4 or 2 or 3
<br> grep "^[^423]" temp	# Line not starting with 4 or 2 or 3
<br> grep ^[bkt] sample 
<br> grep ^[^bkt] sample
<br> grep "[^0-9]$" students  
<br> grep ^$ sample	# It searches for empty blank lines in a file
<br> grep -v ^$ sample>temp	# To Delete all the blank lines in a given file
<br> mv temp sample
<br> grep "^210$" temp 
<br> grep ^unix$ sample
<br> grep "^." temp
<br> grep "^\." temp	# For Special characters escape character '\' is used for non alpha-numeric
<br> grep "^\^" temp
<br> grep "\@$" temp
<br> grep "\$$" temp
<br> file * | grep -v text  
<br> grep 'ch.*se' recipes
<br> The fgrep command is similar to grep, but with three main differences: 
<br> 1)You can use it to search for several targets at once
<br> 2)It does not allow you to use regular expressions to search for patterns
<br> and

#### 3)fgrep - faster than grep
fgrep "text
<br> >all
<br> > word
<br> > example" f1
<br> grep -f special customers 	-f(file) option, you can tell grep / fgrep to take the search targets from a file

#### The egrep command is the most powerful member of the grep command family. You can use it like fgrep to search for multiple targets. Like, grep it allows you to use regular expressions to specify targets, but it provides a fuller, more poweful set of regular expressions than grep.
<br> The egrep command accepts all of the basic regular expressions recognized by grep, as well as several useful extension to the set.
egrep c|c++|unix students	# You can tell egrep to search for several targets by separating them with the vertical bar or pipe symbol(|)
<br> egrep "C |Oracle" students
<br> egrep "^\^|\%$" temp

#### sed s/searching(string)/replacing(string)/g  <filename>
sed s/oldstring/newstring/g filename	# It is used to replace a string 
<br> sed s/oldstring/newstring/gi filename	# To ignore case sensitive
<br> sed "s/smith/sandeep/g" emp
<br> sed "s/smith//g" emp
<br> sed "s/the//g" f1

#### whereis <command name>			# Used to know the path of a UNIX COMMANDS
whereis perl
<br> whereis cp
#### find <filename>			# To find the file in cwd
find <path/filename>			# To find the file in the specified path
<br> find f1
<br> find /dev/null

#### ls
<br> ls -a		# To display all files including the  files starting with '.'
<br> ls -l		# l : symbolic link
<br> - : hyphen is ordinary file
<br> d : directory file
<br> c : character specific file like terminals
<br> b : block specific file like hard disk
<br> l : symbolic link
<br> s : Semaphore
<br> p : named pipe
<br> m : shared memory file

#### chmod
To change the rwxr-x--x  (751)  permissions to rwxrwxrwx  (777)  permissions of file1 is
<br> chmod  777 file1		# Existing file permissions can be  changed with the command chmod.
<br> chmod +w  file1
<br> chmod  -w  file1		# To revoke write permission to file
<br> chmod [who] [+/-/=] [permission] filename
<br> u for user or ownerf
<br> g for group
<br> o for others
<br> + for to add permission
<br> - for to substract permission
<br> = for to assign permission(i.e., add specified permission and take away all other pemissions if present)
<br> r  to read
<br> w for write
<br> x for to execute 
<br> u for user or owner
<br> g for group
<br> o for others
<br> chmod g+w tecno 
<br> chmod u+x,o+x tecno 
<br> chmod uo+x tecno 
<br> chmod g=x file1
<br> chmod o=r,g-w tecno
<br> chmod 700 tecno 
<br> chmod 754 tecno
<br> chmod o=w sample 
<br> chmod g-w sample

#### chgrp <newgroup> <file name>	# Changes the group of the file
chgrp tecnosoftgrp hello
<br> umask  042	# Default File Permissions. If umask is 042, then the default  file permissions are 7-0,7-4,7-2. Going forward all files will be created with 735 (u-rwx, g-rw, o-rx)
<br> Default file creation permissions will be obtained from the umask   value
<br> unmask 077 	# Going forward all files will be created with 700 (7-0,7-7,7-7) (u-rwx)

#### chown username filename 
chown <new owner> filename
<br> chown test2 f1
#### ps			# To see the processes running currently under UNIX
<br> getpid() is the UNIX function to get the process id
<br> 	Try this piece of code to see the  process id given by UNIX.
```
main() {
 int pid;
 pid = getpid();
 printf(“Process id is : %d\n”,pid);
}
```
<br> 	Try this piece of code to know the  parent process id
```
main(){
 int ppid;
 ppid = getppid();
 printf("This is the parent process id :%d\n",ppid);
}
```

#### UNIX Background Process
Time consuming tasks may be run  in background. Place ‘& ’ at the end of the  command, the process will go to  background. Displays the PID after submission. Success or failure of the  background process will not be  reported. Better to redirect the background  process output to some file.  Otherwise, it will disturb the foreground process messages on  the screen

#### UNIX Command - nohup
nohup sort file1 > file2&	# To continue the execution of  background process even after the  logout. If the output is not redirected, it  will be redirected to a file  'nohup.out'

#### Killing a Process
kill PID		# To Terminate a process
<br> kill -9 PID		# ‘sure kill’ signal ‘9’

## Shell (Bash/Unix) Scripting
sh shell
<br> Two basic words in shell are read &  (backslash '\' is used to escape characters)
<br> echo Enter your name\?
<br> read name
<br> echo Good Morning.. $name
<br> dirname=/usr2/bin		# values can be assigned to variable  using '= ' equal sign
<br> a1="" or a1='' or a1=		# ways to create a null variable
<br> echo $name 
<br> PS1=ABC
<br> name=Vijay Suri
<br> name=Vijay age=20
<br> echo Name is $name and age is $age
<br> age=20
<br> readonly age			# User can make a variable  unchanged during execution
<br> unset age			# A variable can be removed from  the shell by using unset command

#### Positional Parameters
ShellScript variable1 variable2 variable3 variable4
<br> In the above example $0 is variable 1 and $1 is variable 2 and so on and so forth. Many occasions, a program  expects the variables in a certain  fashion. This is achieved through positional parameters from $0  through $9. Shell can handle only 9 variables at a time. To access more than 9, the shift command is used.
<br> 0 is the program itself. Thus $abc par1 par2 par3 par4 assigns abc to $0, par1 to $1 … par4 to $4
```
a=10
echo $a
```
<br> mkdir abc abc/a1 abc/a1/a11
<br> x=abc/a1/a11 
<br> shift + : 
<br> Write the following in a file and  execute:
<br> a=10 b=4
<br> echo ‘expr $a + $b’
<br> echo ‘expr $a - $b’
<br> echo ‘expr $a \* $b’
<br> echo ‘expr $a / $b’
<br> echo ‘expr $a % $b’    #modulus
<br> Arithmetic in Shell
<br> On execution, the output is:
<br> 14
<br> 6
<br> 40
<br> 2
<br> 2
<br> In the above Anything after ‘# ’ sign will be  treated as comment. 'expr' is the key word for doing arithmetic
<br> expr can handle only integers. Use  bc to handle real numbers.
<br> echo `expr $a + $b | bc`

#### test
It depends upon the exit status of the command given. test verbs translates the result into success or failure.
<br> if test -d $fdir	# To check whether the directory exist or not (File Test)
<br> If test condition
<br> if test $a -gt $b
<br> if test `expr $n%2`-eq 0
<br> UNIX - test (instead of using 'test')
<br> Use square braces to avoid writing  test
<br> Provide a space after `[`
<br> Provide a space before `]`

<br> __There are three tests namely
<br> 1. Numerical test
<br> 2. String test
<br> 3. File test__

#### test - numerical
Used to compare numerical
<br> -gt  = greater than
<br> -lt   = less than
<br> -ge  = greater than or equal to
<br> -le   = less than or equal to
<br> -ne  = not equal
<br> -eq  = equal
<br> Example:
```
if [ $1 -lt 5 ]
then
  echo the value is < 5
elif [ $1 -le 7 ]
  echo the value is <= or equal 7
else
  echo the value is > 7
fi
```
#### test - file
The following are the file related flags
<br> -s returns True if the file exists and size > 0
<br> -f returns True if the file exists and not directory
<br> -d return True if the file exists and is a directory
<br> e.g.: 
```
if [ -f $1 ] then
  echo File exists
fi
```

#### Decision loops. There are 4 decision making loops
if then fi
<br> if then else fi
<br> if then elif else fi
<br> case - esac
```
if [ $1 -lt 5 ]
then
  echo the value is < 5
elif [ $1 -le 7 ]
  echo the value is <= or equal 7
else
  echo the value is > 7
fi

if cp $1 $2
then echo “Copied successfully”
fi
```

### Operators
<br> && - And Operator
<br> || - Or Operator
<br> $ - To access a value in the variable

### Control Statements
__There are four types of control instructions in shell. They are
<br> 1.Sequence Control Instruction
<br> 2.Decision Control Instructions
<br> 3.Loop Control Instruction
<br> 4.Case Control Instruction__
```
if [ -f $1 ] then
	echo File exists
fi
```
<br> -s returns True if the file exists and size > 0
<br> -f returns True if the file exists and not directory
<br> -d return True if the file exists and is a directory

#### Logical conditions
<br> -a  stands for AND condition
<br> -o  stands for OR condition
<br> -!  Is negation
```
c=10
echo $c
10
c=20
echo $c
20
readonly c
c=70
ksh: c: is read only
echo $c
20
unset c
ksh: unset: c is read only
```

#### case
<br> Can use shell’s pattern matching
<br> e.g.:
```
case $1 in
 [a-z]) echo Small alpha;;
 [A-Z]) echo Capital;;
esac
```
#### case example
```
case $option in
     1) echo Financial accounting;;
     2) echo Materiel accounting;;
     *) echo Invalid Opt - Try;;
esac
```

#### case example (Need not be numbers - may be  strings too)
```
case $option in
     bannana | orange) echo Fruit;;
     chilles | pumpkin) echo Vegatables;;
     *) echo Not Known;;
esac
```

#### Loop Controls
<br> Provided 3 loop constructs namely:
<br> while loop
<br> for loop
<br> until loop

#### while loop
```
while <condition>
do
   statements
done
```
<br> done is the delimiter of do
<br> e.g.:
```
count = 1
while [ $count -le 3 ]
do
  echo Loop value $count
  count = `expr $count + 1`
done
```

#### until loop
```
until <condition>
do
  statements
done
```
<br> until continues its loop so long as  the condition is false. except this, while & until are  identical

#### for loop - Most frequently used loop
```
for control-var in value1 value2…
do
   statements
done
```
<br> for takes a list of variables
<br> e.g.:
```
for word in $*
do
  echo $word
done
```

#### break statement
<br> Used to break the current loop  and comes out of the loop
<br> Usually associated with if
```
if [ $1 -eq 5 ] 
then
  I = 2
  break
fi
```

#### continue statement
<br> To take the control of the  beginning of the loop bypassing  the statements
```
I=1
while [ $I -le 5 ] then
do
  I = `expr $I + 1`
  continue
done
```

#### Metacharacters
Called as regular expressions. Classified as follows:
<br> File name           : ? * […] [!…]
<br> I/O redirection     : < > >> << m> m>&n
<br> Process execution   : ; ( ) & && ||
<br> Positional paras    : $1..$9
<br> Spl characters      : $0 $* $@ $# $! $$ $-

#### File name
<br> ls ??  -lists all files with 2 chars long
<br> ls a*  -lists all file names begin with a
<br> ls [a-c]*  -file names begin with a,b &c
<br> ls [!a-c]  - file names not starting  with a,b,c

#### UNIX - I/O Redirection
<br> <  - take input from
<br> >  - write output to
<br> >> - append output
<br> << - abc  - takes the input till ‘abc’  encountered

## PROGRAMS
<br> +  addition
<br> -   substraction
<br> *  multiplication
<br> /   division
<br> %  modulus division
<br> -gt   greater than
<br> -ge   greater than or equal to 
<br> -lt    less than
<br> -le   less than or equal to 
<br> -eq  equal to
<br> -ne  not equal to 
<br> -a  AND
<br> -o  OR
<br> -n or !  NOT
<br> 	alias and unalias
<br> alias dir='ls'
<br> dir
<br> alias nu='who |wc -l'		# Giving alias to the number of users logged into the server
<br> nu
<br> alias 
<br> unalias <command>		# Giving unalias to the already given name
<br> history 
<br> c=`expr $a \* $b`
<br> Write a program to read data in to a variable and display?
```
vi sp7
echo Enter two float numbers a and b
read a b
c=`echo $a + $b|bc`
echo a+b=$c
c=`echo $a - $b|bc`
echo a-b=$c
c=`echo $a \* $b|bc`
echo a*b=$c
c=`echo $a / $b|bc`
echo a/b=$c
:wq
```
<br> Removing variable from the shell memory
```
x=10
echo $x
10
unset x
echo $x
```
<br> echo today date is:`date`		# We have to use backquote ` (below Tilde ~)
<br> echo my file has `wc -l f1` lines
<br> \n - New line ($echo "hello \n tecnosoft")
<br> \t - Tab Space ($echo "hello\t tecnosoft")
<br> \b - Back Space ($echo "hello\btecnosoft")
<br> \r - Carriage return ($echo "welcome to \r tecnosoft")
<br> \07- Bell Sound ($echo "hello\07")
<br> echo \hello...\c
<br> hello...
<br> echo \hello\
<br> hello

#### Sleep Command
<br> sleep <seconds>		# It stops the execution of the program the specified number of seconds

## Admin Commands
useradd test10
<br> passwd test10
<br> groupadd sandy
<br> useradd  -g  <groupname>  <username>
<br> groupdel <groupname>
<br> tree dir1		# To display directories in a recursive manner

#### Init Run Levels To control the system/server from the admin login
init 0			# Shutdown server/system
<br> init 1 or init s  # To bring the system to single user mode
<br> init 2			# To bring the system to multiuser mode with no resource shared
<br> init 3			# To bring the system to multiuser mode with resource shared
<br> init 5			# Multi-user mode and GUI environment
<br> init 6			# Halt and reboot the system/server to the default run levels
<br> shutdown
<br> halt
<br> reboot
<br> power off
<br> locate agent.txt			# Search for a given file in entire unix file system
<br> locate <filename>

#### Managing Disk Space
du <file_name>		# It displays size (in KB) occupied by each file
<br> du  /home/test1
<br> du -s <path> -It displays the space occupied by directories in KB
<br> free			# It diplays information related to memory

#### Process Status
UNIX is multi-user and multi- tasking Operating System, many  processes will be running simultaneously. UNIX assigns an unique number to each process that is invoked. It  is known as process identification  number shortly called as process- id. A process is BORN  when it starts  execution and DEAD when it is  over. A process can start (birth) another  process. The born process is known as child process. The first/parent process is known  as parent process.
<br> The parent process will wait till  the child process terminates (die)
<br> Then the parent process will  terminate (die)
<br> If the parent process dies  (terminates) before the  termination of the child process,  the child process will become orphan  process.

## Not Used by me but if Used has to be moved
more +5 -20 -p -s file1 # Starts displaying file1 20 lines per  page, starting from 5th line, with  prompt for each page of display
<br> finger			# Displays all the users with full details
<br> ctrl+alt+F1 to F6	# At a time you can enter into 6 users in a server (Shifting from GUI to CUI)
<br> ctrl+alt+F7		# Shifting from CUI to GUI
<br> banner <String>		# Displays banner of a string

#### Communicating with users or Communication Commands(p31)
write <user-name>
<br> hello How are you?
<br> ^d (Ctrl+d)
<br> finger -i	# Can find who are the users logged in. Also can find who set  message -n. User with * set mesg -n
<br> Login  TTY  When  Idle
<br> abc   *tty1 
<br> def    tty2 
<br> ghi    tty3 
<br> mesg -n  		# Message writing can be denied
<br> mesg -y		# Message writing can be denied
<br> wall	# Can be used by super user only. Writes to all users irrespective of  permission
<br> write test2
<br> d 1-5
```
mail <log-name>
mail
/usr/spool/mail directory
mail test2   
Subject: Nope man nope
klsjdf
jksdflh
asjdljkas
kjsdkf
Cc: test3
mail test2 test3 test4
mail test2 test3 test4 < myownprgm.c
mail test2 test3 test4<f1
mail -f
```
<br> d 3
<br> d 1-5 		#  To delete 1 to 5 mails in mail box
<br> & q or ctrl+d
<br> p 3		# Print current message again
<br> p 1-5		# Print the 3rd mail
<br> r		# To reply to that mail
<br> telnet 192.168.0.10
<br> Telnet		# Connecting to Linux Server to the Linux server can be done in two ways first one is using Telnet and second is using Xshell
<br> Xshell
<br> FTP(file transfer protocol)(see the unix book)
<br> System Start Up and Shutdown

#### Changing Process Priority
The process priority can be  changed by:
<br> nice -15 <Command>
<br> Priorities run between 0 to 39
<br> Priority 20 is the default priority
<br> The higher the priority number,  the lower the priority
<br> Only super user can change  priority
<br> Priority can be changed at the  time of firing the command
<br> crontab command-file/command		# Crontab executes a command  everyday at the given time forever

## Actual Interview Questions Faced in the Panel
<br> How to search a string in a file?
<br> if grep $str $fname
<br> How to copy a file?
<br> How to check how many users working on the system?
<br> How to check given number is +ve or -ve number?
<br> if test $n -gt 0
<br> How to check whether the given string is existing or not?
<br> if grep $str $fname>/dev/null
<br> How to check given user is connected to server or not?
<br> if who|grep $usr>/dev/null
<br> How to delete a file?
<br> if test -e $fname
<br> How to print the greetings based on time?
<br> hour=`date|cut -c 12,13`
<br> if test $hour -ge 0 -a $hour -lt 12
<br> elif test $hour -gt 12 -a $hour -lt 17
<br> Decision Control Statement
<br> 1) if-then-fi statement(simple if)
<br> 2)if-then-else-if statement
<br> 3)if-then-elif-else-fi statement(Ladder if)
<br> 4)Nested if
<br> 5)case-esac statement
<br> How to find student result?
<br> How to assign the read permission if file doesn't have a read permission?
<br> if test -r $fname
<br> How to display data from a file, if the file has read permission?
<br> How to check whether the given file is regular file/directory/another type of file?
<br> -f
<br> -d
<br> -l
<br> -r
<br> -w
<br> -x
<br> How to check for ordinary file and display  it contents?
<br> How to check given file is ordinary file or directory file?
<br> How to check read permission?
<br> string1 != string2
<br> string1 = string2
<br> How to compare two strings?
<br> if test str1 = str2
<br> How to check given string is empty or not?
<br> How to check the given character is upper case alphabet or lower case alphabet or digit or special? character
<br> How to display file contents or write on to file or execute based on user choice?
<br> chmod u+w $fname
<br> chmod u+x $fname
<br> write a menu driven program which has following options
<br> 1)Contents of current directory
<br> 2)list of users who have currently logged in 
<br> 3)present working directory
<br> 4)calender
<br> 5)exit
<br> sleep <seconds>
<br> echo THANK YOU
<br> sleep 1
<br> exit 0
<br> How to check given character is lower case vowel or upper case vowel or a digit
<br> How to display numbers from 1 to 10
<br> How to find even sum and odd sum for a given number 
<br> How to check whether given user connected to server or not if user not connected to server continiously check for user until user connected to server using while
```
vi sp48
echo Enter the User name to check
read usrname
while true
do
if who|grep $usrname>/dev/null
then
echo "User $usrname is Connected"
break
else
echo "Checking for the USER $usrname"
sleep 2
continue
fi
done
:wq
```
<br> How for true command
```
vi sp31
while true
do
echo Sandeep
sleep 1
clear
echo Daddy
sleep 1
clear
done
:wq
```
<br> How for false command 
```
vi sp32
until false
do
echo Sandeep
sleep 1
clear
echo Daddy
sleep 1
clear
done
:wq
```
<br> for i in *
<br> for i in tecno soft is a training institute
<br> for i in 1 2 3 4 5
<br> How to display all files in current directory
```
vi sp35
for i in *
do
if test -f $i -a -r $i
then
cat $i | more
sleep 1
clear
fi
done
:wq
```
<br> How to display all sub-directories in the current directory
```
vi sp36
for i in *
do
if test -d $i
then
echo $i
fi
done
:wq
```
<br> How to find sum of given values using for 
<br> wass to find whether the given files has a read permission or not wass to display all directories in the current directory
<br> bc
<br> chmod 744 sp37
<br> sp37 f1 f2
<br> 0  Stores program name 
<br> 1,$2,$3,$4,$5,$6,$7,$8,$9  Holds parameters
<br> # -Counts number of parameters
<br> * -Counts all parameters
<br> ./ or just . is unix shorthand for the current directory.
<br> Similarly, ../ or just .. is shorthand for the directory above the current one
<br> printenv     # print the environment variables of terminal mac / linux
<br> echo $SHELL  # print present shell
<br> echo $PATH   # print path variable in the environment variable
<br> PATH=/opt/anaconda3/bin:/opt/anaconda3/condabin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin export PATH            (For exporting PATH)
