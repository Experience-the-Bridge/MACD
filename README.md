# MACD
"""
Sean O'Brien
-Description: Simple moving averages with the lengths of 9-days, 12-days,
and 26-days. The 9 and 12 day values serve as the dual moving average while
the 26 day is the difference between the 26 and 12 day values. The 26-day
value will be visualized seperately about the y = 0 line for positive and
negative values.
-Using yfinance library. $ pip install yfinance. Using the Public API
(without authentication), you are limited to 2,000 requests per hour per
IP (or up to a total of 48,000 requests a day). Please use time.sleep(1)
to avoid your IP getting blocked.

-Using virtual enviornment with python@3.7 as interpreter
-Column names: Date,Open,High,Low,Close,Volume,Dividends,Stock Splits

-There are more params you can set for history() method:
Arguments           Scenarios                                                                           Example Value
period              date period to download                                                             1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
interval            data interval. If it’s intraday data, the interval needs to be set within 60 days   1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
start               If period is not set- Download start date string (YYYY-MM-DD) or 'datetime'         2020-03-18
end                 If period is not set - Download end date string (YYYY-MM-DD) or ''datetime'         2020-03-18
prepost             Boolean value to include Pre and Post market data                                   Default is False
auto_adjust         Boolean value to adjust all OHLC                                                    Default is True
actions             Boolean value download stock dividends and stock splits events                      Default is True

"""

virtualenv requirements.txt:
appdirs==1.4.4
appnope==0.1.2
APScheduler==3.6.3
astroid==2.4.2
attrs==20.3.0
Automat==20.2.0
autopep8==1.5.4
backcall==0.2.0
beautifulsoup4==4.9.3
cached-property==1.5.2
certifi==2020.4.5.1
cffi==1.14.4
chardet==3.0.4
clang==11.0
constantly==15.1.0
coreml==0.0.4
cron-install==0.2.0
cryptography==3.2.1
cssselect==1.1.0
cycler==0.10.0
DateTime==4.3
decorator==4.4.2
distlib==0.3.0
docker==4.4.0
docker-cron==0.4.0
filelock==3.0.12
h5py==3.1.0
html5lib==1.1
hyperlink==20.0.1
idna==2.10
importlib-metadata==1.7.0
incremental==17.5.0
ipykernel==5.3.4
ipython==7.19.0
ipython-genutils==0.2.0
isort==5.5.1
itemadapter==0.2.0
itemloaders==1.0.4
jedi==0.17.2
jmespath==0.10.0
joblib==0.17.0
jupyter-client==6.1.7
jupyter-core==4.7.0
Keras==2.4.3
kiwisolver==1.3.1
Lasagne==0.1
lazy-object-proxy==1.4.3
lxml==4.6.2
math22==2.2
matplotlib==3.3.3
mccabe==0.6.1
multitasking==0.0.9
mypy==0.790
mypy-extensions==0.4.3
neural-networks-tfw1==0.1
neurolab==0.3.5
node==0.9.25
npm==0.1.1
numpy==1.19.4
odict==1.7.0
optional-django==0.1.0
pandas==1.1.5
pandas-datareader==0.9.0
parsel==1.6.0
parso==0.7.1
pbr==5.4.5
pexpect==4.8.0
pickleshare==0.7.5
Pillow==8.0.1
pipenv==2020.6.2
plumber==1.6
prompt-toolkit==3.0.8
Protego==0.1.16
ptyprocess==0.6.0
py3tools==0.0.6
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycodestyle==2.6.0
pycparser==2.20
PyDispatcher==2.0.5
Pygments==2.7.3
PyHamcrest==2.0.2
pylint==2.6.0
pyOpenSSL==19.1.0
pyparsing==2.4.7
pyrenn==0.1
python-crontab==2.5.1
python-dateutil==2.8.1
python-magic==0.4.18
pytz==2020.4
PyYAML==5.3.1
pyzmq==20.0.0
queuelib==1.5.0
requests==2.25.0
scikit-learn==0.23.2
scipy==1.5.4
Scrapy==2.4.1
seaborn==0.11.0
selenium==3.141.0
service-identity==18.1.0
six==1.15.0
sklearn==0.0
soupsieve==2.0.1
stats==0.1.2a0
stevedore==2.0.0
style==1.1.0
threadpoolctl==2.1.0
tld==0.12.3
toml==0.10.1
tornado==6.1
traitlets==5.0.5
tree-lstm==0.0.2
Twisted==20.3.0
typed-ast==1.4.1
typing-extensions==3.7.4.3
tzlocal==2.1
update==0.0.1
urlfinderlib==0.15.6
urllib3==1.26.2
validators==0.18.1
Vector2==20200430
virtualenv==20.0.21
virtualenv-clone==0.5.4
virtualenvwrapper==4.8.4
w3lib==1.22.0
wcwidth==0.2.5
webencodings==0.5.1
websocket-client==0.57.0
wrapt==1.12.1
yfinance==0.1.55
zipp==3.4.0
zope.component==4.6.2
zope.deferredimport==4.3.1
zope.deprecation==4.4.0
zope.event==4.5.0
zope.hookable==5.0.1
zope.interface==5.2.0
zope.lifecycleevent==4.3
zope.proxy==4.3.5
