#include <listobject.h>
#include <Python.h>
#include <object.h>
/**
 * print_python_list_info - print info of a list in python
 * @x: Python object
 */
void print_python_list_info(PyObject *x)
{
	Py_ssize_t hand, len;
	PyListObject *list;
	PyObject *it;
	PyVarObject *obj;

	list = (PyListObject *)x;
	obj = (PyVarObject *)x;
	len = Py_SIZE(obj);
	printf("[*] Size of the Python list = %li\n", len);
	printf("[*] Allocated = %li\n", list->allocated);
	for (hand = 0; hand < len; hand++)
	{
		it = PyList_GetItem(x, hand);
		printf("Element %li: %s\n", hand, Py_TYPE(it)->tp_name);
	}
}
