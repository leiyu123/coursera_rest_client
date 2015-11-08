coursera.org Python API client library
==================================

oursera_rest api Python client library.


For more information about the API and the return values, visit the `official documentation`_.

Sample API call
======================================================

#. **Search all Courses**::

   courseclient=CourseraClient()
   response=courseclient.get_courses()

#. **Search Couses with mutiple Id**::

   courseclient=CourseraClient()
   response=courseclient.get_courses(id=[247,256])

#. **Search Couses by Id**::

   courseclient=CourseraClient()
   response=courseclient.get_courses(id=[247])

#. **Search Couses with more fields**::

   courseclient=CourseraClient()
   response=courseclient.get_courses(field=['name','language','photo','previewLink'])

#. **Search Couses with linked object**::

   courseclient=CourseraClient()
   response=courseclient.get_courses(include=['sessions','instructors'])

#. **Search Couses by name**::

   courseclient=CourseraClient()
   response=courseclient.search_course("software")




    

.. _coursera.org: http://developers.face.com/
.. _official documentation: https://tech.coursera.org/app-platform/catalog/
