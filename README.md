# MissionControlPythonApp
MissionControlPythonApp is an application developed using Python and the Kivy framework.

# Description:
The application focuses on real-time visualization of data sent through the serial port thanks to an Arduino which has acceleration and rotation sensors on the 3 axes and GPS data (latitude, longitude, and altitude). Likewise, the program is able to record and save the collected data for later analysis either in a third-party software or in the same app which includes an option for the analysis and visualization of data.
# NOTE:
The application at this time is taken as a guide and a first approach to the objective (represent data received by the serial port reliably in a desktop application), because at this time the application despite being functional has several flaws and limitations which at the moment have not been fixed and are not intended to be fixed by the creator. Among these flaws and limitations are:
- Correct display of graphs when scaling the size of the application
- Arduino detection after starting the application
- Automatic detection of Arduino
- Correct display of data in the analysis section during the application
- Correct implementation of the change of data units
- Automatic adjustment of legends and axis values in the graphs (a range should be included to display the data).
- Some others less important
However, the idea and functionalities of the application are being transferred to a new project where it is working in C++ with the QT framework, in this application it has already been solve some of the problems and limitations mentioned above. The application is expected to be ready in its first fully functional version by the end of 2023 or early 2024.

For more information about this or other projects, please contact me at any of the following e-mail addresses:
andreswii6@hotmail.com
andres.rodriguez10@udea.edu.co
