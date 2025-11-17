# Macproxy Classic

A simple HTTP proxy that enables early computers to browse the Web.
*Macproxy Classic* is an improved fork of the original [Macproxy](https://github.com/tghw/macproxy) by Tyler Hicks-Wright,
while integrating improvements from [Macproxy Plus](https://github.com/hunterirving/macproxy_plus) by Hunter Irving.

Despite its name, there is nothing Mac specific about this proxy.
It was originally designed with compatibility with the MacWeb web browser in mind,
but has been tested on a variety of vintage web browsers since.

The proxy.py script runs a Flask server that takes all requests and proxies them,
stripping tags and contents that are incompatible with old browsers such as Netscape 4 or MacWeb.

The proxy server listens to port 5001 by default, but the port number can be changed using a command line parameter.

## Requirements

Python3 for running the script, venv if you want to use the virtual environment, or pip if you want to install libraries manually.

Example installation on Debian/Ubuntu-based systems:

```shell
sudo apt install python3 python3-venv python3-pip
```

## Usage

On a Unix-like system, the start_macproxy.sh shell script will create and manage a venv Python environment,
and if successful launch the proxy script.

```shell
./start_macproxy.sh
```

Launch with a specific port number (defaults to port 5001):

```shell
./start_macproxy.sh --port=5002
```

## Extensions

Macproxy Classic has borrowed support for 'extensions' from Macproxy Plus,
which intercept requests for specific domains and serve simple HTML interfaces,
making it possible to more easily browse certain modern websites from a vintage machine.

Each extension has its own folder within the `extensions` directory.
Extensions can be individually enabled or disabled via a `config.py` file in the root directory.

Descriptions of available extensions follows.

### Hackaday

Serves a pared-down, text-only version of hackaday.com, complete with articles, comments, and search functionality.

### (not) YouTube

A legally distinct parody of YouTube, which uses the fantastic homebrew application [MacFlim](https://www.macflim.com/macflim2/)
(created by Fred Stark) to encode video files as a series of dithered black and white frames.

Requires MacFlim to be installed on the proxy host machine.

### npr.org

Serves articles from the text-only version of the site text.npr.org
and transforms relative urls into absolute urls for compatibility with MacWeb 2.0.

### Reddit

Browse any subreddit or the Reddit homepage, with support for nested comments and downloadable images...
in dithered black and white if you like.

### WayBack Machine

Go to web.archive.org, enter any date between January 1st, 1996 and today,
then browse the web as it existed at that point in time.
Includes full download support for images and other files backed up by the Internet Archive.

### Weather

Get the weather.gov forecast for any zip code in the US. Requires configuring your US zip code in config.py.

### wiby.me

Browse Wiby's collection of personal, handmade webpages (fixes an issue where clicking "surprise me..."
would not redirect users to their final destination).

### Wikipedia

Read any of over 6 million encyclopedia articles on wikipedia.org - complete with clickable links and search function.

## Containerization

With the bundled Dockerfile, you can run Macproxy in a container through the power of Docker Engine.

Either build an image yourself with `docker build`, or pull the [latest image from Docker Hub](https://hub.docker.com/r/rdmark/macproxy):

```shell
docker pull rdmark/macproxy:latest
```

Then launch the container with `docker run` (see below) or `docker compose up`. The examples assume the default port `5001`.

```shell
docker run --rm -p 5001:5001 macproxy
```

## systemd service

This repo comes with a systemd service configuration template,
for controlling Macproxy on systems that use the systemd init system.
Edit the macproxy.service file and point the ExecStart= parameter to the location of the start_macproxy.sh file,
e.g. from a git repo checkout in your home dir:

```ini
ExecStart=/home/myuser/macproxy/start_macproxy.sh
```

Then copy the service file to /etc/systemd/system and enable the service:

```shell
sudo cp macproxy.service /etc/systemd/system/
sudo systemctl enable macproxy
sudo systemctl daemon-reload
sudo systemctl start macproxy
```
