Aleph scripts and snippets
=====
Using this repository to store and share whatever Aleph scripts and snippets I have which are suitable for public consumption!

###Aleph currency updater script (currency_grab.py)

For use with p-acq-20 in Aleph, this script connects with any data source that provides JSON-formatted currency (in this case openexchangerates.org) and writes to a properly formatted Aleph currency.dat file. Running this via a simple cron job at the moment.

Line 5 will have to have a valid openexchangerates.org API key appended for the exchange rate data to be downloaded.
