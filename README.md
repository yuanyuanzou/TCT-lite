# Dependency:

python2.7 python-pip requests

    $ sudo apt-get install python-pip
    $ sudo pip install requests

# How to build:

Build from source code: 

    $ sudo python setup.py build

# How to install:

Install testkit lite  from source code: 

    $ sudo python setup.py install

# How to use:

At first, install a test package or prepare one tests.xml file aligned with schema files: /opt/testkit/lite/xsd/testdefinition-syntax.xsd.

And then,

   1) You can run case on target:
    
   For web test cases:
   
        $ testkit-lite -f device:"<somewhere>/<package_name>/tests.xml" -e 'WRTLauncher <package_name>'
   For native test cases:
   
        $ testkit-lite -f device:"<somewhere>/<package_name>/tests.xml" 

   2) You can run case in single mode :
   
   For web test cases:
   
        $ testkit-lite -f "<somewhere>/<package_name>/tests.xml" -e 'WRTLauncher <package_name>' --comm localhost
   For native test cases:
   
        $ testkit-lite -f "<somewhere>/<package_name>/tests.xml" --comm localhost

   3) You can select on parser engine to simply conduct one or more tests.xml on target:
   
        $ testkit-lite -f device:"<somewhere>/<package_name1>/tests.xml ... <somewhere>/<package_namen>/tests.xml" -e 'WRTLauncher <package_name1> ... <package_namen>'

   4) If you want to execute both auto and manual tests:
    
        $ testkit-lite -f device:"<somewhere>/<package_name>/tests.xml"
        
   5) If you just want to execute manual tests:
   
        $ testkit-lite -f device:"<somewhere>/<package_name>/tests.xml" -M
        
   6) If you just want to execute auto tests:
   
        $ testkit-lite -f device:"<somewhere>/<package_name>/tests.xml" -A
       
   7) If you want to save test result to another file, by default it'll be under /opt/testkit/lite/latest:
   
        $ testkit-lite -f device:"<somewhere>/<package_name>/tests.xml" -o <somewhere>/xxx.xml
        
   8) If you want to choose some filters:
   
        $ testkit-lite -f device:"<somewhere>/<package_name>/tests.xml" --status level1 --type type1 ...

   9) If you want to run test according capability:
   
        $ testkit-lite -f device:"<somewhere>/<package_name>/tests.xml" --capability capability.xml
        
   10) At last, you can freely compose the above parameters together:
   
        $ testkit-lite -f <somewhere1>/tests.xml <somewhere2>/tests.xml -A --priority P1 --type type1 ...

# Get Results:

Test report will be generated as tests.result.xml   
The result will be under /opt/testkit/lite/latest after execution, you can also check the history results in /opt/testkit/lite/yyyy-mm-dd-HH:MM:SS.NNNNNN.

# View Results:

Test report can be viewed in HTML format, so the data in the xml result file looks more human friendly.

Please follow the following steps to view test report:
   1) copy files: application.js back_top.png jquery.min.js testresult.xsl tests.css under directory /opt/testkit/lite/xsd/
   2) put the files from step 1) under the same directory as the xml result file
   3) open xml result file with a web browser(IE, Chrome or Firefox)

# Known Issues:


