from .connection import Connection
class CourseraClient:
    def __init__(self,host="api.coursera.org/api",version="catalog.v1"):
        self.api_connection=Connection(host,version)


    def get_courses(self,**kwargs):
        """ Get course collection
        param id:(optional) int list. List of course id to be sent in the query string to retrive specificed courses
        param field:(optional) string list, List of field to be sent in the query string to retrive the fields in response 
           objects,by default only a minimal set of fields are included in response objects, Allowed list value
            id: int - The Course Id.
            shortName: String - The short name associated with the course.
            name: String - The course name or title.
            language: String - The language code for the course. (e.g. 'en' means English.)
            largeIcon: Option[String] - A large image to represent the course.
            photo: Option[String] - A course photo.
            previewLink: Option[String] - If the course has enabled preview, this is the preview URL.
            shortDescription: Option[String] - A short description of the course.
            smallIcon: Option[String] - A small icon.
            smallIconHover: Option[String] - Hovered icon.
            subtitleLanguagesCsv: String - Translated languages.
            isTranslate: Boolean - Whether the course is translated.
            universityLogo: Option[String] - If there is a special university logo.
            universityLogoSt: Option[String] - Signature track university logo.
            video: Option[String] - The YouTube video code. e.g. <https://www.youtube.com/watch?v=CCmTQW7OebM>
            videoId: Option[String] - Synonym for video
            aboutTheCourse: Option[String] - HTML snippet describing the course.
            targetAudience: Option[Int] - Description of the intended course audience. The target audiences are: 0 - Basic undergraduates, 1 - Advanced undergraduates or beginning graduates, 2 - Advanced graduates, and 3 - Other
            faq: Option[String] - HTML snippet answering frequently asked questions.
            courseSyllabus: Option[String] - HTML snippet containing the course syllabus.
            courseFormat: Option[String] - Format description.
            suggestedReadings: Option[String] - HTML snippet containing suggested readings.
            instructor: Option[String] - Instructor name(s) and title(s).
            estimatedClassWorkload: Option[String] - Description of the estimated workload for the course.
            aboutTheInstructor: Option[String] - HTML snippet about the instructor.
            recommendedBackground: Option[String] - HTML snippet describing recommended background. 
        param include:(optional) List of include to be sent in the query string,so linked objects can be included in response, allowed linked object
            sessions - The sessions for a course.
            instructors - The instructors for a course.
            universities - The universities associated with a course.
            categories - The categories of the course.
        """
        return self.api_connection.get(self._get_path("courses",**kwargs))


    def search_course(self,name,**kwargs):
        """ Search course
        param name: course name
        param field:(optional) List of field to be sent in the query string to retrive the fields in response 
           objects,by default only a minimal set of fields are included in response objects, Allowed list value
            id: String - The Course Id.
            shortName: String - The short name associated with the course.
            name: String - The course name or title.
            language: String - The language code for the course. (e.g. 'en' means English.)
            largeIcon: Option[String] - A large image to represent the course.
            photo: Option[String] - A course photo.
            previewLink: Option[String] - If the course has enabled preview, this is the preview URL.
            shortDescription: Option[String] - A short description of the course.
            smallIcon: Option[String] - A small icon.
            smallIconHover: Option[String] - Hovered icon.
            subtitleLanguagesCsv: String - Translated languages.
            isTranslate: Boolean - Whether the course is translated.
            universityLogo: Option[String] - If there is a special university logo.
            universityLogoSt: Option[String] - Signature track university logo.
            video: Option[String] - The YouTube video code. e.g. <https://www.youtube.com/watch?v=CCmTQW7OebM>
            videoId: Option[String] - Synonym for video
            aboutTheCourse: Option[String] - HTML snippet describing the course.
            targetAudience: Option[Int] - Description of the intended course audience. The target audiences are: 0 - Basic undergraduates, 1 - Advanced undergraduates or beginning graduates, 2 - Advanced graduates, and 3 - Other
            faq: Option[String] - HTML snippet answering frequently asked questions.
            courseSyllabus: Option[String] - HTML snippet containing the course syllabus.
            courseFormat: Option[String] - Format description.
            suggestedReadings: Option[String] - HTML snippet containing suggested readings.
            instructor: Option[String] - Instructor name(s) and title(s).
            estimatedClassWorkload: Option[String] - Description of the estimated workload for the course.
            aboutTheInstructor: Option[String] - HTML snippet about the instructor.
            recommendedBackground: Option[String] - HTML snippet describing recommended background. 
        param include:(optional) List of include to be sent in the query string,so linked objects can be included in response, allowed linked object
            sessions - The sessions for a course.
            instructors - The instructors for a course.
            universities - The universities associated with a course.
            categories - The categories of the course.
        """
        return self.api_connection.get(self._get_path("courses?q=search&query="+name,**kwargs))


    def get_universities(self,**kwargs):
        """ Get course collection
        param id:(optional) int list. List of unversity id to be sent in the query string to retrive specificed unversities
        param field:(optional) string list. List of field to be sent in the query string to retrive the fields in response 
            objects,by default only a minimal set of fields are included in response objects, Allowed list value
            id: int - The University Id
            name: String - The university?s name
            shortName: String - The short name associated with the university.
            description: Option[String] - The university?s description.
            banner: Option[String] - The URL to a background banner image
            homeLink: Option[String] - Link to the university?s home page.
            location: Option[String] - Human-readable description of the partner?s location.
            locationCity: Option[String] - University?s city.
            locationState: Option[String] - University?s state.
            locationCountry: Option[String] - University?s country.
            locationLat: Option[Double] - University?s latitude.
            locationLng: Option[Double] - University?s longitude.
            classLogo: Option[String] - URL to the logo used inside courses.
            website: Option[String] - University?s website.
            websiteTwitter: Option[String] - University?s offical twitter handle.
            websiteFacebook: Option[String] - University?s facebook page.
            websiteYoutube: Option[String] - University?s youtube channel.
            logo: Option[String] - University?s Logo
            squareLogo: Option[String] - University?s Logo (Square)
            landingPageBanner: Option[String] - High-resolution banner for use on the Coursera home landing page.
        param include:(optional) List of include to be sent in the query string,so linked objects can be included in response,allowed include value
            courses - The courses an instructor teaches.
            instructors - The instructors associated with a university.
        """
        return self.api_connection.get(self._get_path("universities",**kwargs))


    def get_categories(self,**kwargs):
        """ Get category collection
        param id:(optional) int list. List of category id to be sent in the query string to retrive specificed categories
        param field:(optional) string list. List of field to be sent in the query string to retrive the fields in response 
           objects,by default only a minimal set of fields are included in response objects
            id: String - The category?s id
            name: String - The category?s name.
            shortName: String - The short name associated with the category.
        description: Option[String] - The category?s description.
        param include:(optional) List of include to be sent in the query string,so linked objects can be included in response
           courses - The courses in a category.
        """
        return self.api_connection.get(self._get_path("categories",**kwargs))


    def get_instructors(self,**kwargs):
        """ Get instructor collection
        param id:(optional) int list. List of instructor id to be sent in the query string to retrive specificed instructors
        param field:(optional) string list. List of field to be sent in the query string to retrive the fields in response 
            objects,by default only a minimal set of fields are included in response objects
            id: Int - Instructor ID
            photo: Option[String] - photo URL
            photo150: Option[String] - photo URL 150x150px
            bio: String - Instructor Biogrophy
            prefixName: Option[String] - Prefix for the instructor?s name
            firstName: Option[String] - Instructor first name
            middleName: Option[String] - Instructor middle name
            lastName: Option[String] - Instructor last name
            suffixName: Option[String] - Suffix for the instructor name
            fullName: Option[String] - Instructor full name
            title: Option[String] - Instructor title
            department: Option[String] - Instructor department
            website: Option[String] - Instructor?s personal website
            websiteTwitter: Option[String] - Instructor?s twitter handle.
            websiteFacebook: Option[String] - Instructor?s facebook page.
            websiteLinkedin: Option[String] - Instructor?s LinkedIn profile.
            websiteGplus: Option[String] - Instructor?s Google+ Website.
            shortName: Option[String] - Instructor?s short name.
        param include:(optional) List of include to be sent in the query string,so linked objects can be included in response
            universities - The universities an instructor is associated with.
            courses - The courses an instructor teaches.
            sessions - The sessions an instructor teaches.
        """
        return self.api_connection.get(self._get_path("instructors",**kwargs))


    def get_sessions(self,**kwargs):
        """ Get session collection
        param id:(optional) List of instructor id to be sent in the query string to retrive specificed instructors
        param field:(optional) List of field to be sent in the query string to retrive the fields in response 
           objects,by default only a minimal set of fields are included in response objects
            id: String - Session Id
            courseId: String - Course Id
            homeLink: Option[String] - Home link for the course.
            status: String - Session status.
            active: String - Whether the session is active.'True' or 'False'
            durationString: Option[String] - Approximate (human readable) duration string. Typically of the format ?XX weeks?.
            startDay: Option[String] - Optional start day.
            startMonth: Option[String] - Optional start month.
            startYear: Option[String] - Optional start year.
            name: Option[String] - Session iteration name.
            signatureTrackCloseTime: Option[DateTime] - Signature track information.
            signatureTrackOpenTime: Option[DateTime] - Signature track information.
            signatureTrackPrice: Option[Double] - Signature track information.
            signatureTrackRegularPrice: Option[Float] - Signature track information.
            eligibleForCertificates: Option[Boolean] - Certificates allowed.
            eligibleForSignatureTrack: Option[Boolean] - Signature track available.
            certificateDescription: Option[String] - Description on the course certificate.
            certificatesReady: Boolean - Whether the certificates have been released.
        param include:(optional) List of include to be sent in the query string,so linked objects can be included in response
            instructors - The instructors for a session.
            courses - The linked course for this session.
        """
        return self.api_connection.get(self._get_path("sessions",**kwargs))


    def _get_path(self,rel_path,id=None,field=None,include=None):
        id=id or {}
        field=field or {}
        include=include or {}
        return "/{0}{1}{2}{3}".format(rel_path,self._build_id(id),self._build_field(field),self._build_include(include))


    def _build_field(self,field):
        if field:
            f=','.join(field)
            return '&fields='+f
        else:
            return ''


    def _build_include(self,include):
        if include:
            i=','.join(include)
            return '&includes='+i
        else:
            return ''


    def _build_id(self,id):
        if  len(id)>1:
            i=','.join(str(x) for x in id)
            return '?ids='+i
        elif len(id)==1:
             return '?id='+str(id[0])
        else:
            return ''

