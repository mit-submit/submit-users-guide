Tutorial 1: Common software packages (python, Julia, MATLAB)
------------------------------------------------------------

.. tags:: Julia

This tutorial will show a few examples of code that you can run on submit immediately after logging in (python, MATLAB), or after some simple setups (Julia). 
For more info on what is immediately available to you on subMIT, see the User's Guide here: `Native System <https://submit.mit.edu/submit-users-guide/program.html#native-system>`_


Python Example:
~~~~~~~~~~~~~~~

subMIT has several languages available in the native system. For this example, we will create a very simple python code to run. Then we can expand on this code by adding in additional packages using pip.


Let's run a simple code. Here is an example:

.. code-block:: sh

     x = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
     y = []
     
     for xval in x:
         y.append(xval**2)
     
     print("The values squared from for loop are:{}".format(y))


Copy this chunk of code into a file called tutorial_1.py and run it with:

.. code-block:: sh

     python tutorial_1.py

pip installations:
..................

Obviously, the code above is very inefficient. Let's use numpy and see if we can make this a bit easier to code and faster.

We want to download numpy to our local directory using pip. Use the command below:

.. code-block:: sh

     python -m pip install numpy --user

You should now see numpy installed in your local directory. You can check that with the command below:

.. code-block:: sh

     python -c "import numpy; print(numpy.__file__)"

Now let's do the same code as above but use numpy instead:

.. code-block:: sh

     x = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
     y = []
     
     for xval in x:
         y.append(xval**2)
     
     print("The values squared from for loop are:{}".format(y))
     
     import numpy as np
     
     x_np = np.linspace(1,10,10)
     y_np = x_np**2
     
     print("The values squared from numpy are:{}".format(y_np))

Types of Python environments:
.............................



#. Global: if you run ``python`` or ``python3`` in a terminal window, you are running in a global environment. However, it is a better practice to create a local environment.

#. Local: in a local environment, you can install packages that won't affect your other local environments, nor the global environment. There are two types:

     * conda

     .. code-block:: sh

          conda create -n test_env

     * venv

     .. code-block:: sh

          python -m venv .venv

Both types of local environments can also be created in Visual Studio Code by using the Command Palette (``Cmd+Shift+P`` in macOS or ``Ctrl+Shift+P`` in Windows) and selecting "Python: Create Environment...". You can then choose the version of Python to install in this environment. See `Visual Studio Code documentation <https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment>`_ for more information.

Julia:
~~~~~~



Once you have installed Julia (see the `Available software page <https://submit.mit.edu/submit-users-guide/program.html#julia>`_), you can try running a simple Julia example:

.. code-block:: sh

     function sphere_vol(r)
         # julia allows Unicode names (in UTF-8 encoding)
         # so either "pi" or the symbol π can be used
         return 4/3*pi*r^3
     end
     
     # functions can also be defined more succinctly
     quadratic(a, sqr_term, b) = (-b + sqr_term) / 2a
     
     # calculates x for 0 = a*x^2+b*x+c, arguments types can be defined in function definitions
     function quadratic2(a::Float64, b::Float64, c::Float64)
         # unlike other languages 2a is equivalent to 2*a
         # a^2 is used instead of a**2 or pow(a,2)
         sqr_term = sqrt(b^2-4a*c)
         r1 = quadratic(a, sqr_term, b)
         r2 = quadratic(a, -sqr_term, b)
         # multiple values can be returned from a function using tuples
         # if the return keyword is omitted, the last term is returned
         r1, r2
     end
     
     vol = sphere_vol(3)
     # @printf allows number formatting but does not automatically append the \n to statements, see below
     using Printf
     @printf "volume = %0.3f\n" vol
     #> volume = 113.097
     
     quad1, quad2 = quadratic2(2.0, -2.0, -12.0)
     println("result 1: ", quad1)
     #> result 1: 3.0
     println("result 2: ", quad2)


Save this into a file named julia_test.jl and this can be run with the following:

.. code-block:: sh

     julia julia_test.jl

MATLAB:
~~~~~~~

Here we can try running a simple MATLAB example:

.. code-block:: sh

     a = 3;
     b = a*a;
     c = a*a*a;
     d = sqrt(a);
     fprintf('%4u square equals %4u \r', a, b)
     fprintf('%4u cube equals %4u \r', a, c)
     fprintf('The square root of %2u is %6.4f \r', a, d)

Save this into a file named matlab_example.m and this can be run with the following:

.. code-block:: sh

     matlab -nodisplay -nodesktop -r "run matlab_example.m"


MATLAB GUI:
...........

In order to enter into the GUI mode of MATLAB on submit you need to log into submit with the -X option:


.. code-block:: sh

     ssh -X <username>@submit.mit.edu

Then you can enter the MATLAB GUI:

.. code-block:: sh

     matlab

