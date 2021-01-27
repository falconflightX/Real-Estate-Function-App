# Real-Estate-Function-App

A http trigger based input and output for launching an ML (python script) code in an Azure function is shown 

## Step 1 :
Create a virtual environment. A simple python code for predicting the price of a house based on age, distance, number of stores in the locality, latitude and longitude is written up. The result is stored as a pkl file. 

## Step 2 :
Fire up the function app via vs code and point it to the existing folder where the python code and the pkl files are stored - requirements file is automatically created. The necessary files needed for running the code are further added. 

## Step 3 :
The init.py file is the file that contains the main code for the function app, that triggers the http and has the post and get requests. Results of the json dump are returned as a numpy array. 

## Step 4 :
Initialize the function app in the command prompt with "func init" command. 
Start the function with "func host start" command. 
You will be directed to a link on the local. Allow it to be. Open up git bash and run the following command: curl -w '\n' 'http://localhost:7071/api/real_estate?Age=25&Dist=251&Num_stores=5&Lat=24.9756&Long=121.5521'   (you can change values for age, dist....). On running, a success in the python terminal should be shown. 

## Step 5 
deploy it to Azure function app directly from vs code from the functions extension. This is pretty straightforward - use the deployment commands as prompted. Your app should be ready. Use the weblink as deployed and add the same parts to the http link (?Age=25&Dist=251&Num_stores=5&Lat=24.9756&Long=121.5521). You should see the response. 
