import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.LIB.ClientFunctionsSvc
// Description: Miscellaneous client functions.
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetAuthenticationModeCodeDescriptionList
   Description: Gets a delimited list of authentication modes.
   OperationID: GetAuthenticationModeCodeDescriptionList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAuthenticationModeCodeDescriptionList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAuthenticationModeCodeDescriptionList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAuthenticationModeCodeDescriptionList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/GetAuthenticationModeCodeDescriptionList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTaxConnect
   Description: This method returns TaxSvcConfig.TaxConnectEnabled for the current Company
otherwise it returns false.
   OperationID: GetTaxConnect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxConnect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTaxConnect(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/GetTaxConnect", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AlertLogAvailable
   Description: Return whether alert log records exist.
   OperationID: AlertLogAvailable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AlertLogAvailable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AlertLogAvailable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AlertLogAvailable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/AlertLogAvailable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWorkstationMethod
   Description: Returns The workstation method for a company.
   OperationID: GetWorkstationMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWorkstationMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWorkstationMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWorkstationMethod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/GetWorkstationMethod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSSRSPrintOption
   Description: Returns SSRS Printer for a company.
   OperationID: GetSSRSPrintOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSSRSPrintOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSSRSPrintOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSSRSPrintOption(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/GetSSRSPrintOption", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPrinterOptions
   Description: Gets the SSRS Printer Options for a company.
   OperationID: GetPrinterOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrinterOptions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrinterOptions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPrinterOptions(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/GetPrinterOptions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessZDHelpTopicOrLabel
   Description: Utility method for clients (often Kinetic clients) to use returned URL launch Epicor help hosted on Zendesk Epicor help portals (also called "Guides"). The return value of this method (the URL) contains a JWT token for Zendesk
that includes a data payload of some of the method parameters. Zendesk logs the user on with the JWT/payload and uses return_to querystring to navigate user to correct topic.
The typical action a client will take on the client with the returned URL is (to give a simple js example) javascript: window.open(url,"epHelpWindow",null,false). The token has a 3 minute window to be used.
   OperationID: ProcessZDHelpTopicOrLabel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessZDHelpTopicOrLabel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessZDHelpTopicOrLabel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessZDHelpTopicOrLabel(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/ProcessZDHelpTopicOrLabel", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClientDownloadAvailable
   Description: Checks if the configuration required for the client download is available.
   OperationID: ClientDownloadAvailable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClientDownloadAvailable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClientDownloadAvailable(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/ClientDownloadAvailable", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetClientDownloadUrl
   Description: Gets the client download URL.
   OperationID: GetClientDownloadUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetClientDownloadUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetClientDownloadUrl(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/GetClientDownloadUrl", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetIsProductionInstance
   Description: Return the boolean value for first  "IsProductionInstance" value from ice.SysLicense table.
   OperationID: GetIsProductionInstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIsProductionInstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetIsProductionInstance(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/GetIsProductionInstance", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetIsProductionInstance
   Description: Set the server/db combination as a production/non-production server.
   OperationID: SetIsProductionInstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetIsProductionInstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetIsProductionInstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetIsProductionInstance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/SetIsProductionInstance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetInstancePurposes
   Description: Set the isProduction value for all records in ice.SysLienses Table
   OperationID: SetInstancePurposes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetInstancePurposes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetInstancePurposes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetInstancePurposes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/SetInstancePurposes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetInstancePurpose
   Description: Set IsProductionInstance Value for the license instance based on the license id, and DB values from current context
   OperationID: SetInstancePurpose
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetInstancePurpose_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetInstancePurpose_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetInstancePurpose(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/SetInstancePurpose", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInstancePurpose
   Description: Getting  the single license purpose based on the installation id in the current context/session
   OperationID: GetInstancePurpose
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstancePurpose_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInstancePurpose(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/GetInstancePurpose", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetProductionServerInstances
   Description: Get Production  Server Instance Details from the DB
   OperationID: GetProductionServerInstances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProductionServerInstances_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetProductionServerInstances(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/GetProductionServerInstances", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetUpdateAvailableToFalse
   Description: Setting UpdateAvailable to false after applying the license
   OperationID: SetUpdateAvailableToFalse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUpdateAvailableToFalse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUpdateAvailableToFalse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUpdateAvailableToFalse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/SetUpdateAvailableToFalse", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetUpdateAvailableToFalseForAllAppliedLicenses
   Description: Flipping UpdateAvailalble field value to false for a list of licenses
   OperationID: SetUpdateAvailableToFalseForAllAppliedLicenses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUpdateAvailableToFalseForAllAppliedLicenses_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUpdateAvailableToFalseForAllAppliedLicenses_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUpdateAvailableToFalseForAllAppliedLicenses(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/SetUpdateAvailableToFalseForAllAppliedLicenses", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveFromFileStore
   Description: Remove the license content from ice.FileStote, once the license is applied
   OperationID: RemoveFromFileStore
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveFromFileStore_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveFromFileStore_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveFromFileStore(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/RemoveFromFileStore", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLicenseLiveStatus
   Description: Get the license live status
   OperationID: GetLicenseLiveStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicenseLiveStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLicenseLiveStatus(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/GetLicenseLiveStatus", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessZDHelpRequestCategory
   Description: Utility method to open online help (in Zendesk) at the category heading level, instead of navigating directly to a topic.
   OperationID: ProcessZDHelpRequestCategory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessZDHelpRequestCategory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessZDHelpRequestCategory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessZDHelpRequestCategory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.LIB.ClientFunctionsSvc/ProcessZDHelpRequestCategory", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param companyID
   */  
export interface AlertLogAvailable_input{
   companyID:string,
}

export interface AlertLogAvailable_output{
      /**  Return false if the user doesn't have permission.  */  
   returnObj:boolean,
}

export interface ClientDownloadAvailable_output{
      /**  `true`if available  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   configurationError:string,
}
}

   /** Required : 
      @param includeIdP
      @param includeToken
      @param includeTcpBinary
      @param includeAzureAD
   */  
export interface GetAuthenticationModeCodeDescriptionList_input{
      /**  Include Idp in list.  */  
   includeIdP:boolean,
      /**  Include Token in list.  */  
   includeToken:boolean,
      /**  Include TcpBinary in list.  */  
   includeTcpBinary:boolean,
      /**  Include AzureAD in list.  */  
   includeAzureAD:boolean,
}

export interface GetAuthenticationModeCodeDescriptionList_output{
   returnObj:string,
}

export interface GetClientDownloadUrl_output{
      /**  Url that can be used to download the ERP client installer.  */  
   returnObj:string,
}

export interface GetInstancePurpose_output{
   returnObj:boolean,
}

export interface GetIsProductionInstance_output{
   returnObj:boolean,
}

export interface GetLicenseLiveStatus_output{
   returnObj:boolean,
}

   /** Required : 
      @param companyID
   */  
export interface GetPrinterOptions_input{
      /**  company ID.  */  
   companyID:string,
}

export interface GetPrinterOptions_output{
   returnObj:Ice_Lib_ClientFunctions_PrinterOptions[],
}

export interface GetProductionServerInstances_output{
   returnObj:Ice_Lib_ClientFunctions_InstanceDetails[],
}

   /** Required : 
      @param companyID
   */  
export interface GetSSRSPrintOption_input{
      /**  Company  */  
   companyID:string,
}

export interface GetSSRSPrintOption_output{
   returnObj:string,
}

export interface GetTaxConnect_output{
parameters : {
      /**  output parameters  */  
   compTaxConnectEnabled:boolean,
}
}

   /** Required : 
      @param companyID
   */  
export interface GetWorkstationMethod_input{
      /**  Company  */  
   companyID:string,
}

export interface GetWorkstationMethod_output{
   returnObj:string,
}

export interface Ice_Lib_ClientFunctions_InstanceDetails{
   LicenseID:string,
   InstanceDescription:string,
   IsProductionInstance:boolean,
}

export interface Ice_Lib_ClientFunctions_PrinterOptions{
   AllowedPrinter:string,
   DefaultPaperSize:number,
}

   /** Required : 
      @param label
      @param category
      @param helpTopic
      @param userName
      @param userEmail
      @param aryTags
      @param zdSubDomain
      @param locale
   */  
export interface ProcessZDHelpRequestCategory_input{
      /**  Corresponds to Label used in Zendesk for an article, and used to locate the URL of an article. Should be lowercase without spaces. In the case of Kinetic forms, use page title as label (lowercasing and trimming spaces)  */  
   label:string,
      /**  search Zendesk for category landing page using category name  */  
   category:string,
      /**  The fully qualified URL of a Zendesk article. Example- 'https://epicorerp.zendesk.com/hc/en-us/articles/360022072552-View-Schedule' If using label (preferred technique) send null for helpTopic.  */  
   helpTopic:string,
      /**  Consult with Epicor University writer on the generic user or users that may be appropriate. Until Epicor Idp is used, most apps will use a single user for the whole app.
            Example- 'Epicor TimeExpenseUser'  */  
   userName:string,
      /**  Email for user. Until actual users are passed (afer Idp), email is just meeting a Zendesk requirement and will not be used (but must consistent for user from call to call).
            Example-'erptimeexpense@epicor.com'  */  
   userEmail:string,
      /**  Tags are used in Zendesk to show or hide (segment) content. Consult with Epicor University writer on appropriate tags for user.
            Tags sent with call replace previous tag set. Example- ['erptime', 'erpexpense']  */  
   aryTags:string,
      /**  Consult with EU writer on the Zendesk subdomain to use  */  
   zdSubDomain:string,
      /**  Set to locale of user session. For example - en-us  */  
   locale:string,
}

export interface ProcessZDHelpRequestCategory_output{
      /**  A URL with Zendesk SSO token and redirect url as querystring.  */  
   returnObj:string,
}

   /** Required : 
      @param label
      @param helpTopic
      @param userName
      @param userEmail
      @param aryTags
      @param zdSubDomain
      @param locale
   */  
export interface ProcessZDHelpTopicOrLabel_input{
      /**  Corresponds to Label used in Zendesk for an article, and used to locate the URL of an article. Should be lowercase without spaces. In the case of Kinetic forms, use page title as label (lowercasing and trimming spaces)  */  
   label:string,
      /**  The fully qualified URL of a Zendesk article. Example- 'https://epicorerp.zendesk.com/hc/en-us/articles/360022072552-View-Schedule' If using label (preferred technique) send null for helpTopic.  */  
   helpTopic:string,
      /**  Consult with Epicor University writer on the generic user or users that may be appropriate. Until Epicor Idp is used, most apps will use a single user for the whole app.
            Example- 'Epicor TimeExpenseUser'  */  
   userName:string,
      /**  Email for user. Until actual users are passed (afer Idp), email is just meeting a Zendesk requirement and will not be used (but must consistent for user from call to call).
            Example-'erptimeexpense@epicor.com'  */  
   userEmail:string,
      /**  Tags are used in Zendesk to show or hide (segment) content. Consult with Epicor University writer on appropriate tags for user.
            Tags sent with call replace previous tag set. Example- ['erptime', 'erpexpense']  */  
   aryTags:string,
      /**  Consult with EU writer on the Zendesk subdomain to use  */  
   zdSubDomain:string,
      /**  Set to locale of user session. For example - en-us  */  
   locale:string,
}

export interface ProcessZDHelpTopicOrLabel_output{
      /**  A URL with Zendesk SSO token and redirect url as querystring.  */  
   returnObj:string,
}

   /** Required : 
      @param fileName
   */  
export interface RemoveFromFileStore_input{
   fileName:string,
}

export interface RemoveFromFileStore_output{
}

   /** Required : 
      @param isProduction
   */  
export interface SetInstancePurpose_input{
   isProduction:boolean,
}

export interface SetInstancePurpose_output{
   returnObj:boolean,
}

   /** Required : 
      @param isProduction
   */  
export interface SetInstancePurposes_input{
   isProduction:boolean,
}

export interface SetInstancePurposes_output{
   returnObj:boolean,
}

   /** Required : 
      @param isProduction
   */  
export interface SetIsProductionInstance_input{
   isProduction:boolean,
}

export interface SetIsProductionInstance_output{
}

   /** Required : 
      @param fileNames
   */  
export interface SetUpdateAvailableToFalseForAllAppliedLicenses_input{
   fileNames:string,
}

export interface SetUpdateAvailableToFalseForAllAppliedLicenses_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param fileName
   */  
export interface SetUpdateAvailableToFalse_input{
   fileName:string,
}

export interface SetUpdateAvailableToFalse_output{
   returnObj:boolean,
}

