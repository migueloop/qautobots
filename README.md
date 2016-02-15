QAutobots
=========

QAutobots is a project that is a framework for quickly setting up and developing 
python driven selenium UI tests

# Developing QAutobots

Clone this and start coding.

    $ git clone <REPO LINK>
    $ cd qautobots
    $ make cybertron

To run unit tests on QAutobots run:

    $ make test

## Directory structure and standard

- **qautobots**: parent directory for selenium tests
    - **components**: contains component page object (any page object that exists on more than one page [i.e. - notification bar])
  	- **fixtures**: classes that help put an account or app in a particular "state"
  	- **framework**: any classes that extends selenium webdriver
  	- **pages**: page objects. See [Page Object Pattern](https://code.google.com/p/selenium/wiki/PageObjects)
  	- **tests**: modules that contains selenium tests
  	- **utilities**: any helper classes that can be used by this project.
- **tests**: primarily unit-tests against QAutobots framework, fixtures, & utilities. Yes, there are tests to test tests...

**OPTIONAL**: set the following global variables:

    $ export PROCESSES=5
    $ export PROCESS_TIMEOUT=120000


# Running Automation Test Modules

Running all QAutobot modules can be done by running: `make autobots-rollout`

To run specific modules: `make autobots-<module-name>`


# Using a Selenium Grid

[Selenium Grid Docs](http://www.seleniumhq.org/docs/07_selenium_grid.jsp)


## Running Tests in Parallel

To run tests in parallel there are some `environment variables to set`, if you haven't already:

- `PROCESSES` : Number of tests to run simultaneously.  Will open a new window for each test.  `default : 0`

- `PROCESS_TIMEOUT` : Set timeout for return of results from each test runner process. `default : 8000`


## Config files

Default: `qautobots/configuration/default.json`

**explanations :**

* `api`: configuration to communication with various APIs
* `database`: configuration to connect to database
* `connections`: configuration for database users. used in fixtures
* `cookie_support`: predefined cookie for the browser
* `application`: configuration for url to test
* `selenium`: configuration needed to set up selenium tests (aka `DESIRED CAPABILITIES`)
	* `remote`: ability to use webdriver remote (selenium grid) or use local browser.  default: `false`
	* `browser`: browser type for testing `FIREFOX`, `CHROME` or `ie`.  defualt: `FIREFOX`
	* `version`: browser version. default: `ANY`
	* `platform`: Operating system of the test platform. default: `MAC`
	* `hub`: configuration of selenium grid hub
		* `provider`: provider of the gird hub `sauce` or `local`
		* `url`: URL of the grid hub.  default: `localhost`
		* `port`: port for grid hub.  default: `4444`
* `decepticons`: Setting a module to `true` will skip it ONLY when running `autobots-rollout`

**OPTIONAL SAUCE CONFIG**

* `sauce`: [saucelabs](https://saucelabs.com) account information (not needed if not using sauce)
	* `user`: username of the sauce account
	* `key`: access key for the account
* `video-upload-on-pass`: toggles video upload on sauce job after test passes
* additional sauce config can be found here [additional config](https://saucelabs.com/docs/additional-config)
