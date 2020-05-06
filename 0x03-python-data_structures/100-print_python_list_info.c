#include <stdio.h>
#include <object.h>
#include <Python.h>
#include <listobject.h>
/**
 * print_python_list_info - print info of a list in python
 * @p: Python object
 */
void print_python_list_info(PyObject *p)
{
	long int hand, len;
	PyListObject *list;
	PyObject *it;
	PyVarObject *obj;

	list = (PyListObject *)p;
	obj = (PyVarObject *)p;
	len = Py_SIZE(obj);
	printf("[*] Size of the Python list = %li\n", len);
	printf("[*] Allocated = %li\n", (long int)list->allocated);
	for (hand = 0; hand < len; hand++)
	{
		it = PyList_GetItem(p, hand);
		printf("Element %li: %s\n", hand, Py_TYPE(it)->tp_name);
	}
}
