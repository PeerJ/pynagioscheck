=============
pynagioscheck
=============

``pynagioscheck`` is a Python framework for Nagios plug-in developers.

``pynagioscheck`` strives to conform to the practices described in the 
`Nagios Plug-in Development Guidelines`_ and, more importantly, save 
valuable system administrator time.

.. _`Nagios Plug-in Development Guidelines`: http://nagiosplug.sourceforge.net/developer-guidelines.html


Usage
-----

Check ``examples/`` for a jump start.

The long version:

    1. Subclass ``nagioscheck.NagiosCheck`` as ``YourCheck``.

    #. Set ``YourCheck.version``.  I prefer the ``major.minor.patch`` 
       format, but you can use whatever you like.  Increment this 
       version number with every revision to your check script.

    #. If your check script takes mandatory arguments, describe them in  
       ``YourCheck.usage``.  Arguments are not the same as options.  
       e.g.::

           YourCheck.usage = '[options] HOST PORT'

    #. From ``YourCheck.__init__()``, invoke ``NagiosCheck.__init__(self)`` 
       before you do anything else.

    #. Let ``NagiosCheck`` know about any optional arguments you might 
       want to parse with ``NagiosCheck.add_option()``.  It makes the most 
       sense to do this from inside ``YourCheck.__init__()``.

    #. Define a ``YourCheck.check()`` method that will implement your 
       actual service check.  This method takes two arguments:

       a. ``opts``: An instance of ``optparse.Values``.
       
          Suppose an option is registered with::

              self.add_option('H', 'host', 'host', 'Hostname or ...')

          then, if the user supplies a hostname with ``-H HOST`` or 
          ``--host HOST`` at the command line, the option argument 
          (``HOST``) will be available from inside the ``check()`` method 
          as::

              host = getattr(opts, 'host')

          Option argument attributes will be ``None`` if the option was 
          not supplied at the command line.

       #. ``args``: A list of mandatory postitional arguments.  This list 
          should match the usage information in ``YourCheck.usage``.

       ``YourCheck.check()`` *must* raise ``nagioscheck.Status`` as soon as 
       the result of the service check is known.  ``YourCheck.check()`` 
       *must not* return.  See the examples and source for details.

    #. With ``YourCheck`` defined, instantiate and make it go with::

           if __name__ == '__main__':
               YourCheck().run() 


What you get for free
---------------------

    - Output string formatting and exit statuses conform to Nagios 
      plug-in development guidelines.  You don't need to remember that 
      exit status 2 is used to signal CRITICAL check status, or that 
      there are twelve inches in a foot.

    - Routines that make it easier to report Nagios perfdata 
      (performance data).

    - A handful of utility functions for common data mangling and 
      presentation chores.

    - A way to clean up after yourself if your execution time limit 
      expires.  This feature may not work with older versions of the 
      Nagios NRPE server::

          --- nagios-nrpe-2.12~/src/nrpe.c 2008-03-11 08:04:43.000000000 +1100
          +++ nagios-nrpe-2.12/src/nrpe.c 2011-05-11 23:01:06.182404333 +1000
          @@ -1467,6 +1467,7 @@

                                  /* send termination signal to child process group */
                                  kill((pid_t)(-pid),SIGTERM);
          +                       sleep(5); /* or whatever */
                                  kill((pid_t)(-pid),SIGKILL);
                                  }

      See ``NagiosCheck.expired()`` for details.

    - ``-v`` works out of the box.  Supply it more than once for 
      additional verbosity.  There are four levels in total.  You 
      control what is output at each level with your arguments to 
      ``nagioscheck.Status()``.  See the examples and source for 
      details.  Use ``-vvv`` to view a backtrace of your check script to 
      the point where it raised ``NagiosCheck.Status``::

          % check_redis -vvv
          CRITICAL: Error 61 connecting 127.0.0.1:6379. Connection refused.

            File "./check_redis", line 29, in check
              info = r.info()
            File "build/bdist.macosx-10.6-universal/egg/redis/client.py", line 380, in info
              return self.execute_command('INFO')
            [...]

    - ``-h`` and ``--help`` work out of the box.

    - ``--version`` works out of the box.


What you probably should get for free, but don't
------------------------------------------------

    - Validation helpers.

    - Threshold helpers.

Author
------

Saj Goonatilleke <sg@redu.cx>
