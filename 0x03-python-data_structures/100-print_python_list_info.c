  
#include <Python.h>
/**
  * print_python_list_info - prints python list info
  * @p: pyobject
  * Return: void
  */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *object;

	size = Py_SIZE(p);
	numElements = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", numElements);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
