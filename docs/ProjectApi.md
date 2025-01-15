# xero_python.ProjectApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /Projects | Create one or more new projects
[**create_task**](ProjectApi.md#create_task) | **POST** /Projects/{projectId}/Tasks | Allows you to create a task
[**create_time_entry**](ProjectApi.md#create_time_entry) | **POST** /Projects/{projectId}/Time | Creates a time entry for a specific project
[**delete_task**](ProjectApi.md#delete_task) | **DELETE** /Projects/{projectId}/Tasks/{taskId} | Allows you to delete a task
[**delete_time_entry**](ProjectApi.md#delete_time_entry) | **DELETE** /Projects/{projectId}/Time/{timeEntryId} | Deletes a time entry for a specific project
[**get_project**](ProjectApi.md#get_project) | **GET** /Projects/{projectId} | Retrieves a single project
[**get_project_users**](ProjectApi.md#get_project_users) | **GET** /ProjectsUsers | Retrieves a list of all project users
[**get_projects**](ProjectApi.md#get_projects) | **GET** /Projects | Retrieves all projects
[**get_task**](ProjectApi.md#get_task) | **GET** /Projects/{projectId}/Tasks/{taskId} | Retrieves a single project task
[**get_tasks**](ProjectApi.md#get_tasks) | **GET** /Projects/{projectId}/Tasks | Retrieves all project tasks
[**get_time_entries**](ProjectApi.md#get_time_entries) | **GET** /Projects/{projectId}/Time | Retrieves all time entries associated with a specific project
[**get_time_entry**](ProjectApi.md#get_time_entry) | **GET** /Projects/{projectId}/Time/{timeEntryId} | Retrieves a single time entry for a specific project
[**patch_project**](ProjectApi.md#patch_project) | **PATCH** /Projects/{projectId} | creates a project for the specified contact
[**update_project**](ProjectApi.md#update_project) | **PUT** /Projects/{projectId} | Updates a specific project
[**update_task**](ProjectApi.md#update_task) | **PUT** /Projects/{projectId}/Tasks/{taskId} | Allows you to update a task
[**update_time_entry**](ProjectApi.md#update_time_entry) | **PUT** /Projects/{projectId}/Time/{timeEntryId} | Updates a time entry for a specific project


# **create_project**
> Project create_project(xero_tenant_id, project_create_or_update, idempotency_key=idempotency_key)

Create one or more new projects

### Example

```python
import time
import os
import xero_python
from xero_python.models.project import Project
from xero_python.models.project_create_or_update import ProjectCreateOrUpdate
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_create_or_update = { "contactId": "00000000-0000-0000-000-000000000000", "name": "New Kitchen", "deadlineUtc": "2019-12-10T12:59:59Z", "estimateAmount": "99.99" } # ProjectCreateOrUpdate | Create a new project with ProjectCreateOrUpdate object
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Create one or more new projects
        api_response = await api_instance.create_project(xero_tenant_id, project_create_or_update, idempotency_key=idempotency_key)
        print("The response of ProjectApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_create_or_update** | [**ProjectCreateOrUpdate**](ProjectCreateOrUpdate.md)| Create a new project with ProjectCreateOrUpdate object | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK/success, returns the new project object |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> Task create_task(xero_tenant_id, project_id, task_create_or_update, idempotency_key=idempotency_key)

Allows you to create a task

Allows you to create a specific task

### Example

```python
import time
import os
import xero_python
from xero_python.models.task import Task
from xero_python.models.task_create_or_update import TaskCreateOrUpdate
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can create a task on a specified projectId
    task_create_or_update = { "status": "INPROGRESS" } # TaskCreateOrUpdate | The task object you are creating
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Allows you to create a task
        api_response = await api_instance.create_task(xero_tenant_id, project_id, task_create_or_update, idempotency_key=idempotency_key)
        print("The response of ProjectApi->create_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can create a task on a specified projectId | 
 **task_create_or_update** | [**TaskCreateOrUpdate**](TaskCreateOrUpdate.md)| The task object you are creating | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK/success, returns the new task object |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_time_entry**
> TimeEntry create_time_entry(xero_tenant_id, project_id, time_entry_create_or_update, idempotency_key=idempotency_key)

Creates a time entry for a specific project

Allows you to create a specific task

### Example

```python
import time
import os
import xero_python
from xero_python.models.time_entry import TimeEntry
from xero_python.models.time_entry_create_or_update import TimeEntryCreateOrUpdate
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint
    time_entry_create_or_update = {userId=00000000-0000-0000-0000-000000000000, taskId=00000000-0000-0000-0000-000000000000, dateUtc=2020-02-26T15:00:00Z, duration=30, description=My description} # TimeEntryCreateOrUpdate | The time entry object you are creating
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Creates a time entry for a specific project
        api_response = await api_instance.create_time_entry(xero_tenant_id, project_id, time_entry_create_or_update, idempotency_key=idempotency_key)
        print("The response of ProjectApi->create_time_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->create_time_entry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 
 **time_entry_create_or_update** | [**TimeEntryCreateOrUpdate**](TimeEntryCreateOrUpdate.md)| The time entry object you are creating | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

[**TimeEntry**](TimeEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK/success, returns the newly created time entry |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> delete_task(xero_tenant_id, project_id, task_id)

Allows you to delete a task

Allows you to delete a specific task

### Example

```python
import time
import os
import xero_python
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint
    task_id = 'task_id_example' # str | You can specify an individual task by appending the id to the endpoint

    try:
        # Allows you to delete a task
        await api_instance.delete_task(xero_tenant_id, project_id, task_id)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 
 **task_id** | **str**| You can specify an individual task by appending the id to the endpoint | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success - return response 204 no content |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_entry**
> delete_time_entry(xero_tenant_id, project_id, time_entry_id)

Deletes a time entry for a specific project

Allows you to delete a specific time entry

### Example

```python
import time
import os
import xero_python
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint
    time_entry_id = 'time_entry_id_example' # str | You can specify an individual task by appending the id to the endpoint

    try:
        # Deletes a time entry for a specific project
        await api_instance.delete_time_entry(xero_tenant_id, project_id, time_entry_id)
    except Exception as e:
        print("Exception when calling ProjectApi->delete_time_entry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 
 **time_entry_id** | **str**| You can specify an individual task by appending the id to the endpoint | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success - return response 204 no content |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(xero_tenant_id, project_id)

Retrieves a single project

Allows you to retrieve a specific project using the projectId

### Example

```python
import time
import os
import xero_python
from xero_python.models.project import Project
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint

    try:
        # Retrieves a single project
        api_response = await api_instance.get_project(xero_tenant_id, project_id)
        print("The response of ProjectApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK/success, returns the specified project object |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_users**
> ProjectUsers get_project_users(xero_tenant_id, page=page, page_size=page_size)

Retrieves a list of all project users

Allows you to retrieve the users on a projects.

### Example

```python
import time
import os
import xero_python
from xero_python.models.project_users import ProjectUsers
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    page = 1 # int | set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0. (optional) (default to 1)
    page_size = 50 # int | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. (optional) (default to 50)

    try:
        # Retrieves a list of all project users
        api_response = await api_instance.get_project_users(xero_tenant_id, page=page, page_size=page_size)
        print("The response of ProjectApi->get_project_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **page** | **int**| set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0. | [optional] [default to 1]
 **page_size** | **int**| Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | [optional] [default to 50]

### Return type

[**ProjectUsers**](ProjectUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK/success, returns a list of project users |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> Projects get_projects(xero_tenant_id, project_ids=project_ids, contact_id=contact_id, states=states, page=page, page_size=page_size)

Retrieves all projects

Allows you to retrieve, create and update projects.

### Example

```python
import time
import os
import xero_python
from xero_python.models.projects import Projects
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_ids = ['project_ids_example'] # List[str] | Search for all projects that match a comma separated list of projectIds (optional)
    contact_id = 'contact_id_example' # str | Filter for projects for a specific contact (optional)
    states = 'states_example' # str | Filter for projects in a particular state (INPROGRESS or CLOSED) (optional)
    page = 1 # int | set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0. (optional) (default to 1)
    page_size = 50 # int | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. (optional) (default to 50)

    try:
        # Retrieves all projects
        api_response = await api_instance.get_projects(xero_tenant_id, project_ids=project_ids, contact_id=contact_id, states=states, page=page, page_size=page_size)
        print("The response of ProjectApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_projects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_ids** | [**List[str]**](str.md)| Search for all projects that match a comma separated list of projectIds | [optional] 
 **contact_id** | **str**| Filter for projects for a specific contact | [optional] 
 **states** | **str**| Filter for projects in a particular state (INPROGRESS or CLOSED) | [optional] 
 **page** | **int**| set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0. | [optional] [default to 1]
 **page_size** | **int**| Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | [optional] [default to 50]

### Return type

[**Projects**](Projects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK/success, returns a list of project objects |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> Task get_task(xero_tenant_id, project_id, task_id)

Retrieves a single project task

Allows you to retrieve a specific project

### Example

```python
import time
import os
import xero_python
from xero_python.models.task import Task
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint
    task_id = 'task_id_example' # str | You can specify an individual task by appending the taskId to the endpoint, i.e. GET https://.../tasks/{taskID}

    try:
        # Retrieves a single project task
        api_response = await api_instance.get_task(xero_tenant_id, project_id, task_id)
        print("The response of ProjectApi->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 
 **task_id** | **str**| You can specify an individual task by appending the taskId to the endpoint, i.e. GET https://.../tasks/{taskID} | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK/success, returns the specified task object |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> Tasks get_tasks(xero_tenant_id, project_id, page=page, page_size=page_size, task_ids=task_ids, charge_type=charge_type)

Retrieves all project tasks

Allows you to retrieve a specific project

### Example

```python
import time
import os
import xero_python
from xero_python.models.charge_type import ChargeType
from xero_python.models.tasks import Tasks
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint
    page = 1 # int | Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0. (optional)
    page_size = 10 # int | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. (optional)
    task_ids = 'task_ids_example' # str | Search for all tasks that match a comma separated list of taskIds, i.e. GET https://.../tasks?taskIds={taskID},{taskID} (optional)
    charge_type = xero_python.ChargeType() # ChargeType |  (optional)

    try:
        # Retrieves all project tasks
        api_response = await api_instance.get_tasks(xero_tenant_id, project_id, page=page, page_size=page_size, task_ids=task_ids, charge_type=charge_type)
        print("The response of ProjectApi->get_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 
 **page** | **int**| Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0. | [optional] 
 **page_size** | **int**| Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | [optional] 
 **task_ids** | **str**| Search for all tasks that match a comma separated list of taskIds, i.e. GET https://.../tasks?taskIds&#x3D;{taskID},{taskID} | [optional] 
 **charge_type** | [**ChargeType**](.md)|  | [optional] 

### Return type

[**Tasks**](Tasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK/success, returns a list of task objects |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_entries**
> TimeEntries get_time_entries(xero_tenant_id, project_id, user_id=user_id, task_id=task_id, invoice_id=invoice_id, contact_id=contact_id, page=page, page_size=page_size, states=states, is_chargeable=is_chargeable, date_after_utc=date_after_utc, date_before_utc=date_before_utc)

Retrieves all time entries associated with a specific project

Allows you to retrieve the time entries associated with a specific project

### Example

```python
import time
import os
import xero_python
from xero_python.models.time_entries import TimeEntries
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | Identifier of the project, that the task (which the time entry is logged against) belongs to.
    user_id = 'user_id_example' # str | The xero user identifier of the person who logged time. (optional)
    task_id = 'task_id_example' # str | Identifier of the task that time entry is logged against. (optional)
    invoice_id = 'invoice_id_example' # str | Finds all time entries for this invoice. (optional)
    contact_id = 'contact_id_example' # str | Finds all time entries for this contact identifier. (optional)
    page = 1 # int | Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0. (optional)
    page_size = 10 # int | Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. (optional)
    states = ['states_example'] # List[str] | Comma-separated list of states to find. Will find all time entries that are in the status of whatever is specified. (optional)
    is_chargeable = True # bool | Finds all time entries which relate to tasks with the charge type `TIME` or `FIXED`. (optional)
    date_after_utc = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 UTC date. Finds all time entries on or after this date filtered on the `dateUtc` field. (optional)
    date_before_utc = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 UTC date. Finds all time entries on or before this date filtered on the `dateUtc` field. (optional)

    try:
        # Retrieves all time entries associated with a specific project
        api_response = await api_instance.get_time_entries(xero_tenant_id, project_id, user_id=user_id, task_id=task_id, invoice_id=invoice_id, contact_id=contact_id, page=page, page_size=page_size, states=states, is_chargeable=is_chargeable, date_after_utc=date_after_utc, date_before_utc=date_before_utc)
        print("The response of ProjectApi->get_time_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_time_entries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| Identifier of the project, that the task (which the time entry is logged against) belongs to. | 
 **user_id** | **str**| The xero user identifier of the person who logged time. | [optional] 
 **task_id** | **str**| Identifier of the task that time entry is logged against. | [optional] 
 **invoice_id** | **str**| Finds all time entries for this invoice. | [optional] 
 **contact_id** | **str**| Finds all time entries for this contact identifier. | [optional] 
 **page** | **int**| Set to 1 by default. The requested number of the page in paged response - Must be a number greater than 0. | [optional] 
 **page_size** | **int**| Optional, it is set to 50 by default. The number of items to return per page in a paged response - Must be a number between 1 and 500. | [optional] 
 **states** | [**List[str]**](str.md)| Comma-separated list of states to find. Will find all time entries that are in the status of whatever is specified. | [optional] 
 **is_chargeable** | **bool**| Finds all time entries which relate to tasks with the charge type &#x60;TIME&#x60; or &#x60;FIXED&#x60;. | [optional] 
 **date_after_utc** | **datetime**| ISO 8601 UTC date. Finds all time entries on or after this date filtered on the &#x60;dateUtc&#x60; field. | [optional] 
 **date_before_utc** | **datetime**| ISO 8601 UTC date. Finds all time entries on or before this date filtered on the &#x60;dateUtc&#x60; field. | [optional] 

### Return type

[**TimeEntries**](TimeEntries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK/success, returns a list of time entry objects |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_entry**
> TimeEntry get_time_entry(xero_tenant_id, project_id, time_entry_id)

Retrieves a single time entry for a specific project

Allows you to get a single time entry in a project

### Example

```python
import time
import os
import xero_python
from xero_python.models.time_entry import TimeEntry
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint
    time_entry_id = 'time_entry_id_example' # str | You can specify an individual time entry by appending the id to the endpoint

    try:
        # Retrieves a single time entry for a specific project
        api_response = await api_instance.get_time_entry(xero_tenant_id, project_id, time_entry_id)
        print("The response of ProjectApi->get_time_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_time_entry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 
 **time_entry_id** | **str**| You can specify an individual time entry by appending the id to the endpoint | 

### Return type

[**TimeEntry**](TimeEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK/success, returns the specified time entry |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project**
> patch_project(xero_tenant_id, project_id, project_patch, idempotency_key=idempotency_key)

creates a project for the specified contact

Allows you to update a specific projects.

### Example

```python
import time
import os
import xero_python
from xero_python.models.project_patch import ProjectPatch
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint
    project_patch = { "status": "INPROGRESS" } # ProjectPatch | Update the status of an existing Project
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # creates a project for the specified contact
        await api_instance.patch_project(xero_tenant_id, project_id, project_patch, idempotency_key=idempotency_key)
    except Exception as e:
        print("Exception when calling ProjectApi->patch_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 
 **project_patch** | [**ProjectPatch**](ProjectPatch.md)| Update the status of an existing Project | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success - return response 204 no content |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> update_project(xero_tenant_id, project_id, project_create_or_update, idempotency_key=idempotency_key)

Updates a specific project

Allows you to update a specific projects.

### Example

```python
import time
import os
import xero_python
from xero_python.models.project_create_or_update import ProjectCreateOrUpdate
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint
    project_create_or_update = { "name": "New Kitchen", "deadlineUtc": "2017-04-23T18:25:43.511Z", "estimateAmount": 99.99 } # ProjectCreateOrUpdate | Request of type ProjectCreateOrUpdate
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Updates a specific project
        await api_instance.update_project(xero_tenant_id, project_id, project_create_or_update, idempotency_key=idempotency_key)
    except Exception as e:
        print("Exception when calling ProjectApi->update_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 
 **project_create_or_update** | [**ProjectCreateOrUpdate**](ProjectCreateOrUpdate.md)| Request of type ProjectCreateOrUpdate | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success - return response 204 no content |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> update_task(xero_tenant_id, project_id, task_id, task_create_or_update, idempotency_key=idempotency_key)

Allows you to update a task

Allows you to update a specific task

### Example

```python
import time
import os
import xero_python
from xero_python.models.task_create_or_update import TaskCreateOrUpdate
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint
    task_id = 'task_id_example' # str | You can specify an individual task by appending the id to the endpoint
    task_create_or_update =  # TaskCreateOrUpdate | The task object you are updating
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Allows you to update a task
        await api_instance.update_task(xero_tenant_id, project_id, task_id, task_create_or_update, idempotency_key=idempotency_key)
    except Exception as e:
        print("Exception when calling ProjectApi->update_task: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 
 **task_id** | **str**| You can specify an individual task by appending the id to the endpoint | 
 **task_create_or_update** | [**TaskCreateOrUpdate**](TaskCreateOrUpdate.md)| The task object you are updating | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK/Success - return response 204 no content |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_entry**
> update_time_entry(xero_tenant_id, project_id, time_entry_id, time_entry_create_or_update, idempotency_key=idempotency_key)

Updates a time entry for a specific project

Allows you to update time entry in a project

### Example

```python
import time
import os
import xero_python
from xero_python.models.time_entry_create_or_update import TimeEntryCreateOrUpdate
from xero_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = xero_python.Configuration(
    host = "http://localhost:8080"
)


# Enter a context with an instance of the API client
async with xero_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xero_python.ProjectApi(api_client)
    xero_tenant_id = 'xero_tenant_id_example' # str | Xero identifier for Tenant
    project_id = 'project_id_example' # str | You can specify an individual project by appending the projectId to the endpoint
    time_entry_id = 'time_entry_id_example' # str | You can specify an individual time entry by appending the id to the endpoint
    time_entry_create_or_update = {userId=00000000-0000-0000-0000-000000000000, taskId=00000000-0000-0000-0000-000000000000, dateUtc=2020-02-27T15:00:00Z, duration=45, description=My UPDATED description} # TimeEntryCreateOrUpdate | The time entry object you are updating
    idempotency_key = 'KEY_VALUE' # str | This allows you to safely retry requests without the risk of duplicate processing. 128 character max. (optional)

    try:
        # Updates a time entry for a specific project
        await api_instance.update_time_entry(xero_tenant_id, project_id, time_entry_id, time_entry_create_or_update, idempotency_key=idempotency_key)
    except Exception as e:
        print("Exception when calling ProjectApi->update_time_entry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_tenant_id** | **str**| Xero identifier for Tenant | 
 **project_id** | **str**| You can specify an individual project by appending the projectId to the endpoint | 
 **time_entry_id** | **str**| You can specify an individual time entry by appending the id to the endpoint | 
 **time_entry_create_or_update** | [**TimeEntryCreateOrUpdate**](TimeEntryCreateOrUpdate.md)| The time entry object you are updating | 
 **idempotency_key** | **str**| This allows you to safely retry requests without the risk of duplicate processing. 128 character max. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success - return response 204 no content |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

