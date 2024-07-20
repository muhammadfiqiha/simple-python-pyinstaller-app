#!/usr/bin/env sh

echo 'Running the Python application...'

# Run the built Python application
./dist/add2vals &
sleep 60
echo $! > .pidfile

echo 'Now...'
echo 'Visit http://localhost:3000 to see your Python application in action.'
echo '(This is why you specified the "args ''-p 3000:3000''" parameter when you'
echo 'created your initial Pipeline as a Jenkinsfile.)'

echo 'The following command terminates the application process using its PID'
echo '(written to ".pidfile"), all of which were conducted when "deliver.sh"'
echo 'was executed.'
set -x
kill $(cat .pidfile)