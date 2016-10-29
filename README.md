# datalog_serial
Serial data loging for Micro:Bit

Very simple voltage over time data loging for BBC MicroBit.

Drive Pin0 with an interesting voltage (maximum 3.3V). Run the logging script on a linux machine (I use a chromebook running Crouton - https://github.com/dnschneid/crouton

Since this was intended to monitor battery discharge over a period of a couple of hours, the sampling and filtering is tuned to that application. There is crude noise rejection, but the logging is sensitive to rapid decreases in sample voltage.

A rough indication of input voltage is provided using 2 vertical 5 bit indicators, and an 'alive' LED blinks.
