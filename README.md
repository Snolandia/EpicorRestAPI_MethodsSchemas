All of Epicors Rest Api Services, their methods, and their schemas. 

Python(.py) Files

Functions should all be there and working. Use configEpicorSchemas file to set the URL and either set username password in there as well or provide headers when calling the function. Classes representing the schemas should mostly work, but may require some massaging. Mostly there as examples.

TypeScript(.ts) Files

All interfaces should work with the functions, some may require some massaging due to the API Schema being slightly off than what its documentation says it is. Mostly with whether the returned results are an array or a dictionary. Use configEpicorSchemas to set the url and set a username and password, or provide headers when calling the functions. 
Every function returns a promise of the type that the api method specifies, or if the api does not return ok, returns an error. 

Example:

import configEpicorSchemas

configEpicorSchemas.setEpicorURL("Your Epicor API URL Here 'https://centralapp.epicorsaas.com/SaaS123/api/v1/"'");

configEpicorSchemas.setEpicorHeaderAuthoriziation(username,pass)

import Erp_BO_JobEntrySvc

Erp_BO_JobEntrySvc.get_JobEntries()
  .then((data)=>{
    doSomething
  }

  or

  var headers:Headers(setUpHeadersHere)

  Erp_BO_JobEntrySvc.get_JobEntries(headers=headers)
  .then((data)=>{
    doSomething
  }
