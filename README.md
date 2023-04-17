#Required Libraries
1. pip install -r requirements.txt
2. Install tessaract and find where the executable file is placed. 
3. Provide the location of tessaract executable file -> (Lin. 9 or 13 at extract_text.py)
4. Replace the image ReadThisImage.jpg with your actual image(Note that the file name should be Intact)
5. run extract_text.py (cmd: python extract_text.py)


#If you want to run from CI servers like Jenkins, use Bash file.
Run the bash file with image location as parameter, 
#file name: run.sh
#parameter: <image_location/image_name.jpg>

Example: bash run.sh '/Users/username/VisualStudio/imageread/captcha.jpg'