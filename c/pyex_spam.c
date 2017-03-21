#include <Python.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

static PyObject* my_callback = NULL;

pthread_t tid;
void* doSomeThing(void* arg)
{
	int i;
	PyObject* arglist;
	PyObject* result;
	
	for(i = 0; i<10; i++)
	{
		arglist = Py_BuildValue("(l)", i);
		result = PyObject_CallObject(my_callback, arglist);
		Py_DECREF(arglist);
		if(result == NULL)
			return NULL;
		sleep(1);		
	}
}


static PyObject* set_callback(PyObject* dummy, PyObject* args)
{
        PyObject* result = NULL;
        PyObject* temp = NULL;

        if(PyArg_ParseTuple(args, "O:set_callback", &temp))
        {
                if(!PyCallable_Check(temp))
                {
                        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
                        return NULL;
                }

                Py_XINCREF(temp);
                Py_XDECREF(my_callback);
                my_callback = temp;
                
                Py_INCREF(Py_None);
                result = Py_None;
        }

	//start a thread to call the python function back
	int err;
	err = pthread_create(&tid, NULL, &doSomeThing, NULL);
	if(err != 0)
		printf("Can't create thread :[%s]", strerror(err));

        return result;
}


static PyObject *SpamError;

static PyObject* spam_system(PyObject* self, PyObject* args)
{
	const char* command;
	int sts;

	if(!PyArg_ParseTuple(args, "s", &command))
		return NULL;

	sts = system(command);
	if(sts < 0)
	{
		PyErr_SetString(SpamError, "System command failed");
		return NULL;
	}
	return PyLong_FromLong(sts);
}




static PyMethodDef SpamMethods[] = {
        {"system", spam_system, METH_VARARGS, "Execute a shell command"},
        {"setcallback", set_callback, METH_VARARGS, "Set a python callback"},
        {NULL, NULL, 0, NULL}
};

static struct PyModuleDef spammodule = {
        PyModuleDef_HEAD_INIT,
        "spam",
        NULL,
        -1,
        SpamMethods
};

PyMODINIT_FUNC PyInit_spam(viod)
{
        return PyModule_Create(&spammodule);
}
     

