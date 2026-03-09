*** Settings ***
Documentation
...  Keywords of Log Parser tool automation

Library    os
Library    OperatingSystem
Library    ${EXECDIR}/library/phase_test.py
Variables  ${EXECDIR}/variablefiles/var_file.py


*** Keywords ***

search log
    [Documentation]         Get the parameter values from the log file.
    ...                     \n Author: LTTS
    lscpu_log

convert to json
    [Documentation]         Convert the captured log file to json file.
    ...                     \n Author: LTTS
    get_lscpu

print table from static data
    [Documentation]         Print the data from the json file in table format.
    ...                     \n Author: LTTS
    lscpu_table


