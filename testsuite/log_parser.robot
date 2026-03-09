*** Settings ***

Documentation
...  Case name: Log Parser tool automation.
...  "Author: LTTS"
...  *How To execute test case:*
...  robot -t "Particular Testcase Name" -d results testsuite/log_parser.robot

Library    os
Library    OperatingSystem
Library    ${EXECDIR}/library/phase_test.py
Variables  ${EXECDIR}/variablefiles/var_file.py
Resource   ${EXECDIR}/resources/logparser_keyword.robot


*** Test Cases ***
logparser_TC1:lscpu
      search log
      convert to json
      print table from static data





