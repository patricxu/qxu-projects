#include <Python.h>
static PyObject* my_callback = NULL;
static PyObject* set_callback(PyObject* dummy, PyObject* args)
{
        PyObject* result = NULL;
        PYObject* temp = NULL;

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
        return result;
}

static PyMethodDef SpamMethods[] = {
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
     
