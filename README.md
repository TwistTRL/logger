# logger
Reads standard inputs and logs them into file chunked by datetime format specified.

# Install
```
pip install git+https://github.com/TwistTRL/logger
```

# Usage
```
logger.py [--local|--utc] --format=<fnformat> --output=<outputDir>
```
e.g. cat streaming_source.pipe | logger.py --local --format="%Y-%m-%d" --output=./log

# Options
```
--utc                   Use UTC date time for log file name (recommended)
--local                 Use local date time for log file name
--format=<fnformat>     date time format for filename, e.g. "%Y-%m-%d"
--output=<outputDir>    output directory
```
